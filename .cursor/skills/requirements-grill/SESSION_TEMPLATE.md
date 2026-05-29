---
doc_id: grill.<project>.<layer>.<slug>
title: Grill Session - <project>/<layer>
doc_type: source
project: [<project>]
layer: raw
role_in_story: context
status: draft
as_of: YYYY-MM-DD
audience: [self]
one_line_thesis: <project> の <layer> 層を grill するセッション状態ファイル
confidence: speculative
grill_target:
  project: <project>
  layers: [V, O, C, F, E, S]
  current_layer: V
  writeout_paths:
    V: knowledge/10_projects/<project>/requirements/vision.md
    O: knowledge/10_projects/<project>/requirements/outcomes.md
    C: knowledge/10_projects/<project>/requirements/capabilities/
    F: knowledge/10_projects/<project>/requirements/features/
    E: knowledge/10_projects/<project>/requirements/evals/
    S: knowledge/10_projects/<project>/requirements/engineering/
---

# Grill Session: <project> / <layers>

---

## State

- turns: 0
- progress_stalled_turns: 0
- last_saved: YYYY-MM-DDTHH:MM:SSZ
- next_action: "Bootstrap → Q-INIT-1 を聞く"
- mode: NEW | RESUME | REVIEW | WRITEOUT_ONLY
- web_gate_suppressed_layers: []
- web_gate_refusal_count: {}

---

## Layer Progress

- V: { answered: 0/8, ready_to_writeout: false, writeout_done: false }
- O: { answered: 0/8, ready_to_writeout: false, writeout_done: false }
- C: { answered: 0/8, ready_to_writeout: false, writeout_done: false, items: [] }
- F: { answered: 0/8, ready_to_writeout: false, writeout_done: false, items: [] }
- E: { answered: 0/8, ready_to_writeout: false, writeout_done: false, items: [] }
- S: { answered: 0/8, ready_to_writeout: false, writeout_done: false }

---

## Open Questions

<!-- open_questions が空になったら Summary へ進む -->
- [V-1] このシステムが解く「誰の・何の痛み」は？
- [V-2] 3年後、このシステムがあるのとないのでは何が違いますか？
- [V-3] 競合・既存解決策ではなく我々がやる必然性は？
- [V-4] 絶対に目指さない方向は？（Non-goals）
- [V-5] 中心に置くステークホルダーは誰ですか？
- [V-6] このシステムが最初に狙う適用範囲・車種・市場は？
- [V-7] 成功したとき関係者が言う1文は？（North Star Quote）
- [V-8] このビジョンを1文で言うと？（one_line_thesis）

---

## QA Log

<!-- 1問1ターン。回答をここに追記する。ラベル: [U] [I: 根拠] [A] [X] [W: source] -->

### V-1: ...
- Q: このシステムが解く「誰の・何の痛み」は？
- recommended: （10_projects/<project>/design-notes/ から引用 or デフォルト）
- answer: （ユーザーの回答）
- label: [U]
- at: YYYY-MM-DDTHH:MM:SSZ

---

## Decisions (Resolved)

<!-- 複数問の回答から導いた確定事項 -->

---

## Conflicts

<!-- 矛盾を検知したときに記録 -->

---

## Writeouts

<!-- WriteoutGate 通過後にここへ記録 -->
<!-- - V -> knowledge/10_projects/<project>/requirements/vision.md (written at YYYY-MM-DDTHH:MM:SSZ) -->

---

## Web Searches

<!-- grill 中に実行した Web 検索のログ -->

---

## Notes

<!-- 自由メモ。層違反で飛んできたアイデア・次回確認事項など -->
