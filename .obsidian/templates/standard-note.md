<%*
const date = tp.date.now("YYYY-MM-DD");
const body = await tp.system.suggester(
  ["iso", "iec", "jis", "internal"],
  ["iso", "iec", "jis", "internal"]
);
const slug = await tp.system.prompt("Standard slug (e.g. 16750-3)");
const title = await tp.system.prompt("Standard title");
await tp.file.move(`/knowledge/30_standards/${body}/${slug}`);
-%>
---
doc_id: std.<% body %>.<% slug %>
title: <% title %>
doc_type: standard-note
project: [all]
layer: canonical
role_in_story: context
status: draft
as_of: <% date %>
audience: [self, engineer]
owners: [self]
one_line_thesis: <% title %>
confidence: high
standard_ref: [<% body.toUpperCase() %>-<% slug %>]
tags: []
relations:
  depends_on: []
  supports: []
  related: []
---

## L0（1文要約）

**[規格の要旨を1文]**

---

## L1（5つの要点）

- **適用範囲**: [説明]
- **試験項目**: [説明]
- **判定基準**: [説明]
- **関連規格**: [説明]
- **社内運用上の注意**: [説明]

---

## L2（詳細・根拠・構造）

### 章構成サマリー

### 試験条件詳細

### 判定基準

### 過去の不合格事例
