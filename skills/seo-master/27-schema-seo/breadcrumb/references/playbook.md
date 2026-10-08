# Playbook: BreadcrumbList

## How to do it
1. BreadcrumbList with ListItem position, name, item
2. Match visible breadcrumb trail

## Common problems and fixes
- Trail differs from UI -> align

## Output
Breadcrumb JSON-LD.

## Tools and data sources
Rich Results Test, Schema Markup Validator (validator.schema.org), GSC Enhancements, JSON-LD generator or code.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.

## Example
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":"https://example.com/"},
 {"@type":"ListItem","position":2,"name":"Shoes","item":"https://example.com/shoes/"},
 {"@type":"ListItem","position":3,"name":"Trail runners"}]}
```
The last item may omit `item` (current page). Names and order must match the visible breadcrumb.
