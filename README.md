# Awesome Claude Skills (1350+)

A curated, deduplicated, quality-audited collection of Claude Code skills (1,351 skills across 15 domains) plus a few original builds.

- `skills/` : part 1 of the library (a11y-audit to linkedin-profile, 557 folders). Part 2 (linkedin-skills to zero-hallucination-coder, 558 folders): https://github.com/Jahangirhussen/awesome-claude-skills-part2
- Split in two repos so GitHub can list every folder (limit 1000 items per folder).
- Original builds: `seo-master` (33 SEO categories, ~190 skills), `master-auto-orchestrator` (routes any task to the right skills), `master-skills` (library index + imports), `erp-saas-analytics-visualization`, `universal-development-planner`, `human-writing-mode`, `originality-guard`, `docs-pdf-clean-output`.
- Quality: each skill scored with a 100-point structural rubric; average 84.5; see `skills/master-skills/QUALITY-AUDIT/`.

## Install
```bash
git clone https://github.com/Jahangirhussen/awesome-claude-skills-1000.git
cp -R awesome-claude-skills-1000/skills/* ~/.claude/skills/
git clone https://github.com/Jahangirhussen/awesome-claude-skills-part2.git
cp -R awesome-claude-skills-part2/skills/* ~/.claude/skills/
```
Restart Claude Code.

## Notes
This is a curated collection, not all original work. See `CREDITS.md` for sources and licenses. Scores come from a heuristic, not human review.
