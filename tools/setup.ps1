# tools/setup.ps1
# One-shot setup for Windows: re-create .claude/skills/ symlinks pointing to .cursor/skills/.
# Re-run after fresh clone, after zip extract, or after adding new skills.

$ErrorActionPreference = "Stop"

$repoRoot = (Get-Item $PSScriptRoot).Parent.FullName
Set-Location $repoRoot

Write-Host "vehicle-mech-kb-starter setup"
Write-Host "Repo root: $repoRoot"

# 1. Verify .cursor/skills/ exists
$cursorSkills = Join-Path $repoRoot ".cursor/skills"
if (-not (Test-Path $cursorSkills)) {
    Write-Error ".cursor/skills not found at $cursorSkills"
    exit 1
}

# 2. Ensure .claude/skills exists
$claudeSkills = Join-Path $repoRoot ".claude/skills"
if (-not (Test-Path $claudeSkills)) {
    New-Item -ItemType Directory -Path $claudeSkills | Out-Null
}

# 3. For each .cursor/skills/<name>/ with a SKILL.md, ensure a matching link/copy in .claude/skills/
$skillDirs = Get-ChildItem -Path $cursorSkills -Directory | Where-Object {
    $_.Name -notlike "_*" -and (Test-Path (Join-Path $_.FullName "SKILL.md"))
}

foreach ($s in $skillDirs) {
    $target = $s.FullName
    $linkPath = Join-Path $claudeSkills $s.Name
    if (Test-Path $linkPath) {
        # Already exists; check whether it points at the right place
        $existing = Get-Item $linkPath -Force
        if ($existing.LinkType -eq "SymbolicLink") {
            continue
        }
        # Plain directory (likely from zip extract). Remove and recreate as link if possible.
        Remove-Item -Recurse -Force $linkPath
    }
    try {
        # Symbolic links on Windows need either Admin or Developer Mode.
        New-Item -ItemType SymbolicLink -Path $linkPath -Target $target -ErrorAction Stop | Out-Null
        Write-Host "  symlink: .claude/skills/$($s.Name) -> .cursor/skills/$($s.Name)"
    } catch {
        # Fallback: directory junction (no admin needed, works for dirs only on same volume)
        try {
            New-Item -ItemType Junction -Path $linkPath -Target $target -ErrorAction Stop | Out-Null
            Write-Host "  junction: .claude/skills/$($s.Name) -> .cursor/skills/$($s.Name)"
        } catch {
            # Final fallback: hard copy
            Copy-Item -Recurse $target $linkPath
            Write-Host "  copy: .claude/skills/$($s.Name) (no symlink available — re-run setup after edits)"
        }
    }
}

Write-Host ""
Write-Host "Done. Next steps:"
Write-Host "  1. conda create -n vehkb-env python=3.12 -y"
Write-Host "  2. conda activate vehkb-env"
Write-Host "  3. pip install -r tools/requirements.txt"
Write-Host "  4. git init && git config core.hooksPath .githooks"
Write-Host "  5. Open this folder in Obsidian, install Templater + Dataview from Community Plugins"
