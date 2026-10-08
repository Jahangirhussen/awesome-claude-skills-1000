# Playbook: Voice and conversational

## How to do it
1. Use natural-language questions and short answers
2. Local intent: hours, near me, directions
3. Fast mobile pages

## Common problems and fixes
- No local data -> complete GBP

## Output
Conversational query list.

## Tools and data sources
Google SERP (PAA, snippets), GSC queries, AlsoAsked/AnswerThePublic, schema validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
