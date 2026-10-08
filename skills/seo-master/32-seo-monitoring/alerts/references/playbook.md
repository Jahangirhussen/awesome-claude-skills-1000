# Playbook: Alerts

## How to do it
1. Define thresholds (clicks -20% week over week, indexed -10%, 5xx > 1%)
2. Route to owner with runbook link
3. Review monthly

## Common problems and fixes
- Too noisy -> raise thresholds

## Output
Alert rules.

## Tools and data sources
GSC, GA4, rank tracker, scheduled crawler, uptime monitor, alerting (Slack/email).

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
