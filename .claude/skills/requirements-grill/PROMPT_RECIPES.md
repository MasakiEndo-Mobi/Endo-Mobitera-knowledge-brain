# PROMPT_RECIPES.md — 推奨回答デフォルト集

各層の「推奨回答」生成が難しいとき、このファイルから適切なデフォルト候補を選ぶ。

---

## V 層: Vision デフォルト

### ビジョン文の 3 スタイル

**スタイル A（課題解決型）**:
> 「[ターゲット車種・市場] の [現状の問題] を、[技術的アプローチ] で解消する。」

**スタイル B（性能向上型）**:
> 「[既存システム] を [N 倍] の [性能指標] に高めることで、[市場価値] を獲得する。」

**スタイル C（規格対応型）**:
> 「[新規格] への適合により、[市場拡大／継続販売] を確保する。」

---

## O 層: Outcomes デフォルト

### 北極星指標フォーマット

**信頼性指向**:
```
North Star: 市場クレーム発生率 / 100 万台
Floor: 現行モデル比 110% 以下
Target Q1: 現行モデル比 50% 以下
Source: 保証 DB / 月次集計
```

**コスト指向**:
```
North Star: 部品単価 (USD)
Floor: 現行モデル比 110% 以下
Target Q1: 現行モデル比 80% 以下
Source: 調達 BOM / 四半期更新
```

**製造性指向**:
```
North Star: 組付け工数 (秒/台)
Floor: 現行モデル比 100%
Target Q1: 現行モデル比 70% 以下
Source: ライン MES / 日次集計
```

---

## C 層: Capabilities 動詞語彙

機構設計の Capability を表す動詞リスト。ここから選んで具体化する。

**機械的機能系**:
- 締結する / 位置決めする / 整列する
- 保持する / 拘束する / 解除する
- 衝撃を吸収する / 振動を減衰する
- 変形を許容する / 復元する
- 摺動する / 回転する

**シール・隔離系**:
- 気密を保つ / 水密を保つ
- 塵埃を遮断する / 油を遮断する
- 電磁波を遮蔽する
- 温度を遮断する / 熱伝導する

**組立・分解系**:
- 工具なしで組付ける / 工具なしで分解する
- 視認確認できる / 触覚確認できる
- ロックする / アンロックする
- 誤組防止する（ポカヨケ）

**メンテナンス系**:
- 交換する / 補修する / 清掃する
- 状態を診断する
- 識別する（マーキング / 形状コード）

**安全系**:
- 過大荷重を吸収する / 切断する（脆弱部）
- 異常時に分離する / フェイルセーフ動作する
- 火災を遮断する / 燃焼を抑制する

---

## F 層: Feature ユーザーストーリーテンプレ

**英語**:
> `As a [stakeholder], I want [goal/action], so that [benefit/outcome].`

**日本語**:
> 「[ステークホルダー] として、[目的] のために、[行動] したい。」

### ステークホルダーテンプレ

```
役割: [ライン作業者 / 整備士 / 設計者 / 品質保証 / エンドユーザー]
作業環境: [量産ライン / サービス工場 / 走行中車内]
作業対象: [対象部品・サブシステム]
Pain: [現状で困っていること]
頻度: [毎日 / 週次 / 月次 / 故障時のみ]
```

---

## E 層: Eval EARS 5 パターン穴埋め

```
U: The <subsystem> shall <do something measurable> <under what conditions>.
E: When <event/trigger>, the <subsystem> shall <response> within <time/threshold>.
S: While <state/environment>, the <subsystem> shall <continuous action> <maintaining what>.
O: Where <option/variant>, the <subsystem> shall <additional behavior>.
W: If <fault/abnormal>, the <subsystem> shall <graceful degradation> and <notify/log>.
```

### 試験条件テンプレ

```
試験項目: <ISO/IEC/JIS 番号 §章>
試験条件:
  温度: <範囲> ±<許容>
  振動: <加速度> G, <周波数帯> Hz, <時間> × <サイクル数>
  湿度: <RH%>
  サンプル: N=<数>
判定: <閾値・観察項目>
```

---

## S 層: 材料プロファイル

### プロファイル A: 樹脂ハウジング（標準）

```
材料: PBT-GF30 (ガラス繊維 30%強化 PBT)
温度範囲: -40〜+150 deg C
強度: 引張 100 MPa / 曲げ 160 MPa
製法: 射出成形
ケース: コネクタハウジング / ECU 筐体
```

### プロファイル B: 金属ブラケット（標準）

```
材料: SPCC (冷間圧延鋼板) または A5052 アルミ
温度範囲: -40〜+200 deg C
製法: プレス + 曲げ + 防錆処理
表面処理: 電気亜鉛メッキ / カチオン電着塗装
ケース: 取付ブラケット / ヒートシンク基板
```

### プロファイル C: シール材（標準）

```
標準: NBR (耐油・常温〜100 deg C)
高温: FKM/Viton (-30〜+200 deg C)
低温: シリコーン VMQ (-60〜+200 deg C)
形状: O-リング / ガスケット / 液状ガスケット
```

---

## Web Search Query Recipes（層別クエリ雛形）

> 各層の Web Search Trigger が発動した時の参照クエリ。
> 今日の年（YYYY）を含めることで最新情報の確率が上がる。

### S 層（Engineering Spec）

```
# 材料情報
"PBT GF30 datasheet automotive 2026"
"FKM seal compression set spec 2026"
"<material name> automotive grade 2026"

# 規格最新版
"ISO 16750-3 latest revision year"
"IEC 60068-2-64 update 2026"
"JIS D 1601 revision 2026"

# サプライヤー
"<vendor name> automotive connector catalog 2026"
"<vendor name> seal material list 2026"
```

### E 層（Evals）

```
# 試験プロファイル
"automotive vibration test profile ISO 16750 2026"
"thermal shock test condition automotive 2026"
"IP67 test method IEC 60529"

# ベンチマーク
"automotive <part> warranty claim rate benchmark 2026"
"<part category> reliability target 2026"
```

### C 層（Capabilities）

```
"automotive <function> design pattern 2026"
"<part category> graceful degradation pattern"
```

### O 層（Outcomes）

```
"automotive <category> warranty cost benchmark 2026"
"automotive component reliability MTBF 2026"
```

### V 層（Vision）

```
"automotive <category> market trend 2026"
"<competitor> <product category> portfolio 2026"
```

### F 層（Features）

```
"<competitor> <feature category> spec range"
"automotive <part category> standard features"
```
