# Playbook: Automated reporting

## How to do it
1. Pull GSC/GA4 via API on schedule
2. Render report template; highlight changes
3. Store history

## Common problems and fixes
- API limits -> incremental pulls

## Output
Report pipeline.

## Tools and data sources
Python/Node scripts, cron or CI, GSC/GA4 APIs, Screaming Frog CLI, Slack/email webhooks, version control.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
