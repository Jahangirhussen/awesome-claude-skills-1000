# Playbook: Alt text

## How to do it
1. Describe image content and purpose concisely
2. Include keyword only when natural
3. Empty alt for decorative images; do not stuff

## Common problems and fixes
- Alt = filename -> rewrite
- Missing alt on product images -> template from product name + attribute

## Output
Alt text table.

## Tools and data sources
Squoosh/ImageMagick/sharp, Lighthouse, Screaming Frog (images), Google Search Console, CDN image transforms.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
