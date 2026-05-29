---
doc_id: req.ai-dx-enablement.cap.design-info-analysis
title: CAP-003 設計・部品情報を解析・要約できる
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: insight
status: draft
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: データシート・設計変更差分・図面情報をAIで解析・要約し、調査時間を削減できる（CAD非言語情報は発展途上）。
confidence: medium
requirement_level: capability
stability: evolving
relations:
  depends_on: [req.ai-dx-enablement.vision, req.ai-dx-enablement.outcomes, req.ai-dx-enablement.cap.markdown-knowledge-base]
  related: [req.ai-dx-enablement.cap.confidentiality-guard]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**部品データシート・設計変更前後の差分・図面情報をAIで解析・要約できる能力（CAD非言語情報は実用化途上）。**

---

## L1（5つの要点）

- **できること**: 設計・部品情報を解析・要約できる（データシート解析、変更前後の差分比較、電気図面の整合チェック等）。
- **実現手段の前提（実装非依存）**: 一部既存（データシート/差分は Copilot/NotebookLM で可）、一部ハードル高（CADの非言語情報は直接読み取りにくく実用化途上）。
- **依存前提**: 解析対象がAI可読形式（PDF/テキスト）であること、機密区分クリア。
- **安定性**: evolving（AI能力の進化に依存、特にCAD/図面解析は発展途上）。
- **Outcome貢献**: 削減工数（データシート解析・差分比較の時間）。

---

## L2（詳細・根拠・構造）

### Graceful Degradation
AI解析が誤る前提で、**一次資料で人が確認し、複数AIでセカンドオピニオン**を取る（鵜呑みにしない）。

### 独立進化・依存
土台の [[CAP-002_markdown-knowledge-base|CAP-002]] の構造化品質に依存。横断制約の [[CAP-005_confidentiality-guard|CAP-005]]（特に他社帰属データシートの扱い）が強く掛かる。

### 制約・将来
CADから言語情報で3Dモデル生成するAI技術（Claude Code拡張等）は存在するが実用化ハードル高い。電気図面（PDF化で2次元）の解析と要件（顧客要求・法律・機能安全・Automotive SPICE）整合チェックは有望領域。
