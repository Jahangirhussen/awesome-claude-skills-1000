# Playbook: Link audit

## How to do it
1. Export links; flag patterns (exact-match anchors, link networks, foreign spam)
2. Review manually before action; most weird links are ignored by Google
3. Disavow only when manual action risk or clear manipulation
4. Document before/after

## Common problems and fixes
- Mass-disavow harming good links -> be conservative
- Manual action present -> remove links, then reconsideration request

## Output
Audit sheet: domain, issue, decision.

## Tools and data sources
Ahrefs, Semrush, Majestic, Google Search Console Links report, Google Alerts, outreach CRM or spreadsheet.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
