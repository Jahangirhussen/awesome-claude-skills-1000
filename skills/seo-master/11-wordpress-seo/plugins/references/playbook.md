# Playbook: SEO plugin conflicts

## How to do it
1. List active plugins affecting head output (SEO, schema, cache, builders)
2. Detect duplicates: meta, OG, schema
3. Remove unused; update; test after changes

## Common problems and fixes
- Builder and SEO plugin both set titles -> choose one source
- Cache plugin serving noindex -> purge and test

## Output
Plugin conflict matrix.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
