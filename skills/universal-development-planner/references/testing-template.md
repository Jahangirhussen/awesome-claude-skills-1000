# Testing template

Pyramid: many unit, fewer integration/API, few E2E.
- Unit: pure logic, validation, calculations (money, tax, stock).
- Integration/API: endpoints with real DB (test containers), auth and RBAC allow/deny, tenant isolation.
- E2E (Playwright): critical journeys (signup, login, core transaction, payment, report); desktop + mobile viewport.
- Regression: bugs get a test first.
- Security: authz bypass, injection, XSS/CSRF, rate limits, dependency audit.
- Performance: load test key endpoints; DB query plans; Core Web Vitals for web.
- Accessibility: automated axe + keyboard pass.

Per feature table: Feature | Requirement | Test type | Scenario | Expected | Status.
Coverage targets: set per area (e.g. 80% business logic). CI runs unit + integration on every PR; E2E on main/staging.
Data: factories/seeds; no production data.
