# Playbook: E-commerce audit

## How to do it
1. Review categories, products, facets, variants, schema, feed
2. Platform specifics (Woo, Shopify)
3. Index bloat and duplicate content

## Common problems and fixes
- Thin supplier copy -> rewrite top sellers first

## Output
E-commerce audit sheet.

## Tools and data sources
Screaming Frog, GSC, GA4, Lighthouse, Ahrefs/Semrush, schema validator, platform-specific plugins.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
