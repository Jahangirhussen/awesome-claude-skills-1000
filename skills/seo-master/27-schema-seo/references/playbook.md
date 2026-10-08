# Playbook: 27. Schema / Structured Data

## How to do it
1. Pick types matching visible content
2. Write JSON-LD in one source of truth
3. Validate in Rich Results Test and Schema.org validator
4. Monitor GSC Enhancements

## Common problems and fixes
- Markup for hidden content -> remove
- Duplicate sources -> keep one

## Output
Schema plan per template.

## Tools and data sources
Rich Results Test, Schema Markup Validator (validator.schema.org), GSC Enhancements, JSON-LD generator or code.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
