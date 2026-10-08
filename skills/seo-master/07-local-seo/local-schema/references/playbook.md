# Playbook: Local schema

## How to do it
1. Add LocalBusiness (or specific subtype) JSON-LD
2. Include name, address, geo, telephone, openingHours, url, sameAs
3. Match visible NAP exactly
4. Validate in Rich Results Test

## Common problems and fixes
- Multiple locations -> one entity per location page
- Schema differs from GBP -> align

## Output
LocalBusiness JSON-LD per location.

## Tools and data sources
Google Business Profile, Local Falcon or geo-grid tool, BrightLocal/Whitespark, Google Maps, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
