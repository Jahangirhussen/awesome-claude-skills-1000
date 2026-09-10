"""Wire the token-efficiency hooks into Claude Code settings.json.

Idempotent and additive: existing hooks on the same events are preserved. Our own
entries are identified by the hooks directory in their command string, so re-running
replaces them rather than stacking duplicates.

    python install.py                 # install into ~/.claude/settings.json
    python install.py --dry-run       # print the resulting hooks block, write nothing
    python install.py --uninstall     # remove only our entries
    python install.py --settings PATH # target a different settings file
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

HOOKS_DIR = Path(__file__).resolve().parent
MARKER = "token-efficiency"

ENTRIES = [
    ("SessionStart", None, "context_budget.py"),
    ("UserPromptSubmit", None, "efficiency_core.py"),
    ("PostToolUse", "Read|Edit|Write|MultiEdit|NotebookEdit|Grep|Glob|Bash", "trajectory_guard.py"),
    ("Stop", None, "session_report.py"),
]


def _quote(value: str) -> str:
    # Always quote: hook commands run through a shell, and on Windows an unquoted
    # backslash path gets eaten as escaping (C:\Python314\python.exe ->
    # C:Python314python.exe: command not found).
    return f'"{value}"'


def _command(script: str) -> str:
    return f"{_quote(sys.executable)} {_quote(str(HOOKS_DIR / script))}"


def _is_ours(entry: dict) -> bool:
    return any(
        MARKER in str(h.get("command", "")).replace("\\", "/")
        for h in entry.get("hooks", [])
    )


def build_hooks(existing: dict, uninstall: bool) -> dict:
    hooks = {event: [e for e in entries if not _is_ours(e)]
             for event, entries in (existing or {}).items()}
    if uninstall:
        return {k: v for k, v in hooks.items() if v}

    for event, matcher, script in ENTRIES:
        entry = {"hooks": [{"type": "command", "command": _command(script)}]}
        if matcher:
            entry["matcher"] = matcher
        hooks.setdefault(event, []).append(entry)
    return hooks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--settings", type=Path, default=Path.home() / ".claude" / "settings.json")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    args = parser.parse_args()

    settings = {}
    if args.settings.exists():
        try:
            settings = json.loads(args.settings.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"error: {args.settings} is not valid JSON ({exc}); refusing to overwrite it")
            return 1

    settings["hooks"] = build_hooks(settings.get("hooks", {}), args.uninstall)

    if args.dry_run:
        print(json.dumps(settings["hooks"], indent=2))
        return 0

    args.settings.parent.mkdir(parents=True, exist_ok=True)
    if args.settings.exists():
        backup = args.settings.with_suffix(".json.bak")
        shutil.copyfile(args.settings, backup)
        print(f"backed up {args.settings} -> {backup}")

    args.settings.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
    action = "removed from" if args.uninstall else "installed into"
    print(f"token-efficiency hooks {action} {args.settings}")
    print("Restart Claude Code (or start a new session) to pick up the change.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
