# SubCurrent — Mark System v2（2026-08-24）

フォントを **Michroma / Orbitron** に変更。縦積みを **SUB / CURRENT 大文字**に直しました。
プレビュー：https://claude.ai/code/artifact/ac49071a-5c99-41a0-a8bf-320b09a68376

```
wordmarks/   横組みロゴ 7案
  wm-1-michroma-driver        ★ マーク（ドライバー）＋ Michroma
  wm-2-michroma-split           SUB CURRENT ／ 罫線で挟む
  wm-3-orbitron-ping            Orbitron ＋ Cから立つ波紋
  wm-4-orbitron-weight        ★ SUB=Black / CURRENT=Regular
  wm-5-michroma-wave            Michroma ＋ 波形の下線
  wm-6-michroma-interference    干渉縞を背景に
  wm-7-michroma-mark            歪んだリング ＋ Michroma

stickers/    ステッカー 9案（SUB / CURRENT 大文字・縦積み）
  st-1-circle-left              円形・左寄せ ＋ 歪んだリング
  st-2-circle-center            円形・中央 ＋ 塗り抜き
  st-3-diecut-left            ★ ダイカット（歪んだ輪郭）＋ Michroma
  st-4-driver                 ★ 円形・ドライバー正面
  st-5-stack-tall               縦長・スピーカースタック
  st-6-square-interference      スクエア・干渉縞
  st-7-minimal                  円形・単環（25mm でも読める）
  st-8-mono-1color              1色シルク用
  st-9-lockgroove               円形・ロックグルーヴ

marks-new/   新しいサイケ層 9案（音・サウンドシステム・低音）
  n-N1-compression      疎密波 — 低音は縦波
  n-N2-interference     2点波源の干渉 — 部屋の中で低音がやっていること
  n-N3-waveform-ring    波形リング — 円形オシロ
  n-N4-scoop            スクープビン断面 — ホーンの指数フレア
  n-N5-phyllotaxis      フィロタキシス — 黄金角配列
  n-N6-speaker-stack    スピーカースタック
  n-N7-lockgroove       ロックグルーヴ
  n-N8-standing-wave    定在波 — 節と腹
  n-N9-driver         ★ ドライバー正面 — 歪んだリング＝スピーカー
```

## 縦積みをどう直したか

前回の違和感の原因は、**Sub を無理にトラッキングで伸ばして Current と同幅にしていた**こと。
字間が空きすぎて「S U B」という別の語に見えていました。

文字数の違う2語は、**幅を揃えず、軸を揃える**のが正解です。

- **左寄せ** — 左の軸が通る。硬く、機材に貼った時に強い
- **中央・自然幅** — 塊としてまとまる。円形ステッカー向き

## フォント

- **Michroma 400**（Google Fonts）— 字面が広くモノライン。間延びさせると「深いところ」に見える
- **Orbitron 400〜900**（Google Fonts）— ウェイトがあるのでワードマーク内で強弱を作れる

SVG 内の文字は**すべてアウトライン化済み**なので、フォントが入っていなくても開けます。
組み直したい時だけ上記2書体をインストールしてください。

## 入稿

- 塗り足し **3mm**、文字は仕上がりから **3mm 以上**内側に
- **CMYK**。黒は K100 ではなくリッチブラック（C40 M30 Y30 K100）
- `st-3` のダイカットは輪郭パスを**カットラインとして別レイヤー**に（スポットカラー指定）
- `st-8` は1色版。白い部分は**紙の地**になります

## 次に決めること

- 横組みは **W1 / W2 / W4** のどれを主にするか
- 正式表記は `SUBCURRENT` か `SUB CURRENT` か
- ステッカー1種類目（**st-3 を60mm** 推奨）
- 回替わり用の土のパレット5色
