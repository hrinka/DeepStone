---
type: meta
title: "Hot Cache"
updated: 2026-08-31
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
---

# Recent Context

> セッション開始時に最初に読むキャッシュ。**10KB 未満に保つ。**
> 追記せず蒸留する。8日以前のエントリは [[log]] にあるのでここからは落とす。
> ルール: `.claude/rules/living-docs.md`

---

## いま動いているもの

**日次自動生成**（claude.ai のクラウドスケジュール実行。ローカルには bot 本体は無い）
- 07:08 JST — `journal/YYYY-MM-DD.md`（今朝のレター）
- 08:12 JST — EP-XX / POST-XX の `carousel.md` + `research.md`
- 08:43 JST — `slides.json` + `caption.md`
- 09:10 JST — 画像レンダー（ローカル launchd `ai.deepstone.render.plist`）

**現在地**: EP-102 / POST-100。レイブと、アロマ・数秘の2ライン。
出力先は `rave-team/output/` と `flava-fm/output/`（`aroma-insta/` は 2026-07-31 に廃止統合）。

> [!warning] 2026-08-01: 分裂が一度再発した
> claude.ai 側 routine の出力先が未修正のため、POST-97 が `aroma-insta/output/` に
> 生成された。手動で `flava-fm/` へ移動済み。**routine のプロンプトを直すまで毎朝再発する。**

**時間管理システム構築中** — [[時間管理システム]] / [[週次レビュー]] / [[月次チェックポイント]]。
Obsidian 内で完結させる方針（Dataview + Tasks + Day Planner + Google Calendar）。
習慣 → 1日 → 1週間 → チェックポイント → 人生 の積み上げ。

**マネー** — [[借金返済-キャッシュフロー計画]]（4社 ¥1,246,753・年利18%）、
[[UK-WHVビザ準備]]（2027年渡航）、[[助成金-補助金-候補]]（持続化補助金 第20回 11/5〜12/15）。

---

## 滞留している事項（未決・要アクション）

- **LINE チャネルアクセストークンの失効** — `scripts/morning_brief.py` は削除したが履歴に残る
- **obsidian-local-rest-api の API キー再生成** — 同上。未使用ならプラグイン無効化でも可
- **claude.ai 側 routine の出力先確認** — プロンプトに `aroma-insta` が直書きされていないか。
  `CLAUDE.md` は修正済みだが、routine 側に直書きがあるとそちらが勝つ
- **壊れた launchd ジョブ** — `local.deepstone.morningbrief.plist`（8:00 JST）が削除済みの
  `scripts/morning_brief.py` を呼んでいる
- **貯蓄目標と借金の整合** — 200万円貯蓄目標が借金 ¥1,246,753 を踏まえずに立てられている
  （[[借金返済-キャッシュフロー計画]] に gap 記録済み）
- **Google Calendar プラグインの OAuth 認証** — 未完了
- **`/vault-health` の cron 登録** — 初回レポートを人間が確認してから

---

## 直近7日

- 2026-08-31: EP-102「Mala / Deep Medi Musik — 低音は祈りだった」→ `rave-team/output/EP-102/` に正常生成
- 2026-08-10: EP-101「Pendulum — Perth からグラストンベリーへ、DnBとメインストリームの衝突」→ `rave-team/output/EP-101/` に正常生成
- 2026-08-09: POST-100「コーナーストーン — 名前の最初の文字が語る、魂の入口」（数秘ピラー）→ `flava-fm/output/POST-100/` に正常生成
- 2026-08-04: POST-99「花が開く前に、摘む。— ハーブ収穫と精油の頂点」（ハーブ菜園ピラー）→ `flava-fm/output/POST-99/` に正常生成
- 2026-08-01: EP-98「Noisia / Vision Recordings」（グローニンゲン発・20年のニューロファンク軌跡）
- 2026-08-01: POST-98「サイプレス — 移行と手放しの周波数」（アロマピラー）→ `flava-fm/output/POST-98/` に正常生成
- 2026-07-31: EP-97「Renegade Hardware」/ POST-97「ファーストヴォーウェルナンバー」
- 2026-07-31: DeepStone 整備（Phase 0〜4）— シークレット除去・pre-commit 導入・SSOT 整理・
  FLAVA FM 統合・`.claude/rules/` 6本・`/vault-health` 新設。詳細は [[log]]
- 2026-07-30: 時間管理システムの構成を決定（[[時間管理システム]]・[[週次レビュー]] 新規）
- 2026-07-30: 音声メモを ingest（[[2026-07-30-自己省察と発信拠点・時間管理]]）
- 2026-07-30: EP-96「Hospital Records / London Elektricity」/ POST-96「コンポストと土の錬金術」
- 2026-07-29: EP-95「Benga」/ POST-95「ジュニパーベリーと4000年の浄化周波数」
- 2026-07-28: EP-94「Skream」/ POST-94「数字は、惑星の声だった」
- 2026-07-27: EP-93「Calibre / Signature Recordings」/ POST-93「地中海ハーブと渇きの哲学」
- 2026-07-26: EP-92「Bad Company UK」/ POST-92「ラベンダー精油とアロマテラピーの誕生」
- 2026-07-25: EP-91「Moving Shadow Records」/ POST-91「パーソナルデーナンバー」

---

## Vault State

- **Owner**: Rinka（人物情報の正典は `Memory.md`）
- **wiki**: concepts / entities / sources / questions / projects / meta
- **読む順序**: hot.md → [[index]] → 関連セクション → 個別ページ
- **規範**: `CLAUDE.md`（薄く保つ）+ `.claude/rules/*.md`（path-scoped）
- **週次メンテ**: `/vault-health`
