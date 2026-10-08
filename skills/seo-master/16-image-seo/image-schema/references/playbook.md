# Playbook: Image structured data

## How to do it
1. Use ImageObject with contentUrl, license, creator when relevant
2. Set primaryImageOfPage; ensure article image sizes meet guidelines
3. Validate

## Common problems and fixes
- Wrong image ratios for Article -> provide 16:9, 4:3, 1:1 variants

## Output
Image JSON-LD example.

## Tools and data sources
Squoosh/ImageMagick/sharp, Lighthouse, Screaming Frog (images), Google Search Console, CDN image transforms.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
