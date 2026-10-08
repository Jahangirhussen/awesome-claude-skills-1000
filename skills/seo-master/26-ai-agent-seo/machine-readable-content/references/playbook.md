# Playbook: Machine-readable content

## How to do it
1. JSON-LD for entities and actions
2. Semantic HTML5 landmarks
3. Consistent data attributes

## Common problems and fixes
- Content in images only -> add text

## Output
Markup review.

## Tools and data sources
OpenAPI tools, schema validator, Lighthouse accessibility, robots.txt, MCP/API docs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
