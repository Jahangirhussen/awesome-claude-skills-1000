# Playbook: Products

## How to do it
1. Unique title/description; use short description for summary, long for detail
2. Set canonical for variations to the parent product
3. Images with alt; gallery optimized
4. Handle out-of-stock (keep page, show notice) and discontinued (301)

## Common problems and fixes
- Product in multiple categories creating duplicate URLs -> primary category in SEO plugin
- Draft/private products leaking -> check status

## Output
Product page checklist.

## Tools and data sources
WooCommerce admin, Yoast/Rank Math, Query Monitor, Screaming Frog, WP-CLI, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
