---
doc_id: index.cap.structured-extraction
title: CAP-002 議事録/日報からの構造化抽出
doc_type: requirement
project: [all]
layer: canonical
role_in_story: execution
status: implementing
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: 議事録・日報から decision/task/question を抽出し、型付きファイルとして経緯を追跡可能にできる
confidence: high
requirement_level: capability
stability: evolving
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_24CY_IVI_825D-V-vision.md
tags: [capability, extraction, decision, task]
relations:
  depends_on: [index.cap.intake, index.outcomes]
  related: [index.cap.review-compilation]
---

## L0（1文要約）

**格納済みの議事録・日報から decision / task / question を抽出して型付きオブジェクトファイル化し、設計判断の経緯を追跡可能にできる能力。**

---

## L1（5つの要点）

- **実装**: ✅ 既存スキル `compile-meeting` / `daily-log` で実現済み。
- **前提**: 議事録・日報が格納済みであること／ops ガードレール（本文の創作禁止・確認ゲート）を守ること。
- **安定性**: `evolving`。
- **失敗時の振る舞い**: 抽出不能なら原文へのリンクのみのスタブを生成し、情報を捨てない。
- **Outcome 貢献**: 「構造化実施率」(Leading) と経緯追跡 → 北極星ゼロ率・部門間手戻り削減 (Lagging) に寄与。

---

## L2（詳細）

### 独立進化・共通化
- CAP-001（取り込み）の出力に依存（格納 → 抽出の順序依存）。
- KB 汎用能力（全プロジェクト共通）。

### Outcome との紐付け
- decision/task の経緯が KB を指せば辿れる状態 → 面談・部門連携での「言った言わない」消失（O-7 定性シグナル）に直結。
