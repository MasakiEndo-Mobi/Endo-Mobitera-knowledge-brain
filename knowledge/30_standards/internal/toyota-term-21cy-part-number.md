---
doc_id: std.internal.toyota-term-21cy-part-number
title: "TOYOTA用語: 21CY部品品番体系"
doc_type: standard-note
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2025-07-14
audience: [self]
one_line_thesis: "21CY部品品番はプロジェクト識別子+フェーズ識別子+部位コード+個別連番で構成され、Wing-2/NEWMOS検索を効率化する。"
confidence: medium
tags: [toyota, terminology, 21cy]
---

# 21CY 部品品番体系

## 概要

21CY開発フェーズにおける部品品番は、**プロジェクト識別子 + フェーズ識別子 + 部位コード + 個別連番**で構成される。 これを理解しておくと、Wing‑2 や NEWMOS などの社内システム検索が効率化する。

```text
【品番フォーマット】  PPPFBBSSSS...
   PPP : プロジェクト識別子 (3〜4桁英数字)
   F   : フェーズ識別子      (1桁数字)
   BB  : 部位コード          (2桁英字)
   SSSS... : 個別連番        (4〜5桁英数字)
```

## 品番構成の可視化（サンプルツリー）

```
CN‑SL5BN0AJ
 └─1CNSL5BN0AJ
     └─2CNSL5BN0AJ
         └─YEP0FX1F147  Display FXK
             ├─YEP0FX       ESC‑Assy / Bonding Assy  (FX11)
             │   ├─K9AB009Y0001  AISエンコーダ            (AE2, AE3)
             │   ├─YEFXU00786    ボンディング済LCD        (FXK1)
             │   │   ├─L5EDDYY01127   TFT                (LCD1)
             │   │   ├─YEFX09         ガラス             (FX1)
             │   │   └─YEFX0703602    Double‑sided tape  (FX2,3)
             │   └─YEFCU03228   フロントESC Assy          (FC1)
             ├─YEP0FX       TFTBKT‑BT‑Assy         (FX1)
             │   ├─YEFAU00394      TFTブラケット           (FA1)
             │   ├─N1KYYYY00063    BTケーブル             (ANT1)
             │   ├─N1KYYYY00066    BTケーブル             (ANT2)
             │   ├─XTB26+6FFJ      BTケーブル用ビス       (TB21〜TB24)
             │   ├─YEFX0703635     BTホルダー            (FX42)
             │   └─YEJT03333A      BTホルダー用ビス       (TB25,26)
             ├─YEP0PTE207A0  IF基板
             ├─YEP0PTE209A0  SW基板
             ├─… (パネル関連部品)
             └─YEP0FX       9.8aisダイアルAssy(中側)
```

## 詳細

- **プロジェクト識別子 (PPP)** 例: YEP, YEF, K9A
- **フェーズ識別子 (F)** 1桁の数字。0 は開発フェーズ (21CY) を示す。
- **部位コード (BB)** 例: FX = Front ESC, PT = 基板, CU = Cover
- **個別連番 (SSSS...)** 4〜5桁の英数字。機種固有シリアル。
- **改訂記号** 末尾 A0, B0 等でリビジョン管理。

## 関連リンク

- 社内品番ルール2023
- Wing‑2検索Tips
- NEWMOS登録手順

**質問:**

- 「部位コード」の最新一覧表をお持ちでしたら共有いただけますか？
- 製造試作 (F=1) 移行時の品番改訂フローは、21CY特有のルールがありますか？

---
### 関連ノート
- [[p-21cy-220d|P-21CY_220D]]
- [[p-21cy-450d|P-21CY_450D]]
- [[p-21cy-900b|P-21CY_900B]]
- [[toyota-term-24cy-naiki|R-TOYOTA_用語_24CY内機]]
- [[toyota-term-dr|R-TOYOTA_用語_DR]]
- [[toyota-term-rddp|R-TOYOTA_用語_RDDP]]
- [[toyota-term-gaisetsushin|R-TOYOTA_用語_外設申]]
- [[toyota-term-shikyu|R-TOYOTA_用語_支給]]
- [[toyota-term-kanri-jikyu|R-TOYOTA_用語_管理自給]]
- [[toyota-term-development-phase|R-TOYOTA_用語_開発フェーズ]]
- [[glass-slimming|R-技術_スリミング_ガラス]]
- [[p-24cy-400d|P-24CY-400D]]
- [[p-24cy-310d|P-24CY_310D]]
- [[p-24cy-410d|P-24CY_410D]]
- [[p-24cy-695d-696d|P-24CY_695D_696D]]
- [[p-24cy-744d|P-24CY_744D]]
- [[p-24cy-744d-summary|P-24CY_744D_summary]]
- [[825d-overview|P-24CY_825D]]
- [[2025-12-11_1sdr-review|P-24CY_825D_1SDR_議事録]]
- [[2025-09-29_dr0-drbfm-review-part1|P-24CY_825D_DR0_DRBFM_review_part1]]
- [[2025-09-29_dr0-drbfm-review-part2|P-24CY_825D_DR0_DRBFM_review_part2]]
