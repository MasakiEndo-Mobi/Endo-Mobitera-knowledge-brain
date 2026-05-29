---
doc_id: req.ai-dx-enablement.cap.task-automation
title: CAP-004 定型業務を自動化できる
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: insight
status: draft
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: 資料変換・PDF抽出・通知・検査スクリプト支援などの定型業務をAIエージェント＋スクリプトで自動化し、削減工数の最大の源泉とする。
confidence: medium
requirement_level: capability
stability: volatile
relations:
  depends_on: [req.ai-dx-enablement.vision, req.ai-dx-enablement.outcomes]
  related: [req.ai-dx-enablement.cap.confidentiality-guard, res.tooling.spo-path-converter]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**資料の言語変換・PDF→整理・Teams通知・検査スクリプトのデバッグ支援などの定型業務を、AIエージェント＋スクリプトで自動化できる能力。**

---

## L1（5つの要点）

- **できること**: 定型業務を自動化できる（資料の日英変換、PDFからのテキスト抽出→Excel整理、通知、検査スクリプトのデバッグ支援）。
- **実現手段の前提（実装非依存）**: 新規構築が中心（GitHub Copilot＋Pythonスクリプトを個別開発。[[spo-path-converter|SPO Tool Box]]・輝度マクロ等の延長）。
- **依存前提**: 入力データ形式の安定、実行環境（VS Code / Python / Copilotライセンス）が揃っていること。
- **安定性**: volatile（対象業務・スクリプトごとに頻繁に変わる）。
- **Outcome貢献**: 削減工数（**最大の貢献源**）／スクリプト・プロンプト整備数（Leading）。

---

## L2（詳細・根拠・構造）

### Graceful Degradation
スクリプト失敗時は**手動フォールバックに切替え、エラー時は停止して通知**する（黙って誤動作させない）。

### 独立進化・依存
**最も独立**した能力（個別スクリプト単位で他に影響せず進化可）。横断制約の [[CAP-005_confidentiality-guard|CAP-005]] が掛かる（自動処理する入力の機密区分に注意）。

### 共通化
汎用能力。全プロジェクトで使える。実績: [[spo-path-converter|SharePointパス変換君]]、輝度ムラ計算マクロ。
