# QUESTIONS_E.md — Eval 層 定型問い

## この層の目的

Capability / Feature の受け入れ基準を **EARS 記法** で形式化し、
試験条件・判定基準を「合格／不合格」が自動判定できる粒度で定義する。

## 完了条件（Exit Criteria）

ユビキタス要件 (U) が最低 1 つ、When/While/If の各パターンが最低 1 つ書けること。
試験方法と判定値が測定可能な形で定義されていること。

## このあと進む層

Evals 完了 → Engineering Spec（S）

## 書き出し先

`knowledge/10_projects/<project>/requirements/evals/<CAP|FEAT>-NNN_evals.md`
EARS 記法の詳細: `EARS_GUIDE.md`

---

## 定型問い一覧

### E-1: ユビキタス要件（Ubiquitous）

**問い**: この Capability / Feature が**常に**満たすべき要件は何ですか？

**推奨フォーマット**: `The system shall [動作].`

**車載機構の例**:
- `The housing shall maintain IP67 rating throughout the product lifetime.`
- `The bracket shall withstand 30G acceleration in all directions.`
- `The connector shall maintain electrical continuity under -40 to +125 deg C.`

**escape hatch**: 「特にない」→ 「温度範囲？振動条件？IP 等級？必ず一つはある」

---

### E-2: イベント駆動要件（Event-driven）

**問い**: 特定のイベント（操作・故障・環境変化）が起きたとき、システムはどう反応すべきですか？

**推奨フォーマット**: `When [event], the system shall [response].`

**車載機構の例**:
- `When the connector is disengaged, the system shall provide tactile feedback within 0.5 seconds.`
- `When external pressure exceeds 200 kPa, the housing shall not deform plastically.`

**escape hatch**: 「わからない」→ F-2 のトリガーを EARS 形式に変換

---

### E-3: 状態駆動要件（State-driven）

**問い**: 特定の状態が続いている間、システムが維持すべき動作は？

**推奨フォーマット**: `While [state], the system shall [continuous action].`

**車載機構の例**:
- `While vibration of 10-2000Hz random is applied, the bracket shall maintain mounting integrity.`
- `While the connector is mated, the system shall maintain contact resistance below 50 mΩ.`

**escape hatch**: 「思いつかない」→ 「ユーザーが使っている間ずっと保証したいことは？」

---

### E-4: オプション要件（Optional）

**問い**: 特定の構成や仕向地で適用される要件はありますか？

**推奨フォーマット**: `Where [option], the system shall [action].`

**車載機構の例**:
- `Where the cold-region package is selected, the housing shall withstand -50 deg C.`
- `Where the high-temperature package is selected, the seal material shall be FKM.`

**escape hatch**: 「ない」→ [A] でスキップ可

---

### E-5: エラー / 異常要件（Unwanted behavior）

**問い**: 異常・故障条件が発生したとき、システムはどう振る舞うべきですか？

**推奨フォーマット**: `If [abnormal condition], the system shall [error handling].`

**車載機構の例**:
- `If a connector pin is bent during assembly, the system shall fail in an open state, not short.`
- `If the seal degrades beyond 30% compression set, the system shall maintain IP65 at minimum.`

**escape hatch**: C-5（Graceful Degradation）の回答を EARS 形式に変換

---

### E-6: 試験方法

**問い**: この受け入れ基準を**どう試験**しますか？

**推奨選択肢**:
- 規格試験（ISO 16750-3, IEC 60068-2-64 等）
- FEA / CFD シミュレーション
- 試作品試験（社内試験設備）
- サンプル抜取り（量産時 QC）
- 全数検査（ライン）

**Web Search Trigger**: 規格の最新版・改定情報
- クエリ例: `"ISO 16750-3 latest revision year"` / `"IEC 60068-2 update 2026"`

**escape hatch**: 「わからない」→ 「合格と言える具体的な数値・観察を 1 つ挙げて」

---

### E-7: 試験条件・判定値の許容範囲

**問い**: 試験条件の許容範囲と判定値の閾値は？

**推奨回答例**:
- 「-40±2 deg C、+85±2 deg C、48 サイクル」
- 「振動 30G ±5%、3 軸各 8 時間」
- 「気密：100 kPa ゲージ圧で漏れ ≤ 1 cm³/min」

**Web Search Trigger**: 業界標準値
- クエリ例: `"automotive connector vibration test acceptance criteria 2026"`

**escape hatch**: 「わからない」→ 「もし不適合なら最悪の影響は？」と問うてリスクから逆算

---

### E-8: 試験データ・サンプル

**問い**: この eval を検証するためのサンプル数・データ取得方法は？

**推奨選択肢**:
- 試作 3〜5 個（DR 段階）
- 量産 30 個（PV 段階）
- ロット抜取り 5/1000（量産時）
- 全数 OK/NG 判定（ライン）

**Web Search Trigger**: ドメイン別サンプル数の標準
- クエリ例: `"<part category> automotive sample size standard 2026"`

**escape hatch**: 「データがない」→ [A] で「最低 3 個試作で検証」と記録

---

## Escape Hatch 共通ルール（E 層）

- 「試験は後で」→ 「今書いておかないと、実装後の手戻りが大きい」と重要性を説明
- Engineering 実装の話 → 「受け入れ基準は実装方法を問わない」
- EARS 記法が不明 → `EARS_GUIDE.md` を Read
