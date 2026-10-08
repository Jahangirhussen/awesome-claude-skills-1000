# Playbook: 11. WordPress SEO

## How to do it
1. Check Settings > Reading (discourage search engines off), Permalinks, SEO plugin config
2. Audit taxonomies, archives, attachments, author pages
3. Review plugin/theme conflicts and speed

## Common problems and fixes
- 'Discourage search engines' checked -> uncheck
- Multiple SEO plugins -> keep one

## Output
WordPress SEO audit.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
