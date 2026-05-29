# Vendored: kepano/obsidian-skills

このディレクトリ配下の以下スキルは外部リポジトリから取り込んだ（vendored）ものであり、
本プロジェクト独自のスキルではない。

- **出典**: https://github.com/kepano/obsidian-skills
- **作者**: Steph Ango (@kepano)
- **ライセンス**: MIT（同梱の `LICENSE` 参照）
- **取り込みコミット**: `553ef99aa3306dd23f268e1ba9af752577684f69`
- **取り込み日**: 2026-05-29

## 取り込んだスキル

| スキル | 役割 |
|---|---|
| `obsidian-markdown` | Obsidian Flavored Markdown（wikilink/callout/properties/embed） |
| `obsidian-bases` | Obsidian Bases（.base：DB ライクなビュー・フィルタ・数式） |
| `json-canvas` | JSON Canvas（.canvas：ノード/エッジ/グループ） |
| `obsidian-cli` | Obsidian CLI による Vault 操作・プラグイン開発 |

（`defuddle` は取り込み対象外）

## 注意

- これらは upstream のまま保持する。改変が必要な場合はこの NOTICE に差分を記録すること。
- 本プロジェクトのスキル改善ループ（`skill-improve-loop` 等）の対象外。upstream 追従は手動。
- `.cursor/skills/` と `.claude/skills/` の両ツリーに複製配置（core.symlinks=false のため既存スキルと同様）。
