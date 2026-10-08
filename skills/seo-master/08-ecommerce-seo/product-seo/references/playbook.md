# Playbook: Product SEO

## How to do it
1. Unique title: product name + key attribute + brand
2. Unique description with benefits, specs, FAQs; avoid supplier copy
3. High-quality images with alt text; reviews on page
4. Product + Offer schema; breadcrumbs; related products links

## Common problems and fixes
- Variants as separate thin URLs -> canonicalize to parent or make unique
- Out-of-stock -> keep page, show alternatives; 301 only if permanently gone

## Output
Product template spec.

## Tools and data sources
Screaming Frog, Google Search Console, Merchant Center, Rich Results Test, platform admin, feed validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
