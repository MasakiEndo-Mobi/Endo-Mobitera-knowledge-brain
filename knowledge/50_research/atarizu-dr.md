---
doc_id: res.process.atarizu-dr
title: "当たり図DR"
doc_type: research
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2025-08-18
audience: [self]
one_line_thesis: "当たり図DR: 設計初期に構造/部品配置/干渉/性能を確認するレビュー工程。"
confidence: medium
tags: [design-review, dr]
---

# 当たり図DR (Design Review)

---

### 🎯 当たり図DRの目的とは？

「当たり図DR（Design Review）」は、製品設計における初期段階での構造・部品配置・干渉・性能などを確認するためのレビュー工程です。特に「当たり図DR」は、設計案が実際の製造・組立・性能要件に対して問題がないかを事前に検証することを目的としています。

---

### 📘 主な目的と役割

#### 1. **設計の妥当性確認**

- 部品配置や構造が母体設計と整合しているかを確認。
- 例えば、[NASDA_当たり図DR](https://jppanasonic.sharepoint.com/sites/TAS.TEST/_layouts/15/Doc.aspx?sourcedoc=%7B7642BEE4-8AC2-48A8-BAEC-649D63B37070%7D&file=NASDA_%E5%BD%93%E3%81%9F%E3%82%8A%E5%9B%B3DR.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1&EntityRepresentationId=b445a4d3-b8b7-4342-9e72-62ab92b63eb7)では、SOC/MAIN基板間接続や熱成り立ち、組立性などが検討されています [1](https://jppanasonic.sharepoint.com/sites/TAS.TEST/_layouts/15/Doc.aspx?sourcedoc=%7B7642BEE4-8AC2-48A8-BAEC-649D63B37070%7D&file=NASDA_%E5%BD%93%E3%81%9F%E3%82%8A%E5%9B%B3DR.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1)。

#### 2. **変更点の明確化と影響評価**

- 母体からの変更点（サイズ、構成、部品配置など）を明確にし、それが性能や製造に与える影響を評価。
- [DR確認項目一覧](https://jppanasonic.sharepoint.com/sites/ONL03772/DesignReview/SitePages/DR%e7%a2%ba%e8%aa%8d%e9%a0%85%e7%9b%ae%e4%b8%80%e8%a6%a7.aspx?web=1&EntityRepresentationId=2abfe4b8-8561-423e-86a5-fcddf58dabd5)では、各DRステージ（DR0〜DR2）で確認すべき項目が整理されており、変更点の管理やDRBFMとの連携が求められています [2](https://jppanasonic.sharepoint.com/sites/ONL03772/DesignReview/SitePages/DR%e7%a2%ba%e8%aa%8d%e9%a0%85%e7%9b%ae%e4%b8%80%e8%a6%a7.aspx?web=1)。

#### 3. **DRBFMとの連携**

- DRBFM（Design Review Based on Failure Mode）と連携し、変更点に対する潜在的な故障モードを洗い出し、対策を検討。
- [155D⑤DRBFMワークシート5](https://jppanasonic.sharepoint.com/sites/ONL02042/Shared%20Documents/W18003A/21CY/70_CarDevelopment/01_Vehicle/005.3_155D_255D/053_Mechanical/31%20DRBFM%28%e6%9c%80%e6%96%b0%29/work/155D_%e2%91%a4DRBFM%e3%83%af%e3%83%bc%e3%82%af%e3%82%b7%e3%83%bc%e3%83%88_5.pdf?web=1&EntityRepresentationId=a4064bd8-04aa-4589-bfe3-cb0cc77560f0)では、変更点の目的、懸念事項、対策、評価方法などが詳細に記載されています [3](https://jppanasonic.sharepoint.com/sites/ONL02042/Shared%20Documents/W18003A/21CY/70_CarDevelopment/01_Vehicle/005.3_155D_255D/053_Mechanical/31%20DRBFM%28%e6%9c%80%e6%96%b0%29/work/155D_%e2%91%a4DRBFM%e3%83%af%e3%83%bc%e3%82%af%e3%82%b7%e3%83%bc%e3%83%88_5.pdf?web=1)。

#### 4. **製造・品質への反映**

- DRで得られた知見を設計図面や製造工程に反映し、品質確保や不具合防止につなげる。
- [DRの進め方 実践編](https://jppanasonic.sharepoint.com/sites/ONL01654/81/SitePages/DR%e3%81%ae%e9%80%b2%e3%82%81%e6%96%b9-%e5%ae%9f%e8%b7%b5%e7%b7%a8.aspx?web=1&EntityRepresentationId=869691d8-3447-4ecb-a22d-f3b8eb7b0ce8)では、DRの運用方法や実践的な進め方が研修教材としてまとめられており、若手技術者向けの教育にも活用されています [4](https://jppanasonic.sharepoint.com/sites/ONL01654/81/SitePages/DR%e3%81%ae%e9%80%b2%e3%82%81%e6%96%b9-%e5%ae%9f%e8%b7%b5%e7%b7%a8.aspx?web=1)。

---

### 🧩 実際の活用例

- [867D当たり図DR20250722](https://jppanasonic.sharepoint.com/sites/ONL04024/_layouts/15/Doc.aspx?sourcedoc=%7B162870AB-CA68-4A8F-B0AA-2926A65A7F75%7D&file=867D_%E5%BD%93%E3%81%9F%E3%82%8A%E5%9B%B3DR_20250722.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1&EntityRepresentationId=bf33b584-e166-4bff-88ed-7018d9302aa0)では、14inchモデルにおける部品配置、板厚、BT-ANTの性能課題、避雷針形状の追加などが議論されており、設計の完成度向上に向けた具体的な検討が行われています [5](https://jppanasonic.sharepoint.com/sites/ONL04024/_layouts/15/Doc.aspx?sourcedoc=%7B162870AB-CA68-4A8F-B0AA-2926A65A7F75%7D&file=867D_%E5%BD%93%E3%81%9F%E3%82%8A%E5%9B%B3DR_20250722.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1)。
- RE: 【開会通知】867D 14inch 当たり図DRでは、DRの対象機種や資料リンク、FMEAとの連携が案内されており、関係者間での情報共有が行われています [6](https://outlook.office365.com/owa/?ItemID=AAMkADczNGQyZDYyLWUwMTQtNGE1My04NzU2LTAyMTk0YzBjM2VhMgBGAAAAAAAIGlZZI6UvS6KisosX9bt6BwCrP0r%2bKRbhT7GrkWB07kK5AAAAAAEMAACrP0r%2bKRbhT7GrkWB07kK5AAFKlqwQAAA%3d&exvsurl=1&viewmodel=ReadMessageItem)。

---

ご希望があれば、特定のDR資料の要点整理や、DRBFMとの関係性についてさらに詳しくご説明できます。どの製品やDRステージに関心がありますか？

  
References

[1]　 [NASDA_当たり図DR](https://jppanasonic.sharepoint.com/sites/TAS.TEST/_layouts/15/Doc.aspx?sourcedoc=%7B7642BEE4-8AC2-48A8-BAEC-649D63B37070%7D&file=NASDA_%E5%BD%93%E3%81%9F%E3%82%8A%E5%9B%B3DR.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1)

[2]　 [DR確認項目一覧](https://jppanasonic.sharepoint.com/sites/ONL03772/DesignReview/SitePages/DR%e7%a2%ba%e8%aa%8d%e9%a0%85%e7%9b%ae%e4%b8%80%e8%a6%a7.aspx?web=1)

[3]　 [155D_⑤DRBFMワークシート_5](https://jppanasonic.sharepoint.com/sites/ONL02042/Shared%20Documents/W18003A/21CY/70_CarDevelopment/01_Vehicle/005.3_155D_255D/053_Mechanical/31%20DRBFM\(%e6%9c%80%e6%96%b0\)/work/155D_%e2%91%a4DRBFM%e3%83%af%e3%83%bc%e3%82%af%e3%82%b7%e3%83%bc%e3%83%88_5.pdf?web=1)

[4]　 [DRの進め方 実践編](https://jppanasonic.sharepoint.com/sites/ONL01654/81/SitePages/DR%e3%81%ae%e9%80%b2%e3%82%81%e6%96%b9-%e5%ae%9f%e8%b7%b5%e7%b7%a8.aspx?web=1)

[5]　 [867D_当たり図DR_20250722](https://jppanasonic.sharepoint.com/sites/ONL04024/_layouts/15/Doc.aspx?sourcedoc=%7B162870AB-CA68-4A8F-B0AA-2926A65A7F75%7D&file=867D_%E5%BD%93%E3%81%9F%E3%82%8A%E5%9B%B3DR_20250722.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1)

[6] 　[RE: 【開催通知】867D 14inch　当たり図DR](https://outlook.office365.com/owa/?ItemID=AAMkADczNGQyZDYyLWUwMTQtNGE1My04NzU2LTAyMTk0YzBjM2VhMgBGAAAAAAAIGlZZI6UvS6KisosX9bt6BwCrP0r%2bKRbhT7GrkWB07kK5AAAAAAEMAACrP0r%2bKRbhT7GrkWB07kK5AAFKlqwQAAA%3d&exvsurl=1&viewmodel=ReadMessageItem)

---
### 関連ノート
- [[p-21cy-220d|P-21CY_220D]]
- [[p-21cy-450d|P-21CY_450D]]
- [[p-21cy-900b|P-21CY_900B]]
- [[p-24cy-867d|P-24CY_867D]]
- [[p-24cy-867d-dp|P-24CY_867D_機構DP_議事録]]
- [[drbfm-design-review-facilitation|R-技術_DRBFM_デザインレビュー実施]]
- [[drbfm-worksheet-creation|R-技術_DRBFM_ワークシート作成]]
- [[drbfm-support-tools|R-技術_DRBFM_実践支援ツール]]
- [[drbfm-training|R-技術_DRBFM_教育トレーニング]]
- [[drbfm-overview|R-技術_DRBFM_概論]]
- [[drbfm-implementation-strategy|R-技術_DRBFM_統合実装戦略]]
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
