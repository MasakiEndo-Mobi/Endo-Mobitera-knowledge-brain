---
doc_id: index.moc-components
title: Components MOC
doc_type: index
project: [all]
layer: canonical
role_in_story: routing
status: canonical
as_of: 2026-05-28
audience: [self, engineer]
one_line_thesis: 部品カテゴリ横断の canonical 知見を component_category 軸で俯瞰する Dataview ビュー。
confidence: high
---

# Components MOC

`20_components/<category>/` 配下の canonical 知見を一覧する。

---

## カテゴリ別ドキュメント

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "Document",
  component_category as "Category",
  one_line_thesis as "Thesis",
  as_of as "Updated"
FROM "20_components"
WHERE doc_type = "component-note"
SORT component_category ASC, as_of DESC
```

---

## 関連規格別

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "Document",
  standard_ref as "Standards",
  one_line_thesis as "Thesis"
FROM "20_components" OR "30_standards" OR "10_projects"
WHERE standard_ref
SORT as_of DESC
LIMIT 30
```
