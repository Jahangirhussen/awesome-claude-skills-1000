# Playbook: Core updates and volatility

## How to do it
1. Get update dates from Google Search Status Dashboard
2. Overlay GSC clicks on dates; segment by page type and query class
3. Compare winners vs losers on intent match, expertise, UX, ads, content freshness
4. Improve content quality and E-E-A-T on affected sections; wait for next update to judge

## Common problems and fixes
- Tempted to change everything -> change only affected segment, log changes
- No recovery in weeks -> normal; recoveries often arrive with later updates

## Output
Impact analysis: affected segments, hypotheses, actions.

## Tools and data sources
Google Search Console (+API), GA4, URL Inspection tool, Search Status Dashboard, Looker Studio.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
