# Playbook: Platform migration

## How to do it
1. Preserve URLs/structure when possible
2. Migrate titles, metas, schema, content, images with alt
3. Test staging with crawler vs old crawl
4. Check speed and rendering

## Common problems and fixes
- URL changes unavoidable -> complete 301 map

## Output
Platform migration QA.

## Tools and data sources
Screaming Frog (before/after crawls), redirect mapping sheet, GSC Change of Address, server config, log analysis.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
