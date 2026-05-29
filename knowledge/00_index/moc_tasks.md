---
doc_id: index.moc-tasks
title: Tasks MOC
doc_type: index
project: [all]
layer: canonical
role_in_story: routing
status: canonical
as_of: 2026-05-28
audience: [self]
one_line_thesis: 全プロジェクトのタスクをステータス・優先度・期限で横断的に俯瞰するハブ。
confidence: high
---

# Tasks MOC

---

## 期限切れ・期限間近（7日以内）

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "Task",
  project as "Project",
  priority as "Priority",
  due_date as "Due",
  status as "Status"
FROM "10_projects"
WHERE doc_type = "task" AND due_date AND status != "done" AND status != "cancelled"
  AND date(due_date) <= date(today) + dur(7 days)
SORT due_date ASC
```

---

## In Progress

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "Task",
  project as "Project",
  priority as "Priority",
  due_date as "Due"
FROM "10_projects"
WHERE doc_type = "task" AND status = "in_progress"
SORT priority DESC, due_date ASC
```

---

## Blocked

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "Task",
  project as "Project",
  one_line_thesis as "Why blocked"
FROM "10_projects"
WHERE doc_type = "task" AND status = "blocked"
```

---

## Proposed（未着手）

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "Task",
  project as "Project",
  priority as "Priority"
FROM "10_projects"
WHERE doc_type = "task" AND status = "proposed"
SORT priority DESC
```
