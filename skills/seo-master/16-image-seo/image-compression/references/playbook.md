# Playbook: Compression and formats

## How to do it
1. Resize to display size (2x for retina max)
2. Convert to WebP/AVIF with fallback
3. Use srcset/sizes and width/height attributes
4. Lazy-load below the fold; never lazy-load the LCP image

## Common problems and fixes
- CLS from missing dimensions -> set width/height
- Quality too low -> test visually

## Output
Image pipeline settings.

## Tools and data sources
Squoosh/ImageMagick/sharp, Lighthouse, Screaming Frog (images), Google Search Console, CDN image transforms.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
