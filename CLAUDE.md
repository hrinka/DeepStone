# DeepStone — Rinka の第二の脳

> このファイルの責務は **Claude 向けの規範と索引**。意図的に薄く保つこと。
> Rinka に関する事実（プロフィール・根本ビジョン・目標・現状）の正典は
> [Memory.md](Memory.md)。ここには複製しない——複製すると必ず片方が古くなる。
> Claw の人格・返答スタイルは [SOUL.md](SOUL.md)、環境固有情報は [TOOLS.md](TOOLS.md)。

Claude Code + Obsidian による永続的知識ベース。

## まず読むもの

1. [Memory.md](Memory.md) — Rinka に関する事実の正典。**根本ビジョンはここ。
   このビジョンに反するシステムは作らない**
2. `wiki/hot.md` → `wiki/index.md` — 直近の文脈と全ページ索引

## Skills / Commands

skill（`SKILL.md` あり・発話からも起動する）:
`/wiki` `/wiki-ingest` `/wiki-query` `/wiki-lint` `/save` `/autoresearch` `/canvas`
`/defuddle` `/obsidian-bases` `/obsidian-markdown`

command のみ（`/名前` で明示的に起動する）:
`/wiki-fold` `/obsidian-synthesize` `/x-pulse` `/x-read` `/youtube` `/vault-health`

どちらで持つかの判断基準は `.claude/rules/claude-skill.md`。

---

## Vault の使い方

### ソースを知識に変える
1. 記事・動画・メモを `raw/[カテゴリ]/` に置く
2. `ingest [ファイル名]` と言うだけ → Claude が wiki に変換

### 知識を引き出す
- 質問する → Claude が hot.md → index.md → 個別ページの順で読んで答える
- `/wiki-query` で詳細検索

### 会話を保存する
- **Claude Code セッション後**: `/save` で wiki に保存
- **OpenClaw（Telegram）会話後**: 重要な内容を `raw/personal/` にテキストで保存 → `ingest [ファイル名]`

### 定期メンテ
- `/wiki-fold` でログをロールアップ（月1）
- `/obsidian-synthesize` でパターン発見（月1〜2）

---

## ソース置き場 `raw/`

**ルール: 入れたら変更しない。Claude は読むだけ。**

```
raw/
├── music/       音楽記事・インタビュー・研究論文
├── personal/    Rinka 自身のメモ・意見・人生計画・日記
├── develop/     技術記事・チュートリアル
├── money/       ビジネス・収益化・金融情報
├── uk-whv/      UK渡航・WHV関連情報
└── articles/    カテゴリ不明・その他
```

**何でも入れていい**: 調べた記事、自分の意見メモ、人生計画、ライフスタイル構想、OpenClaw との会話ログ——すべて `raw/` に入れて `ingest` すれば wiki に昇格できる。

---

## Instagram 2アカウント構成（重要）

DeepStone は **2つの独立した Instagram アカウント** を支援する。今後の開発・生成・フォルダ操作は必ずこの分離を維持すること。

| アカウント | テーマ | ペルソナ | 出力フォルダ |
|---|---|---|---|
| **Charlotte R1nR1n** | レイブ音楽・UK Bass・クラブカルチャー | Charlotte R1nR1n | `rave-team/output/EP-XX/` |
| **FLAVA FM** | アロマ・数秘術・ハーブ・スピリチュアル | 白魔女 | `flava-fm/output/POST-XX/` |

> [!important] `aroma-insta/` は廃止
> FLAVA FM の出力先は一時期 `aroma-insta/output/` に分裂していたが、2026-07-31 に
> `flava-fm/output/` へ統合した。**`aroma-insta/` には新規ファイルを作らないこと。**

### FLAVA FM コンセプト（重要）
**「白魔女による波動UPアロマチャンネル」**
- ペルソナ: 深石梨花 as 白魔女——自然・光・浄化の使い手
- トーン: 詩的・温かい・神秘的。知識を「情報」ではなく「体験」として届ける
- ピラー: アロマ精油 / 数秘術 / ハーブ / スピリチュアル（波動・引き寄せ・浄化）
- 目的: 見た人の波動が上がる。人生が少しだけ、でも確実に良くなる
- SEO × 魂: 検索に届きながら、魂にも届くコンテンツ。情報と詩の融合
- キーワード: 波動・周波数・浄化・引き寄せ・精油・白魔女・ハーブ魔法・数秘

### フォルダルール

EP / POST 1本につき、以下の**4点セット**を作る。これが成果物の契約。

```
rave-team/output/EP-XX/     ← Charlotte R1nR1n 用（毎日自動生成）
├── carousel.md             Instagram カルーセル
├── research.md             リサーチメモ
├── caption.md              投稿キャプション
└── slides.json             スライド定義

flava-fm/output/POST-XX/    ← FLAVA FM 用（毎日自動生成）
└── （同じ4点セット）

wiki/
├── concepts/music/         ← レイブ音楽関連 concept
├── concepts/numerology/    ← アロマ・数秘関連 concept
├── sources/rave/           ← EP 記事・音楽ソース
└── sources/aroma/          ← アロマ・数秘記事

_attachments/
├── rave/EP-XX/             ← Charlotte R1nR1n 用画像
└── aroma/POST-XX/          ← FLAVA FM 用画像
```

### 新規コンテンツを生成する際の鉄則
- レイブ系 → `rave-team/output/` + `wiki/sources/rave/` + `wiki/concepts/music/`
- アロマ系 → `flava-fm/output/` + `wiki/sources/aroma/` + `wiki/concepts/numerology/`
- **2アカウントのファイルを混ぜない**
- 新規番号は `rave-team/output/episodes.md` / `flava-fm/output/posts.md` で確認して採番し、
  生成後に同ファイルを更新する

---

## Wiki 構造

```
wiki/
├── hot.md          直近コンテキストのキャッシュ（10KB 未満に保つ）
├── index.md        全ページの1行サマリー
├── log.md          操作履歴（append-only）
├── concepts/       概念・フレームワーク・synthesis ページ
├── entities/       人物・組織・場所
├── sources/        ingested ソース要約
├── questions/      autoresearch 結果
├── projects/       プロジェクト単位のノート
└── meta/           vault メタ情報
```

**読む順序**: hot.md → index.md → 関連セクション → 個別ページ

`hot.md` と `index.md` は LIVING ドキュメント。追記ではなく蒸留する
（詳細は `.claude/rules/living-docs.md`）。

---

## 他プロジェクトからの参照

別の Claude Code プロジェクトの CLAUDE.md に追記:
```
Wiki: ~/CosmicTheta/DeepStone
Read wiki/hot.md → wiki/index.md → specific pages as needed.
```
