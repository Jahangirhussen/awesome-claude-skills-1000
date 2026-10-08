# Playbook: Title tags

## How to do it
1. Write unique title per URL, ~50-60 chars (pixel width ~580px)
2. Primary keyword near the start; add brand at the end; add differentiator (year, price, benefit)
3. Match search intent; avoid clickbait that mismatches the page

## Common problems and fixes
- Google rewrites title -> shorten, align with H1 and content
- Duplicate titles -> add unique attribute

## Output
Title table: URL, current, proposed, reason.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
