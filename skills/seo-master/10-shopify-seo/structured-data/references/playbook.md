# Playbook: Shopify structured data

## How to do it
1. Use theme product JSON-LD or a single app
2. Validate Product/Offer/Review
3. Add Organization and WebSite schema

## Common problems and fixes
- Duplicate schema -> disable one source
- Rating without reviews -> remove

## Output
Schema validation results.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
