---
name: kb-intake
description: >
  ナレッジベースへのあらゆる「取り込み」を一元処理する統合インテークスキル。
  md ファイル・テキスト・ディレクトリ・議事録・日報を渡すだけで、
  種別自動分類・格納先決定・確認・実行・Changelog更新・relations設定を自動実行する。
  Use when: 「ナレッジベースに入れて」「DBに格納して」「これを保存して」「このリサーチを〜」
  「このアイデアを〜」「この記事を〜」「議事録を取り込んで」「日報をメモして」
  「このフォルダを取り込んで」「この考えをメモして」
  など、何らかのコンテンツを知識ベースに格納したいときはすべてこのスキルを使う。
---

# kb-intake スキル — 統合インテーク

## いつ使うか

**あらゆる「取り込み」操作に使う。ユーザーはスキルを選ばなくてよい。**

| ユーザーの入力 | このスキルが対応 |
|---|---|
| 「このリサーチをナレッジベースに入れて」| 外部リサーチとして自動分類・格納 |
| 「この考えを保存して」| 個人思考として sandbox raw 層に自動格納 |
| 「このアイデアをメモして」| `80_sandbox/inbox/<YYYY-MM-DD>_<slug>.md` を新規作成 |
| 「このフォルダを取り込んで」| ディレクトリ一括処理 |
| 「議事録を取り込んで」| `10_projects/<project>/meetings/<YYYY-MM-DD>_<slug>.md` として格納 |
| 「日報をメモして」| `daily-log` スキルに委譲 |
| 「規格情報を整理して入れて」| `30_standards/<body>/<slug>.md` を作成 |
| 「サプライヤー情報を保存して」| `40_suppliers/<slug>.md` を作成 |

## 前提条件

- `AGENTS.md` を読み済みであること
- `knowledge/00_index/schema_reference.md` のスキーマを理解していること
- `knowledge/00_index/research_map.md` を読んで既存ドキュメント構成を把握していること

---

## Step 0: コンテキスト収集

入力の形式を確認する:
- **単一 md ファイル**: パスが指定されているか、貼り付けられたテキスト
- **ディレクトリ**: 複数ファイルが含まれるパス
- **インラインテキスト**: ファイルなし、チャットで直接入力されたテキスト
- **混合**: ファイル + 追加指示

`10_projects/` を ls してアクティブプロジェクトの slug 一覧を把握する。

---

## Step 1: 自動分類（Classification）

### 1a. 入力形式の判定

```
入力はディレクトリか？
  → YES: ディレクトリ一括処理（複数ファイルを1件ずつ判定して格納）
  → NO: 単一コンテンツとして以下を続ける
```

### 1b. コンテンツ種別の判定

| シグナル | 判定 |
|---------|------|
| 「会議メモ」「ミーティング」「議事録」が冒頭にある | **議事録** |
| 「日報」「daily」「今日のタスク」「明日の予定」 | **日報** |
| 「決定事項」「DEC-」 | **意思決定** |
| 「タスク」「TASK-」「TODO」 | **タスク** |
| 著者本人が「考え」「アイデア」「仮説」「メモ」と言っている | **個人着想** |
| 外部の記事・論文・レポート・調査の内容 | **外部リサーチ** |
| 規格番号 (ISO/IEC/JIS) で始まる | **規格情報** |
| サプライヤー名・部品メーカー名で始まる | **サプライヤー情報** |
| 試験結果・FEA 結果 | **試験レポート** |
| 設計検討・トレードオフ分析 | **設計メモ** |
| L0/L1/L2 構造が既にある | **個人着想（draft）または外部リサーチ** |

### 1c. プロジェクト・格納先の判定

**プロジェクト判定**:
- AGENTS.md のアクティブプロジェクト一覧と入力内のキーワードを照合
- 該当プロジェクトが特定できない場合は確認ゲートで聞く
- 部品/規格/サプライヤーなど横断知見は `project: [all]`

**格納先の決定**:

```
議事録
  → 10_projects/<project>/meetings/<YYYY-MM-DD>_<slug>.md
  ※ 格納後「compile-meeting で意思決定・タスクを抽出しますか？」と提案

日報
  → daily-log スキルに委譲（このスキルでは処理しない）

意思決定（単独）
  → 10_projects/<project>/decisions/DEC-NNNN_<slug>.md
  ※ ID 採番: 既存ファイルから最大番号 +1

タスク（単独）
  → 10_projects/<project>/tasks/TASK-NNNN_<slug>.md

設計メモ
  → 10_projects/<project>/design-notes/<slug>.md

試験レポート
  → 10_projects/<project>/test-reports/<slug>.md

部品横断知見
  → 20_components/<category>/<slug>.md
  ※ <category>: connectors|housings|brackets|thermal|vibration-damping|sealing|fasteners

規格情報
  → 30_standards/<body>/<slug>.md
  ※ <body>: iso|iec|jis|internal

サプライヤー情報
  → 40_suppliers/<slug>.md

技術リサーチ要約
  → 50_research/<slug>.md
  ※ 必要に応じて 90_sources/raw/ にも生データを保存

個人着想（断片的、未分類）
  → 80_sandbox/inbox/<YYYY-MM-DD>_<slug>.md

個人着想（topic 軸で分類できる）
  → 80_sandbox/{ideas,research,discussions}/<YYYY-MM-DD>_<slug>.md

個人着想（L0/L1/L2 構造化済み）
  → 80_sandbox/drafts/<YYYY-MM-DD>_<slug>-draft.md

外部ソース（生データ・長文記事）
  → 90_sources/raw/<topic>_<YYYYMMDD>.md
```

### 1d. 多トピック検出

1 つの文書に複数の独立したトピックが含まれている場合、各トピックを列挙して「分解して格納しますか？」と確認する。

---

## Step 2: 確認ゲート

分類サマリーをユーザーに提示する。**必ず確認を取ってから実行する。**

```
以下の分類で格納します:

種別: [議事録 / 設計メモ / 試験レポート / 部品横断知見 / 規格情報 / ...]
プロジェクト: [<project-slug> / all]
格納先: knowledge/[パス]/<ファイル名>.md
doc_type: <doc_type>
関連候補: [grep で実在確認した doc_id]

この分類で進めますか？修正があれば指示してください。
```

ops 系（task / decision / project）として分類された場合は、`_shared/ops-confirmation-gate.md` に基づく**最終フロントマタープレビュー**を経てから書き込む。

---

## Step 3: 実行

確認後、コンテンツ種別に応じたロジックで実行する。

### 議事録

ファイルを作成: `10_projects/<project>/meetings/<YYYY-MM-DD>_<slug>.md`

フロントマター:
```yaml
---
doc_id: ops.meeting.<YYYY-MM-DD>-<slug>
title: [会議のタイトル]
doc_type: meeting
project: [<project>]
layer: raw
role_in_story: context
status: completed
meeting_type: internal | partner | supplier | review
as_of: <今日の日付>
audience: [self]
attendees: [テキストから読み取れる参加者]
one_line_thesis: [会議の目的・主要議題を1文で]
confidence: medium
---
```

格納後:
> この議事録を compile-meeting スキルで処理して、意思決定・タスク・未解決の問いを抽出しますか？

### 設計メモ・試験レポート・部品横断知見・規格情報・サプライヤー

L0/L1/L2 構造で作成。必須フィールド + 車載固有フィールド（`component_category`, `standard_ref`, `design_phase`）を埋める。

### 個人着想

種別に応じて:
- 未分類 → `80_sandbox/inbox/<YYYY-MM-DD>_<slug>.md`
- topic 分類済 → `80_sandbox/{ideas,research,discussions}/<YYYY-MM-DD>_<slug>.md`
- 構造化済 → `80_sandbox/drafts/<YYYY-MM-DD>_<slug>-draft.md`

フロントマターは sandbox 用の最小セット:
```yaml
---
doc_id: sandbox.<YYYY-MM-DD>-<slug>
title: [タイトル]
doc_type: idea
project: [<project> or all]
layer: raw
role_in_story: context
status: draft
as_of: <今日の日付>
audience: [self]
one_line_thesis: [1文要約]
confidence: speculative
thinking_status: spark | developing | ready_to_propose
---
```

---

## Step 4: 後処理（自動実行、確認不要）

### CHANGELOG.md への追記

`knowledge/00_index/CHANGELOG.md` の最新日付セクションに追記:
```
### Added
- `[ファイルパス]`: [one_line_thesis]
```

### research_map.md への追記

格納先に応じたセクションに新規エントリを追記。

### relations の双方向設定

> ⚠️ relations に doc_id を書く前に必ず実行
> ```bash
> grep -r "^doc_id:" knowledge/ | grep "<キーワード>"
> # → 1件ヒットしたものだけを relations に書く。推測で書かない。
> ```

### Git の提案

```
以下の内容でコミットしますか？
ブランチ: <type>/<slug>（個人運用なら main 直でも可）
コミットメッセージ: <type>: [内容の要約]
```

---

## 品質チェック

- [ ] `doc_id` がリポジトリ全体でユニークか（grep で確認）
- [ ] プロジェクト判定が正しいか
- [ ] sandbox 層は `thinking_status` が設定されているか
- [ ] canonical（設計メモ・試験レポート等）は L0/L1/L2 構造になっているか
- [ ] relations の doc_id が実在するか
- [ ] CHANGELOG.md に追記されているか

---

## 使わないケース

- **壁打ち・思考整理がしたい** → `kb-output`
- **日報を構造化したい** → `daily-log`
- **議事録から decision/task を抽出したい** → `compile-meeting`
- **要件を grill したい** → `requirements-grill`
