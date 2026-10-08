# Playbook: Product schema in Woo

## How to do it
1. Use one schema source (Woo core, Yoast WooCommerce, or Rank Math)
2. Verify price, availability, reviews match page
3. Validate variations schema

## Common problems and fixes
- Schema duplicates -> disable extra output
- Reviews missing -> enable verified-owner reviews

## Output
Schema validation report.

## Tools and data sources
WooCommerce admin, Yoast/Rank Math, Query Monitor, Screaming Frog, WP-CLI, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
