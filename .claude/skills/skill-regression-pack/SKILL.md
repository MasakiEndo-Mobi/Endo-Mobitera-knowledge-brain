---
name: skill-regression-pack
description: Create or refresh a regression pack for a skill, including positive triggers, paraphrases, negative cases, boundary cases, and recently broken examples. Use when you need disciplined QA for skill changes. Do NOT use as a substitute for actually improving the target skill.
---

# Skill Regression Pack

あなたは **Skill 用の回帰パック設計者** として動作する。
目標は、Skill の修正を再現可能な形で検証できるようにし、改善ループを「勘」ではなく「比較」で回せるようにすること。

## 基本方針

1. **正例だけでは不十分** — 負例と境界例を含める
2. **自然な言い換えを入れる** — paraphrase 群を別枠で持つ
3. **最近壊れたケースを最優先で入れる**
4. **期待値を曖昧にしない** — 何が見えれば pass か / 何が出たら fail か明示する

## 作成手順

### 1. 対象 Skill の役割を一文で定義

- この Skill は何のための Skill か
- どんな依頼で起動すべきか
- どんな依頼では起動してはいけないか

### 2. ケースを 5 種類に分ける

- Positive: 5 件以上
- Paraphrase Positive: 5 件以上
- Negative: 5 件以上
- Boundary: 3 件以上
- Recently Broken: 2 件以上

### 3. 各ケースに 4 要素を持たせる

1. Prompt
2. なぜ trigger / non-trigger なのか
3. 期待する挙動
4. 期待する証拠

### 4. 失敗指紋を残す

次の観点で失敗指紋を残す:

- 起動しない
- 誤爆する
- 出力が浅い
- 余計な手順を踏む
- 関連資料を見ない
- SKILL.md の肥大化を助長する

### 5. リリース判定欄を付ける

- 今回 pass か
- 既知の未解決は何か
- 次の改善仮説は何か

## 出力ルール

返答では以下を必ず出す:

1. 作成・更新した regression pack の場所
2. 正例 / 負例 / 境界例の件数
3. 最優先で見る failure fingerprint
4. 次に `skill-improve-loop` へ渡すべき改善仮説

## 保存先

回帰パックは以下のいずれかに保存:
- `.cursor/skills/<name>/regression-pack.md`（推奨）
- `tools/tests/skill-<name>-regression.md`

## 禁止事項

- 正例だけでパックを作らない
- failure evidence を曖昧にしない
- 最近壊れた事例を外さない
- 改善仮説なしでテストだけ並べない
