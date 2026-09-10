# Worked examples

Concrete before/after transformations for each principle in `SKILL.md`. These are
illustrations, not templates to copy verbatim — the point is the *pattern*, not the
wording.

## Reasoning (thinking blocks)

**Task:** "Is 133 prime?"

Bloated reasoning:
> Let me think about this carefully. First, I'll recall what a prime number is: a
> number greater than 1 with no positive divisors other than 1 and itself. Now let me
> check 133. Is it divisible by 2? No, it's odd. Is it divisible by 3? 1+3+3=7, not
> divisible by 3. Is it divisible by 5? Doesn't end in 0 or 5, so no. Is it divisible
> by 7? 133/7 = 19. So 133 = 7 × 19. Let me double check: 7 × 19 = 7×20 - 7 = 140-7 =
> 133. Yes that's correct. So 133 is not prime. Let me also verify by checking 11:
> 133/11 = 12.09, not a whole number, consistent with what we found. So the final
> answer is that 133 is not prime, since it factors as 7 × 19.

Efficient reasoning:
> 133 = 7 × 19 (7×19=133 ✓.) Not prime.

The efficient version checks divisibility by the one factor that resolves it,
confirms with a single multiplication, and stops. It doesn't re-verify with a second
divisor once the answer is certain, and it doesn't narrate the definition of "prime"
back to itself.

## Prose responses

**Task:** "Does this repo use Poetry or pip?"

Bloated:
> Great question! Let's take a look at the repository to figure this out. Dependency
> management is an important part of any Python project, and there are several tools
> commonly used, including pip with requirements.txt, Poetry with pyproject.toml, and
> others like PDM or Hatch. In order to determine which one this project uses, I
> checked the root directory for the relevant marker files. I found a `pyproject.toml`
> file with a `[tool.poetry]` section, which indicates that this project uses Poetry
> for dependency management rather than plain pip with a requirements.txt file. I hope
> this helps! Let me know if you have any other questions about the project setup.

Efficient:
> Poetry — `pyproject.toml` has a `[tool.poetry]` section.

The efficient version leads with the answer, gives exactly the one piece of evidence
needed to trust it, and skips the tour of alternative tools the user didn't ask about.

## Code changes

**Task:** "Change the default timeout to 30s in `parse_config`."

Bloated response: pastes the entire `config.py` file back with one line changed, then
re-explains what the whole file does underneath it.

Efficient response: a single targeted edit —

```diff
- DEFAULT_TIMEOUT = 10
+ DEFAULT_TIMEOUT = 30
```

with one line of prose: "Bumped `DEFAULT_TIMEOUT` in `parse_config` (config.py:14) to
30." No restatement of the surrounding function, no re-paste of unrelated code.

## Agentic tool use

**Task:** "Find where `retry_count` is used and bump the default to 5."

Bloated trajectory:
> 1. Read the entire `config.py` (400 lines) top to bottom looking for `retry_count`.
> 2. Find it on line 212, edit it.
> 3. Read `config.py` again to confirm the edit landed.
> 4. Read three unrelated files "just in case they also reference it."
> 5. Reply by pasting the full new `config.py` back into the chat.

Efficient trajectory:
> 1. Grep for `retry_count` across the repo — two hits: `config.py:212` (the default)
>    and `client.py:88` (a call site that doesn't need changing).
> 2. Edit `config.py:212` directly with a targeted diff.
> 3. Reply: "Bumped the default in `config.py:212` from 3 to 5. `client.py:88` calls
>    it but doesn't hardcode the value, so no change needed there."

The efficient version searches instead of reading blind, trusts the edit tool instead
of re-reading to confirm, doesn't chase files with no evidence they're relevant, and
reports the change by location instead of re-pasting the file.

**Task:** "Check whether the staging and prod configs match, and run the test suite."

Bloated: reads the staging config, summarizes it in prose, reads the prod config,
summarizes it in prose, then does a third pass narrating a manual diff — three serial
tool calls where two could have run together, followed by a summary long enough to
re-derive the diff from scratch. Then runs the full test suite, then reruns it a
second time "to double check" even though nothing changed and it passed cleanly the
first time.

Efficient: reads both config files in the same turn (they don't depend on each
other), diffs them directly, and reports only the deltas: "Configs match except
`timeout_ms` (staging: 2000, prod: 5000)." Runs the test suite once; since it passed
and nothing changed afterward, does not rerun it.

## Context management

**Task:** "Migrate all 30 API handlers off the deprecated `AuthClient`."

Bloated trajectory: reads all 30 handler files up front "to understand the shape of the
work," then starts editing. By handler 12 the window holds 30 full files plus 12 diffs,
the model has started re-reading files it already saw because it no longer trusts what's
in context, and a compaction lands mid-task — taking with it the two exceptions
discovered at handler 4 that were never written down. Those get rediscovered the
expensive way.

Efficient trajectory:
> 1. Grep for `AuthClient` — 30 files, with the call-site line for each.
> 2. Read *one* handler in full to learn the pattern. Write `migration-notes.md`: the
>    transformation, the file list with checkboxes, and an "exceptions" section.
> 3. Migrate in batches, reading only the relevant line range of each file. Append any
>    exception to the notes file the moment it's found.
> 4. After each batch, the durable state is the notes file — not the context window.

The efficient version retrieves just-in-time instead of just-in-case, keeps the
load-bearing state in a file that survives compaction, and never carries 30 full files
of raw evidence forward when a 30-line checklist encodes the same thing.

**Task:** "Which of our services still talk to the legacy billing DB?"

Bloated: greps across a large monorepo, gets 400 hits, and pulls all of them into the
main context to sift through — after which every subsequent turn in the session reasons
around 400 lines of mostly-irrelevant match output.

Efficient: dispatches a subagent to run the search and return just the service names
with one example call site each. The raw 400 hits live and die in the subagent's
context; the main session receives eight lines. This is a context decision, not a
parallelism one — it would be worth doing even if it were slower.

## Non-code work (writing, research, analysis)

The same patterns, outside code — most users are not editing repos.

**Task:** "Summarize this 12-page vendor contract — anything I should worry about?"

Bloated: a section-by-section retelling of the whole contract, most of it standard
boilerplate, with the two real issues buried in paragraphs six and nine.

Efficient:
> Two things to worry about: (1) auto-renewal with a 90-day cancellation notice
> (§7.2) — miss the window and you're locked in for another year; (2) liability is
> capped at one month's fees (§11), which is unusually low for this contract size.
> Everything else is standard terms.

The reader asked "what should I worry about," so the deliverable is the worry list —
not proof that every page was read.

**Task:** "Draft an email asking my landlord to fix the heating."

Bloated: three paragraphs of context-setting, apologies for bothering them, a
history of the tenancy, and the actual request in the final paragraph.

Efficient: subject line stating the issue, one sentence of specifics (since when,
which rooms), the request with a reasonable deadline, and a closing line. The
reader should know what's being asked before the first scroll.

**Task:** "Which of these two phone plans is cheaper for me? I use about 8GB a month."

Bloated: a full feature-by-feature comparison table of both plans — coverage, hotspot
policy, international rates — followed by the answer.

Efficient: "Plan B — at 8GB you'd pay $35 vs Plan A's $45. Plan A only wins above
~15GB/month." The comparison the user asked for is a decision, not a table; the one
crossover fact is the only extra detail that earns its place.

## Common filler to cut

| Filler | Why it adds nothing |
|---|---|
| "It's worth noting that..." | The note is either worth including (say it directly) or not (cut it). |
| "In order to..." | Almost always shortens to "to". |
| "As mentioned previously..." | Either the reader remembers, or repeat the fact plainly without the pointer. |
| "I hope this helps!" | Closing filler with no information. |
| "Please let me know if you have any questions." | Implicit in every conversational turn; doesn't need restating. |
| "Let's dive into..." / "Let's take a look at..." | Announces an action instead of doing it. |
| "Certainly! I'd be happy to help with that." | Restates agreement to do the thing you're about to do anyway. |

## Where NOT to apply this (guardrail examples)

- User: "Will this migration lock the table?" — even if the answer is "no", keep the
  one-sentence caveat about the specific condition under which it *would* lock. That
  caveat is safety-relevant, not filler.
- User: "Set up auth for this endpoint" with no framework specified — one clarifying
  question here (which auth scheme, or which framework) is cheaper than guessing
  wrong and redoing the work.
- User: "Give me a thorough security review of this diff" — this is an explicit
  request for depth; don't apply brevity defaults against it.
- After making a risky change (a migration, a config touching prod) — actually run
  the test/build/check rather than skipping it to save a tool call and asserting it
  probably works. A wrong "it works" costs a full debugging round-trip; the check
  itself is cheap by comparison.
- When dispatching a subagent — include the specific file paths, prior findings, and
  constraints it needs, even though that lengthens the prompt. A subagent that has to
  re-discover context you already had costs more (its own searches, plus a follow-up
  round-trip if it guesses wrong) than the extra context would have.
