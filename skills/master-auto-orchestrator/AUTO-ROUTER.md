# Auto-router

## Project type -> domains (combine; a project can be several)
| Project | Domains / skills |
|---|---|
| Website / landing | 01 frontend, 11 design, 05 `seo-master`, 10 testing |
| Web app / SaaS | `universal-development-planner` -> 01 backend/API, database, 09 auth/RBAC, 02 saas + billing, 11 UI/UX, `erp-saas-analytics-visualization`, 09 security, 10 testing, 08 deploy |
| ERP / POS / CRM / HR / accounting | planner -> 02 business systems (module), 01 backend/DB, 09 RBAC, 11 UI, analytics-visualization, 10 testing |
| E-commerce / WooCommerce / Shopify / WordPress | 02 platform skills, 05 `seo-master` (ecommerce/woocommerce/wordpress), 11 design, 10 testing |
| Mobile / desktop app | planner -> 01 mobile skills, 11 UI, 10 testing |
| API / backend | planner -> 01 api/backend, database, 09, 10 |
| AI / ML / LLM / RAG / agent | 03 AI, 07 data, 04 research (if experiments), 10 evaluation |
| Research / paper / thesis | 04 research, 07 statistics, 03 ML if needed, 14 writing |
| Data analysis / visualization | 07 data, `erp-saas-analytics-visualization` for business dashboards |
| SEO / GEO / AEO | `seo-master` only (plus platform skill if WordPress/Shopify) |
| Marketing / content / ads | 06 marketing (+ 05 for SEO content) |
| DevOps / deploy | 08 devops, 09 security |
| Security audit | 09 security |
| QA / testing | 10 testing (Playwright canonical in 12-AUTOMATION / installed playwright skills) |
| Docs | 14 documentation |
| Debug / fix / migrate / performance | 15 support, then domain skill |
| Automation / scraping | 12 automation |
| Product / PRD / roadmap | 13 product |

## Task intent -> extras
BUILD/CREATE substantial software -> planner first. FIX/DEBUG -> 15 debugging + domain. AUDIT -> domain audit skill (+ security if code). OPTIMIZE -> performance skills. DEPLOY -> 08. TEST -> 10. DOCUMENT -> 14. MIGRATE -> 15/31 SEO migration if SEO.

## Verification pairing
Code -> tests; web UI -> browser/E2E + responsive; SEO -> SEO validation (schema/crawl/GSC); DB -> migration check; research -> reproducibility/statistics; deploy -> health check.

## Existing project
Inspect package files, framework, docs, structure first; route from evidence (e.g. Next.js + Prisma + Stripe -> frontend, API, DB, billing, auth), not from the sentence alone.

## Acceptance tests (what correct routing looks like)
1. "Build a SaaS POS" -> planner, 02 saas+pos, DB, backend, auth/RBAC, UI/UX, analytics-visualization, security, testing.
2. "Improve technical SEO of my WordPress site" -> `seo-master` (03 technical, 11 wordpress, 27 schema, 28 analytics as needed).
3. "Create an ML model for medical diagnosis" -> 04 research, 07 data/statistics, 03 ML, evaluation.
4. "Make this React website mobile responsive" -> 01 frontend/react, 11 responsive/UI, 10 testing.
5. "Analyze this dataset and create visualizations" -> 07 data analysis + visualization (python/pandas).
6. "Set up Stripe subscription billing" -> 02 saas/billing, backend/API, DB, security, testing.
7. "Research explainable federated learning for medical diagnosis" -> 04 research, 03 ML, academic writing.
Run these as dry-runs with `references/routing-dry-run.md` after registry changes.
