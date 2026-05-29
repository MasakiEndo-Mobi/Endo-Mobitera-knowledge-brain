<%*
const date = tp.date.now("YYYY-MM-DD");
const project = await tp.system.prompt("Project slug (e.g. ev-truck-2027)");
const slug = await tp.system.prompt("Meeting slug (e.g. thermal-review)");
const title = await tp.system.prompt("Meeting title (Japanese OK)");
const meetingType = await tp.system.suggester(
  ["internal", "partner", "supplier", "review"],
  ["internal", "partner", "supplier", "review"]
);
const attendees = await tp.system.prompt("Attendees (comma separated)");
await tp.file.move(`/knowledge/10_projects/${project}/meetings/${date}_${slug}`);
-%>
---
doc_id: ops.meeting.<% date %>-<% slug %>
title: <% title %>
doc_type: meeting
project: [<% project %>]
layer: raw
role_in_story: context
status: completed
meeting_type: <% meetingType %>
as_of: <% date %>
audience: [self]
attendees: [<% attendees.split(",").map(s => s.trim()).join(", ") %>]
one_line_thesis: <% title %>
confidence: medium
---

# <% title %>

## 議題

-

## 議論内容

## 決定事項

-

## タスク

-

## 未解決の問い

-
