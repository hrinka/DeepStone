---
name: x-read
description: "Deep-read an X post or thread — verbatim content, TL;DR, key claims, reply sentiment, voices to watch. Triggers on: x-read, read this tweet, read this X post, analyze this X link, what's in this tweet."
---

# x-read: X 投稿ディープリード

XのポストURLを受け取り、内容・スレッド・主張・返信センチメントを構造化して読む。

---

## 手順

1. URLを受け取る。なければ聞く：「どのX投稿URLですか？」
2. WebFetch でそのURLを取得
3. 必要に応じてスレッド全体をWebFetchで追跡
4. WebSearch で投稿者の関連情報・文脈を補完

---

## 出力構造（このフォーマットで表示）

```
## ORIGINAL POST
[投稿の完全テキスト]

## THREAD
[スレッドの続きがある場合]

## TL;DR
[1〜2文の要約]

## KEY CLAIMS
- [主張1]
- [主張2]

## REPLY SENTIMENT
[賛成 / 反論 / 無反応 の比率と代表例]

## NOTABLE COUNTER-ARGUMENTS
- [反論の内容]

## VOICES TO WATCH
- [@handle]: [なぜ注目すべきか]
```

---

## 保存（明示的に頼まれた場合のみ）

ユーザーが「保存して」と言った場合のみ `wiki/sources/X-read — YYYY-MM-DD — [slug].md` に保存：

```yaml
---
type: x-read
date: YYYY-MM-DD
post-url: "[url]"
tags:
  - x-read
  - [topic-tags]
---
```

**デフォルトはチャット表示のみ。自動保存しない。**

---

## Charlotte R1nR1n への適用

気になるrave / dub関連のアカウントや投稿をその場で深く読める。返信のセンチメントを見ることで「どんな角度が刺さるか」の判断材料にする。

---

## 制約

公開投稿のみ有効。非公開アカウントの投稿はWebFetchでアクセスできない。その場合はユーザーにスクリーンショットのテキストを貼り付けてもらう。
