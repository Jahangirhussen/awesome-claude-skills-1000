# Playbook: Shopify migration

## How to do it
1. Export URLs, redirects, and rankings from the old site
2. Match handles where possible; build 301 map via Online Store > Navigation > URL redirects
3. Migrate meta, content, images with alt
4. Monitor GSC after launch

## Common problems and fixes
- Traffic drop after launch -> compare crawl, fix missing redirects
- Blog URL structure change (/blogs/news/) -> map carefully

## Output
Migration redirect map and QA.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
