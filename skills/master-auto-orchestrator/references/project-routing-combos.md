# Routing rules

Match every category that fits. Run the chain in order. Skills marked (opt) are used only if installed; otherwise use the fallback.

| Request looks like | Skill chain | Fallback |
|---|---|---|
| New SaaS / web app / subscription product | `saas-kickoff` -> `senior-architect` -> `database-schema-designer` -> `test-driven-development` | `brainstorming` |
| Resume / continue SaaS (docs/ exists) | `saas-kickoff` (resume mode) -> task skill below | read docs/ manually |
| Payments, billing, Stripe, subscriptions | `stripe-integration-expert` -> `secure-code-guardian` -> `test-driven-development` | `senior-backend` |
| Database, schema, migrations, slow queries | `database-schema-designer` -> `database-optimizer` / `postgres-pro` / `sql-pro` | `senior-backend` |
| Backend / API | `api-designer` -> `senior-backend` -> `test-driven-development` | `senior-fullstack` |
| Frontend / UI / landing page | `frontend-design` -> `senior-frontend` -> `a11y-audit` | `ui-ux-pro-max` |
| Next.js / React / Flutter / mobile | `nextjs-developer` / `react-expert` / `flutter-expert` / `senior-mobile` | `senior-fullstack` |
| Bug, error, failing test | `systematic-debugging` -> `test-failure-diagnosis` -> `verification-before-completion` | `debug` |
| Any SEO, ranking, meta, schema, keywords, AI search / GEO / AEO | `seo-master` (routes to its 33 categories itself) | none |
| WordPress / WooCommerce / Elementor / Bricks | `wordpress-pro`, `woocommerce-health-check`, `wp-performance-review`, the matching `figma-to-*` / `migrate-*` skill | `senior-fullstack` |
| Security review, auth, secrets, OWASP | `security-reviewer` -> `secure-code-guardian` -> `security-pen-testing` (authorized targets only) | `senior-security` |
| Testing, QA, coverage, e2e | `test-master` -> `playwright-expert` / `webapp-testing` -> `coverage` | `senior-qa` |
| Performance / speed | `performance-optimization` -> `performance-profiler` | `wp-performance-review` for WP |
| Deploy, CI/CD, Docker, infra | `ci-cd-pipeline-builder` -> `docker-development` -> `senior-devops` -> `monitoring-and-alerting` | `cloud-architect` |
| Code review / PR | `code-review` -> `requesting-code-review` | `code-reviewer` |
| Refactor / cleanup | `safe-refactor` or `codebase-design` -> `ai-slop-cleaner` | `simplify` |
| Whole-project audit | run in parallel where possible: architecture (`senior-architect`), security (`security-reviewer`), SEO (`seo-master`), testing (`test-master`), performance (`performance-optimization`), then merge into one report | |
| Docs / README / PRD | `create-prd` / `documentation-strategy` / `code-documenter` | `writer` agent |
| Unclear idea | `brainstorming` or `grill-me` first | ask one question |

## Ordering principles

1. Plan / architecture before code.
2. Data model before API, API before UI.
3. Security and tests are part of every build chain, not a last step.
4. Specific skill over generic skill.
5. Parallelize independent audits; serialize dependent work.
