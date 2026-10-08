# Playbook: Video schema

## How to do it
1. VideoObject: name, description, thumbnailUrl, uploadDate, duration, contentUrl/embedUrl
2. Add transcript and key moments (Clip/SeekToAction) if applicable
3. Validate

## Common problems and fixes
- Missing thumbnail -> provide stable URL
- Wrong dates -> use ISO 8601

## Output
VideoObject JSON-LD.

## Tools and data sources
YouTube Studio, VideoObject validator (Rich Results Test), Google Search Console video report, sitemap generator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
