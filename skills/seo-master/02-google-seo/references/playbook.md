# Playbook: 02. Google SEO

## How to do it
1. Verify GSC property ownership (domain property preferred) and GA4 link
2. Read Performance, Pages/Indexing, Sitemaps, Core Web Vitals, Manual actions & Security
3. Cross-check with URL Inspection on key URLs

## Common problems and fixes
- No data -> property not verified or new site; wait and check sitemap submission
- Sudden drop -> check indexing, manual actions, then update dates

## Output
Findings list: issue, evidence (GSC report/URL), fix, expected effect.

## Tools and data sources
Google Search Console (+API), GA4, URL Inspection tool, Search Status Dashboard, Looker Studio.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
