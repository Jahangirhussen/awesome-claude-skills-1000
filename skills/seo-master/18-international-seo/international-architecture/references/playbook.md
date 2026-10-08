# Playbook: International architecture

## How to do it
1. Prefer subfolders (/de/) for shared authority
2. Language switcher with crawlable links
3. Keep consistent URL patterns
4. Separate sitemaps per locale optional

## Common problems and fixes
- Mixed structures -> unify
- Missing x-default -> add

## Output
Architecture diagram.

## Tools and data sources
hreflang validator or Screaming Frog hreflang tab, GSC international targeting data, localization team, sitemap.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
