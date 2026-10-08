# Playbook: Schema validation

## How to do it
1. Test URLs in Rich Results Test and Schema Markup Validator
2. Fix errors first, then warnings that affect eligibility
3. Check GSC Enhancements reports after deploy
4. Crawl site for schema coverage

## Common problems and fixes
- Valid but no rich result -> eligibility/quality, not syntax

## Output
Validation report.

## Tools and data sources
Rich Results Test, Schema Markup Validator (validator.schema.org), GSC Enhancements, JSON-LD generator or code.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
