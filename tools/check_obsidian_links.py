"""Check [[wikilink]] integrity across the Obsidian vault.

For each [[target]] / [[target|alias]] / [[target#header]] reference in any
markdown body, verify that a target note exists. Resolution rules:
  - Strip alias and header anchor
  - Try exact filename match (without .md extension) anywhere in the vault
  - Try doc_id match (some users link by doc_id)

Exit code 1 on broken links.

Usage:
  python tools/check_obsidian_links.py knowledge/
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from parse_frontmatter import iter_md_files, parse_frontmatter

WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")


def collect_note_index(target: Path) -> tuple[set[str], set[str]]:
    """Return (set_of_basenames_without_ext, set_of_doc_ids).

    Indexes both the target directory and its vault-root siblings (the top-level
    governance docs such as AGENTS.md / README.md / CLAUDE.md) because Obsidian
    treats the entire vault as a single namespace for wikilink resolution.
    """
    basenames: set[str] = set()
    doc_ids: set[str] = set()
    for path in iter_md_files(target):
        basenames.add(path.stem)
        fm, _ = parse_frontmatter(path)
        if fm and fm.get("doc_id"):
            doc_ids.add(str(fm["doc_id"]))
    # Also include sibling .md files at the vault root (one level up)
    vault_root = target.parent if target.is_dir() else target.parent.parent
    for path in vault_root.glob("*.md"):
        basenames.add(path.stem)
    return basenames, doc_ids


def resolve_link(raw: str) -> str:
    """Strip alias (|...) and header anchor (#...) and surrounding whitespace."""
    token = raw.split("|", 1)[0]
    token = token.split("#", 1)[0]
    return token.strip()


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: check_obsidian_links.py <vault_dir>", file=sys.stderr)
        return 2
    target = Path(argv[1])
    if not target.exists():
        print(f"path not found: {target}", file=sys.stderr)
        return 2
    repo_root = target.parent if target.is_dir() else target.parent.parent

    basenames, doc_ids = collect_note_index(target)

    broken_count = 0
    checked = 0

    for path in iter_md_files(target):
        _, body = parse_frontmatter(path)
        if not body:
            continue
        rel = path.relative_to(repo_root)
        for m in WIKILINK_RE.finditer(body):
            checked += 1
            tok = resolve_link(m.group(1))
            if not tok:
                continue
            # Resolve: try basename then doc_id
            if tok in basenames or tok in doc_ids:
                continue
            # As a final fallback allow tokens that contain a path separator
            # (e.g. [[20_components/connectors/usb-c]])
            if "/" in tok:
                candidate = repo_root / "knowledge" / (tok + ".md")
                if candidate.exists():
                    continue
                candidate2 = repo_root / (tok + ".md")
                if candidate2.exists():
                    continue
            print(f"BROKEN {rel}: [[{tok}]]")
            broken_count += 1

    print(f"\n--- summary ---")
    print(f"wikilinks checked: {checked}")
    print(f"broken: {broken_count}")

    return 1 if broken_count else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
