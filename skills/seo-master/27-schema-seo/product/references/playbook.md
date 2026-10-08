# Playbook: Product and Offer

## How to do it
1. Product: name, image, description, sku, brand; offers with price, priceCurrency, availability
2. Add gtin/mpn when available
3. AggregateRating only with real visible reviews

## Common problems and fixes
- Price missing in page -> show it

## Output
Product JSON-LD.

## Tools and data sources
Rich Results Test, Schema Markup Validator (validator.schema.org), GSC Enhancements, JSON-LD generator or code.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
