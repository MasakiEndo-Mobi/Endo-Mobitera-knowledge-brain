---
doc_id: ops.project.ai-dx-enablement
title: AI/DX イネーブルメント（AI活用による業務効率化・社内展開）
doc_type: project
project: [ai-dx-enablement]
layer: canonical
role_in_story: execution
status: active
as_of: 2026-05-29
audience: [self, engineer, manager]
owners: [self]
one_line_thesis: ローカルLLMとクラウドAIツール(GitHub Copilot/NotebookLM/M365 Copilot等)を横断的に活用し、ハード設計・工場業務の効率化とAI前提のドキュメント文化(Markdown)を自部署・非開発者へ展開する横断イネーブルメント活動。
confidence: medium
phase: discovery
priority: medium
milestones:
  - name: M0 - 事例ヒアリング・現状把握
    target_date: 2026-05-27
    status: done
---

# AI/DX イネーブルメント

> **位置づけ**: 機構設計プロジェクト（825D 等）と並走する**横断テーマ**。特定機種の設計ではなく、AI活用による業務効率化と社内展開を追跡・推進する。OJT報告の AI 別軸（[[DEC-0002_ojt-focus-on-825d|DEC-0002]] / [[TASK-0003_ai-dx-separate-track|TASK-0003]]）の受け皿。

---

## プロジェクト概要

開発本部発の AI 活用の取り組みを、遠藤が機構設計側の視点で追跡・連携・展開するための横断プロジェクト。スコープは単一ツールに限定せず、以下を含む：

- **ローカルLLM**: LiteLLM（社内AIゲートウェイ）/ DX Spark / Qwen・Gemma 系モデル / Dify / Roo Code 等。機密業務向け。
- **クラウドAIツール**: GitHub Copilot Business（自律エージェント・Pythonスクリプト自動化）/ NotebookLM Enterprise（セキュアな社内情報入力・週次レポート自動生成）/ M365 Copilot 等。
- **ドキュメント文化**: AI が読みやすい Markdown / Obsidian 中心への移行（Excel方眼紙からの脱却）。
- **適用領域**: ハード設計（情報の属人化解消・CAD/電気図面解析の可能性）と工場（検査工程・DSL→Python移行・NG分析・BOM/設計変更の自動連携）。

背景は事例ヒアリング会議（[[2026-04-24_local-llm-hearing]] / [[2026-05-27_ai-agent-efficiency]]）で得た現状把握に基づく。Vision/Outcome の詳細は `requirements-grill` で後日詰める。

---

## 体制（暫定）

- **オーナー**: 遠藤 真輝（self・機構設計側の窓口/推進）
- **開発本部**: 高畠 大輔、下田 晋寛、鍵谷 泰成、渋井 研人、中尾 庄作 ほか（AI活用推進の中心）
- **関連動向**: DX戦略推進室（2026-07-01 新設予定。データマネジメント導入・開発リードタイム短縮・AI活用の意識改革）

---

## マイルストーン

| Milestone | Target Date | Status |
|---|---|---|
| M0 — 事例ヒアリング・現状把握 | 2026-05-27 | done |

> 以降のマイルストーン（横展開方法・効果測定KPI設計等）は未確定。確定次第このテーブルと frontmatter `milestones` を更新する。

---

## ディレクトリ構成（最小）

```
ai-dx-enablement/
├─ README.md           ← このファイル（プロジェクト定義）
├─ meetings/           ← 議事録（doc_type: meeting）
├─ daily-logs/         ← 日報（doc_type: daily-log）
├─ decisions/          ← 意思決定（DEC-NNNN_<slug>.md）
├─ tasks/              ← タスク（TASK-NNNN_<slug>.md）
├─ requirements/       ← Vision/Outcome/Capability/Feature/Eval/EngSpec（requirements-grill が書き出す）
└─ assets/             ← バイナリ
```

> 機構設計を伴わない横断活動のため `design-notes/` `test-reports/` は省略。必要になれば追加する。

---

## 関連リンク

- [[research_map]] — KB 全体マップ
- [[825d-overview|825D 車両データハブ]] — 並走する機構設計プロジェクト
- [[spo-path-converter|SharePointパス変換君]] — 関連する自作効率化ツール
