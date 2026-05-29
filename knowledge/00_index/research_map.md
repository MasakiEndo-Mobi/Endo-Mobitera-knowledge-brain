---
doc_id: index.research-map
title: リサーチマップ・全体ナビゲーション
doc_type: index
project: [all]
layer: canonical
role_in_story: routing
status: canonical
as_of: 2026-05-28
audience: [self]
one_line_thesis: KB全体のドキュメント構成を一覧し、エージェントが関連ドキュメントを高速に発見するためのナビゲーション・ハブ。
confidence: high
---

# リサーチマップ・全体ナビゲーション

このファイルは KB 全体の **エントリポイント**。新しい canonical ドキュメントを追加したら、対応するセクションに 1 行追記する。

> **Dataview ベースの動的ビューは `moc_*.md` に分散している。このファイルはトピック軸の手書きインデックス。**

---

## アクティブプロジェクト

> プロジェクトを起こしたら `10_projects/<project>/README.md` を作り、ここに 1 行追記する。

| Project | One-Line Thesis | Phase |
|---|---|---|
| **24CY_IVI_825D** | 北米向けIVI(21CY 220D母体・Lexus TX)の機構設計。中心ハブ=[[825d-overview]]、文脈/体制=[[project-context]] | development / validation |
| **ai-dx-enablement** | ローカルLLM＋クラウドAI(GitHub Copilot/NotebookLM等)横断活用で業務効率化・社内展開。定義=`ops.project.ai-dx-enablement` | discovery |

> 825D 個人成果物: [[2026-04-24_ojt-4q-final-report-outline|2年目OJT 4Q最終報告アウトライン]]（`80_sandbox/ideas/`）
> AI/DX 会議: [[2026-04-24_local-llm-hearing|ローカルLLMヒアリング]] / [[2026-05-27_ai-agent-efficiency|AIエージェント効率化お喋り場]]

---

## 部品カテゴリ横断知見 (20_components/)

> `comp.<category>.<slug>` の canonical ドキュメントが増えたらここに追記。

### Connectors
- _(未登録)_

### Housings
- _(未登録)_

### Brackets
- _(未登録)_

### Thermal
- _(未登録)_

### Vibration Damping
- _(未登録)_

### Sealing
- _(未登録)_

### Fasteners
- _(未登録)_

---

## 規格・社内基準 (30_standards/)

### ISO
- _(未登録)_

### IEC
- _(未登録)_

### JIS
- _(未登録)_

### 社内基準
- **TOYOTA用語集** (`std.internal.toyota-term-*`): DR / RDDP / 外設申 / 支給 / 管理自給 / 開発フェーズ / 21CY部品品番体系 / 24CY内機
- **IVI開発プロセスガイド** (`std.internal.ivi-development-process`)
- _(旧KB第1波取り込み・`layer: raw`)_

---

## サプライヤー (40_suppliers/)

- **Markforged** (`supp.markforged.overview`) — 金属/複合材3Dプリンタ Digital Forge
- **UMI** (`supp.umi.overview`) — 微細加工専業
- **ホシデンFD** (`supp.hoshiden.bonding-fd`) — ボンディングメーカー（825D採用検討）
- **中沼アートスクリーン** (`supp.nakanuma.art-screen`) — 透過加飾「ガラリット」
- **ファソテック** (`supp.fasotec.ai-design-survey`) — AI設計代行調査

---

## 技術リサーチ (50_research/)

- **DRBFM** (`res.drbfm.*`): 概論 / ワークシート作成 / DR実施 / 教育 / 実践支援ツール / 統合実装戦略
- **3Dプリンティング** (`res.3d-printing.*`): 概要 / 活用未来 / フィラメント吸水性 / 加飾塗装 / Markforged FX10 / Onyx平滑化(chat/report) / PEEK
- **ガラス** (`res.glass.*`): 強度評価4PB/RoR / スリミング
- **塗装・加飾** (`res.coating.*`): 環境対応型機能性塗料 / 透過加飾技術
- **照明** (`res.lighting.*`): RGB-LED温度特性 / アンビエント棒照明
- **電気** (`res.electrical.*`): 板金GNDフレーム / 性能動作マトリクス
- **材料/その他**: CFRTP車載ディスプレイフレーム / FineXメタルメッシュ / 分散マニュファクチャリング / 当たり図DR / Teams議事録ガイド / Keyence 3DP IP / AIエッセイ / IPONCネジの本質
- **ツール (`res.tooling.*`)**: [[spo-path-converter|SharePointパス変換君]]（SP/Teamsリンク→階層フォルダリンク変換, C#） / Keyence 3DP IP
- _(旧KB第1波取り込み・`layer: raw`)_

---

## 旧KB raw アーカイブ (90_sources/raw/) — 第2波・第3波

> 第2波・第3波は `doc_type: source` / `layer: raw` で保全。canonical 昇格は使う時に遅延（Index Now, Polish Later）。

- `old-kb-monthly-reports/` — 月次業務レポート 14（2025-04〜2026-03, `source.monthlyreports.*`）
- `old-kb-work-notes/` — 業務ノート・学習 19（`source.worknotes.*`）
- `old-kb-methods/` — 手法・プロンプト・ツール資産 24（`source.methods.*`）
- `old-kb-projects/` — 終了/非現役案件 20（21CY・24CY非現役・IPONC, `source.projects.*`）

---

## 関連 MOC（動的ビュー）

- [[moc_components]] — 部品カテゴリ別 Dataview ビュー
- [[moc_projects]] — プロジェクト進捗 Dataview ビュー
- [[moc_tasks]] — オープンタスク一覧
