# Playbook: WordPress technical

## How to do it
1. Permalinks: post name; avoid changing without redirects
2. Sitemap from core or SEO plugin, not both
3. Robots.txt correct; noindex search, attachments, thin tag/author archives
4. Canonical output verified

## Common problems and fixes
- Attachment pages indexed -> redirect to parent
- Staging noindex left on -> remove

## Output
Technical config list.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
