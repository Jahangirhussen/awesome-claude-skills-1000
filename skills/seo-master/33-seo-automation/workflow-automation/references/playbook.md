# Playbook: Workflow automation

## How to do it
1. Template-based metadata with variables and human review
2. Schema generator validated before publish
3. Sitemap rebuild on publish; internal link suggestions
4. Log every change

## Common problems and fixes
- Duplicate generated metadata -> add unique attributes

## Output
Automation scripts spec.

## Tools and data sources
Python/Node scripts, cron or CI, GSC/GA4 APIs, Screaming Frog CLI, Slack/email webhooks, version control.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
