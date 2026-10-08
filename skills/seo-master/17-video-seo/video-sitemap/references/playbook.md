# Playbook: Video sitemap

## How to do it
1. List video pages with title, description, thumbnail, content/player loc
2. Keep updated; submit in GSC

## Common problems and fixes
- Pages blocked -> allow crawl

## Output
Video sitemap file.

## Tools and data sources
YouTube Studio, VideoObject validator (Rich Results Test), Google Search Console video report, sitemap generator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.

## Example
```xml
<url><loc>https://example.com/videos/setup-guide</loc>
 <video:video><video:thumbnail_loc>https://example.com/thumbs/setup.jpg</video:thumbnail_loc>
  <video:title>Setup guide</video:title><video:description>How to set up in 5 minutes.</video:description>
  <video:content_loc>https://example.com/media/setup.mp4</video:content_loc><video:duration>300</video:duration></video:video></url>
```
Declare `xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"`. `loc` is the page hosting the video, not the file.
