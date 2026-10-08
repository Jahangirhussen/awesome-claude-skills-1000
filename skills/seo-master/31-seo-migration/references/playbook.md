# Playbook: 31. SEO Migration

## How to do it
1. Crawl and snapshot old site (URLs, titles, canonicals, rankings, backlinks)
2. Map every old URL to a new URL 1:1 where possible
3. Stage and test; launch; monitor daily

## Common problems and fixes
- Launching without redirect map -> do not launch

## Output
Migration plan and QA checklist.

## Tools and data sources
Screaming Frog (before/after crawls), redirect mapping sheet, GSC Change of Address, server config, log analysis.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
