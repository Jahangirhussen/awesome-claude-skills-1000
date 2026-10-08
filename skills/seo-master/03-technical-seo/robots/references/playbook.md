# Playbook: robots.txt

## How to do it
1. Fetch /robots.txt (200, text/plain, <500KB)
2. Test key URLs with the GSC robots tester or a parser
3. Ensure CSS/JS/images needed for rendering are not blocked
4. Add Sitemap: line; use noindex (not Disallow) to remove pages from the index

## Common problems and fixes
- Disallow: / left from staging -> remove immediately
- Blocked page still indexed -> allow crawl and add noindex

## Output
robots.txt diff with reasons.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
