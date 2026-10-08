# Playbook: Programmatic internal linking

## How to do it
1. Hubs link to spokes; spokes link to siblings and hub
2. Related blocks by similarity
3. Segment sitemaps by template
4. Prevent index bloat with noindex rules

## Common problems and fixes
- Orphan generated pages -> add hub links
- Too many links -> cap per page

## Output
Linking rules and sitemap plan.

## Tools and data sources
Dataset or database, template engine, Screaming Frog, GSC (indexing), sitemap generator, QA sampling script.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
