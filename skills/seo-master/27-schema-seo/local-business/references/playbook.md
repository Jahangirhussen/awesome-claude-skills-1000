# Playbook: LocalBusiness

## How to do it
1. Use specific subtype (e.g. Dentist); address, geo, openingHoursSpecification, telephone, priceRange
2. Match GBP and visible NAP
3. One entity per location

## Common problems and fixes
- Mismatched hours -> sync sources

## Output
LocalBusiness JSON-LD.

## Tools and data sources
Rich Results Test, Schema Markup Validator (validator.schema.org), GSC Enhancements, JSON-LD generator or code.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
