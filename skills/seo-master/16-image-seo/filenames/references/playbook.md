# Playbook: Filenames

## How to do it
1. Use descriptive, hyphenated, lowercase filenames
2. Avoid IMG_1234 and spaces
3. Keep stable URLs; redirect if renamed

## Common problems and fixes
- Bulk rename breaking links -> redirect or update references

## Output
Rename map.

## Tools and data sources
Squoosh/ImageMagick/sharp, Lighthouse, Screaming Frog (images), Google Search Console, CDN image transforms.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
