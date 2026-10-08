# Playbook: Backlink analysis

## How to do it
1. Export referring domains and anchors
2. Segment by authority, relevance, follow/nofollow, country
3. Find top linked pages and lost/broken links to reclaim
4. Check anchor distribution is natural (mostly brand/URL)

## Common problems and fixes
- Lost valuable links -> contact site, restore page or 301
- Spammy sudden spike -> monitor, disavow only if harmful

## Output
Backlink profile summary and reclaim list.

## Tools and data sources
Ahrefs, Semrush, Majestic, Google Search Console Links report, Google Alerts, outreach CRM or spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
