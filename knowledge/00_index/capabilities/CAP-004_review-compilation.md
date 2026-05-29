---
doc_id: index.cap.review-compilation
title: CAP-004 月次面談資料の自動編纂
doc_type: requirement
project: [all]
layer: canonical
role_in_story: opportunity
status: draft
as_of: 2026-05-29
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: 蓄積した業務ログを成果×成長ロードマップで突合し、月次面談資料を自動編纂できる（中核ペインの解・未実装）
confidence: medium
requirement_level: capability
stability: volatile
grill_session: knowledge/80_sandbox/grill-sessions/2026-05-29_24CY_IVI_825D-V-vision.md
tags: [capability, review, growth, unimplemented]
relations:
  depends_on: [index.cap.intake, index.cap.structured-extraction, index.outcomes]
  related: [index.vision]
---

## L0（1文要約）

**daily-logs・decisions・tasks の蓄積を「成果 × 成長ロードマップ」で突合し、月次上司面談の資料を自動編纂できる能力。Vision の中核ペイン③の直接解であり、唯一の未実装コア Capability。**

---

## L1（5つの要点）

- **実装**: ❌ 新規実装が必要（既存スキルでカバーされない唯一のコア能力）。
- **前提**: 成長ロードマップ（評価軸）＝職場テンプレ **「Target Design」**。今年度は **2026-07 に作成予定**。これが揃うまで CAP-004 は実装しない。加えて daily-logs / decisions / tasks の継続蓄積が必要。
- **安定性**: `volatile` — 出力フォーマット・評価軸は試行錯誤で頻繁に変わる。
- **失敗時の振る舞い**: 自動編纂できない部分は「要手動補足」と明示し、黙って欠落させない。
- **Outcome 貢献**: 北極星「思い出し作業ゼロ率」と「月次面談資料の作成リードタイム」(Lagging) に**直接**寄与。

---

## L2（詳細）

### 独立進化・共通化
- CAP-001/002 の蓄積に依存する最下流の能力。
- ENDO **個人向け**（成長記録は本人の評価軸に依存するため共通化しない）。

### 実装スケジュールと前提タスク
- **実装時期: 2026-07**。職場の成長ロードマップテンプレ「Target Design」を今年度 7 月に作成するため、それを評価軸として取り込めるようになってから着手する。
1. **Target Design（成長ロードマップ）の作成・KB 化**（2026-07）— どの軸で成長を測るか。完成後に KB へ取り込む。
2. 業務ログ（日報・decision・task）の継続蓄積 ＝ CAP-001/002 の運用定着（7 月までの助走期間で蓄積）。
3. 突合ロジック・出力フォーマットの設計（F/S 層で詰める）。

### Outcome との紐付け
- 痛み③「毎回1から思い出してドキュメント化する負担」の中核解。North Star Quote「投げ込んでおけば KB が憶えていて、業務と成長が毎月繋がって見える」の実現主体。
