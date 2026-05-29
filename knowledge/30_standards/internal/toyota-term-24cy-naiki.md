---
doc_id: std.internal.toyota-term-24cy-naiki
title: "TOYOTA用語: 24CY内機セット仕様書"
doc_type: standard-note
project: [all]
layer: raw
role_in_story: context
status: draft
as_of: 2025-08-18
audience: [self]
one_line_thesis: "24CY内機セット仕様書はAVN一体機/別体DisplayでLCD/カバーガラス/タッチパネルを共通化し19ePFv2/v3に適用。"
confidence: medium
tags: [toyota, terminology, 24cy]
source_docs: [from_old_kb/03_Resources/R-TOYOTA_用語_24CY内機.md]
---

(旧KB埋め込み: 120_24CY_共通Display内機セット仕様書_Ver6.60_20241213.pdf)
### 1. イントロ：最重要ポイント (5 分で把握)

- **対象範囲**は 24CY向け「AVN一体機」および「別体Display」の両内機セット。LCD／カバーガラス／タッチパネルを共通化し、19ePFv2・19ePFv3プラットフォームに適用。
    
- **改訂履歴が頻繁**（2021-08 初版→2024-12 Ver 6.60）。直近は 9.8-inch ライン削除・タッチ固着検知追加など、設計変更点を必ず確認。
    
- **法規順守**は KT法・VOC (TIS01204-00C24)・SOC (TSZ0001G) 等。調達／品質で即チェック必須。
    
- **インターフェースと画質制御**は 40 pin LVDS×2＋I²C／SPI。ユーザ調整は輝度・コントラスト各63 step、ソース別テーブル管理。
    
- **SW／照明仕様が複雑**（昼夜・プレ起動・レオスタット連動）。車両別チューニング前提なので、担当間で引継ぎ時にテーブルを共有すること。
    

---

### 2. セクション 1：仕様書の概要 (What & Why)

1. **目的と適用モデル**
    
    - 24CY 共通 Display 内機のハード／HMI要件を一本化しコスト低減と開発リード短縮を狙う。対象は AVN Assy（統合型）と Display Assy（別体型）。
        
2. **構成要素**
    
    - LCD パネル (in-cell touch)
        
    - DISP PCB（場合により省略し LCD⇄AVN直結）
        
    - Cover Glass（AG/AR/AFP 標準、AR/AFP オプション）
        
    - BT/Wi-Fi アンテナ etc.
        
3. **サイズ展開**
    
    - 14″/12.9″/12.5″/12.3″/10.5″/9.8″/8″（※8″, 9.8″は24CY時点で削除済）。各サイズでヒーコン一体型（トグル／ダイヤル）と標準型を用意。
        
4. **法規・認証 / TOYOTA順守**
    
    - SOC, VOC, 内突, プラスチック材質マーキング, EAR ほかを網羅。生産前に調達部門とコンプライアンスレビューが必須。
        

---

### 3. セクション 2：主要プロセスと技術ポイント

1. **ディスプレイ仕様**
    
    - **外形 & AA**：解像度 1920×1080 (14″/12.9″)、1600×720 (12.5″)…厚さ 6.7-7.6 mm。
        
    - **光学特性**：Assy輝度 400 cd/m² min (LCF無)、コントラスト 1000 : 1 min。視野角±30°/0°。
        
    - **画質調整**：Video ICで入力ソース毎に階調テーブルを持ち、RGB/YUV オフセット・ゲインを独立制御。
        
2. **Cover Glass**
    
    - **厚み 1.2–1.3 mm**、AG/AR/AFP 標準。反射率 SCI 1.5 % max、SCI-SCE 1 % max。指滑り μ≤1.50。
        
    - **AR/AFPのみ仕様**は北米高輝度車向けオプション。
        
3. **タッチパネル**
    
    - 精度 ±1.2 mm (core)／±2.0 mm (edge)。グローブ対応（薄皮・布・フリース）。マルチタッチ 2本指、30 ms 以内応答。
        
    - **タッチ固着検知**：30 秒連続入力で自動リキャリブレーション (Ver 6.50追加)。
        
4. **入力／電気 I/F**
    
    - DISP PCB⇄LCD：CN1/CN2 各40 pin LVDS ×2 (A/Bポート)＋SPI/I²C、CN3で SW 信号。Frame Rate 59.94 Hz固定。
        
5. **HMI 部品**
    
    - **Toggle SW**：温度 UP/DOWN。Click rate 30 %、ストローク 1 mm, F0 3 N (Lexus)／4 N (Toyota)。
        
    - **Dial (14″のみ)**：30 click /360°、12°/step、Torque 13.3 ± 10 mN·m。
        
    - **PWR/VOL Knob**：Push + Encoder (ダイヤル推奨)。
        
    - **SW照明**：昼夜輝度・レオスタット・プレ起動 (55 s) シーケンスあり。
        
6. **照明 & 点灯条件**
    
    - 昼照明有⇄無／ヒーコン一体⇄標準で4 パターン定義。電源線 (+B, ACC, IG, ILL+, ADIM2) の組合せで On/Off。
        
7. **個別 Display Assy 仕様**
    
    - 質量目標 12.3″ : ≤1.32 kg、8″ : ≤0.86 kg。暗電流 0.27 mA max。
        

---

### 4. セクション 3：関係者・関連資料

| 区分             | 主担当                                          | 連携先          | 主要ドキュメント                    |
| -------------- | -------------------------------------------- | ------------ | --------------------------- |
| プロジェクト管理       | 3DPV6G (N. Fujimura / K. Hamajima / T. Kato) | 各車種 PL、調達    | 本仕様書 Ver 6.60               |
| HMI 仕様         | HMI チーム                                      | SoC SW、UI/UX | 203_HMIプロジェクト共通定義書 Appendix |
| 映像処理 IC        | 電装設計                                         | LCD サプライヤ    | 100_マルチメディアシステム仕様書          |
| 法規対応           | 品質保証                                         | 調達、材料        | TSZ0001G, TIS01204-00C24 等  |
| Tier-1 (Panel) | 車両別パネルベンダ                                    | Tier-2 (LCD) | 114_MMパネル設計ガイドライン           |

---

### 5. 結論・次に取るべきアクション

1. **最新バージョンの反映**
    
    - 24CY/Ver 6.60 が最新版。旧モデル（ePF3.0, 8″/9.8″ディスプレイ含む）を扱うプロジェクトはリスク分析を行い差分を明示する。
        
2. **車種別カスタマイズ表の整備**
    
    - サイズ、照明モード、SW有無、F/S値など可変パラメータを Excel マスターに集約し、Tier-1／車両PLと共有。
        
3. **法規・認証チェックリスト**
    
    - VOC、SOC、KT法、EAR、内突などを網羅したチェックシートを品質部門と共同で更新し、サプライヤ監査時に使用。
        
4. **画質調整テーブル管理フロー**
    
    - HMI チームと協働し、ソース ID ↔ ユーザ調整テーブルのリビジョン管理を Git で一元化。
        
5. **タッチ固着フェールセーフ試験**
    
    - 新規追加機能（Ver 6.50）に対し、環境試験と量産 EOL テスト手順を策定。
        
6. **量産変更管理**
    
    - 今後の改訂は「変更履歴」章を必ず起点にし、影響範囲 (HW, SW, 試験, 法規) を Red mark でトラッキングする運用を継続。
        

---

---
### 関連ノート
- P-24CY_310D
- P-24CY_695D_696D
- P-24CY_825D
- P-24CY_838D
- R-TOYOTA_用語_DR
- R-TOYOTA_用語_RDDP
- R-TOYOTA_用語_外設申
- R-TOYOTA_用語_支給
- R-TOYOTA_用語_管理自給
- R-TOYOTA_用語_開発フェーズ
- R-サプライヤ_ホシデンFD
- R-サプライヤ_中沼アートスクリーン
- P-24CY-400D
- P-24CY_410D
- P-24CY_744D
- P-24CY_744D_summary
- P-24CY_825D_1SDR_議事録
- P-24CY_825D_DR0_DRBFM_review_part1
- P-24CY_825D_DR0_DRBFM_review_part2
- P-24CY_825D_DR0_issues_summary
- P-24CY_825D_DRB_review
- P-24CY_825D_HiddenSW_meeting_minutes
