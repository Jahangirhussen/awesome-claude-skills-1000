# Playbook: Data collection

## How to do it
1. Crawl with Screaming Frog/Sitebulb or scripts; set limits
2. Store raw exports for diffing
3. Schedule regular pulls

## Common problems and fixes
- Crawl overload -> throttle

## Output
Data pipeline notes.

## Tools and data sources
GSC API, GA4 Data API, PageSpeed Insights API, DataForSEO, Ahrefs/Semrush APIs, Python or Node scripts.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
