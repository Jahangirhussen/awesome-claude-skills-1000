# Playbook: 18. International SEO

## How to do it
1. Decide structure (subfolders default, ccTLD, subdomain)
2. Localize content (not just translate)
3. Implement hreflang and locale canonicals
4. Check geotargeting and local signals

## Common problems and fixes
- Auto-redirect by IP blocks bots -> use banners instead
- Mixed language pages -> separate URLs per language

## Output
International SEO plan.

## Tools and data sources
hreflang validator or Screaming Frog hreflang tab, GSC international targeting data, localization team, sitemap.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
