<%*
const date = tp.date.now("YYYY-MM-DD");
const slug = await tp.system.prompt("Research slug (kebab-case)");
const title = await tp.system.prompt("Research title");
await tp.file.move(`/knowledge/50_research/${slug}`);
-%>
---
doc_id: res.<% slug %>
title: <% title %>
doc_type: research
project: [all]
layer: canonical
role_in_story: insight
status: draft
as_of: <% date %>
audience: [self, engineer]
owners: [self]
one_line_thesis: <% title %>
confidence: medium
tags: []
source_docs: []
relations:
  depends_on: []
  supports: []
  related: []
key_questions: []
---

## L0（1文要約）

**[リサーチで明らかになった核心を1文]**

---

## L1（5つの要点）

- **[キー1]**: [説明]
- **[キー2]**: [説明]
- **[キー3]**: [説明]
- **[キー4]**: [説明]
- **[キー5]**: [説明]

---

## L2（詳細・根拠・構造）

### 調査目的

### 主要発見

### ソース別整理

### 残課題と次のアクション
