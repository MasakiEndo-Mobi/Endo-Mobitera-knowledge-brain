---
name: html-export
description: >
  ナレッジベース内の Markdown ドキュメントを、外部リソース依存ゼロの単一 HTML
  ファイルに変換出力する。ユーザーから明示指示があった場合のみ起動する。
  CSS / フォント / スクリプトを全てインライン化し、CSP メタで外部呼び出しを物理ブロックする。
  生成後は元 Markdown のフロントマターに `last_html_export: YYYY-MM-DD` を追記する。
  Use when the user says:
    「HTML で出力して」「HTML 化して」「これを HTML にして」「html-export」
    「シングルファイル HTML にして」「self-contained HTML」「読みやすい HTML で」
---

# html-export Skill

Markdown → 単一 HTML 変換を、テンプレート参照と検証フックの一連の流れとして提供する。

## いつ使うか

ユーザーが**特定の Markdown ファイルを HTML で出力したい**と明示したとき:

- 「`<path>.md` を HTML で出して」
- 「この要件、HTML 化して」
- 「シングルファイル HTML にして配布したい」
- 「読みやすい HTML で共有できる形にして」

**起動しないケース** (On Demand 原則):
- ユーザーが指示していないのに HTML を併走生成する
- 全 Markdown を一括 HTML 化する
- 自動・常時生成

## 前提条件

- プロジェクトルート `AGENTS.md` を読み済み
- 対象 Markdown が存在し、フロントマターを持つこと
- `tools/templates/html-export/template.html` が存在すること

## 実行ステップ

### Step 1: 入力の確定

ユーザーから次の3点を確認:

1. **対象 Markdown のパス**（必須）
2. **出力先**（規定: `<source_dir>/assets/<basename>.html`）
3. **生成意図**（review / 配布 / Slack 共有 等）

### Step 2: テンプレートと AI 指示を読み込む

`tools/templates/html-export/template.html` を読み、冒頭コメントの **AI INSTRUCTIONS** 7箇条を厳守:

1. **外部リソース禁止** — CDN / Google Fonts / `<link rel="stylesheet">` / `<script src>` を一切追加しない
2. **CSS 変数のみ** — body 内に生の hex / rgb 値を書かない
3. **callout 4種** — 重要情報は `<div class="callout {info|warn|danger|success}">` でラップ
4. **60 KB 上限** — 単一ファイルが 60 KB を超える場合はセクション分割
5. **構造保持** — `<header class="meta">` → `.lead` → `.l1-grid` → `<section class="l2">` の順序
6. **SVG インライン化、その他画像は `data:` URI**
7. **トーン** — clean / contemplative / trustworthy

### Step 3: HTML 本文を生成する

入力 Markdown の構造を写像:

| Markdown | HTML 出力 |
|---|---|
| フロントマター | `<header class="meta">` 内の `<dl>` + `.eyebrow` + `<h1>` + `.badge` |
| L0（1文要約） | `<p class="lead">` |
| L1（5要点） | `<ul class="l1-grid">` に `<li><b>キー名</b>説明</li>` を5つ |
| L2 セクション | `<section class="l2"><h2>...</h2>...</section>` を必要数 |
| 表 | `<table>` |
| 警告・補足・決定事項 | `<div class="callout info/warn/danger/success">` |
| コードブロック | `<pre><code>...</code></pre>` |
| 引用 | `<blockquote>` |

**L0/L1/L2 構造を持たない Markdown**（議事録・日報・thinking ノート等）:
- フロントマターの `one_line_thesis` を `.lead` に
- 主要セクションのトップを `<section class="l2">` に
- L1 グリッドは省略してよい

### Step 4: 出力先に保存

```
<source_dir>/assets/<basename>.html
```

例: `knowledge/10_projects/ev-truck-2027/meetings/2026-05-28_thermal-review.md`
  → `knowledge/10_projects/ev-truck-2027/meetings/assets/2026-05-28_thermal-review.html`

`assets/` ディレクトリが無ければ作成。

### Step 5: 検証（オプション）

正規表現で簡易検証:
- `<link rel="stylesheet"` / `<script src=` が含まれていない
- ファイルサイズ ≤ 60 KB
- CSP meta が含まれている

### Step 6: ソース Markdown のフロントマター更新

```yaml
last_html_export: <YYYY-MM-DD>
```

### Step 7: ユーザーへの報告

- 生成ファイルのパス
- 検証結果
- ファイルサイズ

---

## Graceful Degradation

| 失敗パターン | 縮退動作 |
|---|---|
| HTML 生成失敗 | 「Markdown のまま表示します」と宣言し、失敗理由を併記 |
| ファイル 60 KB 超過 | セクション分割し `<basename>-1.html` / `<basename>-2.html` … で複数出力 |
| 入力 Markdown のフロントマターが破損 | フロントマター修正を提案し、`last_html_export` 追記は保留 |

**原則**: HTML 生成失敗時は Markdown マスター原則を守り、ナレッジを壊さない。

---

## 禁止事項

- **並走自動生成**: ユーザー明示指示なしの HTML 生成
- **テンプレート無視のスタイル決定**: AI が独自配色・独自レイアウトを採用する
- **外部リソース引用**: 実 `<link>` `<script>` `<img src="https://...">` は不可
- **HTML を MD と同格に扱う**: relations / doc_type / status を HTML に付与しない
