# QUESTIONS_F.md — Feature 層 定型問い

## この層の目的

「どんな体験／機能として切り出すか」を Feature 単位で定義する。
Capability に対する「今の実装ベット」。変わってよい層。
各 Feature は 1 ファイル（`FEAT-NNN_<slug>.md`）。

## 完了条件（Exit Criteria）

1 Feature につき全 8 問が回答済みで、ユーザーストーリーが 1 文で書けること。

## このあと進む層

Feature 完了 → Evals（E）で受け入れ基準を書く

## 書き出し先

`knowledge/10_projects/<project>/requirements/features/FEAT-NNN_<slug>.md`

---

## 定型問い一覧

### F-1: ステークホルダー（誰が使う）

**問い**: この feature を主に使う／影響を受けるのは誰ですか？

**推奨回答**: V-5 Primary Stakeholder の回答を引用。別なら新規定義

**車載機構の典型**:
- ライン作業者（組付け feature）
- 整備士（分解・交換 feature）
- 設計者（DR/FMEA feature）
- エンドユーザー（操作性 feature）

**escape hatch**: 「誰でも」→ 「最初に影響を受ける 1 人を想像してください」

---

### F-2: トリガー（When）

**問い**: ユーザーがこの feature に触れるのはどんな瞬間ですか？

**推奨フォーマット**: 「〔ステークホルダー〕が〔状況〕にあるとき」

**車載機構の例**:
- 「ライン作業者がコネクタを組付ける瞬間」
- 「整備士が車載 ECU を交換する瞬間」
- 「車両が振動環境を通過するとき」

**escape hatch**: 抽象的すぎる → 「具体的に何をしているとき？」

---

### F-3: 完了状態（Done When）

**問い**: この feature を使い終わったとき、ユーザー／システムはどんな状態になっていますか？

**推奨フォーマット**: 「〔ステークホルダー〕が〔できた・確認できた・完了した〕状態」

**escape hatch**: 「よくなった」→ 「具体的に何が変わりましたか？数値で？」

---

### F-4: 上位 Capability との紐付け

**問い**: この feature はどの Capability（C-N）の上に立ちますか？

**推奨**: C 層で定義した capability 一覧を表示して選んでもらう
「CAP-001: 〇〇できる ← これが対象ですか？」

**escape hatch**: 複数 → 「最も関係が深い 1 つは？」

---

### F-5: ユーザーストーリー

**問い**: この feature の 1 文ユーザーストーリーを作ります。

**形式**: 「As a [stakeholder], I want [goal], so that [benefit].」
または日本語: 「[ステークホルダー] として、[目的] のために、[行動] したい」

**推奨**: F-1 + F-2 + F-3 を組み合わせ

**escape hatch**: 「英語が難しい」→ 日本語可

---

### F-6: 受け入れ基準の核（3 つ）

**問い**: この feature が「完成した」と言えるための受け入れ基準を 3 つ挙げてください。
（詳細な EARS 記法は E 層で。今は要点だけ）

**車載機構の例**:
- 「-40〜+85℃ で気密維持できること」
- 「ISO 16750-3 振動試験で破損しないこと」
- 「組付け工数が現行比 20% 削減されること」

**escape hatch**: 3 つ出ない → 「最低限これができれば使えると言えるものは？」

---

### F-7: Out of Scope（境界）

**問い**: この feature が**含まない**もの・やらないことは何ですか？

**推奨**: 「-40℃ 未満の極低温環境は対象外」「水中浸漬は対象外」等

**Web Search Trigger**: 他社の類似 feature 範囲
- クエリ例: `"<競合製品> <feature category> spec range"`

**escape hatch**: 「特にない」→ 「F-4 の Capability より広い範囲に触れていませんか？」

---

### F-8: 実装フェーズ

**問い**: この feature はどのフェーズに入れますか？（concept / detailed / validation / production）

**推奨**: フェーズ未定義なら以下で仮置き:
- concept: アイデア検証段階
- detailed: 詳細設計・CAD/FEA
- validation: 試作・試験
- production: 量産準備・量産後

**escape hatch**: 「すべて concept」→ 「次のマイルストーンで何を出す？」

---

## Escape Hatch 共通ルール（F 層）

- Capability の話に戻る → 「Capability は確認済み」
- Engineering 実装に入る → 「それは S 層」
- Feature が大きすぎる → 「これは 1 機能で完結？複数に分けられる？」
