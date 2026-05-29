---
doc_id: req.ai-dx-enablement.cap.confidentiality-guard
title: CAP-005 機密区分を守ってAIを使い分けできる
doc_type: requirement
project: [ai-dx-enablement]
layer: canonical
role_in_story: insight
status: draft
as_of: 2026-05-29
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: パブリック/社内/マル秘の区分に応じてAIツールを選択し、機密データを汎用クラウドAIに出さない横断的ガード能力。
confidence: medium
requirement_level: capability
stability: evolving
relations:
  depends_on: [req.ai-dx-enablement.vision, req.ai-dx-enablement.outcomes]
  related: [req.ai-dx-enablement.cap.meeting-capture, req.ai-dx-enablement.cap.design-info-analysis, req.ai-dx-enablement.cap.task-automation]
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_ai-dx-enablement-V-vision.md
---

## L0（1文要約）

**データの機密区分（パブリック/社内/マル秘）に応じてAIツールを選択し、機密を汎用クラウドAIに出さないことを担保する横断的ガード能力。**

---

## L1（5つの要点）

- **できること**: 機密区分を守ってAIを使い分けできる（区分に応じてローカルLLM/セキュア環境/汎用クラウドを選択）。
- **実現手段の前提（実装非依存）**: 技術でなく**運用ルール＋判断**（ツール選択の運用基準・規律）。
- **依存前提**: 機密区分の明確な定義と、各ツールのセキュリティ承認状況（学習されないか等）の把握。
- **安定性**: evolving（社内ポリシー・契約・ツールのセキュリティ承認状況で変わる）。
- **Outcome貢献**: コンプラ指標（機密区分の遵守率100%＝マル秘を汎用クラウドAIに投入0件）。

---

## L2（詳細・根拠・構造）

### 区分と扱い
- **パブリック**（誰でも参照可）: AI投入可。
- **社内情報**: Googleに学習されない等のセキュアなツール（NotebookLM Enterprise等）なら入力可。
- **マル秘 / 他社帰属**（Qualcommデータシート、トヨタ仕様書等）: 契約内容を厳密確認の上で慎重に。汎用クラウドAIには出さない。

### Graceful Degradation
区分判断に迷う場合は**常に厳しい側（ローカル/入力しない）に倒す**（fail-safe＝機密保護優先）。

### 横断制約
本能力は単独で価値を出すのではなく、[[CAP-001_meeting-capture|CAP-001]]／[[CAP-003_design-info-analysis|CAP-003]]／[[CAP-004_task-automation|CAP-004]] 全てに掛かる横断的ガード。認証情報は KB でなく git管理外 `secrets/` で管理する方針と整合。
