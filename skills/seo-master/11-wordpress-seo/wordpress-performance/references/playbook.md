# Playbook: WordPress performance

## How to do it
1. Measure with PageSpeed/CrUX and Query Monitor
2. Enable page cache, object cache (Redis), CDN, GZIP/Brotli
3. Optimize images (WebP/AVIF), lazy-load below fold, limit plugins
4. Defer non-critical JS, remove unused CSS carefully

## Common problems and fixes
- Heavy page builder output -> simplify sections or optimize assets
- Slow TTFB -> hosting/caching upgrade

## Output
Performance fix list with expected gains.

## Tools and data sources
WordPress admin, Yoast/Rank Math, Query Monitor, WP-CLI, caching plugin, PageSpeed Insights.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
