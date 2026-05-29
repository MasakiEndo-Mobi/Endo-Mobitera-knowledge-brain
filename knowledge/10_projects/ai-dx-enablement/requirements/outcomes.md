---
doc_id: req.ai-dx-enablement.outcomes
title: AI/DX イネーブルメント Outcomes
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: execution
status: draft
as_of: 2026-05-29
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: AI・自動化による削減工数（時間/月）を北極星とし、機密区分の遵守100%を前提に、設計者が"設計そのもの"に使える時間を測定可能な形で増やす。
confidence: medium
requirement_level: outcome
stability: stable
relations:
  depends_on: [req.ai-dx-enablement.vision]
  related: [ops.meeting.2026-05-27-ai-agent-efficiency]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**AI・自動化による削減工数（時間/月）を North Star とし、機密データ区分の遵守 100% を前提に、設計者が"設計そのもの"に使える時間を測定可能な形で増やす。**

---

## L1（5つの要点）

- **North Star Metric**: AI・自動化による削減工数（時間/月）。議事録作成・タスク抽出・差分比較・資料変換等をAIに肩代わりさせ、設計に使える時間の創出量で成功を測る。
- **Target**: 正式値は未確定（`[X]` 保留／KPI設計後に確定）。初期の目安は「自部署で月10〜20時間/人の削減を体感」。参考実績: 輝度マクロ年間約50時間削減、SPO Tool Boxの日常コスト削減。
- **Floor（失敗下限）**: ①機密データ誤入力が1件でも発生 → 即運用見直し（レッドライン）②削減工数がゼロ/マイナス → ツール・運用見直し ③3ヶ月使われず形骸化 → 横展開アプローチ転換。
- **計測方法**: 自己申告ベースの簡易ログ（「従来手作業の時間 − AI/ツール利用後の時間 × 実施回数」）をMarkdown表に記録し月次集計。定着後にViewt/PowerBI等での自動集計を検討。
- **Leading / Lagging**: Leading=Markdown化率／AI活用作業の週次件数／スクリプト・プロンプト整備数。Lagging=累計削減工数／属人化解消度（後任が経緯を自力で追えるか）／自部署への展開人数。

---

## L2（詳細）

### 詳細指標一覧

| 種別 | 指標 | 計測 | 目標 |
|---|---|---|---|
| North Star | AI・自動化による削減工数（時間/月） | 自己申告ログの月次集計 | 初期目安 月10〜20h/人（正式値はKPI設計後） |
| Leading | 業務ドキュメントのMarkdown化率 | 週次 | 上昇傾向 |
| Leading | AI活用した作業の件数 | 週次カウント | 増加 |
| Leading | スクリプト/プロンプト整備数 | 随時 | 蓄積 |
| Lagging | 累計削減工数 | 月次累計 | 増加 |
| Lagging | 属人化解消度（後任が経緯を追える） | 定性評価 | 改善 |
| Lagging | 自部署への展開人数 | 随時 | 増加 |

### セグメント別の観点
初期は遠藤個人の削減工数のみで見る（最小起点＝自分）。定着後に「自部署メンバー別」「施策/ツール別（議事録自動化・差分比較・資料変換 等）」に分け、どの施策が効いているかを追跡する。

### コンプライアンス成功指標（セキュリティ遵守）
- **機密データ区分の遵守率 100%**: パブリック/社内/マル秘を区分し、マル秘を汎用クラウドAIに投入した事例＝0件（必須・最優先）。
- **許可範囲内の運用**: ITインフラチームが許可したツール・利用条件の範囲内（個人版は機密非入力の条件下のみ）。
- **契約制約の確認**: Qualcomm/トヨタ等の他社帰属データは契約内容を確認した上で扱う。

> ⚠️ North Star のターゲット値（O-2）は未確定。5/27会議で「効果測定（KPI）が未整理」が課題に挙がっており、KPI設計を経て確定する。
