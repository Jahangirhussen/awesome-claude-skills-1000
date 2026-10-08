# Playbook: 03. Technical SEO

## How to do it
1. Crawl with Screaming Frog/Sitebulb or a script: status codes, canonicals, noindex, titles, depth
2. Compare against GSC indexing and sitemap lists
3. Test rendered HTML for JS sites (URL Inspection live test)
4. Run Lighthouse/PageSpeed and CrUX for CWV

## Common problems and fixes
- Crawler finds 5xx -> server/log review first
- Mixed signals (canonical vs sitemap vs internal links) -> make all three agree

## Output
Technical issue list ranked by SEO impact with URLs and fix.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
