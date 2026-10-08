# Playbook: Programmatic SaaS pages

## How to do it
1. Pick templates with unique data per page (integrations, templates, alternatives)
2. Ship a small batch, check indexing and engagement, then scale
3. Noindex pages below quality threshold

## Common problems and fixes
- Index bloat -> prune
- Thin permutations -> add unique value or drop

## Output
Batch plan and quality gate.

## Tools and data sources
Ahrefs/Semrush competitor tools, GSC, analytics funnels, CMS, screenshot tools, schema validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
