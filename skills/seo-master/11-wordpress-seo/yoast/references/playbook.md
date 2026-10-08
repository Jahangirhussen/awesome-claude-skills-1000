# Playbook: Yoast SEO

## How to do it
1. Search appearance templates for post types and taxonomies
2. Indexation settings per type; noindex low-value archives
3. Schema graph settings and organization/person info
4. Review Yoast redirects (premium) and breadcrumbs

## Common problems and fixes
- Titles default to site name only -> set templates
- Category base duplication -> disable if not needed

## Output
Yoast configuration notes.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
