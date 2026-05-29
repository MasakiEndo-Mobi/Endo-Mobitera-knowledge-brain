---
doc_id: sandbox.old-kb-intake-plan
title: "旧KB(from_old_kb)取り込み計画書"
doc_type: idea
project: [all]
layer: raw
role_in_story: proposal
status: draft
as_of: 2026-05-29
audience: [self]
one_line_thesis: "旧KB150ファイルを『参照頻度×陳腐化耐性』で3波に層別し、第1波(用語集9+825D15+技術30/サプライヤ5)をkb-intakeで先行取り込み、終了案件はraw履歴ダンプ、個人系は業務関連のみ、L0/L1/L2正本化は遅延昇格する。"
confidence: medium
relations:
  related: [sandbox.old-kb-intake-plan-discussion]
tags: [migration, intake, from-old-kb, planning]
---

# 旧KB(from_old_kb)取り込み計画書

> 本計画は議論ログ [[2026-05-29_old-kb-intake-plan-discussion-log]]（`sandbox.old-kb-intake-discussion`）を踏まえ、ユーザー確定事項を反映した実行計画。

## 0. 確定した方針（ユーザー判断）

| 論点 | 決定 |
|---|---|
| スコープ境界 | **業務関連のみ取り込む**。学習/OJT/業務改善は対象。副業戦略・保険プラン・純個人キャリアは**対象外**（from_old_kbに残置） |
| 第1波の範囲 | **用語集 ＋ 825D ＋ 主要技術/サプライヤ** |
| 終了案件 | **raw層に履歴ダンプ**（`90_sources/raw/`） |
| 今回の到達点 | 本計画書の作成まで（実取り込みは別途） |

## 1. 素材の現状

- 総量：150 Markdown ＋ 画像24点 ＋ PDF1点（計175ファイル）
- 構造：PARA（`01_Projects` / `02_Areas` / `03_Resources`）
- 旧フロントマター：`type / status / priority / tags / created`（軽量、現行の `doc_id`＋11必須＋L0/L1/L2 と非互換）

## 2. 取り込みの3原則（議論で確立）

1. **Triage Before Transfer**：一律処理しない。「参照頻度 × 陳腐化耐性」で層別し波ごとに方式を変える。
2. **Index Now, Polish Later**：raw層を緩衝材に検索可能性を先に付与し、L0/L1/L2正本化は使う時に遅延昇格。
3. **Automate the Mechanical, Judge the Semantic**：フロントマター機械変換・画像移送は一括、doc_id採番/layer判定/要約は人の判断、要約は昇格対象に限定。

## 3. 波別の対象・方式・格納先

### 🔴 第1波（先行取り込み・今回の主対象）

| カテゴリ | 件数 | 旧パス例 | 方式 | 格納先 |
|---|---|---|---|---|
| TOYOTA用語集＋開発プロセス | 9 | `R-TOYOTA_用語_DR/RDDP/外設申/支給/管理自給/開発フェーズ/品番体系/24CY内機`、`R-Process_IVI開発プロセスガイド` | B（raw取り込み） | `30_standards/internal/` |
| 825D 関連 | 15＋画像 | `P-24CY_825D*`（LCD反り経緯・飛散防止フィルム・DRBFM review・解析依頼書・各議事録） | B→C（現役分は昇格） | `10_projects/24cy-ivi-825d/` 配下（meetings/design-notes/test-reports等に振り分け） |
| 主要技術調査 | 30 | `R-技術_DRBFM_*`、`R-技術_3Dプリンター*`、`R-Tech_cfrtp_*`、`R-Tech_ガラス強度`、`R-技術_透過加飾` 等 | B（raw取り込み） | `50_research/`（部品横断知見は `20_components/`） |
| サプライヤ | 5 | `R-サプライヤ_Markforged/UMI/ホシデンFD/中沼アートスクリーン/ファソテック` | B（raw取り込み） | `40_suppliers/` |

第1波合計 ≈ **59ファイル ＋ 825D画像群**。

### 🟡 第2波（後日・任意）

| カテゴリ | 件数 | 方式 | 格納先 |
|---|---|---|---|
| 月次業務レポート（2025/04〜2026/03） | 14 | B | `10_projects/24cy-ivi-825d/daily-logs/` 相当 or Areas相当（要決定） |
| 業務関連の学習/OJT/業務改善 | 数件 | B | `50_research/` or 適切なAreas相当 |
| プロンプト/ツール資料（R-Prompt_*, R-Tool_*, R-Copilot_*） | 数件 | B | `00_index/` or `30_standards/internal/`（運用資産として） |

### 🟢 第3波（履歴ダンプ）

| カテゴリ | 件数 | 方式 | 格納先 |
|---|---|---|---|
| 終了/非現役案件（21CY系・他24CY・IPONC等） | 21 | A（一括ダンプ） | `90_sources/raw/old-kb-projects/` |

### ⚪ 対象外（from_old_kbに残置）

- 副業戦略（`A-Career_副業戦略`）、保険プラン（`A-第一生命_保険プラン`）、純個人キャリアメモ、GEMINI APIキー等の機密 → KBスコープ外。取り込まない。

## 4. スキーマ変換の3層分担

| 層 | 内容 | 自動化 | 担当 |
|---|---|---|---|
| 機械層 | `type→doc_type`、`created→as_of`、tags引き継ぎ、画像→assets移送＋リネーム | 一括（kb-intake/スクリプト） | 自動 |
| 判断層 | doc_id採番、`project`割当、`layer` raw/canonical判定、`role_in_story` | 選別と同時に1件ずつ | 人/AI |
| 創作層 | `one_line_thesis`、`confidence`、L0/L1/L2要約 | 昇格対象のみ | 人/AI（中身を読んで） |

## 5. 実行手順（明日からの具体アクション）

1. **第1波素材を一時隔離**：用語集9 ＋ 825D15 ＋ 技術30/サプライヤ5 を抽出（≈59＋画像）。
2. **第1波を `kb-intake` にカテゴリ単位で投入**：種別判定 → 格納先確認ゲート → raw取り込み。doc_id・必須フロントマターを付与。
3. **825D 現役分のみ canonical 昇格**：L0/L1/L2＋relations を付け `10_projects/24cy-ivi-825d/` 配下へ振り分け。
4. **画像/PDFのバイナリ規約適用**：各 `assets/` 配下へ、英語ケバブケースにリネーム、画像埋め込みリンクの張り替え。
5. **第3波（終了案件21）を `90_sources/raw/` にダンプ**：最小処理で履歴保全。
6. **リンク整合 → 検証**：`obsidian-link` で wikilink/relations の切れを掃除 → 3バリデータ（frontmatter/integrity/obsidian-links）を通す。

## 6. 注意点・リスク

- **wikilink破壊**：旧来のタイトル参照型 wikilink（二重角括弧でページ名を囲む形式）と現行 doc_id 体系の差で一括変換時に最も壊れる。第1波は無理に張り替えず、リンク整合は後工程（`obsidian-link`）に分離。
- **画像リンク**：旧来の画像埋め込み記法（感嘆符＋二重角括弧、日本語/スペース名）→ 現行は assets/ 強制＋英語ケバブケース。リネームとリンク張り替えが地味に必要。
- **月次レポートのLoop長大URL**：本文URLなので validator 対象外（問題なし）。
- **825Dのプロジェクトslug**：現行の `10_projects/` に 825D ディレクトリが既存か未作成かを実行前に確認（未登録ならテンプレートからスケルトン作成）。
- **機密情報**：`R-GEMINI_API_Key` はKBに取り込まない（対象外確定）。

## 7. 未決事項（実行フェーズで確定）

- [ ] 月次レポートの格納先：`daily-logs/` 相当 か `Areas` 相当か（現行KBにAreas層が無いため要設計）
- [ ] 用語集の格納先：`30_standards/internal/` か `00_index/`（横断参照される基盤資産としての位置づけ）
- [ ] 825D の既存プロジェクトslug（`24cy-ivi-825d` 等）と現行ディレクトリの整合
