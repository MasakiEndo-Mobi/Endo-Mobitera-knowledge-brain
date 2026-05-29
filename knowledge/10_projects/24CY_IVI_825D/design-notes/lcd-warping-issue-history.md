---
doc_id: proj.24cy-ivi-825d.design.lcd-warping-issue-history
title: "825D LCD反り問題 経緯"
doc_type: design-note
project: [24CY_IVI_825D]
layer: canonical
role_in_story: problem
status: review
as_of: 2026-03-24
audience: [self]
one_line_thesis: "825D LCD反り問題の経緯（788Dホシデン貼合での反り→貼付不可の社内共有を起点とする）。"
confidence: medium
relations:
  related: [supp.hoshiden.bonding-fd, ops.project.24cy-ivi-825d]
tags: [825D, LCD, warping, bonding]
design_phase: detailed
---

## L0（1文要約）

**788D（ホシデン貼合）で起きた「LCD反り→貼付不可」を起点に、825D（ミネベア貼合）で同種問題が起きないかを社内資料で確認・整理した経緯であり、因果は未確定箇所を明示している。**

---

## L1（5つの要点）

- **起点（788D）**: 先行20台で反り大により STOP。図面想定0.4mm以内に対し目視1〜2mm程度
- **工程条件**: 受入後に全数アニール（変色/残留応力対策）、アニール後の貼合で反り発覚。アニール前後どちらが原因かは調査中
- **測定方法**: 定盤に液晶面を下向き、隙間ゲージで暫定測定（現場運用）
- **NG内訳（途中）**: 127台中45台確認でNG相当2台（0.9mm/0.6mm）、規格内でも0.5mm前後は念のため回避
- **825Dへの含意**: ミネベア貼合での再発有無を確認中、結論は未確定

---

## L2（詳細・根拠・構造）

以下は、「788Dで発生したホシデンでのLCD反り起因の貼り付け不可」事象を起点に、「825Dのボンディング（ミネベア）で同様の問題が起きないか」を社内資料（Teams投稿・会議メモ/議事録・関連ドキュメント）で確認した範囲を、過不足なく整理したものです。

※結論や因果関係は、資料に明記がない部分は断定せず「確認中/未確定」と明記しています。

---

## 1) 起点：788D（ホシデン貼合）での「LCD反り → 貼り付け不可」発生状況（社内共有内容）

- 788DのPP0に向けてホシデンでボンディングを進めたところ、先行20台で“LCDの反りが大きく発生しSTOP”した、という社内共有がありました。
- その共有では、図面上は「反り0.4mm以内」想定に対し、目視で1～2mm程度ありそう、という記述があります。
- 続報として、ホシデン側でPP0のボンディング開始後、対象母集団の一部で反り確認が進み、162台の中でNGが出ている旨が共有されています（※この段階では「全数」ではない旨も併記）。

---

## 2) 事象の深掘り：ホシデン・天馬との会話/現場ヒアリングで確認されたこと（社内投稿）

社内の[DV_012_10.5吋,12.3吋,14吋 天馬LCD](https://teams.microsoft.com/l/message/19:84504c5cc2ef4cbdabb626e390b13fd3@thread.tacv2/1773658589148?tenantId=4863f5d6-4760-4589-be9c-42f82e075739&groupId=4107c2db-185c-442e-858b-171306253a8e&parentMessageId=1773658589148&teamName=TAM.24CY-Share-All&channelName=DV_012_10.5%E5%90%8B%2C12.3%E5%90%8B%2C14%E5%90%8B%20%E5%A4%A9%E9%A6%ACLCD&createdTime=1773658589148&EntityRepresentationId=aacef0f9-effb-4438-b469-a15230dcaf65)（件名「14inch LCD 不良発生」）で、以下の追加情報が共有されています。

### 2-1. 反りの発生タイミング・工程条件（未確定を含む）

- 受入検査後に全数アニールを掛けている（変色対策＋残留応力の目的）とのこと。
- アニール後に貼合装置へ投入して初めて反りが発覚した、という情報が共有されています。
- 一方で、反りが「アニール前からあったのか／アニール後に出たのか」は“調査中”と明記されています。

### 2-2. 反りの測定方法（現場での暫定運用）

- ホシデンでの測定として、定盤に対して液晶面を下に向け、隙間ができる箇所に隙間ゲージを入れて測定している、という手法が共有されています。

### 2-3. NG判定の内訳（途中経過）

- ホシデンへのヒアリング結果として、「127台中45台を確認し、NG相当2台（液晶面側の反り0.9mmが1台、0.6mmが1台）」という途中経過が共有されています。
- 併せて、規格内だが反りが大きめ（0.5mm、0.47mm等）も念のため避けているという運用が記載されています。

  

> 補足：上記は「確認途中の中間結果」として共有されており、最終的な母数・NG率の確定値としては扱えません。

### 2-4. 原因切り分けの論点（まだ結論なし）

- 投稿内では、設備のNG要因が“液晶面側ではなく外側（表側）”の問題かもしれないという見立ても出ていますが、この点も“問合せ中”とされています。
- トレイ形状が要因になり得るのでは、という懸念も挙がっていますが、正しいトレイかどうかも含め確認中と書かれています。
- さらに、過去に類似事象がありトレイ形状変更をした“うわさレベル”の話も触れられており、ここも確証はありません。

---

## 3) 825D（ミネベア貼合）への波及懸念：社内で実際に「同ロット影響」を確認しようとしている証跡

- [825D　PDT定例](https://teams.microsoft.com/l/meeting/details?eventId=AAMkADczNGQyZDYyLWUwMTQtNGE1My04NzU2LTAyMTk0YzBjM2VhMgFRAAgI3oLu94mAAEYAAAAACBpWWSOlL0uiorKLF-W7egcAqz9K-ikW4U_xq5FgdO5CuQAAAAABDQAAqz9K-ikW4U_xq5FgdO5CuQABI35-TwAAEA%3d%3d&EntityRepresentationId=79699b99-bc95-4625-99cc-94f28f716e03)（書き起こしあり）および同スレッドのTeams投稿で、「788D（ホシデン貼合）でLCD反りが発生している。ミネベアで進行中の825D 2SボンディングASSYは同じロットのLCDを使っているので、ミネベア側では問題がなかったか確認したい」という趣旨の問い合わせが明確に出ています。
- つまり、社内の認識としては

「788Dの反り不具合＝825Dにも波及する可能性がある（同ロット懸念）」があり、実際に“ミネベア側で不具合が出ていないか”を確認タスクとして扱っている、という状態です。

  

---

## 4) では結局、825Dのボンディング（ミネベア）で問題は“出ていない”と言えるのか？

今回の社内資料検索で見つかった範囲では、以下が限界です。

- 「ミネベアでの825D 2SボンディングASSYで反り起因の貼り付け不可が発生した」という確定情報（結果報告）は見つかりませんでした。

→見つかったのは「問題がないか確認する」という“問い”と、“確認中”のやり取りです。

- したがって、現時点のエビデンスベースでは

「788Dで起きたが、825Dでは起きていない」とは断定できません。

断定できるのは、“社内で同ロット影響の可能性を認識し、ミネベア側の状況確認を回し始めている”という事実までです。

  

---

## 5) 参考：今回確認できた「関連ドキュメント（存在）」— ただし“直接の結論”は書かれていない

- 825Dの進捗整理（PDT定例メモ）として、[825D　PDT定例　2026/3/16.onepart](https://jppanasonic.sharepoint.com/sites/ONL04024/_layouts/15/Doc.aspx?action=edit&mobileredirect=true&wdorigin=Sharepoint&DefaultItemOpen=1&sourcedoc={d56ec1e6-b7f3-4886-924f-4a2d9fb02d05}&wd=target%28/825D%E3%80%80PDT%E5%AE%9A%E4%BE%8B.one/%29&wdpartid={5f8ad07e-c290-0aad-3f79-d8cba97859a0}{1}&wdsectionfileid={80fa342b-5fb3-4062-8073-924035d87ef8}&EntityRepresentationId=2d900df8-239b-41d8-a65a-a19a83a0f122)などが存在し、2S/PP0の手配・納期・ボンディング段取りが整理されていますが、このメモ自体には“反り不具合が発生した/しない”の結論記載はありません。[1](https://jppanasonic.sharepoint.com/sites/ONL04024/_layouts/15/Doc.aspx?action=edit&mobileredirect=true&wdorigin=Sharepoint&DefaultItemOpen=1&sourcedoc={d56ec1e6-b7f3-4886-924f-4a2d9fb02d05}&wd=target\(/825D%E3%80%80PDT%E5%AE%9A%E4%BE%8B.one/ "825D_PDT定例")&wdpartid={5f8ad07e-c290-0aad-3f79-d8cba97859a0}{1}&wdsectionfileid={80fa342b-5fb3-4062-8073-924035d87ef8})[1](https://jppanasonic.sharepoint.com/sites/ONL04024/_layouts/15/Doc.aspx?action=edit&mobileredirect=true&wdorigin=Sharepoint&DefaultItemOpen=1&sourcedoc={d56ec1e6-b7f3-4886-924f-4a2d9fb02d05}&wd=target\(/825D%E3%80%80PDT%E5%AE%9A%E4%BE%8B.one/ "825D_PDT定例")&wdpartid={67e3c161-b2a9-44c4-831a-25bc2fa6e2b1}{1}&wdsectionfileid={80fa342b-5fb3-4062-8073-924035d87ef8})
- また、ボンディング図面レビューのメモ（[【825D K-zu】BONDING ASSY 図面 レビュー.loop](https://loop.cloud.microsoft/p/eyJ1IjoiaHR0cHM6Ly9qcHBhbmFzb25pYy1teS5zaGFyZXBvaW50LmNvbS9wZXJzb25hbC9lbmRvX21hc2FraTAwMV9qcF9wYW5hc29uaWNfY29tP25hdj1jejBsTWtad1pYSnpiMjVoYkNVeVJtVnVaRzhsTlVadFlYTmhhMmt3TURFbE5VWnFjQ1UxUm5CaGJtRnpiMjVwWXlVMVJtTnZiU1prUFdJbE1qRlRTMU1sTlVaTVkxRlZVMnRsUVZSalV6SnlVRmhCUzFvMVNUVllibVprWTFwR2FtOW5PVUpUWlV0RU5TVXlSRGhaYWtWWWJUZFlhbEpMZDFvMFlXSjJZekZzTmlabVBUQXhURmcxVVZrMU16SlRURXBUVFVjMFEwRldRVEkyVnpSRldrbzNORmhYUVRjbVl6MGxNa1kifQ%3D%3D?EntityRepresentationId=80cfa342-eabf-49d3-8902-28f5f9eaa2d9)）等はありますが、今回の論点（LCD反り起因の貼り付け不可）に対する結果報告の形ではありません。

---

# 結論（社内資料ベースで“言えること / 言えないこと”）

### 言えること（確定）

1) 788Dで、ホシデン貼合においてLCD反りが原因で貼り付けが止まったという社内共有があり、図面想定0.4mmに対して目視1～2mmという乖離が示されています。

2) ホシデン・天馬とのやり取りが進んでおり、アニール後に反りが顕在化した可能性、測定方法（隙間ゲージ）、中間のNG内訳（0.9/0.6mm）などが共有されています（ただし途中経過）。

3) 825Dについては、「同ロットLCDの可能性があるため、ミネベア貼合で問題が出ていないか確認する」という社内アクションが実際に立ち上がっています。

### 言えないこと（今回の検索結果だけでは未確認）

- ミネベア側の825D 2S貼合で、反り起因の貼り付け不可が“発生していない”という確証
- 反りの真因（アニール前後、トレイ形状、設備起因、液晶面/外面どちらの問題か）の最終結論

---

## 次の一手（“社内資料を確認した結果”として自然に繋がるアクション案）

※ここからは提案（推奨）です。事実ではありません。

- ミネベアの2S貼合状況（不具合の有無、反り検査の有無、検査方法）を結果として残す：現状は「確認したい」という問いが残っている状態なので、PDT定例の次回議事（[825D　PDT定例](https://teams.microsoft.com/l/meeting/details?eventId=AAMkADczNGQyZDYyLWUwMTQtNGE1My04NzU2LTAyMTk0YzBjM2VhMgFRAAgI3oLu94mAAEYAAAAACBpWWSOlL0uiorKLF-W7egcAqz9K-ikW4U_xq5FgdO5CuQAAAAABDQAAqz9K-ikW4U_xq5FgdO5CuQABI35-TwAAEA%3d%3d&EntityRepresentationId=79699b99-bc95-4625-99cc-94f28f716e03)）で“結果”として回収できると、横展開判断が早くなります。
- 788D側の“反り発生タイミング（アニール前後）”を確定させる：社内備蓄サンプルをホシデンで開梱し反り有無を見る、という方針が投稿にあるため、これを結果化すると「工程要因/部材要因」の切り分けが進みます。

---

もしよければ、上の「結論（言える/言えない）」をそのままPDT定例の共有文（200～300字）に整形した短縮版も作ります。

---
### 関連ノート
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
