# Always-on layer

A skill body is model-invoked: only its `name` and `description` sit in context, and
the model decides whether to load the rest. That is the right design for a workflow
skill, and the wrong one for a skill whose whole premise is "apply this to every
response" — it fires on the first turn and drifts out of effect over a long session.

These hooks close that gap. They run in the harness, not the model, so they are
deterministic rather than advisory.

| Hook | Event | What it does |
|---|---|---|
| `efficiency_core.py` | `UserPromptSubmit` | Re-injects the core contract every turn. Full text on turn 1 and every 10th turn, one line otherwise, and the depth *guardrail* instead of the brevity rules when the prompt asks for thoroughness (detected in 12+ languages: EN, RU, UK, ES, PT, IT, FR, DE, ZH, JA, KO). |
| `trajectory_guard.py` | `PostToolUse` | Watches the trajectory and speaks only on a concrete waste pattern: re-reading an unchanged range, reading a file back after this turn's own edit, reading a large file whole with no prior search, or re-running a build/test that already ran. |
| `session_report.py` | `Stop` | On every task completion, parses the transcript and shows the user a one-line usage report — wall-clock time, input/output tokens, cache hit rate, tool calls — plus one targeted optimization tip. Sent as `systemMessage`, so it displays in the terminal but costs zero model tokens. Also appends per-turn metrics to `~/.claude/state/token-efficiency/metrics.jsonl`, and reports accumulated waste into the conversation only once enough of it has piled up to be worth saying. |

The injection budget is deliberately small: roughly 130 tokens on a refresh turn and 35
on the others. A hook that re-sent the whole `SKILL.md` every turn would cost more than
the behaviour it buys.

## Install

```bash
python hooks/install.py --dry-run   # inspect the resulting hooks block
python hooks/install.py             # write it, after backing up settings.json
```

Additive and idempotent: existing hooks on the same events are kept, and re-running
replaces this skill's entries instead of stacking duplicates. Point it elsewhere with
`--settings PATH` (e.g. a project's `.claude/settings.json`), and undo with
`--uninstall`. Restart Claude Code afterwards.

The commands are written with the `python` that ran `install.py`, so run it with the
interpreter you want the hooks to use.

## Tuning

| Env var | Default | Effect |
|---|---|---|
| `TOKEN_EFFICIENCY_OFF` | unset | `1` disables all three hooks — used by `evals/measure.py` for the baseline arm |
| `TOKEN_EFFICIENCY_TASK_REPORT` | `1` | `0` disables the per-task usage report shown after each completed task |
| `TOKEN_EFFICIENCY_REFRESH` | `10` | Re-inject the full contract every N turns |
| `TOKEN_EFFICIENCY_MAX_WARN` | `12` | Cap trajectory warnings per session |
| `TOKEN_EFFICIENCY_REPORT_AT` | `3` | New waste events required before the `Stop` report speaks |

## Design notes

- **Every warning is checkable.** The guard never says "that felt verbose" — it fires
  on a fact it can point at (this range, that turn, this command). Advisory nagging
  from a hook is worse than no hook, because it costs tokens on every false positive.
- **False positives were designed out, not tuned out.** An `Edit`/`Write` clears the
  read record for that path, so re-reading genuinely changed content is silent. The
  rerun check ignores cheap, legitimately-repeated commands like `git status` and only
  matches build/test/lint runners.
- **State is advisory.** Batched tool calls in one turn race on read-modify-write, so
  an occasional lost update just means one missed warning. Nothing about the session
  depends on `~/.claude/state/token-efficiency/`; deleting it is always safe, and files
  older than 7 days are pruned automatically.
- **The hooks never break the session.** Every entry point swallows exceptions and
  exits 0. A malformed payload produces silence, not a failed turn.
