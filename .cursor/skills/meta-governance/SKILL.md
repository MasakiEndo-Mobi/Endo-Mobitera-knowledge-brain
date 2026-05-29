---
name: meta-governance
description: >
  プロジェクトのガバナンス層（AGENTS.md / hooks / skills / CI）を変更するとき、
  ハーネスエンジニアリング手法に基づいて設計・実装・整合性検証・マージまでを一貫して行う。
  Use when: 「ガバナンスを変更したい」「ルールを追加・更新したい」「フックを修正したい」
  「スキルを追加したい」「CI チェックを追加したい」「AGENTS.md を更新したい」
  「ハーネスエンジニアリング的に〜」など、プロジェクトの meta 層（.cursor/ / .github/）に
  変更を加えるときはすべてこのスキルを使う。
---

# meta-governance スキル — ガバナンス層の変更と進化

## いつ使うか

| ユーザーの指示 | このスキルが対応 |
|---|---|
| 「ハーネスを改善して」 | rules / hooks / skills を更新 |
| 「新しいスキルを追加したい」 | skill-factory と連携してスキルを設計・追加 |
| 「フックの挙動を変えたい」 | pre-commit / validators を更新 |
| 「CI チェックを強化したい」 | validate.yml / validators を更新 |
| 「AGENTS.md を更新したい」 | 変更影響範囲を棚卸しした上で編集 |
| 「Obsidian の設定を変えたい」 | .obsidian/ を更新 |

## 使わないケース

- KB への知識取り込み → `kb-intake`
- スキル単体の改善 → `skill-improve-loop`

---

## ガバナンス対象ファイル一覧

| レイヤー | ファイル | 役割 |
|---|---|---|
| 行動ガバナンス | `.githooks/pre-commit` | コミット前検査 |
| ゴールデンパス | `.cursor/skills/*/SKILL.md` | スキル定義 |
| ゴールデンパス | `AGENTS.md` | エージェント永続指示 |
| ゴールデンパス | `.github/copilot-instructions.md` | Copilot 用補足 |
| 出力ガバナンス | `.github/workflows/validate.yml` | CI 検証 |
| 出力ガバナンス | `tools/validate_frontmatter.py` | フロントマター検証 |
| 出力ガバナンス | `tools/validate_integrity.py` | 整合性検証 |
| 出力ガバナンス | `tools/check_obsidian_links.py` | wikilink 切れ検証 |
| 補助 | `.gitignore` | バイナリ誤コミット防止 |
| 補助 | `.obsidian/` | Obsidian Vault 設定 |

---

## Step 1: 現行ガバナンス棚卸し

```
ls .cursor/skills/        # スキル一覧
cat .githooks/pre-commit  # フック内容
ls .github/workflows/     # CI workflow 一覧
ls tools/                 # validator 一覧
```

棚卸し結果を提示:

```
【現行ガバナンス棚卸し】

■ 行動ガバナンス（pre-commit hook）
  - .githooks/pre-commit: validators + skill同期

■ ゴールデンパス（skills / AGENTS.md）
  - スキル一覧: [一覧]
  - AGENTS.md: 全体構造 / スキル一覧 / バイナリポリシー / ops ガードレール
  - copilot-instructions.md: Copilot 用補足

■ 出力ガバナンス（CI）
  - validate.yml: frontmatter + integrity + wikilink チェック
```

---

## Step 2: 変更計画の策定

ユーザーの要望から以下の3層に沿って変更を分類:

| 変更レイヤー | 対象 | 変更内容 |
|---|---|---|
| 行動ガバナンス | hooks | [追加/修正/削除するフック] |
| ゴールデンパス | skills / AGENTS.md | [追加/修正するルール・スキル] |
| 出力ガバナンス | CI / validators | [追加/修正するチェック] |

### 影響範囲の確認

- AGENTS.md を変更 → スキルの description と整合するか
- 新しいスキルを追加 → AGENTS.md のスキル一覧テーブルに追記が必要
- copilot-instructions.md との重複・矛盾がないか

### Pre-Flight Check（新規スキル追加時）

新規スキル追加を計画する場合、以下4項目をユーザーに提示し承認を得る:

| # | 項目 | チェック内容 |
|---|---|---|
| 1 | **DRY** | 既存スキル（kb-intake / kb-output 等）の内部分岐として実装できないか |
| 2 | **責任分界** | 既存スキルでカバーできない独立した動詞・領域があるか |
| 3 | **発火条件** | 自然言語の言い換え 3〜5 件で起動できるか |
| 4 | **テスト** | 回帰ケース（正例 3 + 負例 2）が用意されているか |

通過しない場合は既存スキルの内部分岐として実装するか、提案を撤回する。

---

## Step 3: 変更実行

実装順序:
1. **行動ガバナンス（hooks）** — 影響が小さく早い
2. **ゴールデンパス（skills / AGENTS.md）** — 実行規則の変更
3. **出力ガバナンス（CI / validators）** — 検証・監視の強化

### 各レイヤーの実装指針

#### 行動ガバナンス（hooks）
- pre-commit は失敗時に明確な原因と対処を出力する
- Windows/Linux 両対応（bash で書く、git for windows 同梱の bash を使用）

#### ゴールデンパス（skills）
- 新スキルは `skill-factory` の手順に従って設計する
- 既存スキル改善は `skill-improve-loop` の手順に従う
- スキル追加時は必ず AGENTS.md のスキル一覧テーブルを更新
- `.cursor/skills/<name>/` が実体、`.claude/skills/<name>` はシンボリックリンク（setup.ps1 で再生成）

#### 出力ガバナンス（CI）
- Python スクリプトは Python 3.12 を前提
- `ERROR` は exit code 1、`WARN` は exit code 0

---

## Step 4: 整合性検証

```bash
# Python スクリプトの構文確認
python -m py_compile tools/validate_frontmatter.py
python -m py_compile tools/validate_integrity.py
python -m py_compile tools/check_obsidian_links.py

# AGENTS.md のスキル一覧とディレクトリの整合
ls .cursor/skills/ | sort

# CI YAML 構文確認（python -c で yaml.safe_load）
python -c "import yaml; yaml.safe_load(open('.github/workflows/validate.yml'))"
```

### 意味的整合性チェックリスト

- [ ] AGENTS.md のスキル一覧テーブルに新スキルが追記されているか
- [ ] copilot-instructions.md と AGENTS.md が矛盾していないか
- [ ] hooks の検査パターンが AGENTS.md のルールと一致しているか
- [ ] schema_reference.md と validator の必須フィールドが一致しているか

---

## Step 5: Git ワークフロー

```bash
# 1. 現状確認
git status
git pull origin main

# 2. meta/ ブランチ作成
git checkout -b meta/<slug>

# 3. 変更ファイルをステージ
git add .cursor/skills/<変更ファイル>
git add AGENTS.md
git add .github/

# 4. コミット
git commit -m "meta: [変更内容の要約]"

# 5. プッシュ + PR（個人運用ならローカルマージで可）
```

---

## 出力契約

このスキルは以下を必ず返す:

1. **棚卸し結果**: 現行ガバナンス構成の一覧
2. **変更計画**: 対象ファイル / 変更内容（ユーザー確認後に実行）
3. **整合性検証結果**: 各チェック項目の合否
4. **コミット提案**: ブランチ名・コミットメッセージ
