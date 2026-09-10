"""SessionStart hook: audit (and optionally prune) the always-on context baseline.

Everything the harness loads before the user types — enabled plugins and their skill
listings, personal skills, subagent definitions, MCP tool rosters — is re-read from
cache on *every* request of *every* session. A 60k-token baseline across 3 000 requests
is 180M cache-read tokens a fortnight, and none of it is work the user asked for.
Unlike the other hooks in this skill, which trim what a session does, this one trims
what a session starts with.

Nothing is judged by taste. An item is a candidate only on evidence of disuse:
`~/.claude.json` usage counters plus a scan of recent transcripts for actual
invocations. Anything touched inside the window is left alone.

    python context_budget.py                 # hook mode: audit, inject only if it matters
    python context_budget.py --report        # human-readable audit
    python context_budget.py --fix           # apply; writes an undo manifest
    python context_budget.py --fix --dry-run # show what --fix would do
    python context_budget.py --restore       # undo the last --fix

Env:
  TOKEN_EFFICIENCY_OFF=1        disable entirely
  TOKEN_EFFICIENCY_AUTOFIX=1    hook mode applies the fix instead of only reporting
  TOKEN_EFFICIENCY_BUDGET_MIN=N stay silent below N recoverable tokens (default 4000)
"""

import argparse
import json
import os
import re
import shutil
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _state  # noqa: E402

CLAUDE_DIR = Path.home() / ".claude"
CONFIG = Path.home() / ".claude.json"
SETTINGS = CLAUDE_DIR / "settings.json"
PROJECTS = CLAUDE_DIR / "projects"
STATE_DIR = _state.STATE_DIR
MANIFEST = STATE_DIR / "context-budget-undo.json"
KEEP_FILE = STATE_DIR / "context-budget-keep.json"
AUDIT_CACHE = STATE_DIR / "context-budget-audit.json"

# Disuse is judged on two independent signals, because each is blind on its own: the
# counters miss anything invoked implicitly, the transcript scan misses whatever ran in
# sessions that have since been archived. A plugin used a handful of times months ago is
# a candidate; one used fifteen times is not, however long ago that was.
STALE_STARTUPS = 50
OCCASIONAL_USES = 2
SCAN_DAYS = 30
AUDIT_TTL = 7 * 86400          # re-audit at most weekly; the answer changes slowly
DEFAULT_MIN_TOKENS = 4000
REPORT_DETAIL_TOKENS = 250     # below this an item is folded into a per-kind tally

# An enabled plugin that ships no skills still costs its commands and agents in the
# listing. Charge a floor rather than reporting a misleading zero.
PLUGIN_FLOOR_TOKENS = 60

# Never proposed for removal regardless of counters: this skill is what is doing the
# measuring, and a harness with no escape hatch is worse than a fat one.
PROTECTED = {"token-efficiency", "superpowers@claude-plugins-official"}

CHARS_PER_TOKEN = 4
FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.S)
FM_NAME = re.compile(r"^name:\s*(.*)$", re.M)
FM_DESC = re.compile(r"^description:\s*(.*?)(?=\n[a-zA-Z_-]+:\s|\Z)", re.S | re.M)
TOOL_USE = re.compile(rb'"name":"mcp__([A-Za-z0-9_.-]+?)__')
SKILL_USE = re.compile(rb'"skill":"([A-Za-z0-9_:.-]+)"')
AGENT_USE = re.compile(rb'"subagent_type":"([A-Za-z0-9_:.-]+)"')


# --------------------------------------------------------------------------- helpers

def _load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _frontmatter_tokens(path: Path) -> int:
    """Cost of one entry in an always-on listing: only its name and description ship."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:8000]
    except Exception:
        return 0
    block = FRONTMATTER.search(text)
    if not block:
        return 0
    fm = block.group(1)
    name = FM_NAME.search(fm)
    desc = FM_DESC.search(fm)
    chars = len(name.group(1) if name else "") + len(desc.group(1).strip() if desc else "")
    return (chars + 6) // CHARS_PER_TOKEN


def _tree_tokens(root: Path) -> int:
    if not root.is_dir():
        return 0
    return sum(_frontmatter_tokens(f) for f in root.rglob("SKILL.md"))


def _recent_transcripts():
    cutoff = time.time() - SCAN_DAYS * 86400
    try:
        return [f for f in PROJECTS.glob("*/*.jsonl") if f.stat().st_mtime >= cutoff]
    except Exception:
        return []


def scan_invocations() -> dict:
    """Count what was actually *called* in recent sessions.

    Matches the serialized tool-call shape rather than a bare substring: every server and
    skill name also appears in the prompt's own tool listing, so a substring scan would
    report everything as used and quietly disable nothing.
    """
    mcp, skills, agents = Counter(), Counter(), Counter()
    for path in _recent_transcripts():
        try:
            with path.open("rb") as fh:
                for line in fh:
                    if b'"tool_use"' not in line:
                        continue
                    for m in TOOL_USE.findall(line):
                        mcp[m.decode()] += 1
                    for m in SKILL_USE.findall(line):
                        skills[m.decode()] += 1
                    for m in AGENT_USE.findall(line):
                        agents[m.decode()] += 1
        except Exception:
            continue
    return {"mcp": mcp, "skills": skills, "agents": agents}


def _keep(used_skills=()) -> set:
    """Protected names: the explicit keep-list, plus anything wired into the harness.

    A skill named in CLAUDE.md or launched from a hook command is load-bearing whatever
    the usage counters say — those paths invoke it without ever recording a call.
    """
    wired = ""
    for path in (CLAUDE_DIR / "CLAUDE.md", SETTINGS, CLAUDE_DIR / "settings.local.json"):
        try:
            wired += path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
    all_skills = {d.name for d in (CLAUDE_DIR / "skills").glob("*/")}
    keep = set(_load_json(KEEP_FILE, [])) | PROTECTED | {n for n in all_skills if n in wired}

    # A skill that a *kept* skill delegates to is load-bearing even with no calls of its
    # own: shelving the seo-* workers while the seo umbrella survives leaves a skill that
    # names collaborators the harness can no longer resolve.
    for name in list(keep | set(used_skills)):
        body = ""
        for f in (CLAUDE_DIR / "skills" / name).rglob("*.md"):
            try:
                body += f.read_text(encoding="utf-8", errors="ignore")[:20_000]
            except Exception:
                continue
        keep |= {n for n in all_skills if n != name and n in body}
    return keep


def _is_stale(calls: int, idle: int) -> bool:
    return calls == 0 or (calls <= OCCASIONAL_USES and idle >= STALE_STARTUPS)


# ---------------------------------------------------------------------------- audit

def audit() -> dict:
    config = _load_json(CONFIG, {})
    settings = _load_json(SETTINGS, {})
    used = scan_invocations()
    plugin_usage = config.get("pluginUsage", {})
    skill_usage = config.get("skillUsage", {})
    keep = _keep(set(used["skills"]) | {k for k, v in skill_usage.items()
                                        if int((v or {}).get("usageCount", 0))})
    startups = int(config.get("numStartups", 0))
    install_paths = {
        name: entries[0].get("installPath")
        for name, entries in (_load_json(CLAUDE_DIR / "plugins" / "installed_plugins.json", {})
                              .get("plugins", {}) or {}).items()
        if entries
    }
    items = []

    # Enabled plugins: dead when never invoked and idle for STALE_STARTUPS launches.
    for name, enabled in (settings.get("enabledPlugins") or {}).items():
        if not enabled or name in keep:
            continue
        stat = plugin_usage.get(name, {})
        calls = int(stat.get("usageCount", 0))
        idle = startups - int(stat.get("lastUsedNumStartups", 0))
        if not _is_stale(calls, idle):
            continue
        path = install_paths.get(name)
        tokens = max(_tree_tokens(Path(path)) if path else 0, PLUGIN_FLOOR_TOKENS)
        items.append({
            "kind": "plugin", "name": name, "tokens": tokens,
            "evidence": f"{calls} uses, idle {idle} launches",
        })

    # Global MCP servers: cost is the deferred tool roster, which is per-request context
    # even though the schemas are not. Tool count is read back off the transcripts.
    seen_tools = Counter()
    for path in _recent_transcripts()[:40]:
        try:
            for m in re.findall(rb"mcp__([A-Za-z0-9_.-]+?)__([A-Za-z0-9_]+)",
                                path.read_bytes()[:400_000]):
                seen_tools[m[0].decode()] += 0
                seen_tools[f"{m[0].decode()}::{m[1].decode()}"] = 1
        except Exception:
            continue
    for name in (config.get("mcpServers") or {}):
        if name in keep or used["mcp"].get(name):
            continue
        n_tools = sum(1 for k in seen_tools if k.startswith(f"{name}::"))
        items.append({
            "kind": "mcp", "name": name, "tokens": n_tools * 12 + 40,
            "evidence": f"0 calls in {SCAN_DAYS}d, ~{n_tools} tools listed",
        })

    # Personal skills.
    for skill_dir in sorted((CLAUDE_DIR / "skills").glob("*/")):
        name = skill_dir.name
        if name in keep:
            continue
        calls = int((skill_usage.get(name) or {}).get("usageCount", 0)) + used["skills"].get(name, 0)
        if calls:
            continue
        items.append({
            "kind": "skill", "name": name, "tokens": _frontmatter_tokens(skill_dir / "SKILL.md"),
            "evidence": f"0 uses in {SCAN_DAYS}d",
        })

    # Subagent definitions: name plus description sit in the system prompt verbatim.
    for f in sorted((CLAUDE_DIR / "agents").glob("*.md")):
        name = f.stem
        if name in keep or used["agents"].get(name):
            continue
        items.append({
            "kind": "agent", "name": name, "tokens": _frontmatter_tokens(f),
            "evidence": f"0 dispatches in {SCAN_DAYS}d",
        })

    # Stale project records: no context cost, but ~/.claude.json is parsed at every launch.
    stale_projects = [p for p in (config.get("projects") or {}) if not Path(p).exists()]

    items.sort(key=lambda i: -i["tokens"])
    return {
        "items": items,
        "stale_projects": stale_projects,
        "recoverable": sum(i["tokens"] for i in items),
        "at": int(time.time()),
    }


# ------------------------------------------------------------------------------ fix

def _backup(path: Path, stamp: str) -> str:
    dest = STATE_DIR / f"{path.name}.{stamp}.bak"
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, dest)
    return str(dest)


def apply_fix(result: dict, dry_run: bool, include_config: bool = False) -> list:
    """Disable the dead weight. Every action is reversible via --restore.

    MCP servers and project records live in ~/.claude.json, which a running Claude Code
    rewrites from memory when it exits — editing it mid-session is silently undone. Those
    two categories are therefore gated behind --include-config, to be run with the app
    closed. Plugins (settings.json) and shelved files are safe to change live.
    """
    actions, stamp = [], time.strftime("%Y%m%d-%H%M%S")
    settings = _load_json(SETTINGS, {})
    config = _load_json(CONFIG, {})
    disabled_mcp = _load_json(STATE_DIR / "disabled-mcp.json", {})
    touched_settings = touched_config = False

    for item in result["items"]:
        kind, name = item["kind"], item["name"]
        if kind == "plugin":
            actions.append(f"disable plugin {name}")
            if not dry_run:
                settings.setdefault("enabledPlugins", {})[name] = False
                touched_settings = True
        elif kind == "mcp":
            if not include_config:
                continue
            actions.append(f"unload MCP server {name}")
            if not dry_run:
                disabled_mcp[name] = config.get("mcpServers", {}).pop(name, None)
                touched_config = True
        elif kind in ("skill", "agent"):
            src = (CLAUDE_DIR / "skills" / name) if kind == "skill" else (CLAUDE_DIR / "agents" / f"{name}.md")
            dst_dir = CLAUDE_DIR / (f"{kind}s-disabled")
            actions.append(f"shelve {kind} {name} -> {dst_dir}")
            if not dry_run:
                dst_dir.mkdir(parents=True, exist_ok=True)
                dst = dst_dir / src.name
                if dst.exists():
                    shutil.rmtree(dst, ignore_errors=True) if dst.is_dir() else dst.unlink()
                shutil.move(str(src), str(dst))

    if result["stale_projects"] and include_config:
        actions.append(f"drop {len(result['stale_projects'])} stale project records")
        if not dry_run:
            for p in result["stale_projects"]:
                config.get("projects", {}).pop(p, None)
            touched_config = True

    if dry_run or not actions:
        return actions

    manifest = {"at": stamp, "items": result["items"], "stale_projects": result["stale_projects"]}
    if touched_settings:
        manifest["settings_backup"] = _backup(SETTINGS, stamp)
        SETTINGS.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
    if touched_config:
        manifest["config_backup"] = _backup(CONFIG, stamp)
        CONFIG.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        (STATE_DIR / "disabled-mcp.json").write_text(
            json.dumps(disabled_mcp, indent=2) + "\n", encoding="utf-8")
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return actions


def restore() -> int:
    manifest = _load_json(MANIFEST, None)
    if not manifest:
        print("nothing to restore: no undo manifest")
        return 1
    for key, target in (("settings_backup", SETTINGS), ("config_backup", CONFIG)):
        backup = manifest.get(key)
        if backup and Path(backup).exists():
            shutil.copyfile(backup, target)
            print(f"restored {target}")
    for item in manifest.get("items", []):
        kind, name = item["kind"], item["name"]
        if kind not in ("skill", "agent"):
            continue
        src = CLAUDE_DIR / f"{kind}s-disabled" / (name if kind == "skill" else f"{name}.md")
        if src.exists():
            shutil.move(str(src), str(CLAUDE_DIR / f"{kind}s" / src.name))
            print(f"restored {kind} {name}")
    MANIFEST.unlink(missing_ok=True)
    print("Restart Claude Code to pick up the change.")
    return 0


# ---------------------------------------------------------------------------- output

def format_report(result: dict) -> str:
    if not result["items"] and not result["stale_projects"]:
        return "Context baseline is clean: nothing enabled that recent sessions never used."
    lines = [f"Recoverable always-on context: ~{result['recoverable']} tokens per request.", ""]
    # Individual lines earn their space only above a floor; below it the tail is a count,
    # since a report that costs more to read than it saves defeats its own point.
    head = [i for i in result["items"] if i["tokens"] >= REPORT_DETAIL_TOKENS]
    lines += [f"  {i['kind']:7} {i['name']:44} ~{i['tokens']:6} tok   ({i['evidence']})"
              for i in head]
    tail = Counter()
    for i in result["items"][len(head):]:
        tail[i["kind"]] += i["tokens"]
    for kind, tokens in tail.most_common():
        n = sum(1 for i in result["items"][len(head):] if i["kind"] == kind)
        lines.append(f"  {kind:7} {f'+ {n} more, unused {SCAN_DAYS}d':44} ~{tokens:6} tok")
    if result["stale_projects"]:
        lines.append(f"  config  {len(result['stale_projects'])} project records for paths that no longer exist")
    return "\n".join(lines)


def hook_mode() -> None:
    event = _state.read_event()
    if event.get("source") == "resume":
        return  # a resumed session already paid the baseline; nothing to decide

    cached = _load_json(AUDIT_CACHE, {})
    if time.time() - float(cached.get("at", 0)) < AUDIT_TTL:
        return

    result = audit()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_CACHE.write_text(json.dumps({"at": result["at"]}) + "\n", encoding="utf-8")

    try:
        floor = int(os.environ.get("TOKEN_EFFICIENCY_BUDGET_MIN", DEFAULT_MIN_TOKENS))
    except ValueError:
        floor = DEFAULT_MIN_TOKENS
    if result["recoverable"] < floor:
        return

    top = ", ".join(f"{i['name']} (~{i['tokens']} tok)" for i in result["items"][:4])
    if os.environ.get("TOKEN_EFFICIENCY_AUTOFIX", "").strip() not in ("", "0", "false"):
        actions = apply_fix(result, dry_run=False)
        _state.emit_context(
            "SessionStart",
            f"Context budget: pruned {len(actions)} unused item(s) from the always-on "
            f"baseline, ~{result['recoverable']} tokens per request — {top}. Takes effect "
            "next launch; `context_budget.py --restore` undoes it. No need to reply.",
        )
    _state.emit_context(
        "SessionStart",
        f"Context budget: ~{result['recoverable']} tokens of always-on context are loaded "
        f"every request but went unused in the last {SCAN_DAYS} days — {top}. That is paid "
        "again on every tool call of every session. Mention this once if the user has a "
        "moment; `hooks/context_budget.py --fix` prunes it reversibly. Do not act on it "
        "mid-task and do not reply to this otherwise.",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--fix", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--restore", action="store_true")
    parser.add_argument("--include-config", action="store_true",
                        help="also prune ~/.claude.json (MCP servers, stale projects); "
                             "run with Claude Code closed or the edit is overwritten")
    args = parser.parse_args()

    if _state.disabled():
        return 0
    if args.restore:
        return restore()
    if not (args.report or args.fix):
        hook_mode()
        return 0

    result = audit()
    print(format_report(result))
    if not args.fix:
        return 0

    actions = apply_fix(result, args.dry_run, args.include_config)
    print()
    print("\n".join(f"  {'would ' if args.dry_run else ''}{a}" for a in actions) or "  nothing to do")
    if not args.include_config and (result["stale_projects"]
                                    or any(i["kind"] == "mcp" for i in result["items"])):
        print("\n  skipped ~/.claude.json (MCP servers, stale projects) — rerun with "
              "--include-config and Claude Code closed")
    if actions and not args.dry_run:
        print("\nRestart Claude Code to pick up the change. Undo: --restore")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # a hook must never break the session
