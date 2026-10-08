# Playbook: Product schema

## How to do it
1. Product with name, image, description, sku, brand, offers
2. Offer: price, priceCurrency, availability, url; add gtin if available
3. AggregateRating/Review only if real, visible
4. Validate; compare to feed values

## Common problems and fixes
- Price mismatch with page -> sync from same source
- Duplicate schema from plugin + theme -> keep one

## Output
Product JSON-LD template.

## Tools and data sources
Screaming Frog, Google Search Console, Merchant Center, Rich Results Test, platform admin, feed validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
