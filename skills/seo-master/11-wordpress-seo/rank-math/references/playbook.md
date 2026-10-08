# Playbook: Rank Math

## How to do it
1. Titles & Meta templates per post type and taxonomy
2. Schema: set default type per post type
3. Sitemap settings, redirections, 404 monitor
4. Use Content AI suggestions carefully; review manually

## Common problems and fixes
- Wrong schema type site-wide -> adjust defaults
- Imported Yoast data mismatches -> verify after import

## Output
Rank Math configuration notes.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
