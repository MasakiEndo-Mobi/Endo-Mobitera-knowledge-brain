<%*
const date = tp.date.now("YYYY-MM-DD");
const slug = await tp.system.prompt("Project slug (kebab-case, e.g. ev-truck-2027)");
const title = await tp.system.prompt("Project title");
const phase = await tp.system.suggester(
  ["discovery", "design", "development", "testing", "launch", "maintenance"],
  ["discovery", "design", "development", "testing", "launch", "maintenance"]
);
const priority = await tp.system.suggester(
  ["high", "medium", "low"],
  ["high", "medium", "low"]
);
// Create the directory structure first
const fs = require('fs');
const baseDir = `knowledge/10_projects/${slug}`;
const subdirs = ["meetings", "daily-logs", "design-notes", "test-reports", "decisions", "tasks", "assets"];
for (const d of subdirs) {
  fs.mkdirSync(`${baseDir}/${d}`, { recursive: true });
}
await tp.file.move(`${baseDir}/README`);
-%>
---
doc_id: ops.project.<% slug %>
title: <% title %>
doc_type: project
project: [<% slug %>]
layer: canonical
role_in_story: execution
status: planning
phase: <% phase %>
priority: <% priority %>
as_of: <% date %>
audience: [self]
owners: [self]
one_line_thesis: <% title %>
confidence: medium
milestones:
  - name: M0 - Kickoff
    target_date: <% date %>
    status: pending
---

# <% title %>

## プロジェクト概要

## マイルストーン

| Milestone | Target Date | Status |
|---|---|---|
| M0 — Kickoff | <% date %> | pending |

## 関連

- [[index.research-map]]
- [[index.moc-projects]]
