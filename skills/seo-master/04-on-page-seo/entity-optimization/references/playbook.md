# Playbook: Entity optimization

## How to do it
1. Define the main entities (brand, people, products, places) and consistent names
2. Add Organization/Person schema with sameAs to official profiles
3. Align facts across site, Google Business Profile, LinkedIn, Wikipedia/Wikidata where valid
4. Use clear 'about' content and author pages

## Common problems and fixes
- Inconsistent brand naming -> standardize
- No notable presence -> earn mentions on credible sites

## Output
Entity fact sheet and schema.

## Tools and data sources
Screaming Frog (titles/meta/H1), Google Search Console, SERP checks, SEO plugin or CMS fields, a text diff tool.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
