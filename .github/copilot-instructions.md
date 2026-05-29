# Copilot Instructions

このリポジトリの正本指示書は [AGENTS.md](../AGENTS.md) です。**必ず先にそれを読んでください。**

このファイルは Copilot Chat / Inline Suggestions 向けの補足のみを記載します。

---

## このリポジトリは何か

車載電子機器の機構設計のための個人ナレッジベース。Obsidian Vault + Git。エージェントは Claude Code と GitHub Copilot の両対応。

主な書き物：
- 議事録 (`10_projects/<project>/meetings/`)
- 日報 (`10_projects/<project>/daily-logs/`)
- 設計検討メモ (`10_projects/<project>/design-notes/`)
- 試験レポート (`10_projects/<project>/test-reports/`)
- 部品横断知見 (`20_components/<category>/`)
- 規格情報 (`30_standards/<body>/`)

---

## Copilot Chat で守ること

1. **AGENTS.md のルールが最優先**。本ファイルと矛盾したら AGENTS.md に従う。
2. **新規ファイル作成前に Pre-Flight Check**（AGENTS.md §6）を実行。配置先・命名・フロントマター必須項目を確認。
3. **`doc_type: task / decision / project / meeting / daily-log` のファイルは本文を勝手に書き足さない**。フロントマター＋ユーザー提供素材のみ。
4. **バイナリ（.docx/.pdf/.png/.step 等）は必ず同階層の `assets/` に配置**。ルート直置き禁止。
5. **ファイル名は英語ケバブケース**。日本語・スペース・全角文字は使わない。

---

## Inline Suggestion で守ること

- Markdown フロントマターを書くときは [schema_reference](../knowledge/00_index/schema_reference.md) の必須フィールドを優先補完
- canonical ドキュメントを書くときは L0/L1/L2 の3層構造を提案
- ファイル内本文の関連参照は `[[wikilink]]` を提案、frontmatter の `relations:` には `doc_id` を提案

---

## スキル機能との関係

ユーザーが「kb-intake で取り込んで」「kb-output でまとめて」等と言ったら、それは Claude Code 側のスキル起動です。Copilot Chat 側からは直接スキルを起動できないため、対応する処理を `.cursor/skills/<name>/SKILL.md` を読んでから手作業で再現するか、ユーザーに「Claude Code で実行してください」と案内してください。

---

## コミットメッセージ

```
<type>: <内容の要約>

type: project | research | idea | design | test | meta | fix | docs
```

Co-authored-by 行や絵文字は使わないこと。
