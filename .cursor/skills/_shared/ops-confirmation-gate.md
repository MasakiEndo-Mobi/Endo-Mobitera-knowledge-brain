# ops-confirmation-gate 共通仕様

## 目的

`knowledge/10_projects/<project>/{decisions,tasks,projects}/` を作成・編集するとき、
Write 実行前に必ず同じ確認ゲートを通すための共通仕様。

責務は以下の 4 つ:

1. 最終フロントマターを全文プレビューする
2. 各値の出所を `[U]` / `[I: ...]` / `[A]` / `[X]` で明示する
3. 必須欠落・推測フィラー・禁止フィールドをその場で警告する
4. ユーザー承認前に Write しない

---

## 適用範囲

- `.cursor/skills/compile-meeting/SKILL.md`
- `.cursor/skills/kb-intake/SKILL.md`
- `.cursor/skills/daily-log/SKILL.md`
- 今後追加される ops 作成系スキル

対象 doc_type: `task` / `decision` / `project`

---

## source ラベル規約

| ラベル | 意味 |
|---|---|
| `[U]` | ユーザーが明示的に与えた値 |
| `[I: <根拠>]` | 議事録・日報・文脈から抽出・推測した値 |
| `[A]` | 規定値・今日の日付・自動採番などの自動値 |
| `[X]` | 手動入力すべきでない / 未決 |

運用規則:

- `[I: ...]` を含む値は、**ユーザーが承認するまで確定してはならない**
- `[A]` はそのまま確定してよいが、プレビューには必ず表示する

---

## doc_type 別フィールド規格

`knowledge/00_index/schema_reference.md` を優先ソースとする。

### task

| フィールド | 区分 | 備考 |
|---|---|---|
| `doc_id` | 必須 | `ops.task.<project>.<slug>` |
| `title` | 必須 | ユーザー提供が原則 |
| `doc_type` | 自動 | `task` |
| `project` | 必須 | 配列 |
| `layer` | 自動 | `canonical` |
| `role_in_story` | 自動 | `execution` |
| `status` | 自動 | 初期値 `proposed` |
| `as_of` | 自動 | 当日 |
| `audience` | 推奨 | 通常 `[self]` |
| `owners` | 必須 | 空配列不可（個人運用なら `[self]`） |
| `one_line_thesis` | 必須 | `title` の丸写し不可 |
| `confidence` | 自動 | 原則 `medium` |
| `priority` | 必須 | `high\|medium\|low` |
| `decision_ref` | 任意 | 既存 `ops.decision.*` |
| `source_meeting` | 任意 | 既存 `ops.meeting.*` |
| `due_date` | 任意 | `YYYY-MM-DD` |
| `project_ref` | 必須 | 既存 `ops.project.*` |
| `phase` | 任意 | `discovery\|design\|development\|testing\|launch\|maintenance` |

### decision

| フィールド | 区分 | 備考 |
|---|---|---|
| `doc_id` | 必須 | `ops.decision.<project>.<slug>` |
| `title` | 必須 | ユーザー提供が原則 |
| `doc_type` | 自動 | `decision` |
| `project` | 必須 | 配列 |
| `layer` | 自動 | `canonical` |
| `role_in_story` | 自動 | `execution` |
| `status` | 自動 | 初期値 `proposed` |
| `as_of` | 自動 | 当日 |
| `audience` | 推奨 | 通常 `[self]` |
| `owners` | 必須 | 空配列不可 |
| `one_line_thesis` | 必須 | `title` の丸写し不可 |
| `confidence` | 自動 | 原則 `medium` |
| `impact_areas` | 推奨 | 空なら明示確認 |
| `source_meeting` | 任意 | 既存 `ops.meeting.*` |
| `review_by` | 任意 | `YYYY-MM-DD` |

### project

| フィールド | 区分 | 備考 |
|---|---|---|
| `doc_id` | 必須 | `ops.project.<slug>` |
| `title` | 必須 | ユーザー提供が原則 |
| `doc_type` | 自動 | `project` |
| `project` | 必須 | 配列（slug を要素として含む） |
| `layer` | 自動 | `canonical` |
| `role_in_story` | 自動 | `execution` |
| `status` | 自動 | 初期値 `planning` |
| `phase` | 必須 | `discovery\|design\|development\|testing\|launch\|maintenance` |
| `priority` | 必須 | `high\|medium\|low` |
| `as_of` | 自動 | 当日 |
| `owners` | 必須 | 空配列不可 |
| `one_line_thesis` | 必須 | `title` の丸写し不可 |
| `milestones` | 任意 | 初期値 `[]` 可 |

---

## 最終プレビューの必須要件

Write 実行直前のプレビューは必ず以下を満たす:

1. 生成 / 更新対象のファイルパスを先頭に出す
2. **フロントマター全項目**を省略せずに出す
3. 各値の末尾に source ラベルを付ける
4. 本文が空なら「空」と明示する
5. 自動チェック欄を付ける
6. `y / n / q` の修正ループを案内する

### プレビュー雛形

```text
=== ops 確認ゲート: <doc_type> 最終プレビュー ===
ファイル: knowledge/10_projects/<project>/<dir>/<file>.md

--- フロントマター ---
doc_id:              <value>                           [A]
title:               <value>                           [U]
doc_type:            <value>                           [A]
project:             [<value>]                         [U or I: ...]
layer:               canonical                         [A]
role_in_story:       execution                         [A]
status:              <value>                           [A]
as_of:               <YYYY-MM-DD>                      [A]
audience:            [<value>]                         [U or I: ... or A]
owners:              [<value>]                         [U]
one_line_thesis:     <value>                           [U or I: ...]
confidence:          <value>                           [A or U]
... doc_type 固有フィールド ...

--- 本文 ---
（空）
または
<ユーザー提供本文 / URL のみ>

--- 自動チェック ---
[OK] doc_id 重複なし
[OK] 必須フィールド充足
[WARN] <推測値 / 禁止値 / 欠落候補>

このまま書き込みますか？
  y) はい
  n) 修正する
  q) キャンセル
```

---

## 自動チェック観点

### 共通
- `doc_id` が一意（リポジトリ全体で grep 済み）
- `title` が空でない
- `project` の要素が `10_projects/` 配下に存在するか or `all`
- `owners` が空配列でない
- `one_line_thesis` が空でない、`title` の丸写しでない

### task
- `priority` が存在
- `project_ref` が実在の `ops.project.*` を指す
- `decision_ref` があれば実在確認済み

### decision
- `impact_areas` が空なら要確認
- `related_tasks` があれば実在確認済み

### project
- `phase` が存在
- `priority` が存在
- `milestones` の各 `target_date` が日付形式

---

## 修正ループ

1. プレビュー提示
2. ユーザー応答
3. `n)` の場合は修正内容を反映して再プレビュー
4. `q)` の場合は中止
5. `y)` の場合のみ Write 実行
