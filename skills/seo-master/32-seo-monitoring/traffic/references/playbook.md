# Playbook: Traffic diagnosis

## How to do it
1. Annotate drop date; compare GSC vs GA4
2. Segment by page group, query type, device, country
3. Match with deploys and algorithm updates
4. Pick cause before changing things

## Common problems and fixes
- Tracking broken -> verify GA4 tag before panic

## Output
Traffic diagnosis memo.

## Tools and data sources
GSC, GA4, rank tracker, scheduled crawler, uptime monitor, alerting (Slack/email).

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
