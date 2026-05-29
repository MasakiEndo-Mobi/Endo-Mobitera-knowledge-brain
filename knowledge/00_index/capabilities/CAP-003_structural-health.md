---
doc_id: index.cap.structural-health
title: CAP-003 KB構造健全性の自律維持・検証
doc_type: requirement
project: [all]
layer: canonical
role_in_story: execution
status: implementing
as_of: 2026-05-29
audience: [self, engineer]
owners: [self]
one_line_thesis: doc_id/relations/wikilink の整合と スキーマ適合を自動検証し、切れリンク0・適合率100%を保てる
confidence: medium
requirement_level: capability
stability: stable
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_24CY_IVI_825D-V-vision.md
tags: [capability, integrity, ci, links]
relations:
  depends_on: [index.outcomes]
  related: [index.cap.intake]
---

## L0（1文要約）

**doc_id ↔ wikilink の双方向整合、relations の doc_id 実在、必須フロントマター・L0/L1/L2 充足を自動検証し、切れリンク0・スキーマ適合100%を維持できる能力。**

---

## L1（5つの要点）

- **実装**: ◐ `obsidian-link` ＋ `tools/`（CI 検証）で一部実現。**自動実行（hook/CI トリガ）は未整備**。
- **前提**: doc_id/relations の命名規約／CI 実行環境（vehkb-env、ただし本マシンは .venv 運用）。
- **安定性**: `stable` — 物理原理ならぬ「規約」に近く、年単位で安定。
- **失敗時の振る舞い**: 検証失敗は**警告のみ**（自動修正で内容を壊さない）。切れリンクを一覧化して人手修正へ回す。
- **Outcome 貢献**: 運用健全性指標「切れリンク0・スキーマ適合100%」を直接担保。手動管理 KB が破綻した過去ペイン②の再発防止。

---

## L2（詳細）

### 独立進化・共通化
- 単独で進化可能（横断検査であり個別ドキュメントの内容に介入しない）。
- KB 汎用能力（全プロジェクト共通）。

### 未整備部分（実装ギャップ）
- 検証の**自動実行トリガ**（commit hook / CI）が未整備。現状は手動起動。F/S 層で「いつ・どう走らせるか」を詰める。
