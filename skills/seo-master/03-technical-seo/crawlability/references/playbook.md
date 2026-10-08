# Playbook: Crawlability

## How to do it
1. Check robots.txt, response time, status codes for Googlebot (log files or GSC Crawl stats)
2. Measure click depth; important pages within 3 clicks
3. Find crawl traps: infinite params, calendars, session IDs, faceted combos
4. Reduce waste: block or canonicalize traps, fix redirect chains

## Common problems and fixes
- Googlebot gets 429/5xx -> raise capacity, cache, CDN
- Crawl budget wasted on params -> param handling via robots/noindex/canonical

## Output
Crawl report: depth distribution, waste sources, fixes.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
