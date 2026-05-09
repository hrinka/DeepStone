---
name: x-pulse
description: "Scan X/Twitter for what's trending on a topic — themes, voices, hooks, and post ideas. Triggers on: x-pulse, what's hot on X, X pulse, scan X for, trends on X, what should I post about, X trends."
---

# x-pulse: X トレンドスキャン

指定トピックについてXで何が起きているかをスキャンし、投稿アイデアとフックをvaultに保存する。Charlotte R1nR1n の発信タイミング判断に使う。

---

## 手順

1. ユーザーからトピックを受け取る。なければ聞く：「どのトピックをスキャンしますか？」
2. WebSearch で以下を実行（並行）：
   - `site:x.com "[topic]"` — 直近の投稿
   - `"[topic]" trending 2026` — トレンド記事
   - `"[topic]" discussion twitter` — 議論の流れ
3. 追加でWebSearch：`[topic] viral post format hook`

---

## 出力構造（このフォーマットで表示）

```
## WHAT'S HOT
- テーマ1：[説明] (例投稿スタイル)
- テーマ2：[説明]

## WHAT'S UNDEREXPLORED
- [まだ誰も言っていない角度]

## HOOKS THAT ARE WORKING
- [効いているフックの形式]

## VOICE & TONE
- [どんなトーンが響いているか]

## POST IDEAS FOR YOU TODAY
- TikTok: [具体的なアイデア]
- Instagram: [具体的なアイデア]
- X: [具体的なアイデア]
```

---

## 自動保存

スキャン後、`wiki/sources/X-pulse — YYYY-MM-DD — [topic-slug].md` に保存：

```yaml
---
type: x-pulse
date: YYYY-MM-DD
topic: "[topic]"
tags:
  - x-pulse
  - content-research
  - [topic-tag]
---
```

`wiki/log.md` の先頭に1行追記。

---

## Charlotte R1nR1n への適用

rave / dub / sound system / UK bass などのトピックで週1回実行すると、発信のタイミングと角度が明確になる。DeepStoneの知識 × X のリアルタイムトレンドを組み合わせる。

---

## 制約

WebSearch は X のリアルタイムデータにフルアクセスできない場合がある。「72時間以内のディスコースが見つからない」場合は `/autoresearch [topic]` にフォールバック。
