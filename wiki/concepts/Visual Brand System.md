---
type: concept
title: "Visual Brand System"
created: 2026-06-09
updated: 2026-06-09
tags:
  - branding
  - visual-identity
  - flava-fm
  - plur-system-diary
  - color-palette
  - content-strategy
status: official
related:
  - "[[Rinka Content Vision]]"
---

# Visual Brand System

Rinka の2つの発信アカウントの**正式なビジュアルブランド定義**。毎日の自動投稿（FLAVA FM / PLUR SYSTEM DIARY）はこのページの色・トーンを参照すること。色をブレさせない。

theme-factory 定義ファイル:
- `~/.claude/skills/theme-factory/themes/flava-fm-moonlit-herbalist.md`
- `~/.claude/skills/theme-factory/themes/plur-system-diary-soundsystem-black.md`

プレビュー: `brand/palettes-preview.html`

---

## 🌿 FLAVA FM — Moonlit Herbalist

> 白魔女 × 数秘 × アロマ × ハーブ菜園 × 波動UP × 世界平和
> ムード：ボタニカル・月光・神秘・癒し・聖なる柔らかさ
> 攻撃性ゼロ。見た瞬間に呼吸が深くなる配色。

| 役割 | 色名 | HEX |
|------|------|-----|
| 背景 | 月光のアイボリー | `#F4EFE6` |
| メイン | セージグリーン | `#869177` |
| サブ | ムーンラベンダー | `#A99BC0` |
| アクセント | 光のゴールド | `#C9A86A` |
| 深色 | 森の夜 | `#33403A` |
| テキスト | 大地の墨 | `#2C2A26` |

**フォント**: 見出し=セリフ（詩的・優しい）／本文=サンセリフ
**配色ルール**: 背景はアイボリー固定。見出しは森の夜 or セージ。数秘パートにラベンダー、波動・強調にゴールドを点で。

---

## 🖤 PLUR SYSTEM DIARY — Sound System Black

> UK Bass × Dub × 夜 × PLUR（Peace/Love/Unity/Respect）
> ムード：漆黒・ストロボ・ロウ・削ぎ落とし
> 海賊ラジオの系譜。「低音で世界の周波数を上げる記録」。

| 役割 | 色名 | HEX |
|------|------|-----|
| 背景 | 漆黒 | `#0A0A0A` |
| 準黒 | スモーク | `#171717` |
| 中間 | アッシュグレー | `#4A4A4A` |
| 明 | フォグ | `#9B9B9B` |
| メイン | オフホワイト | `#ECECEC` |
| 強調 | ストロボ白 | `#FFFFFF` |

**隠し味（任意・原則使わない）**: UVパープル `#B026FF` / ストロボレッド `#FF2D2D`（1色だけ・1スライド1箇所まで）
**フォント**: 見出し=サンセリフBold（クラブフライヤー感）／本文=サンセリフ
**配色ルール**: 完全黒白。純白は1スライド1箇所の最強調のみ。グレーは階層付けに使う。

---

## アカウント名の意味（PLUR SYSTEM DIARY）

| 語 | 意味 | 軸との接続 |
|----|------|-----------|
| PLUR | Peace · Love · Unity · Respect | 人生の指針＝世界平和 |
| SYSTEM | サウンドシステム | UK Dub/Bass 文化の心臓部 |
| DIARY | 日記・記録 | 「広める」でなく「綴る」姿勢。FLAVA FM・DeepStone交換日記と一貫 |

ハンドル: `@plur_system_diary`
プロフィール:
```
PLUR SYSTEM DIARY
低音で、世界の周波数を上げる。
UK Bass / Dub / Sound System Culture
Peace · Love · Unity · Respect
🌑
```

---

## 言語ルール（確定 2026-06-09）

| | スライド（画像内） | キャプション |
|--|------------------|------------|
| 🌿 FLAVA FM | 日本語 | 日本語 |
| 🖤 PLUR SYSTEM DIARY | **英語** | **日本語メイン** |

※ Instagramの自動翻訳はキャプションのみ有効（スライドの焼き文字は翻訳されない）。詳細は [[Instagram Carousel Playbook]]。

---

## ビジュアル Signature（確定）

毎日のAI画像生成はしない方針。固有の見た目で「量産ポエムアカウント」と差別化する。

- 🖤 **PLUR**：質感背景（グレイン/スピーカー/コンクリート）＋固有モチーフ（波形/スタック/ダブプレート）＋現場モノクロ実写
- 🌿 **FLAVA**：ハーブ菜園・精油の実写＋月相/ボタニカル線画モチーフ＋月光6色

背景素材は一度作って回す（実質コスト¥0）。

---

## 自動化での扱い

- FLAVA FM 投稿ルーチン → carousel.md の「カラーパレット」欄はこのFLAVA FM定義から選ぶ／スライド日本語
- EP（PLUR SYSTEM DIARY）ルーチン → carousel.md の「カラーパレット」欄はこの黒白定義から選ぶ／スライド英語・キャプション日本語
- Canva: `brand/palettes-preview.html` をブラウザで開き、色見本として参照
