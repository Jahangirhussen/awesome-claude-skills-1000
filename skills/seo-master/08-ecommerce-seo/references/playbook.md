# Playbook: 08. E-commerce SEO

## How to do it
1. Crawl categories, products, filters; compare to GSC indexing
2. Check duplicate/thin product pages and param URLs
3. Validate product schema and feed
4. Review internal linking from categories to products

## Common problems and fixes
- Index bloat from filters -> control facets
- Thin manufacturer copy -> write unique descriptions

## Output
E-commerce SEO audit by template.

## Tools and data sources
Screaming Frog, Google Search Console, Merchant Center, Rich Results Test, platform admin, feed validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
