---
name: compile-meeting
description: >
  議事録および日報から decision / task / question を抽出し、
  10_projects/<project>/decisions/ と tasks/ に型付きオブジェクトファイルを生成する。
  Use when: 「会議メモをコンパイルして」「日報からタスク抽出」「議事録を整理して」
  「ミーティングから意思決定とタスクを抽出して」など。
---

# compile-meeting スキル

## いつ使うか

`10_projects/<project>/meetings/` または `daily-logs/` 配下の `.md` ファイルを元に、
decision / task / question の候補を抽出して canonical object ファイルを生成したいとき。

| 入力 | 対応 |
|---|---|
| 「この議事録をコンパイルして」+ ファイルパス | 指定ファイルを処理 |
| 「日報からタスク抽出」+ ファイルパス | daily-log を処理（「明日の予定」を優先的に拾う） |
| 「議事録からタスクを抽出して」+ テキスト | meetings/ に新規保存してから処理 |
| 「最新の議事録を整理して」（ファイル未指定） | meetings/ の最新ファイルを自動選択 |

---

## Step 0: 入力の確定

```
ユーザーがパスを指定した → そのファイルを読む
ユーザーがテキストを貼り付けた → meetings/ または daily-logs/ に新規保存してから処理
ファイル未指定 → meetings/ と daily-logs/ を ls して最新ファイルを提示
```

---

## Step 1: 議事録/日報の読み込みと候補抽出

会議メモ・日報を読み込み、以下の Standard JSON Schema に沿って候補を抽出する。

### 1.1 抽出スキーマ

```json
{
  "decisions": [
    {
      "title":          "意思決定の見出し（30字以内推奨）",
      "summary":        "1〜2文での意思決定内容",
      "status":         "proposed | decided | superseded | archived",
      "source_meeting": "ops.meeting.<slug> | ops.daily.<project>.<date>",
      "responsible":    "<member-slug> | null"
    }
  ],
  "tasks": [
    {
      "title":          "タスクの見出し",
      "summary":        "1〜2文での作業内容",
      "status":         "proposed | in_progress | blocked | done | cancelled",
      "source_meeting": "ops.meeting.<slug> | ops.daily.<project>.<date>",
      "responsible":    "<member-slug> | null",
      "due_date":       "YYYY-MM-DD | null",
      "project_ref":    "ops.project.<slug>"
    }
  ],
  "questions": [
    {
      "title":          "未解決事項の見出し",
      "summary":        "1〜2文での問題提示",
      "source_meeting": "ops.meeting.<slug> | ops.daily.<project>.<date>"
    }
  ]
}
```

### 1.2 抽出シグナル

| カテゴリ | シグナル語句・パターン |
|---|---|
| **decision** | 「〜と決めた」「〜で行く」「方針は〜」「採用する」「却下する」「決定」「DEC-」 |
| **task** | 「〜する」「〜を確認する」「TODO」「担当:」「@名前」「次回までに」「TASK-」 |
| **question** | 「要確認」「不明」「検討が必要」「課題として残る」 |

**日報の場合の追加ルール**:
- 「明日の予定」セクションの箇条書きは **task 候補として優先抽出**
- 「課題・気づき」セクションは question 候補として抽出
- 「進捗」セクションは既存 task の status 更新候補として扱う

### 1.3 失敗時の縮退

| 失敗 | 対応 |
|---|---|
| structured output が JSON 解釈不能 | 1.2 のシグナルベース抽出に切替 |
| 必須フィールド欠落（title / summary / source_meeting） | 該当候補をスキップして人間に通知 |
| optional フィールド欠落 | `null` で許容、Step 2 の確認ゲートで補正 |

---

## Step 1.5: プロジェクト確認

入力ファイルのパスから自動的にプロジェクト slug を抽出:
```
knowledge/10_projects/<project>/meetings/...
                     ^^^^^^^^^
```

プロジェクトが特定できない場合は確認ゲートで聞く。

---

## Step 2: 抽出候補の確認ゲート

抽出結果をユーザーに提示し、承認を得る。**必ず確認を取ってから実行する。**

```
=== 抽出候補（プロジェクト: <project>）===

[Decisions]
1. <title> — <summary> (responsible: <slug>)
2. ...

[Tasks]
1. <title> — <summary> (due: <date>, responsible: <slug>)
2. ...

[Questions]
1. <title> — <summary>
2. ...

この内容で生成しますか？修正があれば指示してください。
```

---

## Step 3: ID 採番

```bash
# decisions/ の最大番号
ls knowledge/10_projects/<project>/decisions/ | grep -E '^DEC-[0-9]{4}' | sort | tail -1
# tasks/ の最大番号
ls knowledge/10_projects/<project>/tasks/ | grep -E '^TASK-[0-9]{4}' | sort | tail -1
```

---

## Step 3.5: 最終プレビュー

`../_shared/ops-confirmation-gate.md` の仕様で各 decision / task を 1 件ずつプレビュー。
`y / n / q` で確認する。**`y)` が返るまで Write しない。**

---

## Step 4: ファイル生成

### Decision ファイル: `10_projects/<project>/decisions/DEC-NNNN_<slug>.md`

```yaml
---
doc_id: ops.decision.<project>.<slug>
title: <Standard.title>
doc_type: decision
project: [<project>]
layer: canonical
role_in_story: execution
status: <Standard.status>
as_of: <今日の日付>
audience: [self]
owners: [<Standard.responsible> または [self]]
one_line_thesis: <Standard.summary>
confidence: medium
source_meeting: <Standard.source_meeting>
impact_areas: [<影響範囲>]
related_tasks: []
---
```

### Task ファイル: `10_projects/<project>/tasks/TASK-NNNN_<slug>.md`

```yaml
---
doc_id: ops.task.<project>.<slug>
title: <Standard.title>
doc_type: task
project: [<project>]
layer: canonical
role_in_story: execution
status: <Standard.status>
priority: <high|medium|low>
as_of: <今日の日付>
audience: [self]
owners: [<Standard.responsible> または [self]]
one_line_thesis: <Standard.summary>
confidence: medium
source_meeting: <Standard.source_meeting>
due_date: <Standard.due_date>
project_ref: <Standard.project_ref>
phase: <推定 or null>
---
```

### Question（生成しない）

Question は decision / task に比べて重要度が低く、議事録本文に inline 記録 + フロントマター `unresolved_questions: [...]` に集約することで対応する（独立ファイル化しない）。

---

## Step 5: 議事録/日報の更新

```yaml
status: compiled
extracted_decisions:
  - ops.decision.<project>.<slug>
extracted_tasks:
  - ops.task.<project>.<slug>
unresolved_questions:
  - title: <questions[i].title>
    summary: <questions[i].summary>
```

---

## Step 6: 後処理

- CHANGELOG.md に追記
- Git コミットを提案

---

## 品質チェック

- [ ] 各 decision / task の `doc_id` がリポジトリ全体でユニークか
- [ ] `project_ref` がプロジェクトと一致するか
- [ ] owner 不明なタスクは `owners: [self]` で明示
- [ ] 議事録/日報の status が `compiled` に更新されているか
- [ ] `unresolved_questions` が schema.questions と一致しているか
- [ ] CHANGELOG.md に追記されているか
