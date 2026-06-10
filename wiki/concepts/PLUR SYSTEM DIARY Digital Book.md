---
type: concept
title: "PLUR SYSTEM DIARY Digital Book"
created: 2026-06-10
updated: 2026-06-10
tags:
  - plur-system-diary
  - digital-book
  - content-strategy
  - rave-history
status: developing
related:
  - "[[Visual Brand System]]"
  - "[[Rinka Content Vision]]"
  - "[[Hardcore Continuum]]"
---

# PLUR SYSTEM DIARY — Digital Book

@plur_system_diary の投稿（EP）を、**順番に読むと1冊の本になる**ように編集・校正するための目次と編集方針。
LAUNCH-01「PLUR」= 開幕宣言（序章）。そこから番号順に章が進む。

## 読む順の原則（確定 2026-06-10）
**ストーリー性のある年代順**（narrative-chronological）。
レイブ史は「一つのジャンルが次を生む」因果の連鎖（＝[[Hardcore Continuum]]）。だから年代順に並べるだけで、自然に1つの物語になる。「重要部分だけ」では通底する一本の線が切れるので採らない。

- **PART I 根** → **PART II 誕生** → **PART III 系譜（continuum）** → **PART IV 並走** → **PART V 場と文化**
- 各章は単体でも読めるが、順に読むと「なぜそれが生まれたか」が積み上がる。

## 編集方針（校正チェックリスト）
各章（EP）を校正するとき、以下を確認：
- [ ] **前章からの流れ** — 直前の章を踏まえて始まっているか
- [ ] **古い相互参照を消す** — 「次回は◯◯」等の初期ドラフトの名残を除去
- [ ] **1スライド1メッセージ**・フック・8枚目に保存トリガー
- [ ] **声の統一** — Charlotte R1nR1n（短文・夜・「!」なし）
- [ ] **事実の正確さ**（年・人名・場所）
- [ ] スライド=英語 / キャプション=日本語（[[Instagram Carousel Playbook]]）
- [ ] 重複トピックがないか（_archive 済みの初期ドラフトと被らない）

## 読む順＝投稿順（章 ↔ EP ↔ 校正状況）

### 序章
- ⭐ LAUNCH-01「PLUR」— 投稿済み（2026-06-09）

### PART I — 根（何で、なぜ）
- ✅ **第1章** EP-01 WHAT IS A RAVE?（レイブの定義）— 校正済
- ✅ **第2章** EP-02 SOUND SYSTEM（Jamaica→UK の起源）— 校正済
- ✅ **第3章** EP-07 ACID HOUSE（TB-303という失敗作）— 校正済
- ⬜ 第4章 EP-08 レイブ禁止法 1994
- ⬜ 第5章 EP-09 デトロイトの電話番号
- ⬜ 第6章 EP-10 なぜUKだけが音楽を発明し続けるのか
- ⬜ 第7章 EP-11 ジャングルが生まれた夜
- ⬜ 第8章 EP-12 Drum & Bass の進化
- ⬜ 第9章 EP-13 UK Garage

### PART II — 並走と深化（順次校正）
- ⬜ EP-23 Big Beat / EP-26 Grime / EP-28 Dubstep / EP-29 Boiler Room / EP-31 Fabric
- ⬜ EP-32 Pirate Radio / EP-34 Berghain / EP-35 Warehouse Party / EP-37 DJ文化 / EP-38 Roland
- ⬜ EP-39 Second Summer / EP-41 Rave Fashion / EP-42 Haçienda / EP-43 Notting Hill / EP-45 UK Funky
- ⬜ EP-46 Burial / EP-47 Metalheadz / EP-48 Bristol Sound / EP-49 Warp / EP-50 Hardcore Continuum / EP-51 The Prodigy

> ※ 後半の並び順は、本としての流れを見ながら最適化余地あり（年代・系譜順への組み替え提案可）。

## 編集フロー
1. Slides Builder が毎晩 EP を英語 slides.json 化（EP優先・番号順）
2. **Editor（私）が番号順に校正** — 上のチェックリストで slides.json を点検・修正
3. Rinka が render_all.sh → 投稿（常に校正済みの章だけ投稿）

## 将来構想
- このEP群のデータ（carousel.md / slides.json）を元に、**デジタルブック的なWebサイト**を将来作る（章を順に読めるWeb版）。
- **TikTok / リールは当面なし**（カルーセル＝静止画の本に集中）。※ Writer routine の script_ja.md 生成は当面停止可。

## 進捗
- 校正済: 第1章(EP-01)・第2章(EP-02)・第3章(EP-07)
- 次: 第4章 EP-08「レイブ禁止法1994」から
