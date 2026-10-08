# Playbook: Multilingual content

## How to do it
1. Use professional/native localization incl. keywords, currency, units
2. Translate metadata, schema, alt text, URLs where sensible
3. Avoid machine translation without review

## Common problems and fixes
- Duplicate content across locales -> hreflang + unique local elements

## Output
Localization checklist.

## Tools and data sources
hreflang validator or Screaming Frog hreflang tab, GSC international targeting data, localization team, sitemap.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
