# Playbook: JavaScript and rendering SEO

## How to do it
1. Compare 'view source' vs rendered DOM; use URL Inspection live test
2. Ensure content, titles, canonicals and links exist in rendered HTML (links as <a href>)
3. Prefer SSR/SSG/ISR for indexable pages; hydrate after
4. Avoid content that needs clicks/scroll events to appear

## Common problems and fixes
- Content missing in rendered HTML -> SSR the route or prerender
- Links are onClick handlers -> use real anchors

## Output
Rendering report: route, raw vs rendered diff, fix.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
