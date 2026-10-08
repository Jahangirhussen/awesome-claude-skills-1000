# The 38 planning files (docs/NN-NAME.md)

| # | File | Contains (project-specific) |
|---|---|---|
| 01 | README | what it is, setup, run, test, build, links to docs |
| 02 | PROJECT_OVERVIEW | problem, audience, goals, success metrics, constraints, assumptions |
| 03 | PRD | vision, personas, scope summary, features with priority (MoSCoW), success criteria, risks |
| 04 | FEATURES | master list: ID, name, description, priority, module, phase, status; traceability table |
| 05 | REQUIREMENTS | functional (REQ-xxx-nnn) and non-functional (performance, security, availability, compliance) |
| 06 | USER_ROLES | roles, goals, permissions summary, tenancy relation |
| 07 | USER_FLOWS | step flows per role/feature incl. error paths (text or mermaid) |
| 08 | USE_CASES | actor, precondition, main flow, alternatives, postcondition |
| 09 | USER_STORIES | "As a... I want... so that..." + acceptance criteria |
| 10 | SCOPE | in scope, out of scope, assumptions, decisions log (defaults chosen) |
| 11 | ROADMAP | MVP and phases with feature IDs and exit criteria |
| 12 | ARCHITECTURE | components, data flow, boundaries, multi-tenancy, scaling, diagrams |
| 13 | TECH_STACK | frontend, backend, DB, infra, libs; why each; versions |
| 14 | DATABASE_SCHEMA | entities, fields, types, keys, relations, indexes, constraints, migrations, tenancy columns |
| 15 | API_DOCUMENTATION | endpoints, auth, request/response, errors, pagination, rate limits, webhooks |
| 16 | AUTH_FLOW | register, login, MFA, reset, sessions/tokens, logout |
| 17 | RBAC | role x permission matrix, resource scoping, enforcement points |
| 18 | SECURITY | threat model, OWASP controls, secrets, data protection, audit log, compliance |
| 19 | UI_UX_SPEC | screens, layouts, states (empty/loading/error), accessibility, responsive |
| 20 | DESIGN_SYSTEM | colors, typography, spacing, components, themes |
| 21 | ROUTES | frontend routes + guards; backend route map |
| 22 | COMPONENTS | reusable components, props, states, where used |
| 23 | INTEGRATIONS | third-party services, purpose, auth, failure handling |
| 24 | PAYMENTS | plans, billing, taxes, trials, dunning, webhooks, refunds (or N/A) |
| 25 | EMAIL_SYSTEM | provider, templates, triggers, OTP, deliverability |
| 26 | NOTIFICATIONS | in-app/email/SMS/push events, preferences |
| 27 | ERROR_HANDLING | error taxonomy, codes, user messages, logging, retries |
| 28 | VALIDATION_RULES | per-field and business-rule validation (client + server) |
| 29 | TESTING | strategy, test pyramid, cases per feature, tools, coverage targets, E2E scenarios |
| 30 | DEPLOYMENT | environments, CI/CD, release, rollback, migrations |
| 31 | ENVIRONMENT | env vars (name, purpose, required), config, `.env.example` |
| 32 | MONITORING | logs, metrics, alerts, SLOs, error tracking |
| 33 | PERFORMANCE | targets, budgets, caching, load assumptions |
| 34 | BACKUP_RECOVERY | backup schedule, retention, RPO/RTO, restore test |
| 35 | CHANGELOG | versioned changes |
| 36 | TODO | remaining tasks by phase |
| 37 | BUGS | known bugs: severity, repro, status |
| 38 | CHANGE_REQUESTS | requested changes, impact, decision |

Not applicable example:
```
Status: Not Applicable
Reason: No paid or subscription functionality in this project.
```

Project-type additions (inside existing files, not new files): SaaS -> multi-tenancy, plans/limits, audit log in 12/14/24/18; ERP -> modules, accounting rules, approvals in 05/12/14; POS -> offline mode, receipts, barcode, shifts, multi-branch in 05/12/14; e-commerce -> catalog, cart, checkout, shipping, returns in 05/14/15/24. Analytics/dashboards -> use skill `erp-saas-analytics-visualization` and record KPIs in 04/05.
