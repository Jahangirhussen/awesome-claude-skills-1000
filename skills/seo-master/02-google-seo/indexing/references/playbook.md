# Playbook: Google indexing

## How to do it
1. Open URL Inspection for the URL: crawl, index, canonical (Google-selected vs user-declared)
2. Map status to cause: 'Discovered not indexed' (crawl/quality), 'Crawled not indexed' (quality/duplicate), 'Blocked by robots', 'Alternate with canonical'
3. Fix cause, then Request Indexing for a few key URLs only

## Common problems and fixes
- Crawled-not-indexed at scale -> improve unique value, internal links, prune thin pages
- Google picks different canonical -> align content, canonicals, internal links, sitemap

## Output
Per-URL status, cause, fix, re-check date.

## Tools and data sources
Google Search Console (+API), GA4, URL Inspection tool, Search Status Dashboard, Looker Studio.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
