---
doc_id: req.ai-dx-enablement.cap.meeting-capture
title: CAP-001 会議・対話を構造化記録できる
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: insight
status: draft
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: 録音/メモから議事録・決定・タスク・差分を構造化生成し、議事録作成の工数を削減できる。
confidence: medium
requirement_level: capability
stability: stable
relations:
  depends_on: [req.ai-dx-enablement.vision, req.ai-dx-enablement.outcomes]
  related: [req.ai-dx-enablement.cap.markdown-knowledge-base]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**会議・対話を録音/メモから構造化記録し、議事録・決定・タスク・差分を生成できる能力。**

---

## L1（5つの要点）

- **できること**: 会議・対話を構造化記録できる（議事録／決定事項／タスク／変更差分の自動生成）。
- **実現手段の前提（実装非依存）**: 既存ツールで概ね実現可（議事録作成くん / NotebookLM / Copilot 等）。運用ルールの整備が中心。
- **依存前提**: 会議の録音/メモが取得できること（録画・録音前提の情報収集の意識）。
- **安定性**: stable（能力自体は不変。ツールは入れ替わる）。
- **Outcome貢献**: 削減工数（議事録作成時間）。Leading 指標「AI活用作業の件数」にも寄与。

---

## L2（詳細・根拠・構造）

### Graceful Degradation
AI生成議事録が不正確な場合に備え、**原本（録音/メモ）を保持し、人が検証・修正できる**状態を維持する（V-4: AIに最終判断を委ねない）。

### 独立進化・依存
土台の [[CAP-002_markdown-knowledge-base|CAP-002]]（Markdown蓄積）に出力先として依存。横断制約の [[CAP-005_confidentiality-guard|CAP-005]]（機密区分）が掛かる。

### 共通化
汎用能力。825D含む全プロジェクトで使える（KBの `compile-meeting` / `kb-intake` が体現）。
