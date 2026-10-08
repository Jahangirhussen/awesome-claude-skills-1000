# Playbook: 10. Shopify SEO

## How to do it
1. Review theme (Liquid) for H1, meta, canonical, schema
2. Audit collections/products URL patterns and duplicates
3. Review apps injecting scripts/schema
4. Check robots.txt.liquid and sitemap

## Common problems and fixes
- Duplicate product URLs via /collections/ path -> theme should use product canonical
- App bloat -> remove unused apps

## Output
Shopify SEO issue list.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
