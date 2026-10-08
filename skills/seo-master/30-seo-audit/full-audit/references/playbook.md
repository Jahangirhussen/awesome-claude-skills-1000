# Playbook: Full audit

## How to do it
1. Crawl site; pull GSC/GA4
2. Run technical, on-page, content, link, schema, performance checks
3. Merge duplicates between modules
4. Deliver prioritized fix list

## Common problems and fixes
- Huge sites -> sample by template

## Output
Full audit report.

## Tools and data sources
Screaming Frog, GSC, GA4, Lighthouse, Ahrefs/Semrush, schema validator, platform-specific plugins.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
