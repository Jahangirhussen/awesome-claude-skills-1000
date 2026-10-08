# Playbook: LCP

## How to do it
1. Identify LCP element (Chrome DevTools Performance / Lighthouse)
2. Preload the LCP image or font; set fetchpriority=high; never lazy-load it
3. Cut TTFB (cache, CDN, edge), remove render-blocking CSS/JS, inline critical CSS
4. Serve right-sized WebP/AVIF

## Common problems and fixes
- Hero is a CSS background image -> use <img> so it can be preloaded/discovered
- Slow TTFB -> full-page cache or edge rendering

## Output
LCP element, before/after timing.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
