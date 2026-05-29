"""Validate YAML frontmatter on all KB markdown files.

Checks:
  - Frontmatter exists and parses as YAML mapping
  - Required fields present
  - doc_type in allowed enum
  - status in doc_type-specific enum
  - L0/L1/L2 免除外の canonical doc に L0/L1/L2 構造があるか（簡易チェック）

Exit code 1 on ERROR. WARN does not fail.

Usage:
  python tools/validate_frontmatter.py knowledge/
"""
from __future__ import annotations

import sys
from pathlib import Path

from parse_frontmatter import iter_md_files, parse_frontmatter

REQUIRED_FIELDS = [
    "doc_id",
    "title",
    "doc_type",
    "project",
    "layer",
    "role_in_story",
    "status",
    "as_of",
    "audience",
    "one_line_thesis",
    "confidence",
]

DOC_TYPE_ENUM = {
    "index",
    "project",
    "meeting",
    "daily-log",
    "decision",
    "task",
    "design-note",
    "test-report",
    "component-note",
    "standard-note",
    "supplier-note",
    "research",
    "idea",
    "source",
    "requirement",
    "grill_session",
    "discussion",
}

LAYER_ENUM = {"raw", "canonical"}
ROLE_ENUM = {"routing", "problem", "insight", "proposal", "opportunity", "execution", "context"}
CONFIDENCE_ENUM = {"high", "medium", "low", "speculative"}

STATUS_BY_TYPE = {
    "meeting": {"scheduled", "in_progress", "completed", "compiled"},
    "daily-log": {"draft", "compiled"},
    "decision": {"proposed", "decided", "superseded", "archived"},
    "task": {"proposed", "in_progress", "blocked", "done", "cancelled"},
    "project": {"planning", "active", "on_hold", "completed", "cancelled"},
    "requirement": {"draft", "approved", "implementing", "shipped", "deprecated"},
}
DEFAULT_STATUS_ENUM = {"draft", "review", "canonical", "archived"}

L012_EXEMPT_TYPES = {"meeting", "daily-log", "index", "project", "decision", "task", "grill_session", "discussion"}
SANDBOX_EXEMPT_DIRS = {"inbox", "ideas", "research", "discussions", "grill-sessions"}


def check_l012_structure(body: str) -> list[str]:
    issues = []
    if "## L0" not in body:
        issues.append("L0 section missing")
    if "## L1" not in body:
        issues.append("L1 section missing")
    if "## L2" not in body:
        issues.append("L2 section missing")
    return issues


def is_sandbox_exempt(path: Path) -> bool:
    parts = path.parts
    if "80_sandbox" not in parts:
        return False
    idx = parts.index("80_sandbox")
    if idx + 1 < len(parts) and parts[idx + 1] in SANDBOX_EXEMPT_DIRS:
        return True
    if idx + 1 < len(parts) and parts[idx + 1] in {"README.md"}:
        return True
    return False


def validate_file(path: Path, repo_root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    fm, body = parse_frontmatter(path)
    if fm is None:
        if path.name in {"README.md", "CHANGELOG.md"}:
            return errors, warnings
        errors.append("frontmatter missing or unparseable")
        return errors, warnings

    for f in REQUIRED_FIELDS:
        if f not in fm:
            errors.append(f"required field missing: {f}")

    doc_type = fm.get("doc_type")
    if doc_type and doc_type not in DOC_TYPE_ENUM:
        errors.append(f"doc_type not in enum: {doc_type}")

    layer = fm.get("layer")
    if layer and layer not in LAYER_ENUM:
        errors.append(f"layer not in enum: {layer}")

    role = fm.get("role_in_story")
    if role and role not in ROLE_ENUM:
        errors.append(f"role_in_story not in enum: {role}")

    conf = fm.get("confidence")
    if conf and conf not in CONFIDENCE_ENUM:
        errors.append(f"confidence not in enum: {conf}")

    status = fm.get("status")
    allowed_status = STATUS_BY_TYPE.get(doc_type, DEFAULT_STATUS_ENUM)
    if status and status not in allowed_status:
        errors.append(f"status '{status}' not allowed for doc_type '{doc_type}'")

    project = fm.get("project")
    if project is not None and not isinstance(project, list):
        errors.append("project must be a list")

    audience = fm.get("audience")
    if audience is not None and not isinstance(audience, list):
        errors.append("audience must be a list")

    one_line = fm.get("one_line_thesis")
    title = fm.get("title")
    if (
        one_line
        and title
        and isinstance(one_line, str)
        and isinstance(title, str)
        and one_line.strip() == title.strip()
        and doc_type not in {"meeting", "daily-log"}
    ):
        warnings.append("one_line_thesis equals title (filler hint)")

    if (
        layer == "canonical"
        and doc_type not in L012_EXEMPT_TYPES
        and not is_sandbox_exempt(path)
    ):
        l012_issues = check_l012_structure(body)
        for issue in l012_issues:
            warnings.append(f"L0/L1/L2: {issue}")

    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: validate_frontmatter.py <knowledge_dir>", file=sys.stderr)
        return 2
    target = Path(argv[1])
    if not target.exists():
        print(f"path not found: {target}", file=sys.stderr)
        return 2
    repo_root = target.parent if target.is_dir() else target.parent.parent

    error_count = 0
    warn_count = 0
    file_count = 0

    for path in iter_md_files(target):
        file_count += 1
        errors, warnings = validate_file(path, repo_root)
        rel = path.relative_to(repo_root)
        for e in errors:
            print(f"ERROR {rel}: {e}")
            error_count += 1
        for w in warnings:
            print(f"WARN  {rel}: {w}")
            warn_count += 1

    print(f"\n--- summary ---")
    print(f"files checked: {file_count}")
    print(f"errors: {error_count}")
    print(f"warnings: {warn_count}")

    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
