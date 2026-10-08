# Playbook: Scraping (compliant)

## How to do it
1. Respect robots.txt and terms; rate-limit
2. Prefer APIs and official exports
3. Cache results; identify user agent

## Common problems and fixes
- Blocked -> do not evade; use API

## Output
Scraper spec.

## Tools and data sources
GSC API, GA4 Data API, PageSpeed Insights API, DataForSEO, Ahrefs/Semrush APIs, Python or Node scripts.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
