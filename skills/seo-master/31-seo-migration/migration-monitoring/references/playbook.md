# Playbook: Migration monitoring

## How to do it
1. Daily GSC for 30 days: indexing, errors, crawl stats
2. Compare crawl to baseline; fix 404s and redirect gaps
3. Track rankings and traffic by segment
4. Expect temporary fluctuation

## Common problems and fixes
- Persistent drop -> check canonical/robots/noindex first

## Output
Post-launch monitoring log.

## Tools and data sources
Screaming Frog (before/after crawls), redirect mapping sheet, GSC Change of Address, server config, log analysis.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
