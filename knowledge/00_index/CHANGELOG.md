# KB Changelog

このファイルは KB の変更履歴を集約する。kb-intake / kb-output などのスキルが自動追記する。

---

## 2026-05-29

### Added — kb-intake 一括取り込み（OJT報告アウトライン・825Dコンテキスト総括・OJTレビュー議事録）
- `knowledge/80_sandbox/ideas/2026-04-24_ojt-4q-final-report-outline.md` (`sandbox.ojt-4q-final-report-outline`): 2年目OJT最終報告(4/24)のアウトライン。IPONC×825D×効率化の三本柱で1年を総括した成果物（議論プロセスログ込み）。佐藤レビュー議事録に depends_on。
- `knowledge/10_projects/24CY_IVI_825D/meetings/2026-04-16_ojt-4q-report-review.md` (`ops.meeting.2026-04-16-ojt-4q-report-review`): 佐藤さんとのOJT4Q発表資料レビュー。21分→15分圧縮・825D実開発を主軸にAI/組織課題は控えめにする方針合意。↑アウトラインの佐藤フィードバックの出典。

### Compiled — OJTレビュー議事録から decision×2 / task×3 を抽出（compile-meeting）
議事録 `ops.meeting.2026-04-16-ojt-4q-report-review` を `status: compiled` 化。4/24報告実施済のため遠藤タスクは `done`。
- `ops.decision.24cy-ivi-825d.presentation-time-format` (DEC-0001): OJT4Q発表を15分枠に圧縮（decided）
- `ops.decision.24cy-ivi-825d.ojt-focus-on-825d` (DEC-0002): OJT主題を825D実開発に置く（decided）
- `ops.task.24cy-ivi-825d.compress-ojt-slides` (TASK-0001): 資料を15分枠に圧縮・825D主軸へ再構成（done）
- `ops.task.24cy-ivi-825d.share-review-with-sato` (TASK-0002): 佐藤さんへレビュー共有・桐生さんCC追加（done）
- `ops.task.24cy-ivi-825d.ai-dx-separate-track` (TASK-0003): AI/DXを別枠で関係者へ種まき（proposed・佐藤担当）

### Added — ツール仕様（SPO Tool Box）
- `knowledge/50_research/spo-path-converter.md` (`res.tooling.spo-path-converter`): SharePointパス変換君の確定仕様（C#/.NET4.7）。クリップボードのSP/Teamsリンクを階層フォルダリンクに変換。raw版 `source.methods.r-tool-spo-tool-box(-2)` を canonical 整理。

### Note — 認証情報は KB 管理外（git除外 `secrets/`）
Eiger(Markforged) パスワード・LiteLLM(社内AIゲートウェイ) APIキー等は `secrets/credentials.md`（`.gitignore` 済・git履歴に入らない）で一括管理し、`knowledge/` には転記しない方針を確認。

### Added — AI/DX イネーブルメント プロジェクト新設（meta-governance）
横断テーマ「AI活用による業務効率化」を独立プロジェクト化（ローカルLLM＋クラウドAI: GitHub Copilot/NotebookLM/M365 Copilot 等）。
- `knowledge/10_projects/ai-dx-enablement/` skeleton 作成（最小構成: meetings/daily-logs/decisions/tasks/requirements/assets。design-notes/test-reports は省略）
- `ops.project.ai-dx-enablement`（README, status: active, phase: discovery, owner: self）
- `ops.meeting.2026-04-24-local-llm-hearing`: 80_sandbox/research/ から `ai-dx-enablement/meetings/` へ移動・`project: [all]→[ai-dx-enablement]`・仮格納バナー除去
- `ops.meeting.2026-05-27-ai-agent-efficiency`: 5/27 AIエージェント業務効率化お喋り場（高畠主催・20名）を新規格納
- **AGENTS.md / research_map.md** のアクティブプロジェクト表に `24CY_IVI_825D`（従来未登録）と `ai-dx-enablement` を登録
- LiteLLM APIキーは `secrets/`（git管理外）で管理し本議事録には記載しない方針
- `knowledge/10_projects/24CY_IVI_825D/design-notes/project-context.md` (`proj.24cy-ivi-825d.design.project-context`): 825Dプロジェクト・コンテキスト総括（背景・体制・進捗・課題・日程・体制メンバー表）。`status: review`。HTMLタイムライン→MD変換・重複貼付け除去・壊れリンク(Viva Engage)修正済。体制メンバー表は overview より新しい体制更新（水野→トヨタPE異動・北川PE復帰）を含み、突合が必要。

### Added — 旧KB(from_old_kb)取り込み 第1波（計画: `sandbox.old-kb-intake-plan`）
すべて `layer: raw`（L0/L1/L2・再リンクは後工程に遅延）。本文中の wikilink・画像埋め込み記法はテキスト無害化済み。

- **TOYOTA用語・プロセス (9)** → `30_standards/internal/`: `std.internal.toyota-term-{dr,rddp,gaisetsushin,shikyu,kanri-jikyu,development-phase,21cy-part-number,24cy-naiki}`, `std.internal.ivi-development-process`
- **サプライヤ (5)** → `40_suppliers/`: `supp.markforged.overview`, `supp.umi.overview`, `supp.hoshiden.bonding-fd`, `supp.nakanuma.art-screen`, `supp.fasotec.ai-design-survey`
- **技術リサーチ (30)** → `50_research/`: DRBFM 6種(`res.drbfm.*`)・3Dプリンター/Onyx/PEEK 各種(`res.3d-printing.*`)・ガラス(`res.glass.*`)・塗装/加飾(`res.coating.*`)・照明(`res.lighting.*`)・電気(`res.electrical.*`)・CFRTP/材料・分散製造・当たり図DR・Teams議事録ガイド ほか
- **825D 議事録 (9)** → `10_projects/24CY_IVI_825D/meetings/`: `ops.meeting.2025-07-17`〜`2025-12-11` の DR/DRBFM/DRB/HiddenSW/1SDR ほか
- **825D 設計メモ (6)** → `10_projects/24CY_IVI_825D/design-notes/`: `proj.24cy-ivi-825d.design.{825d-overview,dr0-issues-summary,lcd-warping-issue-history,analysis-request,anti-scatter-film-dexerials,anti-scatter-film-vendor-study}`
- **バイナリ保全 (16)** → 各 `assets/`（英語名にサニタイズ、再埋め込みは未実施）: 825D 概要画像2・開発フェーズ図1・24CY内機仕様PDF1・Onyx平滑化図12

### Added — 旧KB取り込み 第2波・第3波（`90_sources/raw/` へ raw ダンプ）
スコープ=業務関連のみ。全て `doc_type: source` / `layer: raw` / `project: [all]`。title に原ファイル名を保持。slug・one_line_thesis は自動抽出。

- **月次業務レポート 14** → `90_sources/raw/old-kb-monthly-reports/` (`source.monthlyreports.*`): 2025-04〜2026-03
- **業務ノート・学習 19** → `90_sources/raw/old-kb-work-notes/` (`source.worknotes.*`): 業務確認/日報まとめ/VC展示会/DRB抵抗感/業績目標/2年目研修/AI勉強会/OJT 等
- **手法・プロンプト資産 24** → `90_sources/raw/old-kb-methods/` (`source.methods.*`): 議事録プロンプト各種/業務改善(Lean Six Sigma等)/Obsidian/Zettelkasten/SPO Tool Box/VTT2MD 等
- **終了案件 20** → `90_sources/raw/old-kb-projects/` (`source.projects.*`): 21CY(220D/450D/900B)・24CY非現役(310D/400D/410D/695D696D/744D/838D/867D)・IPONC・組立手順書

### 取り込み対象外（from_old_kb に残置）
個人領域・機密・雛形のため除外: キャリア開発6・A-Career2・第一生命保険・Udemy学習・リクルータマイページ要件・GEMINI_API_Key・GEMINI.md・P-IVI_template

### Changed — 825D 設計メモ 6点を canonical 昇格
`layer: raw → canonical` / `status: review`（AI生成L0/L1/L2のため人手レビュー待ち）。L0/L1/L2＋relations 付与、825d-overview は画像を `assets/` へ再リンク。

- `proj.24cy-ivi-825d.design.825d-overview`（→ project / 220D / 解析依頼に relations）
- `proj.24cy-ivi-825d.design.dr0-issues-summary`（→ DR0議事録×2 / DRBFM概論）
- `proj.24cy-ivi-825d.design.lcd-warping-issue-history`（→ ホシデンFD / project）
- `proj.24cy-ivi-825d.design.analysis-request`（→ 概要 / ガラス強度評価）
- `proj.24cy-ivi-825d.design.anti-scatter-film-dexerials`（↔ メーカー検討）
- `proj.24cy-ivi-825d.design.anti-scatter-film-vendor-study`（↔ デクセリアルズ情報）

### Changed — 再リンク・バイナリ完全保全・from_old_kb 削除
- **バイナリ完全保全**: 旧KBの全25点を KB 内 `assets/` へ退避（残り9点は `90_sources/raw/old-kb-assets/`）。
- **画像再リンク**: 全 `(旧KB埋め込み: …)` マーカー（19種）→ `assets/` への markdown 画像/PDFリンクに変換。
- **wikilink 再リンク**: 各 doc の原本から二重角括弧リンクを再導出し、移行先 doc に解決するものを 119ファイルで復元（解決不能な旧リンクはプレーンテキスト維持＝切れリンク0）。検証: wikilinks 1260 / broken 0。
- **`source_docs` 除去**: 削除した from_old_kb を指す死参照 136件を除去（provenance は git 履歴・本CHANGELOGに残存）。
- **`from_old_kb/` 削除**: 移行完了につき削除。取り込み対象外の個人領域ファイルは KB 非格納のため完全消去（git 未追跡で履歴にも残らない）。

### Changed — 825D canonical 6点 人手レビュー反映（ENDO, `review → canonical`）
ENDO レビューにより事実を更新し全6点を `status: canonical` に確定:
- **825d-overview**: 搭載車種=Lexus TX 確定、仕向け=北米(米・加)、顧客担当を現:藤本様（前任 櫻井/田中/津田より交代）に更新、目標欄 LX 誤記を TX に修正
- **dr0-issues-summary**: DR0 は 2025-10 実施済み・指摘は全て解消済み（クローズ）
- **lcd-warping-issue-history**: 825D（ミネベアミツミ）では反り未発生・確認済み／788D は調査継続・天馬液晶ウォッチ要
- **analysis-request**: 依頼解析（インパネ衝撃含む）は全て完了済み
- **anti-scatter-film-dexerials**: 採用可否は 10月目途のトヨタ CV インパネ衝撃試験次第
- **anti-scatter-film-vendor-study**: フィルムは Dexerials 決定(0.5mmオフセット)、400D評価が全OK・825Dは400D評価で使用可否判断

### Changed — raw source slug 改名 ＋ 825D 車両データハブ化
- **slug 改名 (14件)**: 純日本語名由来の簡素 slug を意味的名称へ。`r→prompt-samples`、`r-2→biz-improve-monthly-report-prompt`、`r-3→biz-improvement-overview`、`r-4→biz-improvement-howto`、`r-5→internal-systems-links`、`a→mech-design-biz-improvement`、`a-2→second-year-training`、`a-learning→coach-a-suzuki-seminar`、`a-work→performance-goal-report`、`a-work-2→mizuno-handling-manual`、`p-24cy→p-24cy-assembly-procedure`、`p-iponc→p-iponc-ichihara-statements`、`p-iponc-3→p-iponc-3rd-slide-draft`、`p-iponc-16→p-iponc-case16-analysis`。doc_id・参照 wikilink を24ファイルで追従更新。
- **825D 車両データハブ**: `proj.24cy-ivi-825d.design.825d-overview` を「825D 車両データハブ」に再構成（`role: routing`）。車両データ（基本/HW/担当/生産/関連機種）＋主要サプライヤ＋マイルストーンに加え、全825Dドキュメント（設計メモ6・議事録9・関連知見）への**ドキュメントマップ**を追加。

### 未完了（後工程）
- raw source（90_sources）の必要分の canonical 昇格（現状は raw アーカイブ）

---

## 2026-05-28

### Added
- Initial scaffold from `vehicle-mech-kb-starter` zip package
- `index.schema-reference` — フロントマタースキーマ完全仕様
- `index.research-map` — 全体ナビゲーション
- `index.glossary` — 用語集
- `moc_components` / `moc_projects` / `moc_tasks` — Dataview ベース MOC
