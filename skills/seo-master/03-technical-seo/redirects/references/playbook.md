# Playbook: Redirects and status codes

## How to do it
1. Crawl and list all 3xx/4xx/5xx internal URLs
2. Use single-hop 301 for permanent moves; 302/307 only for temporary
3. Update internal links to final URLs; remove chains and loops
4. Serve 404/410 for gone pages; redirect to closest relevant page, not homepage

## Common problems and fixes
- Redirect chains of 3+ hops -> collapse to one
- Soft 404s -> return real 404/410 or restore content

## Output
Redirect map: from, to, type, status.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
