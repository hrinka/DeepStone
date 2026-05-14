# DeepStone — Rinka の第二の脳

Claude Code + Obsidian による永続的知識ベース。

**Skills:** `/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/save`, `/autoresearch`, `/canvas`, `/obsidian-synthesize`, `/x-pulse`, `/x-read`, `/youtube`

---

## Rinka について

- **名前**: 深石梨花（Rinka）/ アーティスト名: Rt3mis
- **ペルソナ**: Rt3mis（アーティスト）/ Charlotte R1nR1n（海賊ライター）/ 深石梨花（素の自分）
- **目標**: UK へ2年間の音楽修行。200万円貯める。1日1万円以上の不労所得。
- **活動**: DJ・楽曲制作・AI活用・レイブカルチャー発信
- **発信**: X / TikTok / Threads — UK Bass・Dub・rave文化
- **使用ツール**: DeepStone（Obsidian）/ OpenClaw（Telegram）/ Claude Code
- **返答スタイル**: 日本語・敬語・簡潔に

## Rinka の根本ビジョン（最重要・常に念頭に置くこと）

> 「自分軸でこの地球でやりたいことをやりながら、自分自身と出会った人の波動を上げて、世界を旅すること。」

- **本質**: 音楽も香りも、目に見えないものこそが本質。周波数・波動・響き。
- **手段**: 音楽（レイブ・UK Bass）と香り（アロマ・ハーブ）を通じて人の周波数を上げる
- **世界観**: 知識・詩・言葉でも波動は上がる。SEO的に届きながら、魂にも届くコンテンツ
- **発信の方向性**: 人生をより良く、波動が上がる、ためになること——を詩のように綴る
- **DeepStone の役割**: Rinka が世界を旅しながら活動するための「知の基地」かつ「自動生成エンジン」

**Claude へ**: このビジョンに反するシステムは作らない。コンテンツ生成・フォルダ設計・ルーティン構築は常にこの軸に沿って提案すること。

---

## Vault の使い方

### ソースを知識に変える
1. 記事・動画・メモを `.raw/[カテゴリ]/` に置く
2. `ingest [ファイル名]` と言うだけ → Claude が wiki に変換

### 知識を引き出す
- 質問する → Claude が hot.md → index.md → 個別ページの順で読んで答える
- `/wiki-query` で詳細検索

### 会話を保存する
- **Claude Code セッション後**: `/save` で wiki に保存
- **OpenClaw（Telegram）会話後**: 重要な内容を `.raw/personal/` にテキストで保存 → `ingest [ファイル名]`

### 定期メンテ
- `/wiki-fold` でログをロールアップ（月1）
- `/obsidian-synthesize` でパターン発見（月1〜2）

---

## ソース置き場 `.raw/`

**ルール: 入れたら変更しない。Claude は読むだけ。**

```
.raw/
├── music/       音楽記事・インタビュー・研究論文
├── personal/    Rinka 自身のメモ・意見・人生計画・日記
├── coding/      技術記事・チュートリアル
├── money/       ビジネス・収益化・金融情報
├── uk-whv/      UK渡航・WHV関連情報
└── articles/    カテゴリ不明・その他
```

**何でも入れていい**: 調べた記事、自分の意見メモ、人生計画、ライフスタイル構想、OpenClaw との会話ログ——すべて `.raw/` に入れて `ingest` すれば wiki に昇格できる。

> Finder で `.raw/` が見えない場合: `Cmd + Shift + .` で隠しファイルを表示

---

## Instagram 2アカウント構成（重要）

DeepStone は **2つの独立した Instagram アカウント** を支援する。今後の開発・生成・フォルダ操作は必ずこの分離を維持すること。

| アカウント | テーマ | ペルソナ | 出力フォルダ |
|---|---|---|---|
| **Charlotte R1nR1n** | レイブ音楽・UK Bass・クラブカルチャー | Charlotte R1nR1n | `rave-team/output/EP-XX/` |
| **FLAVA FM** | アロマ・数秘術・ハーブ・スピリチュアル | 深石梨花（白魔女） | `aroma-insta/output/POST-XX/` |

### FLAVA FM コンセプト（重要）
**「白魔女による波動UPアロマチャンネル」**
- ペルソナ: 深石梨花 as 白魔女——自然・光・浄化の使い手
- トーン: 詩的・温かい・神秘的。知識を「情報」ではなく「体験」として届ける
- ピラー: アロマ精油 / 数秘術 / ハーブ / スピリチュアル（波動・引き寄せ・浄化）
- 目的: 見た人の波動が上がる。人生が少しだけ、でも確実に良くなる
- SEO × 魂: 検索に届きながら、魂にも届くコンテンツ。情報と詩の融合
- キーワード: 波動・周波数・浄化・引き寄せ・精油・白魔女・ハーブ魔法・数秘

### フォルダルール

```
rave-team/
└── output/
    └── EP-XX/              ← Charlotte R1nR1n 用（毎日自動生成）
        ├── script_ja.md    Reels スクリプト（50〜60秒）
        ├── carousel.md     Instagram カルーセル（8枚+画像案）
        └── research.md     リサーチメモ

aroma-insta/
└── output/
    ├── POST-XX/            ← FLAVA FM 用（自動生成分）
    │   ├── carousel.md
    │   └── research.md
    └── stock/              ← ストック投稿（手動制作済み15本）

wiki/
└── concepts/
    ├── music/              ← レイブ音楽関連 concept
    └── numerology/         ← アロマ・数秘関連 concept
└── sources/
    ├── rave/               ← EP 記事・音楽ソース
    └── aroma/              ← アロマ・数秘記事

_attachments/
├── rave/EP-XX/             ← Charlotte R1nR1n 用画像（ローカルのみ）
└── aroma/POST-XX/          ← FLAVA FM 用画像（ローカルのみ）
```

### 新規コンテンツを生成する際の鉄則
- レイブ系 → `rave-team/output/` + `wiki/sources/rave/` + `wiki/concepts/music/`
- アロマ系 → `aroma-insta/output/` + `wiki/sources/aroma/` + `wiki/concepts/numerology/`
- **2アカウントのファイルを混ぜない**

---

## Wiki 構造

```
wiki/
├── hot.md          直近コンテキストのキャッシュ（毎セッション更新）
├── index.md        全ページの1行サマリー
├── log.md          操作履歴
├── concepts/       概念・フレームワーク・synthesis ページ
├── entities/       人物・組織・場所
├── sources/        ingested ソース要約
├── questions/      autoresearch 結果
├── comparisons/    比較分析
├── canvases/       Obsidian ビジュアルマップ
└── meta/           vault メタ情報
```

**読む順序**: hot.md → index.md → 関連セクション → 個別ページ

---

## 他プロジェクトからの参照

別の Claude Code プロジェクトの CLAUDE.md に追記:
```
Wiki: ~/CosmicTheta/DeepStone
Read wiki/hot.md → wiki/index.md → specific pages as needed.
```
