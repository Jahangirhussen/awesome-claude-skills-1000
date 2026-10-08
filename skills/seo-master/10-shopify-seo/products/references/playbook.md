# Playbook: Products

## How to do it
1. Unique title/description; handle slugs set early
2. Use product canonical (/products/handle)
3. Optimize images and alt; variants share one URL with ?variant=
4. Add reviews and FAQs

## Common problems and fixes
- Auto-generated meta -> write manually for top products
- Handle changed -> auto 301 exists; update internal links

## Output
Product page checklist.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
