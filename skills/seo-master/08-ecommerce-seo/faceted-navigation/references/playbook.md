# Playbook: Faceted navigation

## How to do it
1. List all filter parameters and combos
2. Index only combos with demand (e.g. brand + category); canonical/noindex the rest
3. Block infinite combos from crawl (robots / nofollow / JS)
4. Keep clean URLs for indexable facets

## Common problems and fixes
- Millions of param URLs -> robots rules + noindex + canonical strategy
- Faceted pages in sitemap -> remove non-indexable

## Output
Facet policy table: facet, index?, URL pattern.

## Tools and data sources
Screaming Frog, Google Search Console, Merchant Center, Rich Results Test, platform admin, feed validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
