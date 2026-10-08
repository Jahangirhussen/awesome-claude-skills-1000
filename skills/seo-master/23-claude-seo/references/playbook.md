# Playbook: 23. Claude SEO

## How to do it
1. Decide policy for ClaudeBot (training), Claude-User, Claude-SearchBot in robots.txt
2. Provide clean semantic, factual pages
3. Test brand/category prompts in Claude with web search enabled

## Common problems and fixes
- Inconsistent brand facts -> standardize

## Output
Claude visibility notes.

## Tools and data sources
Claude with web search, robots.txt tester, server logs, schema validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
