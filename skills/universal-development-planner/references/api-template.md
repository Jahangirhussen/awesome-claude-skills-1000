# API template

Conventions: base path `/api/v1`, JSON, ISO 8601 UTC dates, pagination `?page&limit` or cursor, consistent error shape `{ "error": { "code", "message", "details" } }`, idempotency keys for payments, rate limits.

Per endpoint:
```
POST /api/v1/orders
Auth: Bearer; roles: sales, admin; tenant-scoped
Request: { customer_id, items:[{product_id, qty}] }
Validation: qty > 0, product active, stock available
Response 201: { id, status, total }
Errors: 400 validation, 401, 403, 404, 409 stock, 429
Side effects: stock movement, audit log, notification
Tests: unit (validation), integration (stock), E2E (checkout)
```
Checklist: every feature has endpoints; every endpoint has auth + role + tenant scope; list endpoints paginated and filterable; webhooks signed and idempotent; OpenAPI spec generated; versioning and deprecation policy.
