# Vehicle Mechanical Design — Personal Knowledge Brain (Starter Kit)

車載電子機器機構設計のための個人用ナレッジベース・スタータキット。
Obsidian Vault + Git + Claude Code / GitHub Copilot 両対応のエージェント連携基盤。

---

## クイックスタート

### 1. リポジトリを初期化

```powershell
cd path\to\vehicle-mech-kb-starter

# Git 初期化
git init
git add .
git commit -m "meta: initial commit from starter kit"

# Git hooks を有効化
git config core.hooksPath .githooks
```

### 2. Python 環境 (conda)

```powershell
conda create -n vehkb-env python=3.12 -y
conda activate vehkb-env
pip install -r tools/requirements.txt
```

### 3. setup スクリプトの実行（symlink 復元）

zip 展開直後は `.claude/skills/` のシンボリックリンクが切れているため、setup スクリプトで貼り直す：

```powershell
# Windows
.\tools\setup.ps1

# macOS / Linux
bash tools/setup.sh
```

### 4. Obsidian で開く

1. Obsidian を起動
2. "Open folder as vault" でこのディレクトリを選択
3. Settings → Community plugins → Browse から以下をインストール：
   - **Templater** (`templater-obsidian`)
   - **Dataview** (`dataview`)
4. Settings → Templater → Template folder location を `.obsidian/templates` に設定
5. Settings → Dataview → JavaScript Queries を有効化（任意）

### 5. 最初のプロジェクトを作る

```powershell
# テンプレートをコピー
Copy-Item -Recurse knowledge/10_projects/_template knowledge/10_projects/ev-truck-2027

# README.md と project スラッグを書き換えてプロジェクト定義を完成
```

または Claude Code で：

```
kb-intake で「ev-truck-2027」プロジェクトを作って
```

---

## ディレクトリ構造

```
.
├─ AGENTS.md                     ← 正本指示書（必読）
├─ CLAUDE.md                     ← @AGENTS.md (1行)
├─ .github/
│  ├─ copilot-instructions.md    ← Copilot 用補足
│  └─ workflows/validate.yml     ← 軽量CI
├─ .vscode/                      ← VS Code 推奨設定
├─ .githooks/pre-commit          ← ローカル検証フック
├─ .obsidian/                    ← Obsidian Vault 設定 + Templater テンプレ
├─ .cursor/skills/               ← スキル実体（自前12 + vendored 4 = 16個）
├─ .claude/skills/               ← `.cursor/skills/` への symlink
├─ tools/                        ← Python validator + setup script
└─ knowledge/                    ← KB 本体
   ├─ 00_index/                  ← schema / glossary / research_map / MOC
   ├─ 10_projects/               ← プロジェクト中心型（meetings/daily-logs/design-notes/...）
   ├─ 20_components/             ← 部品カテゴリ横断知見
   ├─ 30_standards/              ← 規格・社内基準
   ├─ 40_suppliers/              ← サプライヤー情報
   ├─ 50_research/               ← 技術リサーチ要約
   ├─ 80_sandbox/                ← 個人 raw 層
   └─ 90_sources/                ← 外部 raw
```

詳細は [AGENTS.md](AGENTS.md) を参照。

---

## エージェントとの主な使い方

### Claude Code

```
# 議事録を構造化して取り込む
kb-intake で 2026-05-28_thermal-review.md を取り込んで

# 日報を書く
daily-log で ev-truck-2027 の今日の日報を書きたい

# 設計検討の壁打ち
kb-output で connector の熱設計について壁打ちしたい

# 議事録から decision/task を抽出
compile-meeting で最新の議事録をコンパイルして
```

### GitHub Copilot Chat

- AGENTS.md と `.github/copilot-instructions.md` を会話冒頭で参照させる
- Claude Code 専用スキル（kb-intake 等）は Copilot からは直接起動できないので、AGENTS.md のルールに沿った手作業で対応するか「Claude Code で実行して」と案内する

### Obsidian ネイティブ

- Templater の Insert Template から各種ひな型を呼び出して新規 doc を作る
- `knowledge/00_index/moc_*.md` の Dataview ブロックでプロジェクトやタスクを集計閲覧

---

## 検証

```powershell
conda activate vehkb-env

# フロントマター必須項目チェック
python tools/validate_frontmatter.py knowledge/

# relations 参照切れ + doc_id 重複チェック
python tools/validate_integrity.py knowledge/

# wikilink 切れチェック
python tools/check_obsidian_links.py knowledge/
```

pre-commit フックで上記3つが自動実行される（`git config core.hooksPath .githooks` を実行済みなら）。

---

## ライセンス / 機密

完全個人運用前提。社外秘ガードレールは未組み込み（必要なら後付けで `private/` ディレクトリ + `.gitignore` を導入する）。

---

## 構造を変えたいとき

`meta-governance` スキルを使ってください。AGENTS.md / hooks / rules / skills / CI の整合を保ちつつ変更します。

```
meta-governance で 20_components に新カテゴリ "wire-harness" を追加したい
```
