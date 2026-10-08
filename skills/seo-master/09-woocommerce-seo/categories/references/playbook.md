# Playbook: Categories

## How to do it
1. Edit category descriptions and titles in SEO plugin
2. Control pagination and 'products per page'
3. Hide empty categories from nav
4. Link subcategories

## Common problems and fixes
- Shop page thin -> add intro and curated links
- Category base in URL causing duplicates -> pick one structure

## Output
Category template.

## Tools and data sources
WooCommerce admin, Yoast/Rank Math, Query Monitor, Screaming Frog, WP-CLI, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
