# Playbook: Keyword tracking

## How to do it
1. Track by segment: brand, non-brand, money pages, locations
2. Use consistent device/location settings
3. Annotate algorithm updates

## Common problems and fixes
- Daily noise -> weekly averages

## Output
Rank tracker sheet.

## Tools and data sources
GA4, Google Search Console, Looker Studio, GTM, BigQuery export, spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
