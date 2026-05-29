---
doc_id: grill.ai-dx-enablement.v.vision
title: Grill Session - ai-dx-enablement/Vision
doc_type: source
project: [ai-dx-enablement]
layer: raw
role_in_story: context
status: draft
as_of: 2026-05-29
audience: [self]
one_line_thesis: ai-dx-enablement の Vision 層を grill するセッション状態ファイル
confidence: speculative
grill_target:
  project: ai-dx-enablement
  layers: [V, O, C, F, E, S]
  current_layer: C
  writeout_paths:
    V: knowledge/10_projects/ai-dx-enablement/requirements/vision.md
    O: knowledge/10_projects/ai-dx-enablement/requirements/outcomes.md
    C: knowledge/10_projects/ai-dx-enablement/requirements/capabilities/
    F: knowledge/10_projects/ai-dx-enablement/requirements/features/
    E: knowledge/10_projects/ai-dx-enablement/requirements/evals/
    S: knowledge/10_projects/ai-dx-enablement/requirements/engineering/
---

# Grill Session: ai-dx-enablement / Vision

---

## State

- turns: 25
- progress_stalled_turns: 0
- last_saved: 2026-05-29T00:25:00Z
- next_action: "Capability サマリー承認 → CAP-001〜005 書き出し"
- mode: NEW
- web_gate_suppressed_layers: []
- web_gate_refusal_count: {}

---

## Layer Progress

- V: { answered: 8/8, ready_to_writeout: true, writeout_done: true }
- O: { answered: 8/8, ready_to_writeout: true, writeout_done: true }
- C: { answered: 8/8, ready_to_writeout: true, writeout_done: true, items: [CAP-001 会議構造化記録, CAP-002 Markdown蓄積・横断検索, CAP-003 設計・部品情報の解析要約, CAP-004 定型業務自動化, CAP-005 機密区分ガード] }
- F: { answered: 0/8, ready_to_writeout: false, writeout_done: false, items: [] }
- E: { answered: 0/8, ready_to_writeout: false, writeout_done: false, items: [] }
- S: { answered: 0/8, ready_to_writeout: false, writeout_done: false }

---

## Open Questions

<!-- V 層は全問回答済。空。 -->

### V-5: Primary Stakeholder
- answer: 最優先＝ハード設計者本人（遠藤・後任の機構設計PDT）。次点で工場検査担当・非開発者。開発本部(高畠ら)は協働相手であり支援対象の中心ではない。
- label: [A]

### V-6: 適用範囲
- answer: 最小起点＝遠藤の機構設計業務（825D文脈）の議事録・設計メモのMarkdown化とAI要約・タスク抽出（このKB＋AI運用そのもの）。型を作って自部署(ハード設計2部2課)へ。工場自動化・Viewt連携は将来スコープ。
- label: [A]

### V-7: North Star Quote
- answer: 本人/同僚「議事録もタスクも勝手にまとまるから、設計そのものに頭を使えるようになった」／後任「過去の検討経緯と"なぜそうしたか"がすぐ追える」。
- label: [A]

### V-8: One-line Thesis（草案）
- answer: 機構設計者が議事録・設計知識をMarkdownで構造化しAIに横断させることで、属人化を解消し"設計そのもの"に集中できる職場をつくる、現場発のAI活用イネーブルメント。
- label: [A]
- [V-6] このシステムが最初に狙う適用範囲は？
- [V-7] 成功したとき関係者が言う1文は？（North Star Quote）
- [V-8] このビジョンを1文で言うと？（one_line_thesis）

---

## QA Log

<!-- 1問1ターン。ラベル: [U] [I: 根拠] [A] [X] [W: source] -->

### V-1: Pain（誰の・何の痛み）
- answer: ハード設計者・工場検査担当の「情報の属人化・非効率」。設計ノウハウ/変更履歴が属人化（CADはスクショ管理）、Excel方眼紙でAI再利用不可、工場は新機種/設計変更の通知遅延で手戻り・人為ミス。
- label: [A]

### V-2: 3年後の差分
- answer: 知識がMarkdownで構造化されAIが横断参照、会議→自動議事録/タスク/差分生成、設計変更が転記なしで工場へ、検査スクリプトのデバッグ・データシート解析もAIが下支え → 少人数高効率体制。
- label: [A]

### V-3: 我々がやる必然性
- answer: 現場固有ドメイン知識（CAD/DSL検査アプリ/BOM・設計変更フロー）＋機密の壁（トヨタ仕様書・Qualcommデータシートは汎用クラウドに出せず使い分け要）＋内製ツール(SPO Tool Box)実績でボトムアップ可能。
- label: [A]

### V-4: Non-goals
- answer: ①AIに最終判断を委ねない（人がエビデンス確認・AIは下支え/セカンドオピニオン）②機密データを汎用クラウドAIに投入しない（パブリック/社内/マル秘区分厳守）③ツール導入の目的化を避ける ④最初から全社・大規模システム化を狙わない（現場ボトムアップ起点）。
- label: [A]

---

### O-1: North Star Metric
- answer: AI・自動化による削減工数（時間/月）。設計者が"設計そのもの"に使える時間の創出量。
- label: [A]

### O-2: 量産時点ターゲット値
- answer: 確定値なし→保留。方向性: 初期目安 月10〜20時間/人削減（輝度マクロ年50h・SPO Tool Box実績ベース）。正式値はKPI設計後（5/27会議でKPI未整理が課題）。
- label: [X]

### O-3: 失敗とみなす下限値
- answer: ①機密データ誤入力1件で即運用見直し（レッドライン）②削減工数ゼロ/マイナスでツール見直し③3ヶ月形骸化で横展開アプローチ転換。
- label: [A]

### O-4: 計測方法
- answer: 自己申告ベースの簡易ログ（「従来時間−利用後時間×実施回数」をMarkdown表に記録）を月次集計。定着後にViewt/PowerBI等で自動集計検討。
- label: [A]

### O-5: セグメント別の観点
- answer: 初期は遠藤個人の削減工数のみ。定着後に自部署メンバー別・施策/ツール別（議事録自動化/差分比較/資料変換）に分けて追跡。
- label: [A]

### O-6: Leading / Lagging KPI
- answer: Leading=Markdown化率/AI活用作業の週次件数/スクリプト・プロンプト整備数。Lagging=累計削減工数/属人化解消度/自部署展開人数。
- label: [A]

### O-7: 定性的成功シグナル
- answer: 同僚からAI活用相談が来る/会議で「Markdown・AI要約」が自然な前提に/後任・非開発者が自発的にKBを見てメモを残す。
- label: [A]

### O-8: コンプライアンス成功指標（セキュリティ遵守）
- answer: 機密データ区分の遵守率100%（マル秘を汎用クラウドAIに投入＝0件）必須／ITインフラ許可済みツール・条件内で運用／他社帰属データは契約確認の上で扱う。
- label: [A]

### C-1: できること動詞列挙（5能力）
- answer: CAP-001 会議・対話を構造化記録できる／CAP-002 業務知識をMarkdownで蓄積・横断検索できる／CAP-003 設計・部品情報を解析・要約できる／CAP-004 定型業務を自動化できる／CAP-005 機密区分を守ってAIを使い分けできる。
- label: [A]

### C-2: 既存ツール vs 新規構築
- answer: 既存可=CAP-001(議事録くん/NotebookLM/Copilot)・CAP-002(このKB＋AI)／一部ハードル=CAP-003(CAD非言語は発展途上)／新規構築=CAP-004(Copilot＋Python個別開発)／運用規律=CAP-005。
- label: [A]

### C-3: 依存前提
- answer: CAP-001=録音/メモ取得／CAP-002=Markdown＋frontmatter規約・KB運用継続／CAP-003=AI可読形式・機密区分クリア／CAP-004=入力形式安定・実行環境(VS Code/Python/Copilot)／CAP-005=機密区分定義・ツールのセキュリティ承認状況把握。
- label: [A]

### C-4: 安定性
- answer: stable=CAP-001/002／evolving=CAP-003(AI進化依存)・CAP-005(ポリシー/契約/承認状況依存)／volatile=CAP-004(対象業務ごと)。
- label: [A]

### C-5: Graceful Degradation
- answer: CAP-001=原本保持し人が検証修正／CAP-002=doc_id/relations/MOCで辿れる／CAP-003=一次資料確認＋複数AIセカンドオピニオン／CAP-004=手動フォールバック・エラー時停止通知／CAP-005=迷ったら厳しい側(ローカル/入力しない)に倒す。
- label: [A]

### C-6: 独立進化（依存グラフ）
- answer: CAP-002が土台（CAP-001出力先・CAP-003入力源）／CAP-005は横断制約（CAP-001/003/004に掛かる）／CAP-004が最も独立／CAP-001/003はCAP-002の構造化品質に依存。
- label: [A]

### C-7: 複数プロジェクト共通化
- answer: 汎用=CAP-001/002/004（全PJで使える、KBの compile-meeting/kb-intake が体現、00_index/capabilities と将来統合余地）／ドメイン寄り=CAP-003/005（機構設計横断で再利用）。
- label: [A]

### C-8: Outcome紐付け
- answer: CAP-001→削減工数(議事録時間)/Leading AI活用件数／CAP-002→属人化解消度/Markdown化率／CAP-003→削減工数(解析・差分)／CAP-004→削減工数(最大貢献)/スクリプト整備数／CAP-005→コンプラ指標(機密区分遵守100%)。
- label: [A]

---

## Decisions (Resolved)

---

## Conflicts

---

## Writeouts

- V -> knowledge/10_projects/ai-dx-enablement/requirements/vision.md (written at 2026-05-29, doc_id req.ai-dx-enablement.vision)
- O -> knowledge/10_projects/ai-dx-enablement/requirements/outcomes.md (written at 2026-05-29, doc_id req.ai-dx-enablement.outcomes)
- C -> capabilities/CAP-001..005 (written at 2026-05-29): cap.meeting-capture / markdown-knowledge-base / design-info-analysis / task-automation / confidentiality-guard

---

## Web Searches

---

## Notes

- 背景: 開発本部発のAI活用（ローカルLLM: LiteLLM/DX Spark/Qwen/Gemma/Dify ＋ クラウドAI: GitHub Copilot Business/NotebookLM Enterprise/M365 Copilot）を横断活用。
- owner=遠藤（self・機構設計側の窓口/推進）。
- 関連会議: ops.meeting.2026-04-24-local-llm-hearing, ops.meeting.2026-05-27-ai-agent-efficiency。
- DX戦略推進室 2026-07-01 新設予定。AI導入は現場ボトムアップが効果的との議論あり。
