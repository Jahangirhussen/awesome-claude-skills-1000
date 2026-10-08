# Domain checklists

## Architecture
Boundaries and modules, tenancy model, data flow, failure modes, scaling limits. Record choices in `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.

## Development
Match existing code style. Validate input at boundaries. Handle errors explicitly. Keep functions small. Prefer existing libraries over new dependencies.

## Security
Auth and authorization on every route. Org-scoped queries for multi-tenant data. Validate and escape input and output. Secrets only in env. Rate limit public endpoints. Verify Stripe/webhook signatures. Dependency audit.

## SEO
Title and meta per page, one H1, canonical, sitemap and robots, structured data (schema.org), image alt and size, Core Web Vitals, internal links, hreflang if multilingual, no keyword cannibalization. For AI search: clear entities, direct answers, citations.

## Testing
Unit for logic, integration for API and DB, e2e for critical user flows (signup, checkout). Cover error paths. Tests must fail before the fix and pass after.

## Deployment
Env vars documented in `.env.example`. CI runs tests and build. Migrations run safely. Health check, logging, error tracking, backups. Rollback plan.
