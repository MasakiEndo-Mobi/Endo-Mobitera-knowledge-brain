# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

---

> 上の `@AGENTS.md` がこのリポジトリの正本指示書（構造・フロントマター規約・スキル・ops ガードレール）。
> 以下はそれを補う **開発オペレーションと検証ハーネスの実務メモ**。AGENTS.md と重複する内容は書かない。

## このリポジトリの性質

「コードベース」ではなく **Obsidian Vault（個人ナレッジベース）**。成果物の本体は `knowledge/` 配下の**構造化 Markdown**であり、`tools/` の Python は「その Markdown を検証する lint/CI」に相当する。ビルドもアプリ実行も無い。「テストを通す」＝**3つのバリデータを通す**ことを意味する。

## 検証コマンド（= build / lint / test 相当）

```bash
# 3バリデータ（pre-commit と CI が走らせるのと同じもの）
python tools/validate_frontmatter.py knowledge/   # 必須フロントマター・enum・L0/L1/L2 構造
python tools/validate_integrity.py knowledge/     # relations 参照切れ・doc_id 重複
python tools/check_obsidian_links.py knowledge/   # [[wikilink]] 切れ
```

- 引数はディレクトリ。**サブディレクトリを渡せばスコープを絞れる**（例: `python tools/validate_frontmatter.py knowledge/00_index/`）。変更箇所だけ素早く回したいときに有効。
- `ERROR` は exit 1（コミット阻止）、`WARN` は exit 0。
- **pre-commit フック**（`.githooks/pre-commit`）が staged な `knowledge/**/*.md` 変更時に上記3つを自動実行。有効化は `git config core.hooksPath .githooks`（未設定だとフックが走らない）。
- **CI**（`.github/workflows/validate.yml`）は `main` への push / PR で同じ3つを実行。

### Python 環境（実態に注意）

README/AGENTS.md は `conda activate vehkb-env`（Python 3.12）を指示するが、**本マシンに conda は未導入**。実運用は **`.venv/`（Python 3.13.5）+ PyYAML**。バリデータは `python` が PATH にあれば直接動く。依存は `tools/requirements.txt`（PyYAML のみ）。

## 検証ハーネスの構造（big-picture）

3バリデータは `tools/parse_frontmatter.py` の共通パーサ（`iter_md_files` / `parse_frontmatter`）を土台に分業する:

| バリデータ | 何を守るか | 知っておくべき点 |
|---|---|---|
| `validate_frontmatter.py` | 必須フィールド・各 enum・canonical の L0/L1/L2 | **enum の実体はこのファイルが正**（後述） |
| `validate_integrity.py` | `relations.*` の doc_id が実在するか・doc_id 一意性 | HTML は doc_id を持たない前提 |
| `check_obsidian_links.py` | 本文 `[[wikilink]]` の解決可否 | frontmatter の relations は検査対象外 |

### 非自明な落とし穴: enum の正本は validator であって schema ではない

`knowledge/00_index/schema_reference.md` は**人間向けドキュメント**で、`validate_frontmatter.py` の `STATUS_BY_TYPE` / `DOC_TYPE_ENUM` / `*_ENUM` が**実際にコミットを止める判定**。両者はドリフトし得る（過去に `requirement` の status enum で実際にドリフトが起きた）。**両者が食い違ったら validator が勝つ**。フロントマター値を足す前に validator の enum を確認し、schema を変えるときは validator も同時に直す（このタイプの変更は `meta-governance` スキルで行う）。

- doc_type ごとに専用 status を持つものがある（`STATUS_BY_TYPE`）。未登録の doc_type は `DEFAULT_STATUS_ENUM = {draft, review, canonical, archived}` にフォールバック。
- `L012_EXEMPT_TYPES`（meeting/daily-log/index/project/decision/task/grill_session）は L0/L1/L2 構造を免除される。

## スキルの物理構造

スキル実体は **`.cursor/skills/<name>/SKILL.md`**、`.claude/skills/<name>` はそこへの**シンボリックリンク**。リンクが切れたら `tools/setup.ps1`（Windows）/ `tools/setup.sh`（mac/Linux）で貼り直す。スキルを追加・改名したら AGENTS.md のスキル一覧テーブルも更新する（`meta-governance` が面倒を見る）。

ユーザーが覚えるべき入口は2つ（AGENTS.md §8）: **`kb-intake`**（取り込み全般）と **`kb-output`**（アウトプット全般）。他スキルは直接指定も可能。

## 要件管理（6層）と grill セッション

`requirements-grill` が Vision→Outcome→Capability→Feature→Eval→EngSpec を1問ずつ詰めて書き出す。セッション状態は `knowledge/80_sandbox/grill-sessions/<date>_<project>-<layer>.md` に永続化され、別チャットから resume できる。要件 doc は `doc_type: requirement` ＋ `requirement_level` ＋ `stability`。

> 適用範囲が特定プロジェクトでなく KB 全体に及ぶ場合、要件は `10_projects/<project>/requirements/` ではなく `00_index/`（`index.*` 系 doc_id, `project: [all]`）に置くことがある。書き出し先は grill の writeout gate で都度確定する。
