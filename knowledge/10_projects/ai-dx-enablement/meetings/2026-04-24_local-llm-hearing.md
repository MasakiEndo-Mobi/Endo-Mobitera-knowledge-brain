---
doc_id: ops.meeting.2026-04-24-local-llm-hearing
title: 開発本部 ローカルLLM活用事例ヒアリング会議
doc_type: meeting
project: [ai-dx-enablement]
layer: raw
role_in_story: context
status: completed
meeting_type: internal
as_of: 2026-04-24
audience: [self]
attendees: [遠藤 真輝, 中尾 庄作, 越下 裕貴, 小野 大智]
one_line_thesis: 開発本部のローカルLLM(Qwen/Gemma系・DX Spark・LiteLLM・Dify等)活用事例をヒアリング。機密業務向けローカルLLM継続拡大とMarkdown文化推進を確認。AI/DX横断テーマの種まき会議。
confidence: medium
relations:
  related: [ops.project.ai-dx-enablement, ops.decision.24cy-ivi-825d.ojt-focus-on-825d, ops.task.24cy-ivi-825d.ai-dx-separate-track, res.tooling.spo-path-converter]
tags: [ai-dx, local-llm, litellm, obsidian, markdown, hearing]
---

# 開発本部 ローカルLLM活用事例ヒアリング会議

## 会議概要

- **日時**: 2026年04月24日 10:30～11:10
- **参加者**:
  - 設計二部 機構設計PDTリーダー 遠藤 真輝
  - 開発本部 中尾 庄作
  - 開発本部 越下 裕貴
  - 開発本部 小野 大智
- **議題**:
  - 開発本部におけるローカルLLM活用事例の共有
  - AI活用による開発効率化・自動化の現状と課題
  - 今後の連携・展開可能性の確認

---

## アクションアイテム

> ※ AI/DXプロジェクト正式化後に compile-meeting で task 化する候補。

| 担当者 | 内容 | 期限 | 優先度 |
|---|---|---|---|
| 遠藤 真輝 | PASA SVO担当の高田氏へ連絡し、米国トレンド・AI活用事例をヒアリングする | 未定 | 中 |
| 遠藤 真輝 | 松下氏と共同開発中のSPO上Markdownツールを関係者へ紹介する | 未定 | 中 |
| 中尾 庄作 | 非開発者向けObsidian（Markdown）利用手順書を整備・展開する | 未定 | 中 |
| 中尾 庄作 | ローカルLLM活用の効果測定（KPI）案について意見募集・検討を進める | 未定 | 低 |

※担当者・期限が明示されていないものは文脈から補完／担当者で並び替え済み

---

## 決定事項

1. **ローカルLLM活用は継続・拡大方針**
   - 内容：機密情報を扱う開発業務については、引き続きローカルLLMを前提としたAI活用を進める。
   - 背景：クラウドAIでは扱えない社外秘・顧客情報を含むため。
2. **Markdownを中心としたドキュメント文化を推進**
   - 内容：AI活用前提のドキュメント管理として、Markdown形式（Obsidian等）の利用を推奨する。
   - 背景：Excel方眼紙ではAIに読ませにくく、知識活用・再利用性が低いため。

---

## 主な議論内容

### ローカルLLM導入の背景と全体像
- 現状：有志活動から始まり「少人数でも高効率な開発体制」を目標にAI活用を推進。Dify、Deep Wiki、Roo Code 等を組み合わせた実践的利用が進行中。
- 課題：組織全体への横展開、効果測定（KPI）が未整理。
- 方向性：開発工程全体（設計・実装・テスト）にAIエージェントを配置する構想。

### コーディング・設計・テストの自動化
- 現状：ソースコードから設計書自動生成／設計書・API仕様書からのコード自動生成（ビルド通過レベル）／テスト仕様書の期待値自動生成、UI多言語・画面自動テスト。
- 課題：プロジェクト予算がペンディングで一部停止。実装品質評価は今後の検討事項。
- 方向性：AI-DLC（AI駆動開発）やルールベース開発（Automotive SPICE、MISRA）の組み込み。

### ローカルLLM環境・運用
- 現状：DX Spark 約6台、複数のQwen系・Gemma系モデルを運用。LiteLLMで社内提供、APIキーはプロジェクト単位管理。
- 課題：サーバー維持費・運用コストの扱い。
- 方向性：月額費用申請を視野に入れた分離運用の継続。

### 非開発者・情報共有の課題
- 現状：非開発者向けAIツールのUI/UX設計が未成熟。Viva Engageでの情報発信は流れてしまい認知されにくい。
- 課題：活用状況の可視化・情報集約。
- 方向性：SPOページを中心に情報集約、Obsidianを「非開発者のメモ帳」として展開。

---

## 次回予定
- 日時：未定
- 主要議題：ローカルLLM活用の横展開方法／効果測定（KPI）設計の具体案

---

## 備考・補足
- 一部専門用語・固有名詞は音声不明瞭のため「推定」表記を含む。
- 不明点（例：特定ツール名・モデル名）は今後確認が必要。
- 本議事録は「事例ヒアリング」が主目的のため、明確な期限付き決定事項は少なめ。
- LiteLLM APIキー・BaseURL は別途発行され、`secrets/`（git管理外）に格納済（KBには記載しない）。

---

## 使用したツール
Powered by 議事録作成くん（M365 議事録作成くん）
