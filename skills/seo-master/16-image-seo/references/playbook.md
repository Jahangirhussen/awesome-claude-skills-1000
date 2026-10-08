# Playbook: 16. Image SEO

## How to do it
1. Audit image count, size, format, alt, dimensions, lazy-loading
2. Compress and convert; set responsive images
3. Add image sitemap/schema where useful

## Common problems and fixes
- Huge hero images -> resize/serve WebP/AVIF
- Missing alt -> write meaningful alt

## Output
Image optimization list.

## Tools and data sources
Squoosh/ImageMagick/sharp, Lighthouse, Screaming Frog (images), Google Search Console, CDN image transforms.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
