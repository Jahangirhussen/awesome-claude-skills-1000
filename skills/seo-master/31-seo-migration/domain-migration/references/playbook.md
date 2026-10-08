# Playbook: Domain migration

## How to do it
1. 301 old domain to new, URL to URL
2. Use GSC Change of Address (domain properties)
3. Update canonicals, sitemap, hreflang, internal links, GBP, social, key backlinks
4. Keep old domain active and redirected for 1+ year

## Common problems and fixes
- Dropping redirects early -> keep long term

## Output
Domain move runbook.

## Tools and data sources
Screaming Frog (before/after crawls), redirect mapping sheet, GSC Change of Address, server config, log analysis.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
