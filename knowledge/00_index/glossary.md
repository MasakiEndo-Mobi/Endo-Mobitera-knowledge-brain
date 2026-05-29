---
doc_id: index.glossary
title: 用語集
doc_type: index
project: [all]
layer: canonical
role_in_story: routing
status: canonical
as_of: 2026-05-28
audience: [self, engineer]
one_line_thesis: 車載電子機器機構設計KBで使用する専門用語・略語・社内用語の定義集。
confidence: high
---

# 用語集

KB内で使用する用語の定義。新しい専門用語が出てきたら追記する。

---

## 略語

| 略語 | 正式名称 | 説明 |
|---|---|---|
| FEA | Finite Element Analysis | 有限要素解析 |
| EMC | Electromagnetic Compatibility | 電磁両立性 |
| ESD | Electrostatic Discharge | 静電気放電 |
| FMEA | Failure Mode and Effects Analysis | 故障モード影響解析 |
| BOM | Bill of Materials | 部品表 |
| ECU | Electronic Control Unit | 電子制御装置 |
| PCB | Printed Circuit Board | プリント基板 |
| IP | Ingress Protection | 防塵防水保護等級 |
| CFD | Computational Fluid Dynamics | 数値流体力学 |

---

## 規格

| 規格番号 | 内容 |
|---|---|
| ISO 16750-3 | 車載電子機器の機械的負荷試験 |
| ISO 16750-4 | 車載電子機器の気候負荷試験 |
| IEC 60068-2-64 | ランダム振動試験 |
| JIS D 1601 | 自動車部品の振動試験方法 |
| IEC 60529 | 外郭による保護等級 (IPコード) |

> 規格の詳細は `30_standards/<body>/` 配下の standard-note を参照。

---

## 設計フェーズ用語

| 用語 | 定義 |
|---|---|
| **Concept** | 概念検討。スケッチ・初期レイアウト |
| **Detailed Design** | 詳細設計。CAD モデル・FEA 解析 |
| **Validation** | 試作・試験検証 |
| **Production** | 量産準備・量産後フォロー |

---

## 部品カテゴリ用語

| カテゴリ | 説明 |
|---|---|
| Connectors | 信号・電力接続部品（USB-C、車載ハーネスコネクタ等） |
| Housings | 筐体・ケース類 |
| Brackets | 取付ブラケット・ホルダ類 |
| Thermal | 熱対策部品（ヒートシンク・ヒートパイプ・サーマルパッド等） |
| Vibration Damping | 防振部品（ダンパー・ブッシュ等） |
| Sealing | シール部品（O-リング・ガスケット・接着剤等） |
| Fasteners | 締結部品（ネジ・リベット・クリップ等） |
