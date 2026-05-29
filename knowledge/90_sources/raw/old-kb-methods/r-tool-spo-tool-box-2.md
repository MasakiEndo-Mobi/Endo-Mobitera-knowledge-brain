---
doc_id: source.methods.r-tool-spo-tool-box-2
title: "R-Tool_SPO_Tool_Box_マニュアル"
doc_type: source
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2026-03-04
audience: [self]
one_line_thesis: "🔗 SPO Tool Box"
confidence: low
---

# 🔗 SPO Tool Box

**SharePoint Online リンク操作ツール**

SharePoint Online の URL を **ワンキーで** パス変換・コピー・フォルダ表示できる、  
Windows タスクトレイ常駐アプリケーションです。

---

## ✨ できること

| # | 機能 | デフォルトキー | 説明 |
|---|------|:---:|------|
| 1 | **パス変換** | `Ctrl+Alt+P` | クリップボード上の SPO URL を「ファイル名＋パンくず＋リンク」の案内文形式リッチテキストに変換してコピー。複数URLの自動一括変換にも対応 |
| 2 | **フォルダを開く** | `Ctrl+Alt+O` | クリップボード上の SPO URL から親フォルダをブラウザで開く |
| 3 | **パスコピー** | `Ctrl+Alt+C` | URL をデコードした読みやすいパス文字列としてコピー |
| 4 | **ファイル名コピー** | `Ctrl+Alt+N` | URL からファイル名だけを抽出してコピー |
| 5 | **直リンク生成** | `Ctrl+Alt+D` | 共有リンク等のクエリパラメータを除去したクリーンな URL をコピー |
| 6 | **サイトトップ** | `Ctrl+Alt+T` | URL からサイトのトップページをブラウザで開く |
| 7 | **Excel用コピー** | `Ctrl+Alt+E` | ファイル名・フォルダパス・URLの3要素をタブ区切りでコピー。Excel台帳入力用 |
| 8 | **QRコード生成** | `Ctrl+Alt+Q` | URLのQRコード画像を生成してクリップボードにコピー |

> **🌟 リンク種別インジケーター搭載**: すべての機能実行時、対象URLが「共有リンク」や「OneDrive個人領域」の場合、トースト通知に⚠️アイコンと警告メッセージが自動表示され、セキュリティ意識の向上を助けます。

> [!TIP]
> すべての機能は **クリップボードに SPO の URL があること** が前提です。  
> SharePoint のブラウザ上でファイルやフォルダの URL をコピーしてからホットキーを押してください。

---

## 🚀 インストール・起動

### 必要環境

- Windows 10 / 11
- .NET 9 ランタイム（自己完結型ビルドの場合は不要）

### ビルド方法

```powershell
cd SPOToolBox
dotnet build
```

### 実行ファイルとして配布する場合

```powershell
dotnet publish -r win-x64 --self-contained -p:PublishSingleFile=true
```

### 起動

`SPOToolBox.exe` を実行すると、タスクトレイに **SP** アイコンが表示されます。

> 多重起動は防止されています。既に起動中の場合はメッセージが表示されます。

---

## 🖱️ 使い方

### 基本の流れ

```
1. SharePoint Online のブラウザ上で、ファイルやフォルダの URL をコピー
2. ホットキーを押す（または、トレイアイコンを右クリック → 機能を選択）
3. 結果がクリップボードに書き込まれ、通知バルーンに結果が表示される
```

### トレイアイコンのメニュー

タスクトレイの **SP** アイコンを **右クリック** すると、以下のメニューが表示されます：

| メニュー項目 | 説明 |
|---|---|
| パス変換 (Ctrl+Alt+P) | ホットキーと同じ機能をメニューから実行 |
| フォルダを開く (Ctrl+Alt+O) | 〃 |
| パスコピー (Ctrl+Alt+C) | 〃 |
| ファイル名コピー (Ctrl+Alt+N) | 〃 |
| 直リンク生成 (Ctrl+Alt+D) | 〃 |
| サイトトップ (Ctrl+Alt+T) | 〃 |
| Excel用コピー (Ctrl+Alt+E) | 〃 |
| QRコード生成 (Ctrl+Alt+Q) | 〃 |
| **設定…** | 設定画面を開く |
| **終了** | アプリを終了する |

---

## ⚙️ 設定

トレイアイコンの右クリックメニューから **「設定…」** を選ぶと、設定画面が開きます。

### 基本設定

| 項目 | 説明 | デフォルト値 |
|---|---|---|
| **SharePoint ベースURL** | お使いの SharePoint Online のルートURL | `https://jppanasonic.sharepoint.com/` |
| **通知の表示時間** | バルーン通知の表示時間（1〜30秒） | 3 秒 |
| **Windows 起動時に自動で常駐する** | Windows ログオン時に自動起動 | ✅ 有効 |

### ホットキー設定

各機能のショートカットキーをカスタマイズできます。

- **有効/無効** : チェックボックスで各ホットキーの有効・無効を切り替え
- **キー変更** : テキスト欄をクリック → お好みのキーの組み合わせを入力

> [!IMPORTANT]
> 設定変更後は **「💾 保存して再起動」** ボタンを押してください。  
> ホットキーの反映にはアプリの再起動が必要です。

---

## 🔍 各機能の詳細

### 1. パス変換 ── `Ctrl+Alt+P`

SPO の URL を「ファイル名＋パンくず＋リンク」の案内文形式に変換します。

**入力例（クリップボード）：**
```
https://example.sharepoint.com/sites/TeamSite/Shared%20Documents/Reports/2024/report.xlsx
```

**出力（リッチテキスト）：**
```
📄 <b>report.xlsx</b>
[ TeamSite > Shared Documents > Reports > 2024 ]
リンクを開く
```

各セグメントにはリンクが付き、メールや Teams に貼り付けると相手が直接ファイルやフォルダにアクセスしやすくなります。

> **複数URLの一括変換にも対応！**
> クリップボードに改行区切りのSPO URLが複数存在する場合、同じ `Ctrl+Alt+P` キーで自動的にリスト形式に一括変換します。

---

### 2. フォルダを開く ── `Ctrl+Alt+O`

URL の親フォルダをブラウザで直接開きます。  
ファイルそのものではなく、そのファイルが置かれている **フォルダ** に移動したい場合に便利です。

---

### 3. パスコピー ── `Ctrl+Alt+C`

URL を **デコード済みの読みやすいパス** としてクリップボードにコピーします。

**例：**
```
TeamSite/Shared Documents/Reports/2024/report.xlsx
```

---

### 4. ファイル名コピー ── `Ctrl+Alt+N`

URL から **ファイル名のみ** を抽出してコピーします。

**例：**
```
report.xlsx
```

---

### 5. 直リンク生成 ── `Ctrl+Alt+D`

共有リンク等に付加されるクエリパラメータ（`?e=xxxxx` 等）や OneDrive プレフィックスを除去し、  
**クリーンな直リンク URL** を生成してコピーします。

---

### 6. サイトトップ ── `Ctrl+Alt+T`

URL からサイト名を抽出し、そのサイトの **トップページ** をブラウザで開きます。

---

### 7. Excel用タブ区切りコピー ── `Ctrl+Alt+E`

URLから「ファイル名」「フォルダパス」「URL」を抽出し、**タブ区切り（TSV）形式**でクリップボードにコピーします。

**出力例：**
```
report.xlsx [TAB] TeamSite/Shared Documents/Reports/2024 [TAB] https://example...
```

Excelのセルを選択して貼り付けるだけで、自動的に3列に展開されます。ファイル台帳の更新作業に最適です。

---

### 8. QRコード生成 ── `Ctrl+Alt+Q`

SPO URLの **QRコード画像** を生成し、クリップボードに格納します。
PowerPoint等の資料に直接 `Ctrl+V` で貼り付けることができ、モバイルデバイスからのアクセス動線を簡単に作成できます。

---

## 📁 設定ファイル

設定は `settings.json` ファイルに保存されます。  
場所は `SPOToolBox.exe` と同じフォルダです。

通常は設定画面から変更しますが、直接編集も可能です：

```json
{
  "SharePointBaseUrl": "https://example.sharepoint.com/",
  "NotificationDurationMs": 3000,
  "StartWithWindows": true,
  "Hotkeys": {
    "PathConvert": { "KeyCombo": "Ctrl+Alt+P", "Enabled": true },
    "FolderOpen":  { "KeyCombo": "Ctrl+Alt+O", "Enabled": true },
    "PathCopy":    { "KeyCombo": "Ctrl+Alt+C", "Enabled": true },
    "FileNameCopy":{ "KeyCombo": "Ctrl+Alt+N", "Enabled": true },
    "DirectLink":  { "KeyCombo": "Ctrl+Alt+D", "Enabled": true },
    "SiteTop":     { "KeyCombo": "Ctrl+Alt+T", "Enabled": true },
    "ExcelCopy":   { "KeyCombo": "Ctrl+Alt+E", "Enabled": true },
    "QRCode":      { "KeyCombo": "Ctrl+Alt+Q", "Enabled": true }
  }
}
```

---

## ❓ トラブルシューティング

| 症状 | 対処法 |
|---|---|
| ホットキーが反応しない | 他のアプリとショートカットが競合していないか確認。設定画面で別のキーに変更してみてください |
| 「クリップボードにSharePointファイルパスがありません」と表示される | クリップボードに正しい SPO URL がコピーされているか確認してください |
| アプリが起動しない | 「既に起動しています」メッセージが出る場合、タスクマネージャーで既存の SPOToolBox プロセスを終了してください |
| 通知が表示されない | Windows の通知設定で SPO Tool Box の通知が許可されているか確認してください |

---

## 📝 ログ

アプリケーションのログは以下の場所に出力されます：

```
%LOCALAPPDATA%\SPOToolBox\app.log
```

ログファイルは **1MB** を超えると自動でローテーション（`app.log.old` にバックアップ）されます。  
問題が発生した場合は、ログファイルの内容を確認してください。

---

## 🛠️ 開発情報

| 項目 | 内容 |
|---|---|
| フレームワーク | .NET 9 (Windows Forms) |
| 言語 | C# |
| ターゲット | `net9.0-windows` |
| ソリューション | `SPOToolBox.sln` |

---

<p align="center">
  <b>SPO Tool Box</b> — SharePoint をもっと快適に 🚀
</p>

---
### 関連ノート
- [[p-iponc-20250123-report|P-IPONC_20250123_Report]]
- R-GEMINI_API_Key
- [[r-tool-spo-tool-box|R-Tool_SPO_Tool_Box_フィードバック]]
- [[r-tool-vtt2md-requirements|R-Tool_VTT2MD_requirements]]
