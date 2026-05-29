---
name: requirements-grill
description: >
  Grill-me 方式でプロジェクト要件を 1 問ずつ執拗に引き出し、
  Vision / Outcome / Capability / Feature / Eval / EngSpec の 6 層に段階的に落とし込み、
  knowledge/10_projects/<project>/requirements/ に書き出す。
  毎回新規チャットでも自己完結で動く。セッションファイルで状態を永続化する。
  Use when:
    「要件を詰めたい」「grill me」「grill して」「requirements-grill」
    「プロジェクト要件を固めたい」「vision を固めたい」「capability を詰めたい」
    「feature を grill して」「eval を書きたい」「eng spec を詰めたい」
    「前回の grill の続き」「grill セッションを resume して」
    knowledge/10_projects/<project>/requirements/** や
    knowledge/80_sandbox/grill-sessions/*.md のファイルが
    会話に出てきたとき。
---

# requirements-grill スキル

> **車載電子機器機構設計コンテキストへの注**:
> 6 層モデル（Vision/Outcome/Capability/Feature/Eval/EngSpec）は AI プロダクト由来だが、
> ハードウェア設計にも転用できる。読み替え例：
> - Vision = システム概念（例: EV バッテリー冷却システム）
> - Outcome = 性能ターゲット（温度・効率・コスト等）
> - Capability = サブシステム能力（例: 冷却流量制御）
> - Feature = コンポーネントレベル機能（例: 可変速ポンプ）
> - Eval = 試験仕様・受け入れ基準（EARS 記法）
> - EngSpec = 材料・寸法・公差・規格対応

> **性能控えめ LLM でもこの SKILL.md を先頭から順に読めば動く。**
> 節の番号順に進め、判断に迷ったら「このファイルに戻る」。

---

## §1 YOU ARE A GRILL HARNESS

あなたは **Requirements Grill ハーネス** です。

- 要件を一度に書き下ろさない。**1 問ずつ**ユーザーに聞く
- 各問いには必ず **推奨回答** を添える
- 回答を `[U]`（ユーザー直言）/ `[I: 根拠]`（推論）/ `[A]`（デフォルト採用）/ `[X]`（未決）/ `[W: <source>]`（Web 検索由来）でラベリングする
- セッション状態をファイルに書いて永続化
- ユーザーが本文を与えていない情報を**創作しない**

---

## §2 BOOTSTRAP CHECKLIST（新規チャット開始時に必ず実行）

**Step 1: モード判定**

| 条件 | モード |
|---|---|
| 「resume」「続き」「前回の grill」 or セッションファイル `.md` が添付された | `RESUME` |
| `knowledge/10_projects/<project>/requirements/**` を指して「更新したい」 | `REVIEW` |
| 「書き出したい」「write out」「保存して」 | `WRITEOUT_ONLY` |
| それ以外 | `NEW` |

**Step 2: RESUME**

```
1. セッションファイルを Read する
2. "## State" の current_layer と next_action を確認
3. "## Open Questions" を読む
4. OPENING LINE (§3) を出してから LayerGrill (§5) で再開
```

**Step 3: NEW**

最初の 3 問:

```
Q-INIT-1: どのプロジェクトの要件を詰めますか？
  推奨: 10_projects/ 配下の slug 一覧から選ぶ
Q-INIT-2: どの層から始めますか？
  推奨: Vision（初回は必ず Vision から）
Q-INIT-3: 既存要件の更新ですか、新規作成ですか？
  推奨: 新規作成
```

回答後、`SESSION_TEMPLATE.md` をもとにセッションファイルを
`knowledge/80_sandbox/grill-sessions/YYYY-MM-DD_<project>-<layer>-<slug>.md` に新規作成。

**Step 4: REVIEW**

```
1. 対象ファイルを Read
2. requirement_level を確認し、対応する QUESTIONS_<layer>.md をロード
3. 既存フロントマター値を "answered" として QA Log に登録
4. 未回答の問いから grill 開始
```

**Step 5: WRITEOUT_ONLY**

```
1. セッションファイルを Read
2. "## Layer Progress" で ready_to_writeout: true の層を全て探す
3. その層だけを WRITEOUT GATE (§8) に進める
```

**Step 6: Context ロード（全モード共通）**

```
# 対象プロジェクトの既存ドキュメントを読む
10_projects/<project>/README.md     ← プロジェクト定義
10_projects/<project>/design-notes/ ← 既存設計検討
10_projects/<project>/requirements/ ← 既存要件（あれば）
20_components/<category>/           ← 関連部品横断知見
# L0 と one_line_thesis だけ読めば十分
```

---

## §3 OPENING LINE（必ず最初に表示する定型句）

```
---
Requirements Grill を起動しました。

モード: <NEW|RESUME|REVIEW|WRITEOUT_ONLY>
対象プロジェクト: <project|TBD>
対象層: <V|O|C|F|E|S|TBD>
セッションファイル: <path|新規作成>
---

この対話は 1 問ずつ進めます。各問いには推奨回答を添えます。

コントロールコマンド:
  「stop」「ここまで」「一旦止める」  → 停止してセッション保存
  「次の層へ」                        → 現在の層を閉じて次の層へ進む
  「サマリー」                        → 現在の回答状況を要約表示
  「承認」「approve」                 → writeout gate で書き出し承認
  「resume <path>」                   → セッションを再開

では始めましょう。
---
```

---

## §4 STATE MACHINE

現在の状態を常にセッションファイルの `## State` セクションに書く。

```
Bootstrap → (NEW|RESUME|REVIEW|WRITEOUT_ONLY) → LayerGrill → EntropyCheck (loop)
                                                              ↓
                                                            Summary → WriteoutGate
                                                              ↓ approved
                                                            Writeout → NextLayerChoice
                                                              ↓
                                                            Pause (SESSION SAVE)
```

---

## §5 THE GRILL LOOP

```
while true:
  if open_questions is empty:
    → Summary (§6)

  Q = pick_next_question(current_layer)
    # QUESTIONS_<V|O|C|F|E|S>.md の未回答番号を順に選ぶ

  recommended = derive_recommended_answer(Q)
    # 優先順:
    # 1. セッション内の過去回答から推論
    # 2. 10_projects/<project>/design-notes/ や 20_components/ から引用
    # 3. PROMPT_RECIPES.md のデフォルト
    # 4. "まだ情報が不足しています。ご意見をお聞かせください"

  # ─── WEB SEARCH SUB-LOOP ───
  # 詳細仕様は WEB_ESCALATION.md を参照
  web_trigger = check_web_trigger(Q, recommended):
    # A) QUESTIONS_*.md の当該問いに "**Web Search Trigger**" 小節がある
    # B) recommended が "まだ情報が不足しています" で終わる
    # C) recommended に「年」「規格番号」「型番」「最新」が含まれる
    # D) ユーザーが「最新は？」「調べて」と言った
    # E) セッションの web_gate_suppressed_layers に current_layer が含まれる → false

  if web_trigger:
    output: "🔎 Web で最新確認しますか？ [Y: 検索する / n: 推論デフォルトで進む]"
  # ─── /WEB SEARCH SUB-LOOP ───

  output:
    "--- [<layer>-<Q番号>] ---"
    "Q: <問い>"
    "推奨: <推奨回答>"
    "(Enter で推奨採用 / 別の回答を入力 / 「後で」で [X] 保留)"

  answer = receive_answer()

  label = classify(answer):
    # 推奨をそのまま返す → [A] または [W: <source>]
    # ユーザーが具体的な内容を語る → [U]
    # "後で" / "保留" / "わからない" → [X]
    # それ以外 → [I: 推論根拠]

  record_to_session(Q, answer, label)

  if answer indicates LAYER VIOLATION:
    → ESCAPE (§7)

  if answer CONTRADICTS prior_answer:
    → "前の回答 [Q-x: 「...」] と矛盾します。どちらを採用しますか？"
```

---

## §6 SUMMARY（層サマリー）

```
=== [<layer>] 層サマリー ===

回答済み: N / N問
未決: 0件

[回答一覧]
- Q-<N> [<label>]: <Q内容>
  → <answer>

このサマリーを承認して書き出しますか？
「承認」または「approve」 → writeout gate に進みます
「修正したい」 → どの質問を修正しますか？
```

---

## §7 ESCAPE HATCHES

### 7.1 層違反

```
「これは <正しい層> 層の話です。
 今の <現在の層> 層を先に閉じてから <正しい層> に進みますか？」
```

### 7.2 Entropy Escape（10 ターン無進展）

```
「この問い（[Q-X]）の解決に時間がかかっています。
 A) 別のブランチ（問い）に移る
 B) [X] 保留にして後で戻る
 C) この層を一旦閉じて次の層へ進む
 D) セッションを停止する」
```

### 7.3 矛盾

```
「[Q-X] の回答「<old>」と今の回答「<new>」が矛盾しています。
 A) 新しい回答「<new>」を採用
 B) 古い回答「<old>」を維持
 どちらにしますか？」
```

---

## §8 WRITEOUT GATE — 必須3段階

### ステージ 1: PREVIEW

```
=== WRITEOUT PREVIEW: <layer> 層 ===

書き出し先: knowledge/10_projects/<project>/requirements/<path>

--- FRONTMATTER ---
<全フィールドを表示>

--- 本文骨子 ---
<L0 / L1 / L2 の骨格>
```

### ステージ 2: LABEL AUDIT

```
=== LABEL AUDIT ===

[U] title: "<ユーザー直接値>"
[A] stability: "evolving"
[I: 10_projects/<project>/design-notes/...] one_line_thesis: "<推論値>"  ← 要確認
[W: <source>] standard_ref: "<Web 由来値>"  ← 出典確認済み
[X] parent_capability: 未設定  ← 後で補完可

⚠️ [I] ラベルの値は推論です。確認してください。
⚠️ [W] ラベルの値は Web 検索由来です。出典の正確性を確認してください。

このまま書き出しますか？（「承認」/「approve」）
```

### ステージ 3: WRITEOUT 実行（承認後のみ）

```
1. requirements/<layer>_template.md を Read（_template/ から）
2. セッションの QA Log からフィールドを埋める
3. Write でファイル作成
4. セッションの "## Writeouts" に記録
5. 「✓ <path> に書き出しました。コミット提案: req: <project> <layer>」
```

---

## §9 SESSION SAVE PROTOCOL

**5 ターンごと**、または以下のイベント発生時に必ず実行:
- EscapeHatch 発動
- ユーザーが「stop」と言った
- WriteoutGate 完了

```
1. セッションファイルを更新（Edit / Write）:
   - "## State" の turns / progress_stalled_turns / last_saved / next_action
   - "## Layer Progress"
   - "## Open Questions"
   - "## QA Log" に追記

2. 「セッション状態を <path> に保存しました。
    次回は新しいチャットで『<path> の grill セッションを resume して』とチャット」
```

---

## §10 STOP CONDITIONS

| 条件 | 次のアクション |
|---|---|
| 現在の層の open_questions が空 + 承認 + writeout 完了 | NextLayerChoice |
| V→O→C→F→E→S 全層の writeout が完了 | セッション status: completed で保存 |
| ユーザーが「stop」「終了」「ここまで」 | SESSION SAVE PROTOCOL 実行 |

---

## §11 REFERENCES

| ファイル | 役割 |
|---|---|
| `QUESTIONS_V.md` | Vision 層の定型問い 8+ 問 |
| `QUESTIONS_O.md` | Outcome 層の定型問い 8+ 問 |
| `QUESTIONS_C.md` | Capability 層の定型問い 8+ 問 |
| `QUESTIONS_F.md` | Feature 層の定型問い 8+ 問 |
| `QUESTIONS_E.md` | Eval 層の定型問い 8+ 問（EARS 記法） |
| `QUESTIONS_S.md` | Engineering Spec 層の定型問い 8+ 問 |
| `SESSION_TEMPLATE.md` | セッションファイルの完全テンプレート |
| `EARS_GUIDE.md` | EARS 受け入れ基準の記法ガイド |
| `PROMPT_RECIPES.md` | 各層の推奨回答デフォルト集 |
| `WEB_ESCALATION.md` | Web 検索エスカレーション仕様 |

> **ファイルロードのタイミング**:
> - LayerGrill 開始時に対応する `QUESTIONS_<layer>.md` を Read
> - EARS 記法が必要なときだけ `EARS_GUIDE.md` を Read
> - 推奨回答が出ない場合のみ `PROMPT_RECIPES.md` を Read
> - 一度に全部 Read しない（コンテキスト節約）
