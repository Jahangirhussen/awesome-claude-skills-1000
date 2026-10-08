# Playbook: Mobile SEO

## How to do it
1. Test with Mobile-Friendly checks and real devices
2. Confirm same content, metadata, structured data on mobile and desktop
3. Viewport meta, readable font sizes, tap targets >= 48px, no intrusive interstitials
4. Check mobile CWV separately

## Common problems and fixes
- Content hidden/cut on mobile -> include it (mobile-first indexing)
- Separate m. site -> migrate to responsive

## Output
Mobile issue list by template.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
