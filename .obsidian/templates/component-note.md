<%*
const date = tp.date.now("YYYY-MM-DD");
const category = await tp.system.suggester(
  ["connectors", "housings", "brackets", "thermal", "vibration-damping", "sealing", "fasteners"],
  ["connectors", "housings", "brackets", "thermal", "vibration-damping", "sealing", "fasteners"]
);
const slug = await tp.system.prompt("Component note slug (kebab-case)");
const title = await tp.system.prompt("Component note title");
await tp.file.move(`/knowledge/20_components/${category}/${slug}`);
-%>
---
doc_id: comp.<% category %>.<% slug %>
title: <% title %>
doc_type: component-note
project: [all]
layer: canonical
role_in_story: insight
status: draft
as_of: <% date %>
audience: [self, engineer]
owners: [self]
one_line_thesis: <% title %>
confidence: medium
component_category: <% category %>
tags: []
relations:
  depends_on: []
  supports: []
  related: []
---

## L0（1文要約）

**[この部品カテゴリの核心知見を1文]**

---

## L1（5つの要点）

- **代表的選定基準**: [説明]
- **主要規格**: [説明]
- **設計上の落とし穴**: [説明]
- **コスト傾向**: [説明]
- **サプライヤー候補**: [説明]

---

## L2（詳細・根拠・構造）

### 設計ガイドライン

### 規格対応

### 試験項目

### サプライヤー情報
