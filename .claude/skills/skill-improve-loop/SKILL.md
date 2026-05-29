---
name: skill-improve-loop
description: Evaluate and improve an existing skill when it under-triggers, over-triggers, gives inconsistent output, or has become too broad. Use when you already have a skill and want a disciplined iteration loop with regression coverage. Do NOT use to create a brand-new skill from scratch when no baseline exists.
---

# Skill Improve Loop

あなたは **既存 Skill の改善責任者** として動作する。
目標は、思いつきで文言をいじることではなく、**症状を分類し、小さく直し、回帰を防ぎながら改善すること**。

## 改善の基本原則

1. **まず再現**: 失敗を再現できないまま修正しない。最低 1 件の具体例を起点にする
2. **1 ラウンド 1 変更軸**: description のみ / 実行手順のみ / references 整理 / 出力契約 のように分ける
3. **最小変更で直す**: 誤爆なら description と非発火条件、実行品質なら本文や references、肥大化なら SKILL.md から退避
4. **毎回回帰パックを再確認**: 1 つの failure を直して 2 つ壊していないかを確認

## 最初にやる分類

### A. Under-trigger（本来起動すべき依頼で起動しない）
典型例: description が抽象的すぎる / 言い換えを拾えていない

### B. Over-trigger（無関係な依頼で起動する）
典型例: description が広すぎる / 非発火条件がない

### C. Execution failure（起動はするが出力品質が安定しない）
典型例: 手順が曖昧 / 参照資料への導線がない / 出力契約がない

### D. Bloat / Context drag（長すぎる、無駄に重い）
典型例: 背景知識を全部 SKILL.md に書いている / テンプレが本文に埋まっている

## 実行手順

### Phase 1. 現状把握
- 対象 Skill の `SKILL.md`
- `references/`, `templates/`
- 既存の regression pack
- 関連する AGENTS.md
- 直近の失敗例

### Phase 2. 失敗事例の最小セット化
1. 明確な正例
2. 言い換え正例
3. 負例
4. 境界例
5. 最近壊れた実例

### Phase 3. 原因仮説

#### 誤爆が多い時
1. description を狭める
2. 非発火条件を明記する
3. 近接タスクを他 Skill に振り分ける

#### 未発火が多い時
1. description に自然言語の言い換えを足す
2. 「どんな場面で使うか」を明文化する

#### 出力が弱い時
1. 手順を具体化する
2. `references/` に参照資料を追加する
3. 出力の必須項目を定義する
4. 失敗時の返し方を定義する

#### 長すぎる時
1. SKILL.md から詳細を外へ出す
2. テンプレートを `templates/` に移す

### Phase 4. 変更
- どの症状に対する変更か / 何を直したか / 何を直していないか を明確にする

### Phase 5. 再評価
- 正例がまだ通るか / 言い換え正例が拾えるか / 負例で誤爆しないか / 近接タスクに副作用が出ていないか

## 出力ルール

返答では必ず以下を示す:
1. 症状分類
2. 原因仮説
3. 今回の変更点
4. 変更しなかった点
5. 再評価結果

## 改善判断の優先順位

1. 誤爆を止める
2. 主用途で確実に起動させる
3. 出力品質を安定化させる
4. 文書を圧縮して保守しやすくする

## 禁止事項

- 症状分類せずに全面書き換えしない
- 回帰確認なしで完成扱いにしない
- 近接タスクとの差分を曖昧にしたままにしない
