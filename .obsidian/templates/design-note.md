<%*
const date = tp.date.now("YYYY-MM-DD");
const project = await tp.system.prompt("Project slug");
const slug = await tp.system.prompt("Design note slug (kebab-case)");
const title = await tp.system.prompt("Design note title");
const componentCategory = await tp.system.suggester(
  ["connectors", "housings", "brackets", "thermal", "vibration-damping", "sealing", "fasteners", "(none)"],
  ["connectors", "housings", "brackets", "thermal", "vibration-damping", "sealing", "fasteners", ""]
);
const designPhase = await tp.system.suggester(
  ["concept", "detailed", "validation", "production"],
  ["concept", "detailed", "validation", "production"]
);
await tp.file.move(`/knowledge/10_projects/${project}/design-notes/${slug}`);
-%>
---
doc_id: proj.<% project %>.design.<% slug %>
title: <% title %>
doc_type: design-note
project: [<% project %>]
layer: canonical
role_in_story: proposal
status: draft
as_of: <% date %>
audience: [self, engineer]
owners: [self]
one_line_thesis: <% title %>
confidence: medium
<% componentCategory ? `component_category: ${componentCategory}` : "" %>
design_phase: <% designPhase %>
tags: []
relations:
  depends_on: []
  supports: []
  related: []
key_questions: []
---

## L0（1文要約）

**[ここに核心的主張を1文]**

---

## L1（5つの要点）

- **[キー1]**: [説明]
- **[キー2]**: [説明]
- **[キー3]**: [説明]
- **[キー4]**: [説明]
- **[キー5]**: [説明]

---

## L2（詳細・根拠・構造）

### 背景

### 設計案

### トレードオフ

### 関連試験・解析

### 残課題
