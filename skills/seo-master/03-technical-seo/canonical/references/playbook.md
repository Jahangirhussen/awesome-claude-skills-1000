# Playbook: Canonicals

## How to do it
1. Read rel=canonical in rendered HTML and HTTP header
2. Verify self-referencing on indexable pages; absolute URLs; one tag per page
3. Check canonical target returns 200, indexable, not redirected
4. Align protocol/www/trailing-slash across canonical, sitemap, internal links

## Common problems and fixes
- Canonical points to noindex/redirect -> point to final indexable URL
- Param URLs indexed -> canonical to clean URL

## Output
Canonical audit: URL, declared canonical, Google-selected, issue.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
