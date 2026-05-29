---
name: skill-factory
description: Create a reusable skill for Cursor or Claude Code from a repeated workflow, existing rules, slash commands, or a manual playbook. Use when the task recurs, has stable acceptance criteria, and benefits from a reusable procedure. Do NOT use for one-off feature work or always-on repository conventions better handled by rules or AGENTS.md.
---

# Skill Factory

あなたは **Skill を作る専門家** として動作する。
目標は、単発の上手い会話を再現することではなく、**繰り返し使える Skill として再利用可能な形** に落とし込むこと。

## まず守る原則

1. **最初に 1 件の難しい実例を勝たせる**
   - いきなり汎化しすぎない
   - まず 1 件の代表的で難しいケースを end-to-end で成功させ、その勝ち筋を Skill に抽出する

2. **Skill の責務を狭く切る**
   - 何をする Skill か / 何をしない Skill か
   - どんな入力で起動すべきか / どんな入力では起動してはいけないか
   を明示する

3. **SKILL.md には中核だけを書く**
   - 長い背景知識、チェックリスト、例外対応、出力例は `references/` や `templates/` に逃がす
   - `SKILL.md` は「目的 / 発火条件 / 実行手順 / 出力契約」に集中させる

4. **命令は具体的・行動可能に書く**
   - 悪い例: 「丁寧に確認する」
   - 良い例: 「関連する skills, AGENTS.md, docs を確認し、競合する指示を列挙する」

5. **失敗時の扱いを書く**
   - 情報不足 / 競合するルール / 適切なテストがない / 依存資料がない などの時にどう縮退するか

## この Skill がやること

ユーザーから作りたい Skill の要件を受けたら、以下の順序で進める。

### Phase 1. 既存資産の監査

- 既存の `.cursor/skills/`
- `AGENTS.md`
- `tools/`, `.githooks/`

監査の目的:
1. 既に似た Skill / Rule がないか
2. 常時ルール向きか、Skill 向きか
3. Skill に埋め込むべき repo 固有知識は何か

### Phase 2. Skill 境界の定義

次の 6 項目を必ず決める:

1. **Skill 名**（kebab-case、役割が一目でわかる）
2. **発火条件**（ユーザーが実際に言いそうな表現で）
3. **非発火条件**（似ているが別 Skill に寄せるべきケース）
4. **入出力契約**
5. **成功条件**
6. **失敗時の縮退**

### Phase 3. Skill 実装

最低でも以下を作る:

- `.cursor/skills/<skill-name>/SKILL.md`
- 必要なら `references/` 配下の補助ファイル
- 必要なら `templates/` 配下のテンプレート

`SKILL.md` には次を含める:

1. 目的
2. 使うべき場面
3. 使うべきでない場面
4. 実行手順
5. 出力形式
6. 失敗時の扱い

### Phase 4. 初期評価設計

新しい Skill を作ったら、同時に簡易回帰パックも作る:

- 正例 5 件
- 言い換え正例 5 件
- 負例 5 件
- 境界例 3 件
- 期待する出力の要点

`skill-regression-pack` スキルを使うとよい。

### Phase 5. 自己レビュー

- 説明が汎用的すぎないか
- 正例と言い換えに反応しそうか
- 無関係な依頼に誤爆しそうでないか
- `SKILL.md` が長すぎないか
- 長文知識を `references/` に切り出したか
- 失敗時の戻り値が曖昧でないか

### Phase 6. AGENTS.md への登録

新スキルは AGENTS.md §8 のスキル一覧テーブルに追記する。

## 出力ルール

返答では必ず以下をまとめる:

1. 作成した Skill 名
2. 追加・変更したファイル一覧
3. 発火条件の要約
4. 非発火条件の要約
5. 最初に回すべき回帰ケース 3〜5 件

## 禁止事項

- 何でも屋の巨大 Skill を作らない
- repo の常時ルールを無理に Skill 化しない
- 具体的な発火表現なしで description を書かない
- 例外処理を書かずに「よしなに判断」で逃げない

## 迷った時の判断

- **常に効くべき制約** → AGENTS.md 向き
- **特定状況で呼ばれる手順** → Skill 向き
- **1 回限りの作業** → 会話で十分、Skill 化しない
