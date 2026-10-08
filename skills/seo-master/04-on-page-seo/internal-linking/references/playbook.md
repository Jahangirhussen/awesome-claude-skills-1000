# Playbook: Internal linking

## How to do it
1. Crawl link graph; find orphans and pages with few inlinks
2. Link from high-authority, relevant pages to priority pages with descriptive anchors
3. Add contextual links in body, hubs, related blocks; fix broken internal links
4. Avoid sitewide footers/nav as the only links

## Common problems and fixes
- Generic anchors ('click here') -> descriptive
- Too many links per page -> prioritize relevance

## Output
Link plan: source URL, target URL, anchor.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
