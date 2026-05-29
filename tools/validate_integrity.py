"""Validate KB integrity: doc_id uniqueness, relations resolvability, HTML non-equal-rank guard.

Checks:
  - doc_id is unique across the repo
  - All relations.{depends_on, supports, contradicts, related} doc_ids exist
  - source_docs paths exist
  - No .html paths inside relations.*

Exit code 1 on ERROR.

Usage:
  python tools/validate_integrity.py knowledge/
"""
from __future__ import annotations

import sys
from pathlib import Path

from parse_frontmatter import iter_md_files, parse_frontmatter

RELATION_FIELDS = ["depends_on", "supports", "contradicts", "related"]


def collect_doc_ids(target: Path) -> dict[str, list[Path]]:
    by_id: dict[str, list[Path]] = {}
    for path in iter_md_files(target):
        fm, _ = parse_frontmatter(path)
        if not fm:
            continue
        doc_id = fm.get("doc_id")
        if doc_id:
            by_id.setdefault(doc_id, []).append(path)
    return by_id


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: validate_integrity.py <knowledge_dir>", file=sys.stderr)
        return 2
    target = Path(argv[1])
    if not target.exists():
        print(f"path not found: {target}", file=sys.stderr)
        return 2
    repo_root = target.parent if target.is_dir() else target.parent.parent

    by_id = collect_doc_ids(target)
    all_ids = set(by_id.keys())

    error_count = 0
    warn_count = 0

    for doc_id, paths in by_id.items():
        if len(paths) > 1:
            rels = [str(p.relative_to(repo_root)) for p in paths]
            print(f"ERROR doc_id duplicated: {doc_id} -> {rels}")
            error_count += 1

    for path in iter_md_files(target):
        fm, _ = parse_frontmatter(path)
        if not fm:
            continue
        rel = path.relative_to(repo_root)
        relations = fm.get("relations") or {}
        if isinstance(relations, dict):
            for field in RELATION_FIELDS:
                values = relations.get(field) or []
                if not isinstance(values, list):
                    continue
                for v in values:
                    if not isinstance(v, str):
                        continue
                    if v.endswith(".html") or "/assets/" in v:
                        print(f"ERROR {rel}: relations.{field} contains HTML/asset path: {v}")
                        error_count += 1
                        continue
                    if v not in all_ids:
                        print(f"ERROR {rel}: relations.{field} -> unknown doc_id: {v}")
                        error_count += 1

        source_docs = fm.get("source_docs") or []
        if isinstance(source_docs, list):
            for sd in source_docs:
                if not isinstance(sd, str):
                    continue
                if sd.endswith(".html"):
                    print(f"ERROR {rel}: source_docs contains HTML path: {sd}")
                    error_count += 1
                    continue
                candidate = repo_root / sd
                if not candidate.exists():
                    print(f"WARN  {rel}: source_docs path not found: {sd}")
                    warn_count += 1

    print(f"\n--- summary ---")
    print(f"doc_ids: {len(all_ids)}")
    print(f"errors: {error_count}")
    print(f"warnings: {warn_count}")

    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
