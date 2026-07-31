# aroma-insta/ — 廃止

FLAVA FM の出力先は `flava-fm/output/` に統合済み。このディレクトリには新規ファイルを
作らないこと。POST-01〜96 は全て `flava-fm/output/` にある。

## 経緯

FLAVA FM の出力先は当初 `flava-fm/output/` だったが、2026-06-10（POST-52）から
`aroma-insta/output/` に切り替わり、以降 POST-96 まで分裂した状態が続いていた。
2026-07-31 に `flava-fm/` へ統合し、元の1箇所に戻した。

## 再発防止

`/vault-health` に「`aroma-insta/` 配下に POST ディレクトリが出現したら FAIL」の
検査を入れてある。日次生成は claude.ai 側のスケジュール実行で、セッション開始時に
`CLAUDE.md` を読んで出力先を決めるため、出力先の正典は [CLAUDE.md](../CLAUDE.md) にある。
