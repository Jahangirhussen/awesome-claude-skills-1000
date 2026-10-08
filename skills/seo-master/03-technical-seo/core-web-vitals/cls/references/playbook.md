# Playbook: CLS

## How to do it
1. Record layout shifts (DevTools Layout Shift regions)
2. Set width/height or aspect-ratio on images, video, embeds
3. Reserve space for ads, banners, late widgets
4. Use font-display: swap with matched fallback metrics

## Common problems and fixes
- Cookie banner pushes content -> overlay or reserved space
- Late-loading fonts -> preload and size-adjust

## Output
Shifting elements and fixes.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
