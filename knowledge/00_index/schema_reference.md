---
doc_id: index.schema-reference
title: フロントマタースキーマ仕様書
doc_type: index
project: [all]
layer: canonical
role_in_story: routing
status: canonical
as_of: 2026-05-28
audience: [self, engineer]
one_line_thesis: このナレッジベースのすべてのドキュメントが従うYAMLフロントマタースキーマの完全仕様。
confidence: high
---

# フロントマタースキーマ仕様書

このファイルは、`knowledge/` 配下のすべてのMarkdownドキュメントに付与するYAMLフロントマターの完全仕様を定義する。
AIエージェントはこのスキーマに従ってドキュメントを作成・更新し、ナレッジグラフの整合性を維持する。

---

## L0（1文要約）

**車載電子機器機構設計KBは「project + doc_type + layer + relations」の4軸でドキュメントを位置付け、エージェント可読な要約階層（L0/L1/L2）と組み合わせて検索効率と思考整理の両立を達成する。**

---

## L1（5つの要点）

- **必須フィールド**: `doc_id` / `title` / `doc_type` / `project` / `layer` / `role_in_story` / `status` / `as_of` / `audience` / `one_line_thesis` / `confidence`
- **doc_id 命名規則**: `<scope>.<project>.<type>.<slug>` ケバブケース、日本語不可
- **L0/L1/L2 構造**: `layer: canonical` 文書は必須。meeting/daily-log/project/decision/task/index は免除
- **車載固有フィールド**: `component_category` / `standard_ref` / `design_phase` を canonical doc で活用
- **HTML 非同格**: HTML 派生物には doc_id / status / relations を付与しない

---

## L2（詳細・根拠・構造）

### 完全スキーマ（コメント付き）

```yaml
# ── 必須フィールド ──────────────────────────────────────

doc_id: string
# 一意の階層ID。ドット区切りで階層を表現する。
# フォーマット: <scope>.<project>.<type>.<slug>
# 例:
#   proj.ev-truck-2027.design.thermal-strategy
#   comp.connector.usb-c-thermal
#   std.iso.16750-3
#   sandbox.thermal-hypothesis
#   ops.meeting.2026-05-28-weekly-sync
#   ops.decision.connector-supplier-selection
#   ops.task.fea-thermal-rerun
# ルール: スラッグはケバブケース、日本語不可

title: string
# ドキュメントの表示タイトル（日本語可）

doc_type: enum
# ドキュメントの種別
# 値: index | project | meeting | daily-log | decision | task |
#     design-note | test-report | component-note | standard-note |
#     supplier-note | research | idea | source | requirement | grill_session
#
# - index           : ナビゲーション・スキーマ・MOC・用語集
# - project         : プロジェクト定義（10_projects/<project>/README.md）
# - meeting         : 議事録（raw 層、L0/L1/L2 免除）
# - daily-log       : 日報（raw 層、L0/L1/L2 免除）
# - decision        : 意思決定レコード（canonical、L0/L1/L2 免除）
# - task            : タスクレコード（canonical、L0/L1/L2 免除）
# - design-note     : 設計検討メモ（canonical 候補、L0/L1/L2 必須）
# - test-report     : 試験結果レポート（canonical、L0/L1/L2 必須）
# - component-note  : 部品横断知見（20_components/、L0/L1/L2 必須）
# - standard-note   : 規格情報（30_standards/、L0/L1/L2 必須）
# - supplier-note   : サプライヤー情報（40_suppliers/、L0/L1/L2 必須）
# - research        : 技術リサーチ要約（50_research/、L0/L1/L2 必須）
# - idea            : 着想・未構造化メモ（sandbox や 90_sources/ideas）
# - source          : 外部ソース・生データ（90_sources/raw/、grill-sessions/）
# - requirement     : 要件ドキュメント（10_projects/<project>/requirements/ 配下）
# - grill_session   : requirements-grill のセッション状態（80_sandbox/grill-sessions/、source として扱う）

project: list[enum]
# このドキュメントが属するプロジェクト（複数可）
# 値: AGENTS.md のアクティブプロジェクト一覧を参照
# - <project-slug>  : 特定プロジェクト（10_projects/<slug>/ に対応）
# - all             : 全プロジェクト共通・横断（20_components/ や 30_standards/ 等）

layer: enum
# ドキュメントの情報層
# 値: raw | canonical
# - raw      : 一次情報・未整理（80_sandbox/, 90_sources/, meetings/, daily-logs/）
# - canonical: 要約階層付き・構造化済み正本（その他すべて）

role_in_story: enum
# このドキュメントが担う論理的役割
# 値: routing | problem | insight | proposal | opportunity | execution | context
# - routing    : 目次・マップ・ナビゲーション
# - problem    : 課題・現状の問い
# - insight    : 洞察・構造的理解
# - proposal   : 解決策・設計・仕様
# - opportunity: 設計機会・改善余地
# - execution  : 実行計画・タスク・決定
# - context    : 背景・補足情報

status: enum
# ドキュメントの成熟度
# 値: draft | review | canonical | archived
# - draft    : 作業中・未検証
# - review   : レビュー待ち
# - canonical: 正本・信頼できる状態
# - archived : 古くなった・参照のみ
#
# ⚠️ 一部 doc_type は専用の status 値を使用する：
# - meeting   : scheduled | in_progress | completed | compiled
# - daily-log : draft | compiled
# - decision  : proposed | decided | superseded | archived
# - task      : proposed | in_progress | blocked | done | cancelled
# - project   : planning | active | on_hold | completed | cancelled

as_of: date
# ドキュメントの最終更新日 (YYYY-MM-DD形式)

audience: list[enum]
# 想定読者（複数可）
# 値: self | engineer | partner | supplier | manager
# - self     : 自分用メモ
# - engineer : 同僚エンジニア・後任者
# - partner  : パートナー企業との共有想定
# - supplier : サプライヤーとの共有想定
# - manager  : 上長・マネジメント層への報告想定

one_line_thesis: string
# このドキュメントの主張・要旨を1文で表現（日本語推奨）
# AIエージェントがコンテキストウィンドウを節約するための最重要フィールド

confidence: enum
# この文書内の主張の確信度
# 値: high | medium | low | speculative
# - high      : 試験データや規格で裏付けあり
# - medium    : 1ソースまたは推論ベース
# - low       : 仮説段階
# - speculative: 着想段階

# ── 推奨フィールド ──────────────────────────────────────

tags: list[string]
# 横断テーマタグ（複数可）
# 推奨値: thermal | vibration | emc | sealing | manufacturing |
#         cost-reduction | reliability | safety | testing | fea

relations:
  depends_on: list[doc_id]
  # このドキュメントを理解するために前提となるドキュメントのdoc_id
  supports: list[doc_id]
  # このドキュメントが根拠・補強として支持するdoc_idリスト
  contradicts: list[doc_id]
  # 矛盾・対立する見解を持つドキュメントのdoc_id
  related: list[doc_id]
  # 関連するが依存・支持関係ではないdoc_id

key_questions: list[string]
# このドキュメントが答えようとしている問い（3〜5個推奨）

source_docs: list[filepath]
# 根拠となるrawファイルへの相対パス

# ── 車載機構設計ドメイン固有フィールド ──────────────────

component_category: enum
# 値: connectors | housings | brackets | thermal | vibration-damping | sealing | fasteners
# 20_components/ 配下、または該当部品に紐づく design-note で使用

standard_ref: list[string]
# 関連規格の識別子
# 例: ['ISO-16750-3', 'IEC-60068-2-64', 'JIS-D-1601']
# 30_standards/ 配下のドキュメントは自身の規格番号を含める

design_phase: enum
# 設計フェーズ（design-note / test-report 等で使用）
# 値: concept | detailed | validation | production
# - concept   : 概念検討・初期スケッチ
# - detailed  : 詳細設計・CAD/FEA
# - validation: 試作・試験検証
# - production: 量産準備・量産後

# ── オプションフィールド ────────────────────────────────

next_docs: list[filepath]
# 次に読むべき推奨ドキュメントへの相対パス

summary_short: string
# 1〜2文の要約（エージェントがリスト表示用に使用）

summary_medium: string
# 3〜5文の要約（エージェントがコンテキスト節約用に使用）

last_html_export: date
# html-export スキルが自動付与。HTML 経由再参照シグナル

# ── sandbox 層専用フィールド ────────────────────────────

thinking_status: enum
# sandbox ドキュメントの成熟度
# 値: spark | developing | ready_to_propose | merged
# - spark            : 着想段階（inbox/）
# - developing       : topic 分類後の深掘り中（ideas/ / research/ / discussions/）
# - ready_to_propose : canonical 昇格候補（drafts/）
# - merged           : canonical 層にマージ済み
```

---

### doc_id 命名規則

#### フォーマット

```
<scope>.<project>.<type>.<slug>
```

| プレフィックス | 対応ディレクトリ | 例 |
|---|---|---|
| `index.*` | `00_index/` | `index.schema-reference` |
| `proj.<project>.*` | `10_projects/<project>/` | `proj.ev-truck-2027.design.thermal-strategy` |
| `comp.<category>.*` | `20_components/<category>/` | `comp.connector.usb-c-thermal` |
| `std.<body>.*` | `30_standards/<body>/` | `std.iso.16750-3` |
| `supp.<vendor>.*` | `40_suppliers/` | `supp.molex.connector-portfolio` |
| `res.<topic>.*` | `50_research/` | `res.thermal.heat-pipe-survey-2026` |
| `sandbox.*` | `80_sandbox/` | `sandbox.thermal-hypothesis-20260528` |
| `source.*` | `90_sources/raw/` | `source.iso-16750-3-overview-20260528` |
| `idea.*` | `90_sources/ideas/` | `idea.bracket-redesign-proposal` |
| `ops.meeting.*` | `10_projects/<project>/meetings/` | `ops.meeting.2026-05-28-weekly-sync` |
| `ops.daily.*` | `10_projects/<project>/daily-logs/` | `ops.daily.2026-05-28` |
| `ops.decision.*` | `10_projects/<project>/decisions/` | `ops.decision.connector-supplier-selection` |
| `ops.task.*` | `10_projects/<project>/tasks/` | `ops.task.fea-thermal-rerun` |
| `ops.project.*` | `10_projects/<project>/README.md` | `ops.project.ev-truck-2027` |

#### スラッグルール
- ケバブケース（`some-slug`）
- 日本語・スペース・特殊文字は使用不可
- 30文字以内を推奨

---

### L0/L1/L2 要約階層

`layer: canonical` のドキュメントは以下の3層構造で本文を記述する（免除 doc_type を除く）:

```markdown
## L0（1文要約）

**[太字で核心的主張を1文]**

---

## L1（5つの要点）

- **[キーワード]**: [説明]
- **[キーワード]**: [説明]
- **[キーワード]**: [説明]
- **[キーワード]**: [説明]
- **[キーワード]**: [説明]

---

## L2（詳細・根拠・構造）

[セクション分けした詳細内容]
```

**L0/L1/L2 免除対象**:
- `doc_type: meeting | daily-log` — 一次情報の自由形式
- `doc_type: project` — README 構造（マイルストーン等）
- `doc_type: decision | task` — アクション指向の構造
- `doc_type: index` — 目次・ナビゲーション
- `80_sandbox/{inbox,ideas,research,discussions}/` — 自由形式

---

### ファイル命名規則

| 種別 | 命名ルール | 例 |
|---|---|---|
| canonical | `<topic>.md`（内容を表す名前） | `thermal-strategy.md`, `connector-selection.md` |
| idea | `<YYYY-MM-DD>_<slug>.md` | `2026-05-28_thermal-hypothesis.md` |
| source/raw | `<topic>_<YYYYMMDD>.md` | `iso_16750_overview_20260528.md` |
| sandbox/inbox | `<YYYY-MM-DD>_<slug>.md` | `2026-05-28_bracket-idea.md` |
| sandbox/drafts | `<YYYY-MM-DD>_<slug>-draft.md` | `2026-05-28_thermal-strategy-draft.md` |
| meeting | `<YYYY-MM-DD>_<slug>.md` | `2026-05-28_thermal-review.md` |
| daily-log | `<YYYY-MM-DD>.md`（1日1ファイル） | `2026-05-28.md` |
| decision | `DEC-NNNN_<slug>.md` | `DEC-0001_connector-supplier.md` |
| task | `TASK-NNNN_<slug>.md` | `TASK-0001_fea-rerun.md` |
| project | `README.md` (`10_projects/<project>/`) | — |

---

### relations グラフ

`relations` フィールドはナレッジグラフを構成する。以下の関係タイプを使い分ける:

| 関係タイプ | 使用する場合 | 例 |
|---|---|---|
| `depends_on` | このドキュメントの前提知識 | 試験結果ドキュメントが設計仕様に依存 |
| `supports` | このドキュメントが根拠・証拠を提供 | 試験データが設計判断を支持 |
| `contradicts` | 矛盾・対立する見解 | 古い設計判断 vs 新試験結果 |
| `related` | 関連するが直接の依存/支持ではない | 類似テーマの横断ドキュメント |

**注意**: `relations.*` には必ず実在する `doc_id` を書く。存在しない doc_id を書くと CI で検出される。

---

### ops 層の専用フィールド

#### meeting 固有（doc_type: meeting）

```yaml
meeting_type: internal | partner | supplier | review
attendees: [string, ...]
extracted_decisions: [doc_id, ...]   # compile-meeting が自動設定
extracted_tasks: [doc_id, ...]       # compile-meeting が自動設定
```

#### daily-log 固有（doc_type: daily-log）

```yaml
project: [<project-slug>]            # どのプロジェクトの日報か（複数可）
extracted_tasks: [doc_id, ...]       # compile-meeting/daily-log が自動設定
```

#### decision 固有（doc_type: decision）

```yaml
source_meeting: doc_id              # 元の議事録（任意）
review_by: YYYY-MM-DD               # 再検討期限（任意）
impact_areas: [string, ...]         # 影響範囲
related_tasks: [doc_id, ...]
```

#### task 固有（doc_type: task）

```yaml
priority: high | medium | low
decision_ref: doc_id                # 根拠決定（任意）
source_meeting: doc_id              # 元議事録（任意）
due_date: YYYY-MM-DD
owners: [string, ...]
project_ref: doc_id                 # 属するプロジェクト（ops.project.* 形式）
phase: discovery | design | development | testing | launch | maintenance
```

#### project 固有（doc_type: project）

```yaml
phase: discovery | design | development | testing | launch | maintenance
priority: high | medium | low
milestones:
  - name: string
    target_date: YYYY-MM-DD
    status: pending | in_progress | done
```

#### requirement 固有フィールド（doc_type: requirement）

```yaml
# 10_projects/<project>/requirements/ 配下の要件ドキュメント専用

requirement_level: vision | outcome | capability | feature | eval | engineering | adr
# - vision      : なぜ存在するか（project 1 つにつき 1 ファイル）
# - outcome     : 成功定義・北極星指標（project 1 つにつき 1 ファイル）
# - capability  : 実装非依存の能力単位（CAP-NNN_<slug>.md）
# - feature     : 体験・コンポーネント機能単位（FEAT-NNN_<slug>.md）
# - eval        : EARS 受け入れ基準（<CAP|FEAT>-NNN_evals.md）
# - engineering : 材料 / 寸法 / 公差 / 試験条件 / サプライヤー
# - adr         : Architecture Decision Record（ADR-NNN_<slug>.md）

stability: stable | evolving | volatile
# - stable  : Vision / Outcomes（数ヶ月〜年単位で安定）
# - evolving: Capabilities（四半期単位で変化）
# - volatile: Features / Engineering（週〜月単位で変化）

parent_capability: req.<project>.cap.<slug>   # feature/eval が紐づく上位 capability
acceptance_refs: [req.<project>.eval.<slug>, ...]
grill_session: knowledge/80_sandbox/grill-sessions/<file>.md

# status（requirement 専用）
# - draft / approved / implementing / shipped / deprecated
```

#### grill_session 固有フィールド（doc_type: source として保存）

```yaml
# knowledge/80_sandbox/grill-sessions/ 配下専用
# requirements-grill スキルが自動管理するセッション状態ファイル

grill_target:
  project: <project>
  layers:  [<V|O|C|F|E|S>, ...]
  current_layer: <V|O|C|F|E|S>
  writeout_paths:
    V: knowledge/10_projects/<project>/requirements/vision.md
    # ...

# 内部 status は本文の "## State" セクションで管理（in_progress / paused / completed / abandoned）
```
