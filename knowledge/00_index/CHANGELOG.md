# KB Changelog

このファイルは KB の変更履歴を集約する。kb-intake / kb-output などのスキルが自動追記する。

---

## 2026-05-29

### Added — 旧KB(from_old_kb)取り込み 第1波（計画: `sandbox.old-kb-intake-plan`）
すべて `layer: raw`（L0/L1/L2・再リンクは後工程に遅延）。本文中の wikilink・画像埋め込み記法はテキスト無害化済み。

- **TOYOTA用語・プロセス (9)** → `30_standards/internal/`: `std.internal.toyota-term-{dr,rddp,gaisetsushin,shikyu,kanri-jikyu,development-phase,21cy-part-number,24cy-naiki}`, `std.internal.ivi-development-process`
- **サプライヤ (5)** → `40_suppliers/`: `supp.markforged.overview`, `supp.umi.overview`, `supp.hoshiden.bonding-fd`, `supp.nakanuma.art-screen`, `supp.fasotec.ai-design-survey`
- **技術リサーチ (30)** → `50_research/`: DRBFM 6種(`res.drbfm.*`)・3Dプリンター/Onyx/PEEK 各種(`res.3d-printing.*`)・ガラス(`res.glass.*`)・塗装/加飾(`res.coating.*`)・照明(`res.lighting.*`)・電気(`res.electrical.*`)・CFRTP/材料・分散製造・当たり図DR・Teams議事録ガイド ほか
- **825D 議事録 (9)** → `10_projects/24CY_IVI_825D/meetings/`: `ops.meeting.2025-07-17`〜`2025-12-11` の DR/DRBFM/DRB/HiddenSW/1SDR ほか
- **825D 設計メモ (6)** → `10_projects/24CY_IVI_825D/design-notes/`: `proj.24cy-ivi-825d.design.{825d-overview,dr0-issues-summary,lcd-warping-issue-history,analysis-request,anti-scatter-film-dexerials,anti-scatter-film-vendor-study}`
- **バイナリ保全 (16)** → 各 `assets/`（英語名にサニタイズ、再埋め込みは未実施）: 825D 概要画像2・開発フェーズ図1・24CY内機仕様PDF1・Onyx平滑化図12

### 未完了（後工程）
- L0/L1/L2 への canonical 昇格（現役825D優先）
- wikilink・画像埋め込みの再リンク（`obsidian-link`）
- 第2波（月次レポート等）・第3波（終了案件ダンプ）

---

## 2026-05-28

### Added
- Initial scaffold from `vehicle-mech-kb-starter` zip package
- `index.schema-reference` — フロントマタースキーマ完全仕様
- `index.research-map` — 全体ナビゲーション
- `index.glossary` — 用語集
- `moc_components` / `moc_projects` / `moc_tasks` — Dataview ベース MOC
