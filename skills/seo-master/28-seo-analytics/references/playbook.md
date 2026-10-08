# Playbook: 28. SEO Analytics

## How to do it
1. Verify GA4 and GSC tracking
2. Segment organic by landing page, brand vs non-brand, device
3. Report trends with annotations (releases, updates)

## Common problems and fixes
- Unattributed traffic -> UTM/consent issues

## Output
SEO report template.

## Tools and data sources
GA4, Google Search Console, Looker Studio, GTM, BigQuery export, spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
