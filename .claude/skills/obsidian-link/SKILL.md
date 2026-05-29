---
name: obsidian-link
description: >
  doc_id ↔ [[wikilink]] の双方向変換、切れリンク検出、Graph 用 MOC ノード生成を行う。
  Obsidian Vault の relations / wikilinks 整合を保つメンテナンス系スキル。
  Use when: 「リンクを直して」「wikilink に変換して」「doc_id に変換して」
  「切れリンクを探して」「Graph に出ないドキュメントを接続して」「MOC を更新して」など。
---

# obsidian-link スキル — Vault リンク整合

Obsidian の `[[wikilink]]` と frontmatter の `doc_id` / `relations` を双方向に翻訳・整合させる。

## いつ使うか

| ユーザーの入力 | このスキルが対応 |
|---|---|
| 「リンクを直して」「切れリンクを探して」 | `check_obsidian_links.py` を実行して切れリンクを列挙 |
| 「`[[foo]]` を `doc_id` に変換して」 | 本文中の wikilink を `doc_id` 表記に書き換え |
| 「`doc_id` を `[[wikilink]]` に変換して」 | frontmatter の `relations` を本文 wikilink にプレビュー化 |
| 「MOC を更新して」 | `knowledge/00_index/moc_*.md` の Dataview クエリを点検・追加 |
| 「graph に孤立しているドキュメントを探して」 | relations / wikilink どちらも持たない doc を列挙 |

## 使うべきでない場面

- 新規ドキュメント作成 → `kb-intake`
- 関連を追加するアイデア出し → `knowledge-rally`
- スキーマ自体の変更 → `meta-governance`

---

## 実行手順

### モード判定

```
入力: ファイルパス + 「変換して」「直して」 → CONVERT / FIX モード
入力: 「切れリンクを探して」「監査」                → AUDIT モード
入力: 「MOC を更新して」                            → MOC_REFRESH モード
入力: 「孤立を探して」                              → ORPHAN モード
```

---

### AUDIT モード（切れリンク検出）

```bash
python tools/check_obsidian_links.py knowledge/
```

出力例:
```
BROKEN knowledge/10_projects/ev-truck-2027/design-notes/thermal-strategy.md: [[2026-05-15-thermal-review]]
BROKEN knowledge/20_components/connectors/usb-c-thermal.md: [[ops.decision.connector-supplier]]
...
broken: 2
```

切れリンクごとに「修正候補」を提示:

```
BROKEN: [[2026-05-15-thermal-review]]
  候補:
    1. [[2026-05-15_thermal-review]]      (basename 一致候補)
    2. [[ops.meeting.2026-05-15-thermal-review]] (doc_id 候補)
  対応:
    a) 修正案 1 を採用
    b) 修正案 2 を採用
    c) 該当 wikilink を削除
    d) スキップ
```

ユーザー承認後、Edit ツールで対象ファイルを更新。

---

### CONVERT / FIX モード（wikilink ↔ doc_id 変換）

#### wikilink → doc_id

対象ファイルを Read → 本文中の `[[X]]` を検出 → X が basename なら対応する doc_id を grep で取得 → relations 形式に格納提案

```yaml
# 提案
relations:
  related:
    - ops.meeting.2026-05-15-thermal-review
```

#### doc_id → wikilink

対象ファイルを Read → frontmatter `relations.*` の各 doc_id について、対応するファイルの basename を取得 → 本文末尾に「## 関連」セクションを追加（既存なら追記）

```markdown
## 関連

- [[2026-05-15_thermal-review]]
- [[connector-supplier-selection]]
```

---

### MOC_REFRESH モード

`knowledge/00_index/moc_*.md` を読み、Dataview クエリが現行スキーマと一致しているかを点検:

- `doc_type` enum の追加に対応しているか
- `status` enum の追加に対応しているか
- 新しく追加された `component_category` / `standard_ref` の値を補足

不一致があれば修正案を提示し、ユーザー承認後に更新。

---

### ORPHAN モード（孤立ドキュメント検出）

各 .md ファイルについて以下を確認:
1. その doc_id を `relations.*` で参照している他ドキュメントが 1 件以上あるか
2. その basename を `[[wikilink]]` で参照している本文が 1 件以上あるか

両方 0 のドキュメントを「孤立」として列挙:

```
ORPHAN knowledge/20_components/sealing/o-ring-material-survey.md
  - doc_id: comp.sealing.o-ring-material-survey
  - 参照元: 0 件
  - 候補アクション: 関連付け / 統合 / 削除 / sandbox 降格
```

ただし以下は孤立判定から除外:
- `00_index/` 配下（MOC・スキーマは参照されにくい）
- `status: archived` のドキュメント
- 直近 30 日以内に作成されたドキュメント（まだ未接続が普通）

---

## 出力契約

このスキルは以下を必ず返す:

1. 実行モード
2. 検出結果サマリー（件数）
3. ファイル別の変更プレビュー
4. ユーザー承認後の変更内容と次のアクション

---

## 禁止事項

- ユーザー承認なしに本文を書き換えない
- `relations.*` に存在しない doc_id を「予測」で追加しない（必ず grep で実在確認）
- HTML ファイル (`*.html`) を relations のターゲットにしない
- `assets/` 配下のファイルを wikilink ターゲットにしない
