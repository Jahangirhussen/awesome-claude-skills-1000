# Playbook: Country targeting

## How to do it
1. Choose structure to match business (ccTLD strongest signal)
2. Add local signals: currency, address, phone, local links
3. Use GSC where relevant

## Common problems and fixes
- Same content for multiple countries -> hreflang with regional variants

## Output
Targeting matrix.

## Tools and data sources
hreflang validator or Screaming Frog hreflang tab, GSC international targeting data, localization team, sitemap.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
