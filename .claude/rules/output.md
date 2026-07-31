---
paths:
  - "flava-fm/**"
  - "rave-team/**"
  - "aroma-insta/**"
---

# コンテンツ出力ルール

## 2 アカウントの分離（鉄則）

| アカウント | テーマ | 出力先 |
|---|---|---|
| Charlotte R1nR1n | レイブ・UK Bass・クラブカルチャー | `rave-team/output/EP-XX/` |
| FLAVA FM | アロマ・数秘・ハーブ・スピリチュアル | `flava-fm/output/POST-XX/` |

**2 アカウントのファイルを混ぜない。**

## 廃止パス

`aroma-insta/output/` は**廃止**。FLAVA FM の出力は `flava-fm/output/` に統合済み。
ここに新規ファイルを作らないこと。

## 成果物契約

EP / POST 1 本につき、以下の 4 点セットを作る:

- `carousel.md` — Instagram カルーセル
- `research.md` — リサーチメモ
- `caption.md` — 投稿キャプション
- `slides.json` — スライド定義

過去には `discussion.md` / `script.md` / `social.md` / `production_brief.md` を作る
7 エージェント構成があったが EP-02 前後で廃止した。復活させないこと
（経緯は `rave-team/agents/_archive/README.md`）。

## 連番

新規番号は `rave-team/output/episodes.md` / `flava-fm/output/posts.md` で確認して採番し、
生成後に同ファイルを更新する。
