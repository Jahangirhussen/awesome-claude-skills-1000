# Playbook: Hreflang

## How to do it
1. Use ISO 639-1 language and ISO 3166-1 region codes
2. Every page references all alternates including itself and x-default
3. Alternates must be reciprocal; canonicals self-referencing per locale
4. Implement via HTML, headers, or sitemap

## Common problems and fixes
- Non-reciprocal tags ignored -> fix both sides
- Wrong codes (en-uk) -> en-gb

## Output
Hreflang map.

## Tools and data sources
hreflang validator or Screaming Frog hreflang tab, GSC international targeting data, localization team, sitemap.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
