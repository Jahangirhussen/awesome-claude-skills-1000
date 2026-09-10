"""A/B harness: measure what the token-efficiency skill and hooks actually cost.

Each eval prompt is run headless twice — once with the skill and hooks active, once
with both suppressed — against a fresh disposable copy of the sample repo, repeated N
times because model variance across single runs is larger than the effect being
measured. Reports the median of each arm.

    python measure.py                    # 3 reps per arm, all evals
    python measure.py --reps 5           # more reps, tighter medians
    python measure.py --only 0 2         # just those eval ids
    python measure.py --json out.json    # also dump raw per-run records

Requires the `claude` CLI on PATH and an authenticated session.

WARNING: runs the agent with --dangerously-skip-permissions so it can edit files
without prompting. It only ever points at a throwaway copy under
token-efficiency-workspace/, never the real repo — but don't run it on a machine where
that flag is unacceptable.
"""

import argparse
import json
import os
import shutil
import statistics
import subprocess
import sys
import time
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent
SKILL_DIR = EVALS_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent
WORKSPACE = REPO_ROOT / "token-efficiency-workspace"
SAMPLE_REPO = WORKSPACE / "sample-repo"

# Metrics where lower is better, in the order they are reported.
METRICS = ["output_tokens", "num_turns", "duration_s", "cost_usd"]


def prepare_run_dir(tag: str) -> Path:
    run_dir = WORKSPACE / f"run-{tag}"
    if run_dir.exists():
        shutil.rmtree(run_dir, ignore_errors=True)
    shutil.copytree(
        SAMPLE_REPO,
        run_dir / "sample-repo",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    return run_dir


def run_with_retry(prompt: str, run_dir: Path, skill_on: bool, timeout: int,
                   attempts: int = 4, backoff: int = 20) -> dict:
    """Back-to-back headless runs get throttled (HTTP 403); retry those with backoff."""
    for attempt in range(attempts):
        result = run_once(prompt, run_dir, skill_on, timeout)
        if not result.get("throttled"):
            return result
        if attempt < attempts - 1:
            wait = backoff * (attempt + 1)
            print(f"    throttled, retrying in {wait}s ...", flush=True)
            time.sleep(wait)
    return result


def run_once(prompt: str, run_dir: Path, skill_on: bool, timeout: int) -> dict:
    env = dict(os.environ)
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "json",
        "--dangerously-skip-permissions",
        "--add-dir", str(run_dir),
    ]
    if not skill_on:
        env["TOKEN_EFFICIENCY_OFF"] = "1"
        cmd += ["--disallowedTools", "Skill"]
    else:
        env.pop("TOKEN_EFFICIENCY_OFF", None)

    started = time.time()
    proc = subprocess.run(
        cmd, cwd=run_dir, env=env, capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=timeout,
    )
    elapsed = time.time() - started

    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError:
        if proc.returncode != 0:
            return {"error": (proc.stderr or proc.stdout or "").strip()[:400]}
        return {"error": f"unparseable CLI output: {proc.stdout[:200]}"}

    if result.get("is_error") or proc.returncode != 0:
        return {
            "error": str(result.get("result") or proc.stderr)[:200],
            "throttled": result.get("api_error_status") in (403, 429, 529),
        }

    usage = result.get("usage") or {}
    return {
        "output_tokens": usage.get("output_tokens", 0),
        "input_tokens": usage.get("input_tokens", 0),
        "cache_read_tokens": usage.get("cache_read_input_tokens", 0),
        "num_turns": result.get("num_turns", 0),
        "cost_usd": round(result.get("total_cost_usd", 0.0), 4),
        "duration_s": round(elapsed, 1),
        "reply_chars": len(result.get("result", "") or ""),
    }


def median_of(runs: list, key: str):
    values = [r[key] for r in runs if key in r and isinstance(r[key], (int, float))]
    return round(statistics.median(values), 4) if values else None


def format_delta(on, off) -> str:
    if not on or not off:
        return "n/a"
    pct = (on - off) / off * 100
    return f"{pct:+.0f}%"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reps", type=int, default=3)
    parser.add_argument("--only", type=int, nargs="*")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--delay", type=int, default=8,
                        help="seconds to pause between runs so the CLI isn't throttled")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    if shutil.which("claude") is None:
        print("error: `claude` CLI not found on PATH")
        return 1
    if not SAMPLE_REPO.exists():
        print(f"error: sample repo missing at {SAMPLE_REPO}")
        return 1

    evals = json.loads((EVALS_DIR / "evals.json").read_text(encoding="utf-8"))["evals"]
    if args.only:
        evals = [e for e in evals if e["id"] in args.only]

    records, rows = [], []
    for ev in evals:
        arms = {}
        for arm, skill_on in (("on", True), ("off", False)):
            runs = []
            for rep in range(args.reps):
                tag = f"{ev['id']}-{arm}-{rep}"
                run_dir = prepare_run_dir(tag)
                prompt = ev["prompt"].replace("<RUN_DIR>", run_dir.name)
                print(f"  [{ev['eval_name']}] {arm} rep {rep + 1}/{args.reps} ...", flush=True)
                try:
                    result = run_with_retry(prompt, run_dir, skill_on, args.timeout)
                except subprocess.TimeoutExpired:
                    result = {"error": f"timed out after {args.timeout}s"}
                if "error" in result:
                    print(f"    failed: {result['error']}")
                time.sleep(args.delay)
                result.update(eval=ev["eval_name"], arm=arm, rep=rep)
                runs.append(result)
                records.append(result)
                shutil.rmtree(run_dir, ignore_errors=True)
            arms[arm] = runs
        rows.append((ev["eval_name"], arms))

    print("\n| eval | metric | skill on | skill off | delta |")
    print("|---|---|---|---|---|")
    for name, arms in rows:
        for metric in METRICS:
            on, off = median_of(arms["on"], metric), median_of(arms["off"], metric)
            print(f"| {name} | {metric} | {on} | {off} | {format_delta(on, off)} |")

    print(
        "\nDelta is skill-on relative to skill-off; negative is cheaper. Medians over "
        f"{args.reps} rep(s) — treat anything under ~10% as noise and raise --reps."
    )

    if args.json:
        args.json.write_text(json.dumps(records, indent=2), encoding="utf-8")
        print(f"raw runs written to {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
