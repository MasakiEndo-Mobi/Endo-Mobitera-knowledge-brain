---
doc_id: source.methods.r-lean-six-sigma
title: "R-業務改善_Lean_Six_Sigma"
doc_type: source
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2025-07-08
audience: [self]
one_line_thesis: "業務改善説明レポート：Lean Six Sigma とDXによる効率化"
confidence: low
---

# 業務改善説明レポート：Lean Six Sigma とDXによる効率化

---

## 1. 目的と背景
- **現状認識**：手作業や紙ベースの業務が多く、ミスや手戻りが発生
- **課題**：リードタイムの長さ、手戻り率の高さ、ブラックボックス化したプロセス
- **目標**：Lean Six SigmaのDMAIC手法を適用し、プロセスの可視化・標準化・自動化を通じて以下を実現する
  - リードタイム短縮
  - 初回合格率向上（手戻り率低減）
  - 継続的改善体制の確立

---

## 2. DMAICフレームワーク概要
1. **Define（定義）**：プロジェクト範囲と効果を明確化
2. **Measure（測定）**：SIPOCやVSMで現状を可視化・定量化
3. **Analyze（分析）**：根本原因をパレート図・フィッシュボーンで特定
4. **Improve（改善）**：施策立案（ECRS視点＋DX技術活用）と実行
5. **Control（管理）**：標準化・研修・ダッシュボード運用で定着・維持

---

## 3. Define（定義）フェーズ
1. **プロジェクト定義書**（1枚完結）に以下を明示
   - **現状認識**：例）注文処理に平均10日、初回合格率80%
   - **目的**：リードタイム5日以内、初回合格率95%以上
   - **対象範囲**：国内EC注文プロセス全体
   - **投資**：RPAライセンス、担当工数20人日
2. **役割分担**（オーナー／マネージャー／メンバー）
3. **マイルストーンと期日**：業務ヒアリング完了、VSM作成、改善案実装など
4. **目指す効果（QCD）**：品質（Quality）、コスト（Cost）、納期（Delivery）

---

## 4. Measure（測定）フェーズ
- **SIPOC**：サプライヤー→インプット→プロセス→アウトプット→カスタマーを一覧化
- **Value Stream Map**：
  - リードタイム、サイクルタイム、プロセスタイム、手戻り率、バッチサイズを可視化
  - プロセス間の待機時間（非付加価値時間）を抽出

---

## 5. Analyze（分析）フェーズ
1. **パレート図**：欠陥・手戻り件数上位項目（例：入力ミス、再確認作業）を80%特定
2. **フィッシュボーン（特性要因図）**：4M（Man/Method/Machine/Material）で根本原因を深掘り
3. **VA／BNVA／NVA**分析：7つの無駄視点で付加価値のない作業を抽出

---

## 6. Improve（改善）フェーズ
- **ECRS**視点で“あるべき姿”を描く
  - Eliminate：紙の印刷・郵送を排除
  - Combine：顧客データ入力と照合統合
  - Rearrange：承認手順を並列化
  - Simplify：手順書・チェックリストで標準化
- **DX／RPA**適用ポイント
  - OCRで紙帳票をデジタル化
  - API連携でシステム間データ自動連携
  - RPAで定型作業自動化
  - ワークフローシステムで申請承認の遅延を解消
- **改善施策の効果検証**：因果関係マトリクスで各施策→QCDへの影響を論理的に整理
- **パイロット実行**：部署・期間絞り込みでリスク低減し検証・修正後に全社展開

---

## 7. Control（管理）フェーズ
- **ドキュメント整備**：手順書、社内規定、動画マニュアル
- **研修プログラム**：OJT・ワークショップで定着促進
- **ダッシュボード運用**：KPI（リードタイム、手戻り率など）をリアルタイム可視化
- **継続的改善**：定期的なアイデア募集、改善会議でPDCAサイクルを回す

---

以上の流れで、Lean Six SigmaのDMAIC手法とDX技術を融合し、持続的な業務改善と高付加価値業務へのシフトを実現します。

---
### 関連ノート
- [[r-udemy|R-Udemy_業務改善]]
- [[biz-improve-monthly-report-prompt|R-業務改善_月次業務レポート作成プロンプト]]
- [[biz-improvement-overview|R-業務改善_概論]]
- [[biz-improvement-howto|R-業務改善_進め方概論]]
- [[a-learning-ojt-2q|A-Learning_OJT_2Q資料_質問一覧]]
- R-GEMINI_API_Key
- [[r-tool-spo-tool-box-2|R-Tool_SPO_Tool_Box_マニュアル]]
- [[markforged-overview|R-サプライヤ_Markforged]]
- [[umi-overview|R-サプライヤ_UMI]]
- [[fasotec-ai-design-survey|R-サプライヤ_ファソテック_AI設計代行調査レポート]]
- [[hoshiden-fd|R-サプライヤ_ホシデンFD]]
- [[nakanuma-art-screen|R-サプライヤ_中沼アートスクリーン]]
- [[onyx-surface-smoothing-report|R-技術_Onyx表面平滑化_レポート]]
- MOC_Resources_サプライヤ
