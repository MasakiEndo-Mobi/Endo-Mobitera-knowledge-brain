---
doc_id: req.ai-dx-enablement.vision
title: AI/DX イネーブルメント Vision
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: routing
status: draft
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: 機構設計者が議事録・設計知識をMarkdownで構造化しAIに横断させることで、属人化を解消し"設計そのもの"に集中できる職場をつくる、現場発のAI活用イネーブルメント。
confidence: medium
requirement_level: vision
stability: stable
relations:
  related: [ops.project.ai-dx-enablement, ops.meeting.2026-04-24-local-llm-hearing, ops.meeting.2026-05-27-ai-agent-efficiency]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**機構設計者が議事録・設計知識を Markdown で構造化し AI に横断させることで、属人化を解消し"設計そのもの"に集中できる職場をつくる、現場発の AI 活用イネーブルメント。**

---

## L1（5つの要点）

- **Pain**: ハード設計者・工場検査担当の「情報の属人化・非効率」。設計ノウハウや変更履歴が属人化（CAD変更点がスクショでしか残らない）、Excel方眼紙でAIに読ませられず知識が再利用できない、工場では新機種・設計変更の通知遅延で手戻り・人為ミスが起きる。
- **3-Year Differential**: 知識がMarkdownで構造化されAIが横断参照でき、会議は録画→AIが議事録・タスク・差分を自動生成、設計変更が人手の転記なしに工場へ伝わり、検査スクリプトのデバッグやデータシート解析もAIが下支え。少人数でも高効率な開発体制が回る。
- **必然性**: 現場固有のドメイン知識（CAD・DSL検査アプリ・BOM/設計変更フロー）は現場にしか分からず汎用AI/外部ベンダーでは要件定義できない。機密データ（トヨタ仕様書・Qualcommデータシート等）は汎用クラウドに出せず使い分けの現場判断が要る。SPO Tool Box等の内製実績があり、トップダウンを待たずボトムアップで回せる。
- **Non-goals**: ①AIに最終判断を委ねない（人がエビデンスを確認、AIは下支え・セカンドオピニオン）②機密データを汎用クラウドAIに投入しない（パブリック/社内/マル秘の区分を厳守）③ツール導入自体を目的化しない ④最初から全社・大規模システム化を狙わない（現場ボトムアップ起点）。
- **North Star Quote**: 本人/同僚「議事録もタスクも勝手にまとまるから、設計そのものに頭を使えるようになった」／後任「過去の検討経緯と"なぜそうしたか"がすぐ追える」。

---

## L2（詳細）

### Primary Stakeholder
最優先は **ハード設計者本人（遠藤および後任の機構設計PDTメンバー）**。まず自分たちの設計業務の属人化解消・効率化を起点とし、次点で工場検査担当・非開発者メンバー（Obsidianを「非開発者のメモ帳」として展開する対象）へ広げる。開発本部（高畠ら）は協働相手であり、この活動が支援する中心ではない。

### 適用範囲（最初の起点）
最小起点は **遠藤自身の機構設計業務（825D文脈）の議事録・設計メモのMarkdown化とAI要約・タスク抽出**（＝このKB＋AI運用そのもの）。そこで型を作ってから自部署（ハード設計2部2課）へ。工場検査の自動化やViewt（Redshift）連携など大型テーマは将来スコープとして切り出す。

### 関連プロジェクト・前段
- 並走: [[825d-overview|24CY_IVI_825D 機構設計]]（最小起点の文脈・KB＋AIパイロット）
- 起点となった議論: [[2026-04-24_local-llm-hearing|ローカルLLMヒアリング]] / [[2026-05-27_ai-agent-efficiency|AIエージェント効率化お喋り場]]
- OJT報告での「AI別軸」: [[DEC-0002_ojt-focus-on-825d|DEC-0002]] / [[TASK-0003_ai-dx-separate-track|TASK-0003]]
- 関連動向: DX戦略推進室（2026-07-01 新設予定）
