# Playbook: 19. AI SEO

## How to do it
1. Check AI crawler access in robots.txt per policy (OAI-SearchBot, GPTBot, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended, Applebot-Extended)
2. Make key pages crawlable, fast, server-rendered
3. Write quotable answer-first passages with sources and dates
4. Build entity and brand consistency; earn third-party mentions
5. Track mentions/citations and AI referrals

## Common problems and fixes
- Blocked all AI bots -> decide training vs search access separately
- Content only behind JS/login -> make accessible

## Output
AI visibility plan and tracking sheet.

## Tools and data sources
Prompt tracking sheet, ChatGPT/Gemini/Perplexity/Claude/AI Overviews, GA4 referral reports, server logs for AI bots.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
