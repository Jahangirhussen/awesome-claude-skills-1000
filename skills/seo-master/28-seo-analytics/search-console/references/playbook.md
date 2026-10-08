# Playbook: Search Console analysis

## How to do it
1. Queries x pages x countries x devices
2. Compare periods; find striking-distance and low-CTR items
3. Use Looker Studio or API for history beyond 16 months

## Common problems and fixes
- Sampling/limits -> API export

## Output
GSC analysis sheet.

## Tools and data sources
GA4, Google Search Console, Looker Studio, GTM, BigQuery export, spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
