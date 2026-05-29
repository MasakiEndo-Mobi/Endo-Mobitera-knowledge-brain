<%*
const date = tp.date.now("YYYY-MM-DD");
const project = await tp.system.prompt("Project slug");
const slug = await tp.system.prompt("Test report slug (kebab-case)");
const title = await tp.system.prompt("Test report title");
const standardRef = await tp.system.prompt("Standard ref (e.g. ISO-16750-3, optional)");
await tp.file.move(`/knowledge/10_projects/${project}/test-reports/${slug}`);
-%>
---
doc_id: proj.<% project %>.test.<% slug %>
title: <% title %>
doc_type: test-report
project: [<% project %>]
layer: canonical
role_in_story: insight
status: draft
as_of: <% date %>
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: <% title %>
confidence: high
design_phase: validation
<% standardRef ? `standard_ref: [${standardRef}]` : "" %>
tags: [testing]
relations:
  depends_on: []
  supports: []
  related: []
---

## L0（1文要約）

**[試験結果と判定を1文で]**

---

## L1（5つの要点）

- **試験対象**: [DUT]
- **試験条件**: [温度範囲 / 振動条件 等]
- **結果**: [合格 / 不合格 / 数値]
- **マージン**: [規格に対する余裕度]
- **次アクション**: [再試験 / 設計変更 / リリース判定]

---

## L2（詳細・根拠・構造）

### 試験目的

### 試験条件詳細

### 結果データ

### 不合格時の原因分析

### 関連
