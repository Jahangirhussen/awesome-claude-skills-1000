# Playbook: Template pages

## How to do it
1. Design template with variable sections and fixed value blocks
2. Unique title/H1/intro from real data
3. Structured data where relevant

## Common problems and fixes
- Identical text across pages -> add differentiating data
- Too many variables -> keep readable

## Output
Template spec.

## Tools and data sources
Dataset or database, template engine, Screaming Frog, GSC (indexing), sitemap generator, QA sampling script.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
