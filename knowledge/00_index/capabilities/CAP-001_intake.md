---
doc_id: index.cap.intake
title: CAP-001 自動取り込み・分類・格納
doc_type: requirement
project: [all]
layer: canonical
role_in_story: execution
status: implementing
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: 雑な入力（md/テキスト/ディレクトリ/議事録/日報）を自動分類して正しい層・場所に格納できる
confidence: high
requirement_level: capability
stability: evolving
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_24CY_IVI_825D-V-vision.md
tags: [capability, intake]
relations:
  depends_on: [index.outcomes]
  related: [index.cap.structured-extraction]
---

## L0（1文要約）

**雑な入力を受け取り、種別を自動判定して KB の正しい層・ディレクトリに、規約準拠のフロントマター付きで格納できる能力。**

---

## L1（5つの要点）

- **実装**: ✅ 既存スキル `kb-intake` で実現済み。
- **前提**: 入力が KB 配下に渡されること／AGENTS.md の層・命名規約が維持されていること。
- **安定性**: `evolving` — 分類ルールは運用の中で育つ。
- **失敗時の振る舞い**: 分類に迷ったら `80_sandbox/inbox/` に退避して人手判断に委ねる（誤格納より保留を優先し、情報を捨てない）。
- **Outcome 貢献**: 「KB 投入継続」(Leading) の入口。投入摩擦を下げることで北極星「思い出し作業ゼロ率」に間接寄与。

---

## L2（詳細）

### 独立進化・共通化
- 単独で進化可能（下流の CAP は格納結果のみを参照するため、分類ロジックの変更が下流を壊さない）。
- KB 汎用能力（全プロジェクト共通）。20_components のような特定プロジェクト依存ではない。

### Outcome との紐付け
- Leading「KB 投入継続日数」「構造化実施率」の前段。投入が雑でも成立する＝Non-goal「手動管理を人間に強いない」の実現手段。
