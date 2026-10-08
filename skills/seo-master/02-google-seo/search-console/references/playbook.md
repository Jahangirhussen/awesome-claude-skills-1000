# Playbook: Search Console

## How to do it
1. Performance: filter by query/page/country/device, compare 3 months vs previous
2. Find striking-distance queries (position 8-20) and low-CTR high-impression pages
3. Page indexing: group 'not indexed' reasons, fix biggest group first
4. Sitemaps: submitted vs indexed counts
5. Export via API for large sites (1000-row UI limit)

## Common problems and fixes
- CTR low at good position -> rewrite title/meta, check SERP features
- Brand queries inflate results -> filter brand terms with regex

## Output
Opportunity sheet: query/page, impressions, CTR, position, action.

## Tools and data sources
Google Search Console (+API), GA4, URL Inspection tool, Search Status Dashboard, Looker Studio.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
