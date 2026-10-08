# Playbook: Liquid / theme SEO

## How to do it
1. Ensure one H1 in templates
2. Output title/meta via {{ page_title }} patterns with fallbacks
3. Add JSON-LD in theme or via one app
4. Use image_url with width/height and loading attributes

## Common problems and fixes
- Hardcoded titles -> use Liquid variables
- Missing alt -> add image.alt filter fallback

## Output
Liquid snippets reviewed.

## Tools and data sources
Shopify admin (themes, redirects, navigation), Liquid editor, Screaming Frog, Rich Results Test, app list.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
