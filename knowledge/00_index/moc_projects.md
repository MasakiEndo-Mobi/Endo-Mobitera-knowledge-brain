---
doc_id: index.moc-projects
title: Projects MOC
doc_type: index
project: [all]
layer: canonical
role_in_story: routing
status: canonical
as_of: 2026-05-28
audience: [self]
one_line_thesis: アクティブな全プロジェクトを横断的に俯瞰する Dataview ベースの動的ビュー。
confidence: high
---

# Projects MOC

`10_projects/<project>/README.md`（`doc_type: project`）を横断して俯瞰する。

---

## アクティブプロジェクト一覧

```dataview
TABLE
  phase as "Phase",
  priority as "Priority",
  status as "Status",
  as_of as "Updated"
FROM "10_projects"
WHERE doc_type = "project" AND status != "completed" AND status != "cancelled"
SORT priority DESC, as_of DESC
```

---

## 直近の意思決定（全プロジェクト横断）

```dataview
TABLE
  project as "Project",
  status as "Status",
  one_line_thesis as "Thesis",
  as_of as "Date"
FROM "10_projects"
WHERE doc_type = "decision"
SORT as_of DESC
LIMIT 20
```

---

## オープンタスク（priority 順）

```dataview
TABLE
  project as "Project",
  priority as "Priority",
  due_date as "Due",
  one_line_thesis as "Thesis"
FROM "10_projects"
WHERE doc_type = "task" AND (status = "proposed" OR status = "in_progress" OR status = "blocked")
SORT priority DESC, due_date ASC
```
