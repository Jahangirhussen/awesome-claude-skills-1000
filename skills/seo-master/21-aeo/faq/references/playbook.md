# Playbook: FAQ

## How to do it
1. Use real user questions
2. Visible Q&A on the page; keep answers short
3. FAQPage schema only when allowed (rich results are limited for most sites)

## Common problems and fixes
- Hidden FAQ markup -> remove or make visible

## Output
FAQ block and JSON-LD.

## Tools and data sources
Google SERP (PAA, snippets), GSC queries, AlsoAsked/AnswerThePublic, schema validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
