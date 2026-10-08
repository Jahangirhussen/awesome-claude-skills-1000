# Playbook: Image sitemap

## How to do it
1. Include important images (esp. JS-loaded) in sitemap
2. Use image extension tags with canonical page URL
3. Make image URLs crawlable

## Common problems and fixes
- Blocked image folder -> allow in robots.txt

## Output
Image sitemap file.

## Tools and data sources
Squoosh/ImageMagick/sharp, Lighthouse, Screaming Frog (images), Google Search Console, CDN image transforms.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
