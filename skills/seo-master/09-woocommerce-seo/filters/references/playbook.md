# Playbook: Filters

## How to do it
1. Identify filter plugin URL params (e.g. ?filter_color=, ?min_price=)
2. Canonical to base category; noindex combos
3. Block heavy param crawling
4. Ensure AJAX filters do not break back button/URLs

## Common problems and fixes
- Crawl waste on filters -> rules above
- Filtered pages indexed -> remove from sitemap and noindex

## Output
Filter URL rules.

## Tools and data sources
WooCommerce admin, Yoast/Rank Math, Query Monitor, Screaming Frog, WP-CLI, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
