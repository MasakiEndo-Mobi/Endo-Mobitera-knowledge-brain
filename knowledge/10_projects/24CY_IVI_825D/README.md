---
doc_id: ops.project.24cy-ivi-825d
title: 24CY IVI 825D 機構設計（北米仕向 / PASA）
doc_type: project
project: [24CY_IVI_825D]
layer: canonical
role_in_story: execution
status: planning
as_of: 2026-05-29
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: 北米仕向 IVI ユニット 825D の機構設計・図面・承認図・試作評価・サプライヤ調整・顧客説明を推進するプロジェクト
confidence: medium
phase: development
priority: high
milestones:
  - name: 825D 承認図（CV/PP0）
    target_date: TBD
    status: in_progress
  - name: PP0 BONDING 図面（K01→K02）
    target_date: TBD
    status: in_progress
---

# 24CY IVI 825D 機構設計（北米仕向 / PASA）

> **注**: `status` / `phase` / マイルストーン日程は暫定（TBD）。実態が固まり次第更新する。

---

## プロジェクト概要

24CY 825D（北米仕向 / PASA 顧客）の IVI（In-Vehicle Infotainment）ユニット機構設計。機構側の設計・図面・承認図・試作/評価・サプライヤ調整・顧客説明を ENDO が推進する。

本プロジェクトは KB＋AI 支援システムの**最初のパイロット適用先**でもある（→ [[vision]] / `index.vision`）。日々の業務（議事録・日報・決定・タスク）をこの KB に流し込み、情報同期・自己維持・月次面談資料の自動編纂を 825D 文脈で検証する。

---

## 体制

- **社内**: Kitagawa Maiki, Kiryu Masayoshi, Ebata Tosiyuki, TANAKA HIDEKI, MIZUNO RYOTA
- **PASA（北米拠点）**: Yuji Kimizuka, Julia Dixon
- **サプライヤ**: AGC（ガラス / DT-Pro）, Minebea, WNC

---

## 進行中の主要業務

- 825D 承認図（CV/PP0）／ PP0 BONDING 図面（K01→K02）
- 機能シボ（Functional texture）／ シボ・凹形状の要望反映可否の社内協議
- DT-Pro（AGC）／ AGC 納入仕様書 MTG ／ ポロン貼付前提の運用案合意
- LCD 反りの根本原因解析 ／ 荷重印可試験の原因切り分け計画
- 不織布コスト見積り取得（案1〜5 比較整理）／ 製造仕様書の改訂・貿易関連書類の整備
- 並行プロジェクト: 410D 承認図・外観図作成

---

## マイルストーン

| Milestone | Target Date | Status |
|---|---|---|
| 825D 承認図（CV/PP0） | TBD | in_progress |
| PP0 BONDING 図面（K01→K02） | TBD | in_progress |

> 実日程は未確定。確定次第このテーブルとフロントマター `milestones` を更新する。

---

## ディレクトリ構成

```
24CY_IVI_825D/
├─ README.md           ← このファイル（プロジェクト定義）
├─ meetings/           ← 議事録（doc_type: meeting）
├─ daily-logs/         ← 日報（doc_type: daily-log）
├─ design-notes/       ← 設計検討メモ（doc_type: design-note, canonical）
├─ test-reports/       ← 試験結果（doc_type: test-report, canonical）
├─ decisions/          ← 意思決定（DEC-NNNN_<slug>.md）
├─ tasks/              ← タスク（TASK-NNNN_<slug>.md）
├─ requirements/       ← Vision/Outcome/Capability/Feature/Eval/EngSpec の 6 層
└─ assets/             ← バイナリ（.docx / .pdf / .png / .step 等）
```

---

## 関連リンク

- [[vision]] — KB 全体 Vision（`index.vision`。本 PJ はパイロット適用先）
- [[research_map]] — KB 全体マップ・ナビゲーション
- [[moc_projects]] — プロジェクト横断 Dataview ビュー
