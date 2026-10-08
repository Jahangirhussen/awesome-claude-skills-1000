# Awesome Claude Skills (1350+)

A curated, deduplicated, quality-audited collection of Claude Code skills (1,351 skills across 15 domains) plus a few original builds.

- `skills/` : Part 1 = SEO, development and all non-agent skills (962 folders). Part 2 (all agent skills): https://github.com/Jahangirhussen/awesome-claude-skills-part2
- Split in two repos so GitHub can list every folder (limit 1000 items per folder).
- Original builds: `seo-master` (33 SEO categories, ~190 skills), `master-auto-orchestrator` (routes any task to the right skills), `master-skills` (library index + imports), `erp-saas-analytics-visualization`, `universal-development-planner`, `human-writing-mode`, `originality-guard`, `docs-pdf-clean-output`.
- Quality: each skill scored with a 100-point structural rubric; average 84.5; see `skills/master-skills/QUALITY-AUDIT/`.


## One-click setup
Installs **both parts** (all 1,351 skills) and enables auto-routing. Needs only Git and Claude Code. It overwrites same-name skills in `~/.claude/skills` and appends two short rule blocks to `~/.claude/CLAUDE.md` (backup `CLAUDE.md.bak`; set `SKIP_RULES=1` to skip the rules).

macOS / Linux / Git Bash:
```bash
curl -fsSL https://raw.githubusercontent.com/Jahangirhussen/awesome-claude-skills-1000/main/install.sh | bash
```
Windows PowerShell:
```powershell
irm https://raw.githubusercontent.com/Jahangirhussen/awesome-claude-skills-1000/main/install.ps1 | iex
```
Then restart Claude Code. Read the script first if you like: [install.sh](install.sh), [install.ps1](install.ps1).

## What is in this repo
Library is split in two repos: Part 1 = [awesome-claude-skills-1000](https://github.com/Jahangirhussen/awesome-claude-skills-1000), Part 2 = [awesome-claude-skills-part2](https://github.com/Jahangirhussen/awesome-claude-skills-part2).
This repo: **Part 1 (awesome-claude-skills-1000)**, 962 skill folders (SEO, development, business systems, data, marketing, design, security, testing and everything that is not an agent skill). Full per-skill list with score and source: [SKILLS-TABLE.md](SKILLS-TABLE.md).

Scores are /100 from a heuristic structure rubric (not human review). Sub category exists mainly for SEO; other domains are flat.

| Skill Category | Sub Category | Skills in this repo | Avg Score /100 | Skill files incl. nested |
|---|---|---:|---:|---:|
| 01-DEVELOPMENT | general | 85 | 83 | 85 |
| 02-BUSINESS-SYSTEMS | accounting | 14 | 85 | 14 |
| 02-BUSINESS-SYSTEMS | business-automation | 100 | 85 | 100 |
| 02-BUSINESS-SYSTEMS | crm | 14 | 86 | 14 |
| 02-BUSINESS-SYSTEMS | ecommerce | 5 | 81 | 5 |
| 02-BUSINESS-SYSTEMS | hr | 22 | 84 | 22 |
| 02-BUSINESS-SYSTEMS | saas | 11 | 85 | 11 |
| 02-BUSINESS-SYSTEMS | shopify | 1 | 85 | 1 |
| 02-BUSINESS-SYSTEMS | woocommerce | 6 | 82 | 6 |
| 02-BUSINESS-SYSTEMS | wordpress | 35 | 81 | 35 |
| 03-AI | general | 37 | 85 | 37 |
| 04-RESEARCH | general | 121 | 87 | 125 |
| 05-SEO | 33 parent categories | 1 | 90 | 179 |
| 05-SEO | general | 6 | 87 | 6 |
| 06-MARKETING | general | 70 | 84 | 70 |
| 07-DATA | general | 39 | 87 | 39 |
| 08-DEVOPS | general | 47 | 85 | 47 |
| 09-SECURITY | general | 57 | 86 | 57 |
| 10-TESTING | general | 50 | 84 | 50 |
| 11-DESIGN | general | 109 | 84 | 109 |
| 12-AUTOMATION | general | 7 | 89 | 7 |
| 13-PRODUCT | general | 41 | 83 | 42 |
| 14-DOCUMENTATION | general | 38 | 83 | 38 |
| 15-SUPPORT | general | 14 | 87 | 14 |
| 99-UNCLASSIFIED | general | 31 | 52 | 20 |
| Library index | domains 01-15 + imports | 1 | 85 | 60 |
| **Total** | | **962** | **84** | **1193** |


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
