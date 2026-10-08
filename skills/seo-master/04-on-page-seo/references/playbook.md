# Playbook: 04. On-Page SEO

## How to do it
1. Crawl titles, meta, H1, canonical, word count by template
2. Compare against top SERP intent for each target keyword
3. Fix patterns per template first, then individual pages

## Common problems and fixes
- Duplicate titles by template -> add variable pattern with unique attribute
- Keyword stuffing -> rewrite for intent and clarity

## Output
On-page fix list per template and per key page.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
