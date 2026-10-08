# Playbook: Indexing monitoring

## How to do it
1. Track GSC indexed pages vs sitemap
2. Alert on spikes in 'excluded' or 'not indexed'
3. Spot-check with URL Inspection

## Common problems and fixes
- Sudden deindex -> check noindex/robots/server

## Output
Indexing log.

## Tools and data sources
GSC, GA4, rank tracker, scheduled crawler, uptime monitor, alerting (Slack/email).

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
