# EARS_GUIDE.md — EARS 記法ガイド（1 ページで読み切る）

> EARS = Easy Approach to Requirements Syntax
> 機構設計・電気設計・組込みソフト共通の要件記述パターン

---

## 5 パターン早見表

| パターン | 形式 | いつ使う |
|---|---|---|
| **Ubiquitous** | `The system shall [動作].` | 常時成立する要件 |
| **Event-driven** | `When [イベント], the system shall [応答].` | トリガーで発動する要件 |
| **State-driven** | `While [状態], the system shall [継続動作].` | 状態中ずっと成立する要件 |
| **Optional** | `Where [設定/オプション], the system shall [動作].` | 特定構成のみに適用 |
| **Unwanted** | `If [異常条件], the system shall [エラー処理].` | エラー・例外処理 |

---

## パターン別 定型文と例（車載機構）

### 1. Ubiquitous（ユビキタス）

**形式**: `The system shall [動作].`

| ダメな書き方 | 良い書き方 |
|---|---|
| 「高い耐久性を持つこと」 | `The housing shall maintain structural integrity for 200,000 km of vehicle operation.` |
| 「軽量であること」 | `The bracket shall weigh no more than 120 grams.` |
| 「防水であること」 | `The connector shall meet IP67 ingress protection rating.` |

---

### 2. Event-driven（イベント駆動）

**形式**: `When [イベント], the system shall [応答].`

| ダメな書き方 | 良い書き方 |
|---|---|
| 「操作したら反応する」 | `When the latch is depressed with 5N force, the connector shall disengage within 1 second.` |
| 「衝撃が来たら」 | `When a mechanical shock of 50G is applied, the system shall not produce visible deformation.` |

---

### 3. State-driven（状態駆動）

**形式**: `While [状態], the system shall [継続動作].`

| ダメな書き方 | 良い書き方 |
|---|---|
| 「振動環境で動く」 | `While vibration of 10-2000Hz random per ISO 16750-3 is applied, the bracket shall maintain bolt preload above 80% of initial.` |
| 「高温で性能維持」 | `While ambient temperature is between 85 and 125 deg C, the seal shall maintain compression set below 25%.` |

---

### 4. Optional（オプション）

**形式**: `Where [設定], the system shall [動作].`

| ダメな書き方 | 良い書き方 |
|---|---|
| 「寒冷地版」 | `Where the cold-region package is selected, the housing shall withstand -50 deg C without becoming brittle.` |
| 「高負荷用」 | `Where the high-load configuration is selected, the fastener shall use M8 grade 10.9 steel.` |

---

### 5. Unwanted behavior（異常・エラー）

**形式**: `If [異常条件], the system shall [エラー処理].`

| ダメな書き方 | 良い書き方 |
|---|---|
| 「故障時の挙動」 | `If a single bolt loses preload, the bracket shall maintain mounting integrity through the remaining N-1 fasteners.` |
| 「シール劣化時」 | `If the primary seal degrades, the system shall maintain IP65 rating through the secondary seal.` |

---

## よくある間違い（チェックリスト）

- [ ] 「高い」「強い」「軽い」「良い」など主観的形容詞を使っていない（数値で書く）
- [ ] 「など」「できる限り」「必要に応じて」などの曖昧表現を使っていない
- [ ] `shall` を使っている（`should` / `must` / `may` は EARS では使わない）
- [ ] 1 文に 2 つの要件を混ぜていない（1 shall = 1 要件）
- [ ] 実装方法を書いていない（「FKM ゴムを使って」等は ADR・S 層に書く）
- [ ] 単位を明記している（deg C / N / mm / Hz 等）
- [ ] 試験条件を明示している（測定方法を含めて）
