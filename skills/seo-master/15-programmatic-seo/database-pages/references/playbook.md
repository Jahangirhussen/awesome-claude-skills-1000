# Playbook: Database-driven pages

## How to do it
1. Clean, accurate data source with update process
2. Set quality thresholds; noindex incomplete entries
3. Pagination and internal linking from hubs

## Common problems and fixes
- Stale data -> schedule refresh
- Duplicate entities -> dedupe

## Output
Data schema and indexing rules.

## Tools and data sources
Dataset or database, template engine, Screaming Frog, GSC (indexing), sitemap generator, QA sampling script.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
