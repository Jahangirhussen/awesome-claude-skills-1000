# Playbook: AI visibility tracking

## How to do it
1. Define 20-50 prompts per topic (brand, category, comparison, problem)
2. Run them across ChatGPT, Gemini, Perplexity, Google AI Overviews, Claude; log mention, citation, position, sentiment
3. Repeat monthly; note variance (answers change run to run)
4. Track AI referral traffic in GA4 (referrers like chatgpt.com, perplexity.ai)

## Common problems and fixes
- Single-run results are noisy -> average several runs

## Output
Visibility tracker: prompt, engine, mention?, cited URL, date.

## Tools and data sources
Prompt tracking sheet, ChatGPT/Gemini/Perplexity/Claude/AI Overviews, GA4 referral reports, server logs for AI bots.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
