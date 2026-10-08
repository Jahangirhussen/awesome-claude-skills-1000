# Playbook: 32. SEO Monitoring

## How to do it
1. Baseline metrics; define thresholds
2. Monitor rankings, indexing, traffic, CWV, errors, backlinks, AI visibility
3. Diagnose cause before acting

## Common problems and fixes
- Alert fatigue -> tune thresholds

## Output
Monitoring setup and alert rules.

## Tools and data sources
GSC, GA4, rank tracker, scheduled crawler, uptime monitor, alerting (Slack/email).

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
