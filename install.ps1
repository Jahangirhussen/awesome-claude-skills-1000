# One-click setup (Windows): installs the full skill library into ~/.claude/skills and enables auto-routing.
# Usage: irm https://raw.githubusercontent.com/Jahangirhussen/awesome-claude-skills-1000/main/install.ps1 | iex
$ErrorActionPreference = "Stop"
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Write-Error "git is required"; exit 1 }
$dst = Join-Path $env:USERPROFILE ".claude"
$tmp = Join-Path $env:TEMP ("claude-skills-" + [guid]::NewGuid())
New-Item -ItemType Directory -Force $tmp | Out-Null
try {
  Write-Host "== downloading both parts =="
  git clone --depth 1 -q https://github.com/Jahangirhussen/awesome-claude-skills-1000.git "$tmp\p1"
  git clone --depth 1 -q https://github.com/Jahangirhussen/awesome-claude-skills-part2.git "$tmp\p2"
  New-Item -ItemType Directory -Force "$dst\skills" | Out-Null
  Write-Host "== installing skills into $dst\skills (same-name skills are overwritten) =="
  Copy-Item "$tmp\p1\skills\*" "$dst\skills" -Recurse -Force
  Copy-Item "$tmp\p2\skills\*" "$dst\skills" -Recurse -Force
  if ($env:SKIP_RULES -ne "1") {
    $f = Join-Path $dst "CLAUDE.md"
    if (-not (Test-Path $f)) { New-Item -ItemType File $f | Out-Null }
    $cur = Get-Content $f -Raw -ErrorAction SilentlyContinue
    if (-not $cur -or $cur -notmatch "claude-skills-autoroute") {
      Copy-Item $f "$f.bak" -Force
      $rules = @"

<!-- claude-skills-autoroute -->
## Orchestrator
On any meaningful task, invoke the ``master-auto-orchestrator`` skill first, silently. It picks the right skills from the library. For substantial software builds it runs ``universal-development-planner`` before coding. SEO goes to ``seo-master``. Dashboards, KPIs, charts go to ``erp-saas-analytics-visualization``.

## Writing quality
When writing documents, emails, essays or reports for the user, apply ``human-writing-mode`` and ``originality-guard``, and build files via ``docs-pdf-clean-output``. Never invent facts or citations.
"@
      Add-Content -Path $f -Value $rules
      Write-Host "== auto-routing rules added to $f (backup: CLAUDE.md.bak) =="
    }
  }
  Write-Host "Done. Restart Claude Code. Set `$env:SKIP_RULES=1 to skip editing CLAUDE.md."
} finally { Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue }
