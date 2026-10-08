# Playbook: Collections

## How to do it
1. Add unique intro and meta; keep filters crawlable only where wanted
2. Avoid thin duplicate collections
3. Link subcollections; use pagination links

## Common problems and fixes
- Tag-filter URLs indexed -> noindex or canonical
- Automated collections overlapping -> consolidate

## Output
Collection template.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
