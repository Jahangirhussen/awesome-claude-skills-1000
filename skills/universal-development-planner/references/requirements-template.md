# Requirements template

ID format: `REQ-<AREA>-<nnn>` (e.g. REQ-INV-001). One testable statement each.

## Functional
| ID | Requirement | Priority | Feature | Acceptance criteria |
|---|---|---|---|---|
| REQ-AUTH-001 | A user can reset a password by email link valid 30 min | Must | F-003 | link expires; token single-use |

## Non-functional
- Performance: p95 API < 300 ms at N concurrent users; page LCP < 2.5 s
- Security: OWASP ASVS L2 controls, password hashing (argon2/bcrypt), rate limiting
- Availability: target %, maintenance windows
- Scalability: expected users/data growth
- Compliance: GDPR / PCI / local tax rules where relevant
- Accessibility: WCAG 2.1 AA
- Browser/device support

## Rules
- No requirement without a feature and a test.
- Mark each Must/Should/Could. Remove duplicates and contradictions during the audit.

## User story format
As a <role>, I want <capability> so that <benefit>.
Acceptance: Given <context> When <action> Then <result>.
