# Playbook: WordPress schema

## How to do it
1. Choose one schema source (SEO plugin or theme)
2. Validate Organization, WebSite, Article, Breadcrumb; product schema for WooCommerce
3. Remove duplicates from builder or add-ons

## Common problems and fixes
- Schema duplicated by theme -> disable theme schema
- Invalid Article image sizes -> set featured image properly

## Output
Schema validation report.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
