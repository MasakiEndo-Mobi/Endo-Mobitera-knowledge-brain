<%*
const date = tp.date.now("YYYY-MM-DD");
const project = await tp.system.prompt("Project slug (e.g. ev-truck-2027)");
const slug = await tp.system.prompt("Decision slug (kebab-case)");
const title = await tp.system.prompt("Decision title");
// Find next DEC-NNNN number
const fs = require('fs');
const path = `knowledge/10_projects/${project}/decisions`;
let next = 1;
try {
  const files = fs.readdirSync(path);
  const nums = files.map(f => parseInt((f.match(/^DEC-(\d{4})_/) || [])[1])).filter(n => !isNaN(n));
  if (nums.length) next = Math.max(...nums) + 1;
} catch (e) {}
const num = String(next).padStart(4, '0');
await tp.file.move(`/knowledge/10_projects/${project}/decisions/DEC-${num}_${slug}`);
-%>
---
doc_id: ops.decision.<% project %>.<% slug %>
title: <% title %>
doc_type: decision
project: [<% project %>]
layer: canonical
role_in_story: execution
status: proposed
as_of: <% date %>
audience: [self]
owners: [self]
one_line_thesis: <% title %>
confidence: medium
impact_areas: []
related_tasks: []
---

# <% title %>

## コンテキスト

## 決定内容

## 根拠

## 影響範囲

## 関連

-
