# Playbook: Core Web Vitals and speed

## How to do it
1. Use field data first: CrUX/GSC CWV; then lab (Lighthouse, WebPageTest)
2. Targets at p75: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1
3. Fix server (TTFB, cache, CDN, compression), then assets (images, fonts, JS)
4. Re-measure after deploy; field data lags ~28 days

## Common problems and fixes
- Lab good but field bad -> real-user conditions (mobile, slow CPU); test throttled
- Third-party scripts dominate -> defer, facade, or remove

## Output
CWV table: metric, p75, cause, fix, owner.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
