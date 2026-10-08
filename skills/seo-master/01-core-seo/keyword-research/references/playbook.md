# Playbook: Keyword research

## How to do it
1. Seed terms from offer, product pages, GSC queries, competitor URLs, People Also Ask
2. Expand with autocomplete, related searches, competitor ranking keywords (Ahrefs/Semrush if available)
3. Label intent: informational / commercial / transactional / navigational
4. Cluster by SERP overlap (same top-10 URLs = same page)
5. Score: volume x business value / difficulty; assign 1 primary keyword per URL

## Common problems and fixes
- Cannibalization (two URLs for one intent) -> merge or differentiate intent
- High volume but wrong intent -> drop or create the right page type

## Output
Keyword map table: keyword, intent, volume, difficulty, target URL, priority.

## Tools and data sources
Google Search Console, GA4, Ahrefs/Semrush (keywords, competitors), Google Trends, AnswerThePublic, a spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
