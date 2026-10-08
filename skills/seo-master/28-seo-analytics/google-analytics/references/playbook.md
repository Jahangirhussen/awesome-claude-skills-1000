# Playbook: GA4

## How to do it
1. GA4: confirm key events and conversions
2. Explore organic landing pages, engagement, revenue
3. Link GA4 with GSC

## Common problems and fixes
- Consent mode losing data -> note in reports

## Output
GA4 organic dashboard.

## Tools and data sources
GA4, Google Search Console, Looker Studio, GTM, BigQuery export, spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.

## Example
Organic landing-page report in GA4 Explore: dimension `Landing page + query string`, filter `Session default channel group = Organic Search`, metrics `Sessions, Engaged sessions, Key events, Total revenue`. Compare with GSC clicks per page; large gaps point to tracking, consent, or redirect issues.
