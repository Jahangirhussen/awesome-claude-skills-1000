---
name: tdd
description: Enforce test-driven development (write the test first, watch it fail, then make it pass) for production code, bug fixes, and refactors. Make sure to use this skill WHENEVER writing or changing production code, fixing a bug, or refactoring — even outside a formal spec-driven workflow, and even if the user doesn't say "test". It is reusable on its own. Do NOT force it on exploratory/throwaway/analysis code where the correct output isn't known in advance (there, use data-validation, regression/snapshot, and reproducibility checks instead — this skill explains that alternative).
---

# Test-Driven Development (TDD)

Write tests before the code, so the code is shaped by what "correct" means rather than the other way around.

## Interaction contract

Explain each step in plain words as you go. TDD is unfamiliar to many people; narrate *why* each step matters, not just what.

## When TDD applies vs. when it doesn't

- **Applies:** production code — anything that must keep working and that others depend on (services, scheduled pipelines, dashboards, libraries), plus bug fixes and refactors.
- **Does NOT apply:** exploratory or throwaway code where you don't yet know the right answer. You can't write a meaningful failing test for a result you haven't discovered. Say so, and use the alternative below.

## The cycle: red → green → refactor

1. **Red — write a failing test first.** From the requirement or contract, write a test for the behavior you want. Run it and **confirm it fails.** This is the crux: a test that passes before you've written anything (or can't fail) proves nothing — it's the most common way AI-written tests go wrong.
2. Commit the failing test as a checkpoint (optional but recommended).
3. **Green — write the minimum code to pass.** Just enough. Do **not** edit the test to make it pass; the test is the specification.
4. **Refactor — improve the code without changing behavior.** Tests stay green.
5. Repeat for the next behavior.

## What makes a good test

- Tests **behavior and contract**, not internal implementation details (so refactors don't break it needlessly).
- Uses realistic inputs. For anything data-related, prefer **fixtures of real, frozen data** over **mocks** (fake stand-in objects) — mocks often test that your mock works, not that your code does.
- Covers the failure modes, not just the happy path. For production/scheduled code, the highest-value tests are usually: runs-twice-safely (idempotency), bad-input-is-handled, and boundary/edge cases.
- Each test's name states the behavior it checks, so a failure is self-explaining.

## The alternative for exploratory / analysis code

When TDD doesn't fit, keep discipline a different way:
- **Data validation** — assert schemas, ranges, nulls, counts on inputs and outputs.
- **Regression / snapshot** — freeze a known-good result and detect unintended drift when you change the pipeline.
- **Property / sanity checks** — general truths that must hold (probabilities sum to 1; an interval contains its point estimate).
- **Reproducibility** — fixed seeds, pinned dependency versions, a lockfile.

Offer these explicitly when the user is in exploratory territory, so "no TDD here" doesn't mean "no rigor here."
