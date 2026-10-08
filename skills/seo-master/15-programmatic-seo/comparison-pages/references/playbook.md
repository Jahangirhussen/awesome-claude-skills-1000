# Playbook: Programmatic comparisons

## How to do it
1. Use accurate data and dates
2. Focus on valuable pairs only
3. Add decision guidance

## Common problems and fixes
- Thin permutations -> prune
- Out-of-date specs -> automate refresh

## Output
Comparison dataset and template.

## Tools and data sources
Dataset or database, template engine, Screaming Frog, GSC (indexing), sitemap generator, QA sampling script.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
