---
doc_id: ops.project.<project-slug>
title: <プロジェクト名>
doc_type: project
project: [<project-slug>]
layer: canonical
role_in_story: execution
status: planning
as_of: 2026-05-28
audience: [self]
owners: [self]
one_line_thesis: <このプロジェクトが何を達成しようとしているかを1文で>
confidence: medium
phase: discovery
priority: medium
milestones:
  - name: M0 - Kickoff
    target_date: 2026-06-01
    status: pending
---

# <プロジェクト名>

> **このファイルをコピーして使う:**
> ```
> Copy-Item -Recurse knowledge/10_projects/_template knowledge/10_projects/<your-slug>
> ```
> その後、フロントマターの `<project-slug>` をすべて置換し、`doc_id` と `project` を実際のスラッグに書き換える。

---

## プロジェクト概要

[1〜2 段落で背景・目的・スコープを記載]

---

## マイルストーン

| Milestone | Target Date | Status |
|---|---|---|
| M0 — Kickoff | 2026-06-01 | pending |

---

## ディレクトリ構成

```
<project-slug>/
├─ README.md           ← このファイル（プロジェクト定義）
├─ meetings/           ← 議事録（doc_type: meeting）
├─ daily-logs/         ← 日報（doc_type: daily-log）
├─ design-notes/       ← 設計検討メモ（doc_type: design-note, canonical）
├─ test-reports/       ← 試験結果（doc_type: test-report, canonical）
├─ decisions/          ← 意思決定（DEC-NNNN_<slug>.md）
├─ tasks/              ← タスク（TASK-NNNN_<slug>.md）
├─ requirements/       ← Vision/Outcome/Capability/Feature/Eval/EngSpec の 6 層（requirements-grill が書き出す）
│  ├─ vision.md
│  ├─ outcomes.md
│  ├─ capabilities/    CAP-NNN_<slug>.md
│  ├─ features/        FEAT-NNN_<slug>.md
│  ├─ evals/           <CAP|FEAT>-NNN_evals.md
│  └─ engineering/     materials.md / interfaces.md / test_procedures.md
└─ assets/             ← バイナリ（.docx / .pdf / .png / .step 等）
```

---

## 関連リンク

- [[index.research-map]] — KB 全体マップ
- [[index.moc-projects]] — プロジェクト横断 Dataview ビュー
