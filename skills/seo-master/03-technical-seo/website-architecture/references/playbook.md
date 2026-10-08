# Playbook: Website architecture

## How to do it
1. Map content into hierarchy: home > category > subcategory > page
2. Keep important pages within 3 clicks; URLs mirror hierarchy
3. Use hub pages and breadcrumbs; link hubs to children and back
4. Avoid deep or flat extremes; merge thin branches

## Common problems and fixes
- Orphan sections -> link from hubs and nav
- Duplicate paths to same content -> choose one canonical path

## Output
Architecture diagram and migration notes.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
