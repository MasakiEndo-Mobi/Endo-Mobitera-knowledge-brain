#!/usr/bin/env bash
# tools/setup.sh
# One-shot setup for macOS / Linux: ensure .claude/skills/ symlinks to .cursor/skills/.

set -e

cd "$(dirname "$0")/.."
REPO_ROOT="$(pwd)"

echo "vehicle-mech-kb-starter setup"
echo "Repo root: $REPO_ROOT"

if [ ! -d ".cursor/skills" ]; then
  echo ".cursor/skills not found" >&2
  exit 1
fi

mkdir -p .claude/skills

for skill_dir in .cursor/skills/*/; do
  name=$(basename "$skill_dir")
  case "$name" in
    _*) continue ;;
  esac
  if [ ! -f "$skill_dir/SKILL.md" ]; then
    continue
  fi
  link=".claude/skills/$name"
  if [ -L "$link" ]; then
    continue
  fi
  if [ -e "$link" ]; then
    rm -rf "$link"
  fi
  ln -s "../../$skill_dir" "$link"
  echo "  symlink: .claude/skills/$name -> ../../$skill_dir"
done

echo ""
echo "Done. Next steps:"
echo "  1. conda create -n vehkb-env python=3.12 -y"
echo "  2. conda activate vehkb-env"
echo "  3. pip install -r tools/requirements.txt"
echo "  4. git init && git config core.hooksPath .githooks"
echo "  5. Open this folder in Obsidian, install Templater + Dataview from Community Plugins"
