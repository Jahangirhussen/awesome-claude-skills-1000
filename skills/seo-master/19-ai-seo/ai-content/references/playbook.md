# Playbook: AI-ready content

## How to do it
1. Use semantic HTML and short self-contained passages (50-150 words)
2. Lead with the answer, then support
3. Include named entities, numbers, citations
4. Add author and last-updated

## Common problems and fixes
- Wall-of-text -> break into scannable sections

## Output
Passage-level rewrite list.

## Tools and data sources
Prompt tracking sheet, ChatGPT/Gemini/Perplexity/Claude/AI Overviews, GA4 referral reports, server logs for AI bots.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
