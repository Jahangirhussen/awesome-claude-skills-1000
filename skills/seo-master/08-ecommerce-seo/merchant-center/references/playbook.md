# Playbook: Merchant Center and Shopping

## How to do it
1. Create feed with required attributes; match page price/stock
2. Fix disapprovals (images, GTIN, policy)
3. Enable free listings; optimize titles with brand + attributes
4. Monitor diagnostics weekly

## Common problems and fixes
- Feed price differs from site -> schedule sync
- Missing GTIN -> add or mark identifier_exists properly

## Output
Feed spec and error fixes.

## Tools and data sources
Screaming Frog, Google Search Console, Merchant Center, Rich Results Test, platform admin, feed validator.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
