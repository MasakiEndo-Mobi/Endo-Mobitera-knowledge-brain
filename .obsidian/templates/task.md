<%*
const date = tp.date.now("YYYY-MM-DD");
const project = await tp.system.prompt("Project slug (e.g. ev-truck-2027)");
const slug = await tp.system.prompt("Task slug (kebab-case)");
const title = await tp.system.prompt("Task title");
const priority = await tp.system.suggester(
  ["high", "medium", "low"],
  ["high", "medium", "low"]
);
const dueDate = await tp.system.prompt("Due date (YYYY-MM-DD or empty)");
const fs = require('fs');
const path = `knowledge/10_projects/${project}/tasks`;
let next = 1;
try {
  const files = fs.readdirSync(path);
  const nums = files.map(f => parseInt((f.match(/^TASK-(\d{4})_/) || [])[1])).filter(n => !isNaN(n));
  if (nums.length) next = Math.max(...nums) + 1;
} catch (e) {}
const num = String(next).padStart(4, '0');
await tp.file.move(`/knowledge/10_projects/${project}/tasks/TASK-${num}_${slug}`);
-%>
---
doc_id: ops.task.<% project %>.<% slug %>
title: <% title %>
doc_type: task
project: [<% project %>]
layer: canonical
role_in_story: execution
status: proposed
priority: <% priority %>
as_of: <% date %>
audience: [self]
owners: [self]
one_line_thesis: <% title %>
confidence: medium
<% dueDate ? `due_date: ${dueDate}` : "" %>
project_ref: ops.project.<% project %>
---

# <% title %>

## 内容

## 完了条件

-
