"""Helper: parse YAML frontmatter from Markdown files."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml


def parse_frontmatter(path: Path) -> tuple[Optional[dict], str]:
    """Return (frontmatter_dict_or_None, body_str). On parse error returns (None, full_text)."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None, ""

    if not text.startswith("---"):
        return None, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text

    fm_raw = parts[1]
    body = parts[2].lstrip("\n")
    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict):
            return None, text
        return fm, body
    except yaml.YAMLError:
        return None, text


def iter_md_files(root: Path):
    """Yield .md paths under root, skipping .obsidian/, assets/, hidden dirs."""
    for path in root.rglob("*.md"):
        parts = path.parts
        if any(p.startswith(".") and p != "." for p in parts):
            continue
        if "assets" in parts:
            continue
        if "_archive" in parts:
            continue
        yield path
