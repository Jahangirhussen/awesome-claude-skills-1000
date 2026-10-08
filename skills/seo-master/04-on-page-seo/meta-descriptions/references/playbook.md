# Playbook: Meta descriptions

## How to do it
1. Write unique descriptions ~140-160 chars with benefit + CTA
2. Include primary term naturally; match the query intent
3. For templates, build patterns with product/location variables

## Common problems and fixes
- Description ignored by Google -> it may rewrite; keep it accurate
- Duplicate descriptions -> unique or omit

## Output
Meta table: URL, current, proposed.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
