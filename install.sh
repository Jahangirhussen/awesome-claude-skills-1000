#!/usr/bin/env bash
# One-click setup: installs the full skill library into ~/.claude/skills and enables auto-routing.
# Usage: curl -fsSL https://raw.githubusercontent.com/Jahangirhussen/awesome-claude-skills-1000/main/install.sh | bash
set -euo pipefail
command -v git >/dev/null 2>&1 || { echo "git is required"; exit 1; }
dst="$HOME/.claude"; tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
echo "== downloading both parts =="
git clone --depth 1 -q https://github.com/Jahangirhussen/awesome-claude-skills-1000.git "$tmp/p1"
git clone --depth 1 -q https://github.com/Jahangirhussen/awesome-claude-skills-part2.git "$tmp/p2"
mkdir -p "$dst/skills"
echo "== installing skills into $dst/skills (same-name skills are overwritten) =="
cp -R "$tmp/p1/skills/." "$dst/skills/"
cp -R "$tmp/p2/skills/." "$dst/skills/"
if [ "${SKIP_RULES:-0}" != "1" ]; then
  marker="<!-- claude-skills-autoroute -->"
  touch "$dst/CLAUDE.md"
  if ! grep -q "$marker" "$dst/CLAUDE.md"; then
    cp "$dst/CLAUDE.md" "$dst/CLAUDE.md.bak" 2>/dev/null || true
    cat >> "$dst/CLAUDE.md" <<'RULES'

<!-- claude-skills-autoroute -->
## Orchestrator
On any meaningful task, invoke the `master-auto-orchestrator` skill first, silently. It picks the right skills from the library. For substantial software builds it runs `universal-development-planner` before coding. SEO goes to `seo-master`. Dashboards, KPIs, charts go to `erp-saas-analytics-visualization`.

## Writing quality
When writing documents, emails, essays or reports for the user, apply `human-writing-mode` and `originality-guard`, and build files via `docs-pdf-clean-output`. Never invent facts or citations.
RULES
    echo "== auto-routing rules added to $dst/CLAUDE.md (backup: CLAUDE.md.bak) =="
  fi
fi
echo "Done. Restart Claude Code. Set SKIP_RULES=1 to skip editing CLAUDE.md."
