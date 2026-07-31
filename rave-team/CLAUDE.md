# rave-team — Charlotte R1nR1n（レイブ）コンテンツ

> このファイルの責務は **rave-team の成果物契約**。
> Rinka に関する事実の正典は [Memory.md](../Memory.md)、vault 全体の規範は
> [CLAUDE.md](../CLAUDE.md)。出力ルールは `.claude/rules/output.md` にもある。

Charlotte R1nR1n（女海賊ライター）名義の Instagram 向けレイブ文化コンテンツ。
EP 番号で管理し、日次で自動生成されている。

---

## 成果物契約

EP 1本につき `output/EP-XX/` に以下の**4点セット**を作る。これがこのプロジェクトの
唯一の出力契約。

| ファイル | 内容 |
|---|---|
| `carousel.md` | Instagram カルーセル |
| `research.md` | リサーチメモ（一次資料・年号・人名の裏取り） |
| `caption.md` | 投稿キャプション |
| `slides.json` | スライド定義（`tools/carousel-render/` が画像化する） |

## 連番

新規番号は `output/episodes.md` で確認して採番し、生成後に同ファイルを更新する。

## 内容の基準

- **史実の正確さを最優先**。人名・年号・レーベル・楽曲名は一次資料で裏を取る
- 既存 EP との接続を必ず書く（「EP-47 Metalheadz との直接接続」のように）。
  シリーズとして読めることが価値
- サウンドシステム／ダブ／ジャマイカ系譜という DeepStone の背骨を意識する

---

## やらないこと

過去には `discussion.md` / `script.md` / `production_brief.md` / `social.md` を
7つのサブエージェント（producer / dj / researcher / scriptwriter / director /
social / archivist）で作るパイプライン構成があったが、**EP-02 前後で廃止した**。

実績: 全 96 EP のうち `script.md` は 0 件、`discussion.md` と `social.md` は各 2 件。
一方 `carousel.md` / `research.md` / `caption.md` / `slides.json` は各 69 件。
記述だけが残って実体が無い状態だったため、記述の側を実体に合わせた。

復活させないこと。当時の設計は `agents/_archive/` に残してある。
