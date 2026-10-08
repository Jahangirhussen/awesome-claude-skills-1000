# Playbook: INP

## How to do it
1. Record interactions in DevTools; find long tasks (>50ms)
2. Break up/defer JS, remove unused bundles, use web workers for heavy work
3. Optimize event handlers; avoid forced reflow; debounce input
4. Check third-party tag impact

## Common problems and fixes
- Hydration blocks input -> partial/lazy hydration
- Heavy filter UIs -> virtualize lists

## Output
Slowest interactions with cause and fix.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
