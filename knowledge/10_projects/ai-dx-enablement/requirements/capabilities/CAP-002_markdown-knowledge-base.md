---
doc_id: req.ai-dx-enablement.cap.markdown-knowledge-base
title: CAP-002 業務知識をMarkdownで蓄積・横断検索できる
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: insight
status: draft
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: 業務知識をAI可読な構造（Markdown＋frontmatter）で蓄積し、横断検索・参照することで属人化を解消できる。
confidence: medium
requirement_level: capability
stability: stable
relations:
  depends_on: [req.ai-dx-enablement.vision, req.ai-dx-enablement.outcomes]
  related: [req.ai-dx-enablement.cap.meeting-capture, req.ai-dx-enablement.cap.design-info-analysis]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**業務知識をMarkdown＋frontmatterの構造で蓄積し、AIと人が横断検索・参照できる能力（属人化解消の土台）。**

---

## L1（5つの要点）

- **できること**: 業務知識をAI可読な構造（Markdown）で蓄積・横断検索できる。後任が経緯を自力で追える。
- **実現手段の前提（実装非依存）**: 既存基盤＋運用（このObsidian KB＋AI）。仕組みは整備済、定着が課題。
- **依存前提**: ドキュメントがMarkdown＋frontmatter規約で書かれていること、KB運用の継続。
- **安定性**: stable（KB原理に近い）。
- **Outcome貢献**: 属人化解消度（Lagging）／Markdown化率（Leading）。

---

## L2（詳細・根拠・構造）

### Graceful Degradation
AI検索が拾えない場合でも、**doc_id / relations / MOC で辿れる**（AI検索は補助で、機械可読IDが正本）。

### 独立進化・依存
**本能力が土台**。[[CAP-001_meeting-capture|CAP-001]] の出力先、[[CAP-003_design-info-analysis|CAP-003]] の入力源。横断制約の [[CAP-005_confidentiality-guard|CAP-005]] が掛かる。

### 共通化
汎用能力。全プロジェクトで使える。KB の `00_index/capabilities/` の intake/structured-extraction と将来統合する余地。
