# Playbook: Technical audit

## How to do it
1. Crawl + GSC indexing + CWV + log files if available
2. Triage by SEO impact (not by error count)
3. Group by root cause (template, plugin, server)

## Common problems and fixes
- Thousands of identical errors -> fix once at template

## Output
Technical findings table.

## Tools and data sources
Screaming Frog, GSC, GA4, Lighthouse, Ahrefs/Semrush, schema validator, platform-specific plugins.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
