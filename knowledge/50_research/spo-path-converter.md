---
doc_id: res.tooling.spo-path-converter
title: SharePointパス変換君（SPO Tool Box）仕様
doc_type: research
project: [all]
layer: canonical
role_in_story: insight
status: canonical
as_of: 2026-05-29
audience: [self, engineer]
one_line_thesis: クリップボード上のSharePoint/Teamsファイルリンクを、ルート→ファイルの階層フォルダリンク群に変換してTeams/Outlookに貼れる形で書き戻す、遠藤製C#(.NET 4.7)社内ツール。
confidence: high
tags: [tooling, productivity, sharepoint, teams, csharp]
relations:
  related: [source.methods.r-tool-spo-tool-box, source.methods.r-tool-spo-tool-box-2, sandbox.ojt-4q-final-report-outline]
key_questions:
  - 共有リンクからファイルの「場所」を相手に直感的に伝えるには？
  - 通常版と短縮版の出力をどう使い分けるか？
  - Outlook貼り付け時の文字化け/抜けをどう解消するか？
source_docs:
  - knowledge/90_sources/raw/old-kb-methods/r-tool-spo-tool-box.md
  - knowledge/90_sources/raw/old-kb-methods/r-tool-spo-tool-box-2.md
---

# SharePointパス変換君（SPO Tool Box）仕様

## L0（1文要約）

**クリップボードにコピーされたSharePoint/Teamsのファイルリンクを、ルートから当該ファイルまでの親フォルダ階層リンク群に変換してクリップボードへ書き戻し、Teams/Outlookに貼って「場所」を直感的に伝えられるようにする遠藤製C#(.NET Framework 4.7)社内ユーティリティ。**

---

## L1（5つの要点）

- **コア機能**: クリップボードのSharePoint/Teamsリンクを読み取り → 階層リンク付きテキストに変換 → クリップボードへ上書き。
- **入出力**: 入力＝コピー済み共有リンク／出力＝Teams・Outlookでリッチテキスト/HTML解釈される階層リンクテキスト。
- **2モード**: 通常版（ルート→ファイルの全親フォルダを階層表示）と短縮版（`-s`/`--short`：一つ上のフォルダのみ）。
- **動作環境**: Windows 10以降 / Microsoft .NET Framework 4.7。
- **既知の不具合**: クリップボードロック時にまれに書込失敗。Outlook貼り付けは開発中で文字化け/抜けの可能性あり。社内利用想定・動作保証対象外。

---

## L2（詳細・根拠・構造）

### 概要
SharePointまたはMicrosoft Teamsで共有されたファイルリンクを、そのファイルが格納されているフォルダ階層を示すリンク群に変換するユーティリティ。変換後のリンクをTeamsチャットやOutlookメールに貼り付けることで、ファイルの場所を直感的に伝えられる。OJT4Q報告（[[2026-04-24_ojt-4q-final-report-outline|OJTアウトライン]]）でも業務効率化ツールとして言及。

### 機能仕様

#### コア機能
実行すると、クリップボードにコピーされているSharePoint/Teamsのファイルリンクを読み取り、階層リンクを含むテキストに変換して結果をクリップボードに上書きする。

- **入力**: クリップボードにコピーされた、SharePoint/Teams上のファイル/フォルダへの共有リンク。
- **出力**: 変換された階層リンク情報を含むテキスト（クリップボードに格納）。Teams/Outlookメールでリッチテキスト/HTMLとして解釈される形式。

#### 出力形式（2モード切替・コマンドライン引数）

| モード | 引数 | 挙動 | 例 |
|---|---|---|---|
| 通常版（デフォルト） | なし | ファイルへのリンク＋ルートから当該ファイルまでの全親フォルダリンクを階層表示 | `[ルート > フォルダA > フォルダB > ファイル.xlsx]` |
| 短縮版 | `-s` / `--short` | ファイルへのリンク＋一つ上のフォルダのリンクのみを省略表示 | `[... > ファイル.xlsx]` |

### 動作環境
- **OS**: Windows 10 以降
- **フレームワーク**: Microsoft .NET Framework 4.7

### 使い方
1. SharePoint/Teamsで対象ファイル/フォルダの「リンクをコピー」する。
2. コマンドプロンプト/PowerShell/バッチ等から `SharePointパス変換君.exe` を実行。
   - 通常版: `SharePointパス変換君.exe`
   - 短縮版: `SharePointパス変換君.exe -s`
3. Teamsチャット/Outlookメール作成画面で貼り付け（Ctrl+V）。
   - **注意**: Outlookメールではリッチテキスト形式またはHTML形式を選択する必要がある。

### 注意事項・既知の不具合
- 社内利用想定であり動作保証の対象外。
- 実行時に他ツールがクリップボードをロックしていると、まれに書込みに失敗しエラー表示。
- Outlookメールへの貼り付け機能は開発中で、文字化けやテキスト抜けが発生することがある。

### （参考）関連ツール
- **SharePointフォルダ開く君**: 兄弟ツール。Teamsチャットに貼られたファイルリンクから、その親フォルダを直接ブラウザ(Edge)で開く。
