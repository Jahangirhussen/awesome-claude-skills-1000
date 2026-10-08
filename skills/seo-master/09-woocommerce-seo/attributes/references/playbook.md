# Playbook: Attributes

## How to do it
1. Decide which attribute archives are useful (brand, size)
2. Noindex low-value attribute archives
3. Make useful ones real landing pages with content

## Common problems and fixes
- Thousands of attribute URLs -> noindex or disable archives
- Duplicate content with filters -> canonicalize

## Output
Attribute indexing policy.

## Tools and data sources
WooCommerce admin, Yoast/Rank Math, Query Monitor, Screaming Frog, WP-CLI, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
