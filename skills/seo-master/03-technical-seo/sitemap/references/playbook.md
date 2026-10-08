# Playbook: XML sitemaps

## How to do it
1. Generate only canonical, 200, indexable URLs
2. Split at 50k URLs/50MB; use sitemap index; set accurate lastmod
3. Add image/video/news sitemaps where relevant
4. Submit in GSC; compare submitted vs indexed

## Common problems and fixes
- Sitemap contains redirects/404 -> regenerate from live indexable URLs
- lastmod always 'now' -> use real modification dates or omit

## Output
Sitemap spec: files, URL rules, update trigger.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
