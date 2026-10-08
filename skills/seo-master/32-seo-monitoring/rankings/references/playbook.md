# Playbook: Rank tracking

## How to do it
1. Track keywords by segment with fixed location/device
2. Compare vs competitors; weekly trend
3. Use GSC average position as sanity check

## Common problems and fixes
- Rank tracker differs from GSC -> expected; use GSC for truth

## Output
Ranking report.

## Tools and data sources
GSC, GA4, rank tracker, scheduled crawler, uptime monitor, alerting (Slack/email).

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
