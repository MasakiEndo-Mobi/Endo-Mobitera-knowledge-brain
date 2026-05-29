---
doc_id: res.3d-printing.markforged-fx10
title: "Markforged FX10 仕様"
doc_type: research
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2025-08-18
audience: [self]
one_line_thesis: "Markforged FX10の仕様: FFF+連続繊維強化/金属、ビルドボリューム375×300×300mm。"
confidence: medium
tags: [markforged, 3d-printer]
source_docs: [from_old_kb/03_Resources/R-技術_Markforged_FX10.md]
---

## 要点（箇条書き）

- **プリント方式**：FFF（熱溶解積層）＋連続繊維強化／金属バインダーフィラメント積層 [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **ビルドボリューム**：375×300×300 mm（樹脂・複合材／金属とも同一ビルドエリア） [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **レイヤー精度**：50 μm・125 μm・250 μm（複合材）／ポストシンタリング後127 μm（金属） [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)[matterhackers.com](https://www.matterhackers.com/store/l/markforged-fx10-industrial-metal-and-composite-3d-printer/sk/MRX7KV1M?srsltid=AfmBOoqoh7QL09wQ1TH5OK8f-ECQptwo6UOgNj6Wpsp_M2tbTu8YAm-e&utm_source=chatgpt.com)
    
- **加熱チャンバー＆真空シールベッド**：チャンバー60 °C、真空シール付きアルミベッドで温度均一・高密着 [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **材料ラインアップ**：Onyx™系樹脂、連続炭素繊維／Kevlar®／HSHTファイバーほか、金属フィラメント（17-4 PH v2、316Lほか） [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **ソフトウェア機能**：Eiger™（スライス・シミュレーション・インスペクション）＋レーザーマイクロメーター＆Vision Module [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **本体寸法・重量**：760×640×1,200 mm、109 kg；電源230 V [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **拡張性**：標準で複合材、オプションのMetal Kitで金属3Dプリント対応 [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **用途例**：構造治具・金型・エンドユース部品・代替アルミ部品の速出力 [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    

---

## 詳しい説明

**1. プリント方式と精度**  
FX10はFFF方式をベースに、連続繊維を組み込むCFR（Continuous Fiber Reinforcement）と、金属バインダーフィラメント積層（Metal FFF）を1台で実現。樹脂・複合材では50–250 μm、金属ではポストシンタリング後に約127 μmの精度を保持し、小さな凹凸やホールも再現可能です [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)[matterhackers.com](https://www.matterhackers.com/store/l/markforged-fx10-industrial-metal-and-composite-3d-printer/sk/MRX7KV1M?srsltid=AfmBOoqoh7QL09wQ1TH5OK8f-ECQptwo6UOgNj6Wpsp_M2tbTu8YAm-e&utm_source=chatgpt.com)。

**2. 大型ビルドと環境制御**  
375×300×300 mmの大型ビルドエリアを、60 °Cまで加熱可能なチャンバーと真空シールベッドで維持。これにより、樹脂・金属いずれも**歪みや層間剥離を抑制**し、長尺品や高温成形が求められるワークにも対応します [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)。

**3. 多彩な材料対応**

- **複合材**：Onyx™（PA6+マイクロ炭素）・Onyx ESD™・Onyx FR™ほか、連続炭素繊維／Kevlar®／HSHTファイバー [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    
- **金属**：17-4 PH v2、D2 v2、Copper、H13といった金属フィラメント＋316L（Metal Kit適用時） [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)
    

これにより、**強度1.4倍～6倍**（Onyx比）からステンレス相当の高剛性部品まで、用途に応じて素材を選べます。

**4. 操作性と品質保証**  
Eiger™ソフトウェア上で**シミュレーション→スライス→プリント→インスペクション**まで一気通貫。ヘッド搭載レーザーマイクロメーターとVision Moduleが**印刷中に寸法検査・キャリブレーション**し、歩留まりと再現性を高めます [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)。

**5. 製造工程と後処理（金属）**  
Metal Kitで出力した「グリーンパーツ」は、洗浄（脱バインダー）→熱処理（シンタリング）を経て**密度99%超**の金属部品に仕上がります。これにより、**金型部品の試作や小ロット金属部品製造**が実現可能です [mark3d.com](https://www.mark3d.com/en/markforged-fx10/)。

---

### Markforged まとめ

1. **総括**  
    産業用金属・複合材3Dプリンタを展開する米 Markforgedは、ハード／クラウドソフト／材料を統合した「Digital Forge」を約70 か国に供給。24年売上132億円も訴訟費用で赤字。25年4月にNano Dimensionが1.16億ドルで買収し再建を図る。競合はStratasys等。
    
2. **主要財務指標（2024）**  
    売上132億円／営利▲134億円／純利▲133億円／営利率▲102%／ROE▲99%／自己資本比率51%
    
3. **事業構成**  
    ハード58%、消耗材27%、サービス15%
    
4. **販売先主要国**  
    米国、カナダ、日本、独、仏、伊、英、西、韓、中、印、豪 ほか約70 か国
    
5. **直近ニュース**
    

- 25/04/25 Nano社が買収完了
    
- 24/09/19 1:10株式併合を実施
    
- 24/08/27 FX10 Metal Kitを発表
    

6. **業績トレンド（億円）**  
    |期|24|23|22|  
    |売上|132|145|156|  
    |営利|▲134|▲172|▲134|
    
7. **リスク**  
    赤字継続と訴訟費用、買収後統合の遅延が財務・競争面の主要リスク。

8. **競合**  
    Stratasys, 3D Systems, Desktop Metal, Velo3D, EOS, GE Additive, HP, Carbon, Formlabs, Ultimaker, Prusa Research, Zortrax, Anycubic, Elegoo, Creality, Bambu Lab, Flashforge, MakerBot, BigRep, ExOne, SLM Solutions, Renishaw, Optomec, Xact Metal, Meltio, Sinterit, Farsoon Technologies, Eplus3D, UnionTech, Shining 3D, Raise3D, Roboze, CEAD, Massivit 3D, Nexa3D, Origin, Digital Alloys, Additive Industries, Aconity3D, Spee3D, Titomic, Aurora Labs, AML3D, Conflux Technology, InssTek, MELD Manufacturing, Sciaky, DM3D Technology, Fabrisonic, GE Additive, Trumpf, Concept Laser, Arcam, Voxeljet, Prodways, Lithoz, XJet, Nano Dimension, Stratasys Direct Manufacturing, Protolabs, Materialise, Sculpteo, Shapeways, Fictiv, Xometry, 3D Hubs, Craftcloud, FacFox, Quickparts, GoProto, Star Rapid, GKN Additive, Sandvik Additive Manufacturing, Höganäs, Carpenter Technology, ATI, Haynes International, QuesTek Innovations, Elementum 3D, Uniformity Labs, HRL Laboratories, Lawrence Livermore National Laboratory, Oak Ridge National Laboratory, Fraunhofer, EOS GmbH, SLM Solutions Group AG, Velo3D Inc., Desktop Metal Inc., 3D Systems Corporation, Stratasys Ltd., HP Inc., Carbon, Inc., Formlabs Inc., Ultimaker B.V., Prusa Research s.r.o., Zortrax S.A., Anycubic, Elegoo, Creality 3D, Bambu Lab, Flashforge, MakerBot Industries, LLC, BigRep GmbH, ExOne GmbH, SLM Solutions Group AG, Renishaw plc, Optomec Inc., Xact Metal Inc., Meltio, Sinterit, Farsoon Technologies, Eplus3D, UnionTech, Shining 3D, Raise3D, Roboze, CEAD, Massivit 3D, Nexa3D, Origin, Digital Alloys, Additive Industries, Aconity3D, Spee3D, Titomic, Aurora Labs, AML3D, Conflux Technology, InssTek, MELD Manufacturing, Sciaky Inc., DM3D Technology, Fabrisonic LLC, GE Additive, Trumpf GmbH + Co. KG, Concept Laser GmbH, Arcam AB, Voxeljet AG, Prodways Group, Lithoz GmbH, XJet Ltd., Nano Dimension Ltd., Stratasys Direct Manufacturing, Protolabs, Materialise NV, Sculpteo, Shapeways, Fictiv, Xometry, 3D Hubs, Craftcloud, FacFox, Quickparts, GoProto, Star Rapid, GKN Additive, Sandvik Additive Manufacturing, Höganäs AB, Carpenter Technology Corporation, ATI, Haynes International, QuesTek Innovations LLC, Elementum 3D, Uniformity Labs, HRL Laboratories, Lawrence Livermore National Laboratory, Oak Ridge National Laboratory, Fraunhofer-Gesellschaft.

---
### 関連ノート
- R-サプライヤ_Markforged
- R-meta-prompting-best-practices-japanese
- R-Tech_cfrtp_車載ディスプレイフレーム_技術調査レポート
- R-Tech_Keyence_3DP_IPアドレス
- R-Tech_ガラス強度評価_4PB_RoR
- R-Tech_板金部品のGNDフレームについて
- R-Tech_電気_性能動作マトリクス
- R-サプライヤ_UMI
- R-サプライヤ_ファソテック_AI設計代行調査レポート
- R-サプライヤ_ホシデンFD
- R-サプライヤ_中沼アートスクリーン
