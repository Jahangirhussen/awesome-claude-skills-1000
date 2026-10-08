# Awesome Claude Skills (1350+)

A curated, deduplicated, quality-audited collection of Claude Code skills (1,351 skills across 15 domains) plus a few original builds.

- `skills/` : part 1 of the library (a11y-audit to linkedin-profile, 557 folders). Part 2 (linkedin-skills to zero-hallucination-coder, 558 folders): https://github.com/Jahangirhussen/awesome-claude-skills-part2
- Split in two repos so GitHub can list every folder (limit 1000 items per folder).
- Original builds: `seo-master` (33 SEO categories, ~190 skills), `master-auto-orchestrator` (routes any task to the right skills), `master-skills` (library index + imports), `erp-saas-analytics-visualization`, `universal-development-planner`, `human-writing-mode`, `originality-guard`, `docs-pdf-clean-output`.
- Quality: each skill scored with a 100-point structural rubric; average 84.5; see `skills/master-skills/QUALITY-AUDIT/`.

## Setup (for anyone)

**Requirements:** [Claude Code](https://docs.claude.com/en/docs/claude-code) installed, Git. Nothing else is needed for the skills themselves.

### 1. Download both parts
The library is split across two repos so every folder shows on GitHub (limit 1000 items per folder).

macOS / Linux / Git Bash:
```bash
git clone https://github.com/Jahangirhussen/awesome-claude-skills-1000.git
git clone https://github.com/Jahangirhussen/awesome-claude-skills-part2.git
mkdir -p ~/.claude/skills
cp -R awesome-claude-skills-1000/skills/* ~/.claude/skills/
cp -R awesome-claude-skills-part2/skills/* ~/.claude/skills/
```

Windows PowerShell:
```powershell
git clone https://github.com/Jahangirhussen/awesome-claude-skills-1000.git
git clone https://github.com/Jahangirhussen/awesome-claude-skills-part2.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item awesome-claude-skills-1000\skills\* "$env:USERPROFILE\.claude\skills" -Recurse -Force
Copy-Item awesome-claude-skills-part2\skills\* "$env:USERPROFILE\.claude\skills" -Recurse -Force
```
Want only a few skills? Copy just those folders (each folder is one skill with a `SKILL.md`).

### 2. Turn on automatic routing (recommended)
Skills work on their own, but for the "just describe the task" experience add this to `~/.claude/CLAUDE.md` (create the file if missing):

```markdown
## Orchestrator
On any meaningful task, invoke the `master-auto-orchestrator` skill first, silently. It picks the right skills from the library. For substantial software builds it runs `universal-development-planner` before coding. SEO goes to `seo-master`. Dashboards, KPIs, charts go to `erp-saas-analytics-visualization`.

## Writing quality
When writing documents, emails, essays or reports for the user, apply `human-writing-mode` and `originality-guard`, and build files via `docs-pdf-clean-output`. Never invent facts or citations.
```

### 3. Restart and check
Restart Claude Code, then ask: *"Build me a small POS system"* (planner + orchestrator should start), or *"Audit the SEO of my site"* (`seo-master`). Type `/skills` or ask Claude to list skills to confirm they loaded.

### Notes
- **Claude Desktop** does not read `~/.claude/skills`. Zip a skill folder and upload it under Settings > Capabilities > Skills.
- ~1,350 skills means a long skill list. If it feels heavy, copy only the domains you use (for example `seo-master`, `master-auto-orchestrator`, `universal-development-planner`).
- Some skills need extra tools or accounts (MCP servers, API keys, Ahrefs, Stripe). Read the skill's `SKILL.md`. Never commit your own keys.
- Skills are third-party and original mixed; check `CREDITS.md` for licenses before commercial reuse.
- Quality scores come from a heuristic rubric (average 84.5), not human review. Report problems via GitHub issues.

## Notes
This is a curated collection, not all original work. See `CREDITS.md` for sources and licenses. Scores come from a heuristic, not human review.
