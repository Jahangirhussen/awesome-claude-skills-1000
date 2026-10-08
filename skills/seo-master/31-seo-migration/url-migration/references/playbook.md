# Playbook: URL migration

## How to do it
1. Build mapping file (old, new, status)
2. Single-hop 301; update internal links/sitemaps
3. Avoid chains; handle query strings

## Common problems and fixes
- Mass redirect to homepage -> map to relevant pages

## Output
Redirect map.

## Tools and data sources
Screaming Frog (before/after crawls), redirect mapping sheet, GSC Change of Address, server config, log analysis.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
