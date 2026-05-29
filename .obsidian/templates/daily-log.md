<%*
const date = tp.date.now("YYYY-MM-DD");
const project = await tp.system.prompt("Project slug (e.g. ev-truck-2027)");
await tp.file.move(`/knowledge/10_projects/${project}/daily-logs/${date}`);
-%>
---
doc_id: ops.daily.<% project %>.<% date %>
title: 日報 <% date %>
doc_type: daily-log
project: [<% project %>]
layer: raw
role_in_story: context
status: draft
as_of: <% date %>
audience: [self]
one_line_thesis: <% date %> の作業ログ
confidence: medium
---

# 日報 <% date %>

## 今日のタスク

-

## 進捗

-

## 課題・気づき

-

## 明日の予定

-

## 関連

-
