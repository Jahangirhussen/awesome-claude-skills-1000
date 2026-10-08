# Playbook: Shopify technical

## How to do it
1. Review theme.liquid canonical and meta robots
2. Edit robots.txt.liquid carefully (can add disallow rules)
3. Check sitemap.xml index structure
4. Speed: reduce apps, defer scripts, compress images

## Common problems and fixes
- Duplicate pages from /collections/x/products/y -> canonical
- Slow theme -> audit sections and app scripts

## Output
Technical checklist.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
