# Playbook: Indexability

## How to do it
1. List indexable URLs (200, no noindex, self-canonical) vs sitemap vs GSC indexed
2. Find accidental noindex (meta, X-Robots-Tag, staging leftovers)
3. Orphans: pages with no internal links (compare crawl to sitemap/GSC)
4. Consolidate duplicates; remove or noindex low-value URLs

## Common problems and fixes
- Important page noindexed -> remove directive, resubmit
- Index bloat from tags/params -> noindex + remove from sitemap

## Output
Indexability matrix: URL group, intended, actual, fix.

## Tools and data sources
Screaming Frog or Sitebulb, Google Search Console, Lighthouse, PageSpeed Insights, CrUX, WebPageTest, curl -I, server logs.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
