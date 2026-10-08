# Audit

## Counts
- SEO-only skills found at start: 22 (+ 8 related general skills kept in place: site-architecture, internal-link-builder, content-refresh-system, content-brief-authoring, competitor-alternatives, pillar-content-architecture, content-strategy, competitor-experience-audit)
- Merged into canonical structure and retired from top level: 22 (full text preserved in `_source/`)
- Duplicate/overlap groups: 6 (AI search; audits; keyword; content; link; platform pages)
- Final canonical: 33 parents, 142 children, 3 grandchildren
- Engine pages (22-25) and ERP/POS (13-14) are parent-only on purpose, reusing 19 and 12
- Missing skills created: children with no prior source, written from best-practice checks (see REGISTRY rows with empty Merged-from)

## Duplicate report
| Existing Skill | Similar Skill | Decision | Reason | Canonical Skill |
|---|---|---|---|---|
| ai-seo | seo-aeo-amplifier | MERGED | AI-search visibility + audit overlap | 19-ai-seo |
| ai-seo | seo-aeo-geo | MERGED | generative search overlap | 19-ai-seo + 20-geo |
| seo-aeo-geo | aeo | CHILD OF | AEO is direct-answer subset of GEO/AI | 21-aeo (separate parent kept) |
| seo-audit | seo-technical | CHILD OF | audit orchestrates; technical holds method | 30-seo-audit/full-audit -> 03-technical-seo |
| seo-audit | seo-audit-orchestration | MERGED | same orchestrator purpose (Ahrefs variant) | 30-seo-audit |
| seo-technical | seo-site-health-audit | CHILD OF | triage layer over technical audit | 30-seo-audit/technical-audit |
| seo-keyword | seo-keyword-gap-audit | MERGED | keyword gap is part of keyword research | 01-core-seo/keyword-research |
| seo-content-audit | seo-content-gap-audit | KEEP SEPARATE | audit existing vs find missing; both under content | 06-content-seo/content-refresh, content-gap |
| seo-content-audit | content-refresh-system | DEPENDENCY OF | general refresh discipline kept installed | 06-content-seo/content-refresh |
| seo-offpage | seo-backlink-audit | CHILD OF | audit is a specialization | 05-off-page-seo/link-audit |
| seo-specialist | seo-keyword / seo-onpage | MERGED | generalist overlaps strategy | 01-core-seo/seo-strategy |
| site-architecture | seo-technical (architecture) | DEPENDENCY OF | general IA skill kept installed | 03-technical-seo/website-architecture |
| internal-link-builder | seo-onpage (links) | DEPENDENCY OF | general skill kept installed | 04-on-page-seo/internal-linking |
| competitor-alternatives | seo-competitor | KEEP SEPARATE | page creation vs analysis | 12-saas-seo/comparison-pages |
| pillar-content-architecture | seo-keyword (clusters) | DEPENDENCY OF | hub design kept installed | 06-content-seo/content-clusters |
| aeo / ai-seo / seo-aeo-geo / seo-aeo-amplifier | chatgpt/claude/gemini/perplexity pages | MERGED | engine pages share one method | 19-ai-seo (engine pages hold only engine specifics) |
| ERP / POS pages | SaaS pages | MERGED | same page types, different matrix | 12-saas-seo children reused |

## Retired (moved to `_source/`)
aeo, ai-seo, local-seo-manager, programmatic-seo, schema-markup, seo-aeo-amplifier, seo-aeo-geo, seo-audit, seo-audit-orchestration, seo-backlink-audit, seo-competitor, seo-content-audit, seo-content-gap-audit, seo-keyword, seo-keyword-gap-audit, seo-offpage, seo-onpage, seo-rank-tracking, seo-site-health-audit, seo-specialist, seo-technical, seo-traffic-diagnosis
