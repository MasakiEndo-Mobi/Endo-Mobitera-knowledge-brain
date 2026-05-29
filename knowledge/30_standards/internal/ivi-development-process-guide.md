---
doc_id: std.internal.ivi-development-process
title: "IVI開発プロセスガイド"
doc_type: standard-note
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2025-10-09
audience: [self]
one_line_thesis: "IVI製品開発プロセスを企画〜各フェーズで標準化し品質・コスト・納期の最適化を図る社内ガイド。"
confidence: medium
tags: [Process, IVI, guide]
---

# IVI開発プロセスガイド

## 1. はじめに

本ガイドは、IVI（In-Vehicle Infotainment）製品の開発プロセスを標準化し、品質、コスト、納期の最適化を図ることを目的とする。

## 2. 開発フェーズ

IVI開発は、以下のフェーズで構成される。

- **企画フェーズ:** 市場調査、競合分析、製品コンセプトの策定
- **要件定義フェーズ:** 機能要件、非機能要件の定義、仕様書の作成
- **設計フェーズ:** ハードウェア設計、ソフトウェア設計、筐体設計
- **試作フェーズ:** プロトタイプの製作、評価
- **量産準備フェーズ:** 生産ラインの構築、品質管理体制の確立
- **量産・保守フェーズ:** 製品の量産、市場投入後のサポート

## 3. 主要な設計レビュー

各開発フェーズで、以下の設計レビューを実施する。

- **DR0（デザインレビュー0）:** 企画・要件定義フェーズの完了時に実施。製品コンセプト、主要な仕様、開発計画の妥当性を評価する。
- **DR1（デザインレビュー1）:** 基本設計の完了時に実施。アーキテクチャ、主要部品の選定、コスト目標の妥当性を評価する。
- **DR2（デザインレビュー2）:** 詳細設計の完了時に実施。回路図、基板レイアウト、筐体設計の妥当性を評価する。
- **DR3（デザインレビュー3）:** 試作品の評価完了時に実施。評価結果、品質目標の達成度、量産移行の可否を評価する。

## 4. 品質管理

- **DRBFM（Design Review Based on Failure Mode）:** 設計段階での故障モードの洗い出しと対策
- **FMEA（Failure Mode and Effect Analysis）:** 故障モードの影響解析
- **FTA（Fault Tree Analysis）:** 故障の根本原因解析
- **信頼性試験:** 製品の耐久性、信頼性を評価するための各種試験

## 5. ドキュメント管理

- **仕様書:** 製品の機能、性能、インターフェースなどを定義
- **設計書:** 回路図、基板レイアウト、筐体図面など
- **評価報告書:** 各種評価試験の結果を記録
- **製造指示書:** 製品の製造手順、品質基準などを定義

## 6. 関連部署との連携

- **企画部門:** 市場ニーズ、製品戦略の共有
- **調達部門:** 部品選定、コスト交渉
- **製造部門:** 生産性、品質管理に関する情報共有
- **品質保証部門:** 品質基準の設定、評価試験の実施

## 7. 改訂履歴

- 2025-10-09: Ver.1.0 作成

---
### 関連ノート
- [[2025-09-29_dr0-drbfm-review-part1|P-24CY_825D_DR0_DRBFM_review_part1]]
- [[2025-09-29_dr0-drbfm-review-part2|P-24CY_825D_DR0_DRBFM_review_part2]]
- [[dr0-issues-summary|P-24CY_825D_DR0_issues_summary]]
- [[2025-09-16_drb-review|P-24CY_825D_DRB_review]]
- P-IVI_template
- [[toyota-term-development-phase|R-TOYOTA_用語_開発フェーズ]]
- [[drbfm-design-review-facilitation|R-技術_DRBFM_デザインレビュー実施]]
- [[drbfm-worksheet-creation|R-技術_DRBFM_ワークシート作成]]
- [[drbfm-support-tools|R-技術_DRBFM_実践支援ツール]]
- [[drbfm-training|R-技術_DRBFM_教育トレーニング]]
