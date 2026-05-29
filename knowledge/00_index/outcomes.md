---
doc_id: index.outcomes
title: Knowledge Brain Outcomes — 成功定義と北極星指標
doc_type: requirement
project: [all]
layer: canonical
role_in_story: execution
status: draft
as_of: 2026-05-29
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: KB＋AI 支援システムの成功は「思い出し作業ゼロ率」で測り、KB投入の継続と構造的健全性を先行指標として積み上げる
confidence: medium
requirement_level: outcome
stability: stable
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_24CY_IVI_825D-V-vision.md
tags: [outcomes, kpi, north-star, knowledge-base]
relations:
  depends_on: [index.vision]
  related: [index.research-map]
key_questions:
  - 「思い出し作業ゼロ率」のベースライン現状値はいくつか？（計測後に O-2 ターゲットを再設定）
  - セルフ申告の運用が形骸化しないための仕組みは？
---

## L0（1文要約）

**KB＋AI 支援システムの成功は単一指標「思い出し作業ゼロ率」で測り、KB 投入の継続（先行指標）と構造的健全性（切れリンク0・スキーマ適合100%）を土台に、月次面談・報告の準備負担をなくす状態を目指す。**

---

## L1（5つの要点）

- **North Star Metric**: **思い出し作業ゼロ率** — 月次面談・週次報告などで、過去を記憶から再構成せず KB の出力（日報集約・decision/task 履歴・成長差分）だけで臨めた割合。
- **Target**: 具体数値は未定（ベースライン計測後に設定）。**定性的に「現状から向上」**を当面のターゲットとする。
- **Floor（失敗ライン）**: ①KB 投入が **2週間以上途切れる**（定着失敗の兆候・最重要）②ゼロ率が現状を下回る（KB を使う方が遅い）③KB 出力の信頼性が崩壊し報告に使えない。いずれかで仕組み自体を見直す。
- **計測方法**: ゼロ率＝面談/報告直後の1問セルフ申告（KB だけで完結できた回数 ÷ 全報告回数、月次）／投入継続＝`daily-logs/`・`meetings/` の最新ファイル日付から自動判定（週次）／信頼性＝誤りに気づいた件数のセルフ申告。**計測自体が負担にならないことを優先**。
- **Leading / Lagging**: Leading（週次）＝KB 投入継続日数・投入→構造化（decision/task 抽出・relations 付与）の実施率。Lagging（月次〜四半期）＝思い出し作業ゼロ率・月次面談資料の作成リードタイム・部門間の情報手戻り件数。因果は「投入できている → 報告が楽になる」。

---

## L2（詳細）

### 詳細指標一覧

| 区分 | 指標 | 計測 | 頻度 |
|---|---|---|---|
| North Star (Lagging) | 思い出し作業ゼロ率 | 面談/報告直後セルフ申告（完結回数÷全回数） | 月次 |
| Lagging | 月次面談資料の作成リードタイム | 投入済みログ→提出可能資料までの所要時間 | 月次 |
| Lagging | 部門間の情報手戻り件数 | 齟齬による差し戻し回数のセルフ申告 | 月次 |
| Leading | KB 投入継続日数 | daily-logs/・meetings/ の最新ファイル日付から自動 | 週次 |
| Leading | 構造化実施率 | 投入ログのうち decision/task 抽出・relations 付与済みの割合 | 週次 |

### セグメント別の観点

初期は **全体値のみ**（825D パイロットに集中、分割の母数が小さい）。横展開フェーズで **プロジェクト別（825D / 410D …）** に分割。将来的に「面談（対上司）」と「部門連携報告（対製造 / PASA）」で分ける可能性を残す。

### 定性的成功シグナル

- 面談前の憂鬱（「また1から思い出して資料を作らなきゃ」）がなくなる
- 上司から「業務と成長が繋がって見える」と言われる（Vision の North Star Quote の実現）
- 部門連携で「言った言わない」が起きなくなる（経緯は KB を指せば済む）
- 後任・同僚に「これ見といて」で渡せる（暗黙知の外在化の実感）

### 運用健全性（KB 構造の規律）

手動管理 KB が破綻した過去ペインの再発防止指標:
- **切れリンク件数 = 0**（`tools/check_obsidian_links.py` / relations の doc_id 実在チェック）— 最重要
- **スキーマ適合率 = 100%**（canonical doc の必須フロントマター・L0/L1/L2 充足）— 最重要
- 未分類 inbox の滞留数（`80_sandbox/inbox/` に2週間以上居座るアイデア → 少ないほど良い）
- 孤立ノート率（relations も wikilink も持たない canonical doc の割合）

### 関連

- [[vision]] — 上位 Vision（index.vision）
- [[research_map]] — KB 全体マップ
