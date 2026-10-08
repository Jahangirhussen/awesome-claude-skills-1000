# Playbook: Headings

## How to do it
1. Exactly one H1 reflecting the page topic
2. H2/H3 outline mirrors subtopics and questions users ask
3. Do not skip levels for styling; use CSS for appearance

## Common problems and fixes
- Logo is the H1 -> make page title the H1
- Multiple H1 from theme -> fix template

## Output
Heading outline per page.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
