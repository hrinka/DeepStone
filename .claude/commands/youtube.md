---
name: youtube
description: "Extract content from a YouTube video — transcript, summary, key points, themes, and vault-ready notes. Triggers on: youtube, summarize this video, what's in this video, extract this YouTube link, transcribe this video."
---

# youtube: YouTube 動画知識化

YouTubeのURLを受け取り、トランスクリプト・要約・キーポイントを抽出してvaultに保存する。DJセット・レクチャー・ドキュメンタリーをDeepStoneの知識に変換する。

---

## 手順

1. URLまたは動画IDを受け取る。なければ聞く：「どのYouTube動画ですか？」
   - 対応形式：`https://www.youtube.com/watch?v=...` / `https://youtu.be/...` / `https://www.youtube.com/shorts/...`

2. WebFetch でYouTubeページを取得（タイトル・チャンネル・説明欄・自動字幕）

3. WebSearch で動画関連情報を補完：
   - `"[video title]" site:youtube.com`
   - `"[channel name]" [topic]`

4. 内容を構造化して分析

---

## 出力構造（このフォーマットで表示）

```
## VIDEO INFO
- タイトル：
- チャンネル：
- 長さ・公開日（取得できる場合）

## TL;DR
[1〜3文の要約]

## KEY POINTS
- [ポイント1]
- [ポイント2]
- ...

## NOTABLE QUOTES
> "[印象的な発言]"

## THEMES & TOPICS
- [[関連concept]] との接続
- [[関連entity]] との接続

## WORTH FOLLOWING UP ON
- [この動画から派生する調査トピック]
```

---

## 自動保存

デフォルトで `wiki/sources/YouTube — YYYY-MM-DD — [video-title-slug].md` に保存：

```yaml
---
type: source
source_type: video
title: "[動画タイトル]"
channel: "[チャンネル名]"
url: "[URL]"
date_published: YYYY-MM-DD
fetched: YYYY-MM-DD
tags:
  - youtube
  - [topic-tags]
confidence: medium
related:
  - "[[関連ページ]]"
---
```

`wiki/log.md` の先頭に1行追記。`wiki/index.md` の Sources セクションに追加。

---

## DeepStone への適用

Charlotte R1nR1n の発信に直結する動画カテゴリ：
- King Tubby / Augustus Pablo / Lee Perry のドキュメンタリー
- Kingston Dub Club の映像
- UK Sound Systemのドキュメンタリー
- DJセット（Burial、Digital Mystikz、Jah Shakaなど）
- rave culture 関連のレクチャー・インタビュー

---

## 制約

自動字幕がない動画（非英語・字幕オフ）は説明欄のみ取得。その場合は「字幕が取得できませんでした。説明欄の情報のみで処理します。」と明示する。
