# Playbook: URL optimization

## How to do it
1. Short, lowercase, hyphenated, descriptive slugs
2. Avoid params, dates, IDs when possible
3. On change: 301 old to new, update internal links and sitemap

## Common problems and fixes
- Changing URLs without redirects -> add 301 map
- Keyword-stuffed long URLs -> shorten

## Output
URL change map.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
