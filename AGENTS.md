# AGENTS.md — 車載電子機器機構設計 個人ナレッジベース

このファイルはAIエージェント（Claude Code / GitHub Copilot）への永続的な指示書である。
本リポジトリで作業するすべてのエージェントはこの指示に従うこと。

---

## 1. プロジェクト概要

**目的**: 車載電子機器の機構設計に関わる個人ナレッジベース。議事録・日報・リサーチ・設計検討メモを構造化して蓄積し、AIエージェントが思考・要約・接続のパートナーとして機能する基盤を提供する。

**言語**: 日本語メイン。技術用語・規格名・部品名・サプライヤー名は英語可。

**運用前提**: Obsidian Vault として開く + Git で履歴管理。完全個人運用（チーム共有・PR フローなし）。

### アクティブプロジェクト

> 新規プロジェクトを起こすときは `knowledge/10_projects/_template/` をコピーして `10_projects/<project-slug>/` に置き、ここに追記する。

| Slug | プロジェクト名 | 概要 | フェーズ |
|---|---|---|---|
| _(未登録)_ | _(初回プロジェクト)_ | _(概要)_ | _(planning / design / development / testing / launch / maintenance)_ |

---

## 2. ナレッジベース構造

```
knowledge/
  00_index/            ナビゲーション・スキーマ仕様・用語集・MOC・CHANGELOG
  10_projects/         プロジェクト中心型の運用レイヤー
    _template/         新規プロジェクトのひな型（コピーして使う）
    <project>/
      README.md            プロジェクト定義 (doc_type: project)
      meetings/            会議メモ (raw 層、L0/L1/L2 免除)
      daily-logs/          日報メモ (raw 層、日次)
      design-notes/        設計検討メモ (canonical 候補)
      test-reports/        試験結果 (canonical)
      decisions/           意思決定 (canonical)
      tasks/               タスク (canonical)
      assets/              バイナリ (.docx/.pdf/.png/.html 等)
  20_components/       部品カテゴリ横断知見
    connectors/ housings/ brackets/ thermal/ vibration-damping/ sealing/ fasteners/
  30_standards/        規格・社内基準
    iso/ iec/ jis/ internal/
  40_suppliers/        サプライヤー情報
  50_research/         技術リサーチ要約 (canonical)
  80_sandbox/          個人 raw 層
    inbox/             未分類アイデア (1 アイデア = 1 ファイル)
    ideas/             着想・戦略メモ
    research/          外部リサーチ要約・記事
    discussions/       議論ログ
    drafts/            canonical 昇格候補 (L0/L1/L2 構造)
    assets/            派生物 (HTML / 画像 / SVG 等)
  90_sources/          外部 raw
    raw/               外部記事・論文・スクリーンショット等
    ideas/             共有レベルのアイデア
```

加えて、要件管理のためのサブ層が `10_projects/<project>/requirements/` 配下にある（`requirements-grill` スキルが書き出す）:

```
10_projects/<project>/requirements/
  vision.md             Vision 層（1 ファイル）
  outcomes.md           Outcome 層（1 ファイル）
  capabilities/
    CAP-NNN_<slug>.md   Capability ごと 1 ファイル
  features/
    FEAT-NNN_<slug>.md  Feature ごと 1 ファイル
  evals/
    <CAP|FEAT>-NNN_evals.md  受け入れ基準（EARS 記法）
  engineering/
    materials.md / interfaces.md / test_procedures.md 等
```

grill セッションファイル（状態保存）は `80_sandbox/grill-sessions/` に置く。

### 4 層構造の原則

- **raw**: 個人 sandbox + 外部ソース + 議事録・日報。エージェントは必要時のみ読む。
  - `80_sandbox/` — 個人 raw（inbox + 分類済みフォルダ群）
  - `90_sources/raw/` — 外部 raw
  - `10_projects/<project>/meetings/` + `daily-logs/` — 一次情報
- **canonical**: 要約階層付き構造化済み正本。エージェントが主に読む層。
  - `20_components/` `30_standards/` `40_suppliers/` `50_research/`
  - `10_projects/<project>/{design-notes,test-reports,decisions,tasks}/`
- **derived (pitch相当はこのプロジェクトでは廃止)**: 個人運用のため廃止。HTML 派生物のみ各 `assets/` 配下に格納。
- **operations**: `10_projects/<project>/` 直下の `meetings/decisions/tasks/` が operations 機能を担う（個人運用のため別ディレクトリは設けない）。

### sandbox 内の分類軸（トピック軸）

`80_sandbox/` の分類済みフォルダ群はトピック軸で切る:

| フォルダ | 役割 | 例 |
|---|---|---|
| `inbox/` | 未分類アイデア（1 アイデア = 1 ファイル） | `2026-05-28_thermal-hypothesis.md` |
| `ideas/` | 着想・戦略メモ・提案 | `2026-05-28_connector-redesign-proposal.md` |
| `research/` | 外部リサーチ要約・記事・評価レポート | `2026-05-28_isr16750-summary.md` |
| `discussions/` | 議論ログ・対話記録 | `2026-05-28_vibration-spec-discussion.md` |
| `drafts/` | canonical 昇格候補（L0/L1/L2 構造を持つ） | `2026-05-28_thermal-strategy-draft.md` |
| `assets/` | 派生物（HTML / 画像 / SVG 等） | `2026-05-28_thermal-map.html` |

### 4 段階昇格フロー（raw → canonical）

```
80_sandbox/inbox/<topic>.md（未分類アイデア）
  ↓ 人手: topic 判断
80_sandbox/{ideas,research,discussions}/<file>.md（raw 内分類）
  ↓ 人手: L0/L1/L2 を書く価値あり
80_sandbox/drafts/<YYYY-MM-DD>_<slug>-draft.md（canonical 昇格候補）
  ↓ 人手: 内容を確定
canonical 配置 (10_projects/<project>/design-notes/ など)
```

### 議事録・日報からタスク・意思決定へのコンパイル

```
10_projects/<project>/meetings/<YYYY-MM-DD>_<slug>.md（議事録）
  または
10_projects/<project>/daily-logs/<YYYY-MM-DD>.md（日報）
  ↓ compile-meeting スキル
10_projects/<project>/decisions/DEC-NNNN_<slug>.md
10_projects/<project>/tasks/TASK-NNNN_<slug>.md
```

`compile-meeting` は **議事録と日報の両方を入力** として受け付ける。日報の「明日の予定」セクションは tasks の供給源として優先的に拾う。

### 2.5 バイナリファイルポリシー

**対象拡張子**: `.docx`, `.xlsx`, `.pptx`, `.pdf`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.mp4`, `.zip`, `.step`, `.stp`, `.iges`, `.igs`, `.dxf`, `.dwg`, `.html`

#### 原則
- バイナリファイルは必ず **同階層の `assets/` サブディレクトリ**に配置する
- **リポジトリルート直下にバイナリを置かない**
- **日本語・スペースを含むファイル名は使用しない**（Git管理・検索性のため）

#### 配置ルール早見表

| 用途 | Markdown 配置先 | バイナリ配置先 |
|---|---|---|
| プロジェクト議事録 | `10_projects/<project>/meetings/*.md` | `10_projects/<project>/assets/` |
| 設計メモ・CAD図 | `10_projects/<project>/design-notes/*.md` | `10_projects/<project>/assets/` |
| 試験データ | `10_projects/<project>/test-reports/*.md` | `10_projects/<project>/assets/` |
| 部品カタログ・規格PDF | `20_components/<cat>/*.md`, `30_standards/<body>/*.md` | 各 `assets/` |
| sandbox 図解・派生物 | `80_sandbox/{ideas,research,discussions,drafts}/*.md` | `80_sandbox/assets/` |

#### 命名規則
- 英語ケバブケース必須
- `<context>_YYYYMMDD.<ext>` または `YYYY-MM-DD_<slug>.<ext>`

#### HTML 非同格ガード

`.html` ファイルは MD の派生物であり MD と同格ではない:
- 必ず `assets/` に配置
- `relations.*` 値に書かない
- `doc_type` / `status` / `owners` を HTML 自体に付与しない
- 検索 / インデックス対象外（research_map.md 等に書かない）
- 再参照シグナルは元 MD の `last_html_export: YYYY-MM-DD` フィールドのみで表現

---

## 3. フロントマタールール

すべての canonical ドキュメントには必須フィールドを含むYAMLフロントマターを付与すること。

### 必須フィールド

```yaml
doc_id: <プレフィックスは用途別。命名規則の詳細は knowledge/00_index/schema_reference.md を参照>
title: string
doc_type: index|project|meeting|daily-log|decision|task|design-note|test-report|component-note|standard-note|supplier-note|research|idea|source
project: [<project-slug>]   # 該当プロジェクトのスラッグ。横断知見の場合は [all]
layer: raw|canonical
role_in_story: routing|problem|insight|proposal|opportunity|execution|context
status: draft|review|canonical|archived
as_of: YYYY-MM-DD
audience: [self|engineer|partner|supplier|manager]
one_line_thesis: string
confidence: high|medium|low|speculative
```

### 推奨フィールド（canonical ドキュメントには必ず付与）

```yaml
tags: [関連タグ]
relations:
  depends_on: [doc_id, ...]
  supports: [doc_id, ...]
  related: [doc_id, ...]
key_questions: [string, ...]
source_docs: [filepath, ...]
```

### 車載機構設計ドメイン特有フィールド

```yaml
component_category: connectors|housings|brackets|thermal|vibration-damping|sealing|fasteners
standard_ref: [ISO-16750-3, IEC-60068-2-64, ...]   # 関連規格
design_phase: concept|detailed|validation|production
```

**完全仕様**: `knowledge/00_index/schema_reference.md` を参照。

---

## 4. canonical ドキュメントの必須本文構造

`layer: canonical` のドキュメントは以下の3層要約構造で本文を記述する:

```markdown
## L0（1文要約）
**[核心的主張を太字で1文]**

---

## L1（5つの要点）
- **[キー]**: [説明]
...（5項目）

---

## L2（詳細・根拠・構造）
[セクション分けした詳細内容]
```

エージェントはL0から読み始め、必要に応じてL1・L2へ深掘りすること。コンテキストウィンドウの節約が目的。

**L0/L1/L2 免除対象**: `doc_type: meeting | daily-log | index | project | decision | task` および sandbox の `inbox/ideas/research/discussions/` ノート。

---

## 5. Obsidian 運用ルール

このリポジトリは **Obsidian Vault** として開かれることを前提とする。

### Obsidian 機能の使い分け

| 機能 | 役割 | 使い方 |
|---|---|---|
| **doc_id + frontmatter** | 機械可読な正本ID。Dataview や CI 検証の主軸 | すべての canonical doc に必須 |
| **`[[wikilink]]`** | 人間が読み書きする本文中のリンク | 本文中の参照は wikilink を使う。frontmatter の `relations:` には doc_id を書く |
| **`#tag`** | 軽量な横断分類 | 補助。`tags:` フィールドと重複させない |
| **Templater** | テンプレートからの doc 生成 | `.obsidian/templates/` の各種テンプレートを使う |
| **Dataview** | MOC・進捗集計・タスク一覧 | `knowledge/00_index/moc_*.md` で活用 |

### wikilink と doc_id の使い分け

- **本文中の関連参照**: `[[2026-05-28 サーマル設計レビュー]]` のように人間が読みやすい wikilink
- **frontmatter の relations**: `relations.related: [ops.decision.thermal-strategy]` のように doc_id
- **CI が検証するのは doc_id 側**。wikilink は `tools/check_obsidian_links.py` が切れリンクのみ検査する

### 必須 Obsidian プラグイン

`.obsidian/community-plugins.json` で宣言済み:
- **Templater** (`templater-obsidian`) — テンプレートからの doc 生成
- **Dataview** (`dataview`) — MOC・進捗集計のクエリ

これらが未インストールだとテンプレートと MOC が機能しない。Obsidian で本 vault を開いた直後に Settings → Community plugins からインストールすること。

---

## 6. ツール実行前のセルフチェック（Pre-Flight Check）

新しいドキュメントを作成したり、ファイルへ書き込む前に、エージェントは以下を必ず確認すること：

- [ ] **リポジトリルートへの配置禁止**: `knowledge/`, `tools/`, `.cursor/`, `.claude/`, `.github/`, `.obsidian/` のいずれかの配下か（README.md等の例外は除く）
- [ ] **日本語・スペースの禁止**: ファイル名に日本語文字やスペースが含まれていないか（英語ケバブケースになっているか）
- [ ] **バイナリファイルの配置**: 拡張子が `.docx`, `.xlsx`, `.pptx`, `.pdf`, `.png`, `.step` 等のバイナリファイルは必ず同階層の `assets/` ディレクトリに配置されているか
- [ ] `doc_id` がユニークか（既存IDと重複していないか）
- [ ] フロントマターの必須フィールドがすべて埋まっているか
- [ ] `relations` で関連ドキュメントへの接続が設定されているか
- [ ] canonical の場合、L0/L1/L2 の3層構造になっているか
- [ ] `90_sources/` に対応するrawファイルがあれば `source_docs` に参照があるか

---

## 7. ドキュメント読み込み優先順位

エージェントが作業開始時に読む順序:

1. **このファイル** (AGENTS.md) — 現在読み中
2. `knowledge/00_index/research_map.md` — 全体マップ・ナビゲーション
3. 作業に関連するプロジェクトの `knowledge/10_projects/<project>/README.md`
4. 必要なら `knowledge/00_index/schema_reference.md` — スキーマ詳細

不要なファイルを全部読まないこと。`one_line_thesis` を使って必要なドキュメントだけに絞ること。

---

## 8. 利用可能なSkills

### メインスキル（ユーザーはこの2つだけ覚えればよい）

| Skill | 用途 | 呼び出し方 |
|---|---|---|
| `kb-intake` | **取り込み統合スキル**。md・テキスト・ディレクトリ・議事録・日報を渡すだけで自動分類・格納先決定・確認・実行を一括処理。 | 「ナレッジベースに入れて」「これを保存して」「日報をメモして」「議事録を取り込んで」 |
| `kb-output` | **アウトプット統合スキル**。KB参照・素材自動収集・目的判定を経て、壁打ち / 分析 / HTML 出力 / ドキュメント編集を実行。 | 「まとめて」「壁打ちしたい」「分析して」「HTML で出力して」 |

### 個別スキル（直接指定も可能）

| Skill | 用途 |
|---|---|
| `compile-meeting` | 議事録・日報から decision/task を抽出してファイル生成 |
| `daily-log` | 日報メモを `10_projects/<project>/daily-logs/YYYY-MM-DD.md` として構造化 |
| `obsidian-link` | doc_id ↔ `[[wikilink]]` の双方向変換、切れリンク検出、MOC 自動生成 |
| `knowledge-rally` | ナレッジを参照しながら壁打ち・理解深化ラリーを行う |
| `html-export` | Markdown を単一 HTML（外部リソース依存ゼロ）に変換 |
| `requirements-grill` | Vision / Outcome / Capability / Feature / Eval / EngSpec の 6 層を 1 問ずつ grill して `10_projects/<project>/requirements/` に書き出す |
| `meta-governance` | AGENTS.md / rules / hooks / skills / CI を変更するときに使う |
| `skill-factory` | 新規スキルを設計・追加 |
| `skill-improve-loop` | 既存スキルの誤爆・未発火・品質低下を直す改善ループ |
| `skill-regression-pack` | スキル改善時の回帰パックを作る |

### スキル管理方針

スキルの実体は **`.cursor/skills/<name>/`** に置き、`.claude/skills/<name>` はシンボリックリンクで参照する。

新スキル追加時の手順:
```bash
# 1. .cursor/skills/ に実体を作る
mkdir -p .cursor/skills/<name>
# SKILL.md を作成・編集

# 2. .claude/skills/ にシンボリックリンクを張る（相対パス必須）
cd .claude/skills
ln -s ../../.cursor/skills/<name>/ <name>      # macOS/Linux
# Windows の場合 setup.ps1 が自動で貼り直す

# 3. コミット
git add .claude/skills/<name>
git commit -m "meta: add skill <name>"
```

---

## 9. Python 仮想環境（conda）

`tools/` 配下の Python スクリプトは miniconda の専用環境で実行すること。

### 環境名: `vehkb-env`

```bash
# 初回のみ
conda create -n vehkb-env python=3.12 -y

# 有効化
conda activate vehkb-env

# 依存パッケージ
pip install -r tools/requirements.txt
```

エージェントへの指示:
- `tools/` 配下のスクリプトを実行する前に `conda activate vehkb-env` を行うこと
- 新しい Python パッケージを追加したら `tools/requirements.txt` を更新すること
- `base` 環境や他プロジェクトの環境を使用しないこと

---

## 10. 禁止事項

- `doc_id` の命名に日本語・スペースを使わない
- `status: canonical` のドキュメントを理由なく `archived` にしない
- バイナリファイルを `assets/` 以外に配置しない
- **HTML を MD と同格に扱わない**: HTML は MD の派生物として `assets/` にのみ配置し、`relations.*` への参照・`doc_type`/`status`/`owners` の付与・MOC への登録を行わない
- リポジトリルートに散らかったファイルを置かない（`debug.txt`、一時メモ等）
- canonical ドキュメントに L0/L1/L2 構造を欠いた状態で `status: canonical` を付けない

---

## 11. Git ワークフロー

完全個人運用のため、Git は履歴管理目的のみ。PR フローは強制しない。

### コミットメッセージ規則

```
<type>: <内容の要約>

type: project | research | idea | design | test | meta | fix | docs
```

例:
- `project: add ev-truck-2027 project skeleton`
- `design: thermal strategy for connector housing`
- `meta: update schema reference`

### 推奨ブランチ運用

個人運用ではブランチを切らず `main` 直で作業して問題ない。ただし以下は別ブランチを推奨:
- `meta/<slug>` — AGENTS.md / rules / hooks / skills を変更するとき
- `experiment/<slug>` — 実験的に大きな構造変更を試すとき

---

## 12. ops 系ドキュメントのガードレール

**適用対象**: `doc_type: task / decision / project / meeting / daily-log` のファイルを作成・編集する操作

これらを扱う際、エージェントは以下を厳守:

- **本文を勝手に書き足すことは禁止**: 「なぜ今やるのか」「背景」「アクション」等のセクションを自己判断で生成してはならない
- **許可される本文**: ユーザーが明示的に提供した情報（URL・リスト・説明文など）のみ転記可。基本はフロントマター＋URLのみのスタブ形式で有効なドキュメントとして扱う
- **フロントマター値の創作は禁止**: ユーザーが提供したプランや指示から直接読み取れる値のみ使用
- **確認ゲート義務**: ファイル作成・編集の直前に最終フロントマターのプレビューを提示し、ユーザー承認を得る

詳細は `.cursor/skills/_shared/ops-confirmation-gate.md` を参照。
