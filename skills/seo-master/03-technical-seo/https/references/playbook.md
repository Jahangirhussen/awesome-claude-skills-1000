# Playbook: HTTPS and security headers

## How to do it
1. Valid certificate, auto-renew, no mixed content
2. 301 all HTTP to HTTPS (single hop), preferred host (www/non-www)
3. Add HSTS after verifying; set basic security headers
4. Update canonicals, sitemap, internal links, GSC property

## Common problems and fixes
- Mixed content warnings -> update asset URLs to HTTPS
- Redirect loop behind CDN -> fix origin protocol setting

## Output
HTTPS checklist with status.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
