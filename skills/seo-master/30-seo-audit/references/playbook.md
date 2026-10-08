# Playbook: 30. SEO Audit

## How to do it
1. Detect platform and site type first
2. Run applicable modules: technical, on-page, content, links, schema, speed, platform-specific, AI visibility
3. Score by impact and effort; P0/P1/P2
4. Fix in scope and re-test if asked

## Common problems and fixes
- Everything critical -> rank by traffic/revenue impact

## Output
Audit report: findings, evidence, fix, priority.

## Tools and data sources
Screaming Frog, GSC, GA4, Lighthouse, Ahrefs/Semrush, schema validator, platform-specific plugins.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
