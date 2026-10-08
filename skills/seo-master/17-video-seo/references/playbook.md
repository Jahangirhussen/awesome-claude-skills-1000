# Playbook: 17. Video SEO

## How to do it
1. Host videos on a crawlable page with surrounding text
2. Add VideoObject schema, transcript, thumbnail
3. Submit video sitemap if many videos
4. Optimize YouTube separately

## Common problems and fixes
- Video not indexed -> page quality and visibility; ensure video is main content
- Embed only via iframe without page text -> add transcript

## Output
Video SEO checklist.

## Tools and data sources
YouTube Studio, VideoObject validator (Rich Results Test), Google Search Console video report, sitemap generator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
