---
name: vault-health
description: "週次の vault 健康診断オーケストレータ。hot.md の二層再構築・index.md の再生成・log.md のロールアップ・wiki-lint・禁止パターン検査・drift 検査をこの順で実行し、レポートを出力する。破壊的な修正はしない。Triggers on: vault health, 健康診断, 週次メンテ, vault-health, vault の健康診断."
---

# vault-health: 週次 vault 健康診断

既存の `wiki-lint` を置き換えるものではなく、**その上位に立つ週次オーケストレータ**。

> [!important] すべてレポート出力までで止める
> 破壊的な修正（ページ削除・マージ・大量リネーム）は**人間承認後に別途行う**。
> このコマンド自身が行う書き込みは hot.md / index.md の整形と lint レポートの出力のみ。

---

## 実行順序

### 1. `wiki/hot.md` の二層再構築

hot.md は「セッション開始時に最初に読むキャッシュ」。log.md の劣化コピーにしない。

- 先頭に**現在形の蒸留サマリ**を置く
  - 稼働中のライン（日次生成・進行中プロジェクト）
  - いま追っているテーマ
  - 滞留している事項（gap / 未決）
- その下に**直近 7 日**の圧縮エントリ。1 件 1 行 + `[[wikilink]]` まで
- 8 日以前のエントリは `wiki/log.md` に残し、hot.md からは落とす（消すのではなく落とす）
- **完成形の目標: 10KB 未満**

```bash
wc -c wiki/hot.md   # 再構築後に必ず確認する
```

10KB を超えたままなら、それは失敗。もう一段圧縮する。

### 2. `wiki/index.md` の再生成

- 新規ページを拾って 1 行サマリーを追加
- 実在しないページへの行を削除
- `updated:` を更新

```bash
# index に載っていない wiki ページを洗い出す
comm -23 \
  <(git -c core.quotePath=false ls-files 'wiki/**/*.md' | grep -vE 'wiki/(hot|index|log)\.md' | xargs -n1 basename | sed 's/\.md$//' | sort -u) \
  <(grep -o '\[\[[^]]*\]\]' wiki/index.md | tr -d '[]' | sed 's/|.*//' | sort -u)
```

### 3. `wiki/log.md` のロールアップ

`/wiki-fold` を呼び `wiki/folds/` へ。**一度も動いていないので、初回は小さい batch
（k=3 = 8 件）から試して挙動を確認する。** dry-run を通してから commit すること。

### 4. `wiki-lint` の実行

orphan / dead link / frontmatter gap を検査し、レポートを
`wiki/meta/lint-report-YYYY-MM-DD.md` に出力する。

### 5. 禁止パターン検査

Phase 1〜2 で消した参照が復活していないかを検査する。**統治文書側のみが対象**
（wiki の歴史記述は対象外）。

検査は 2 段に分ける。**どこにあっても誤り**のものと、**root の構造記述にある場合だけ誤り**の
ものを混ぜると誤検出する。

```bash
# A. どこにあっても誤り（統治文書 + .claude/）
#    自分自身（vault-health.md）はパターンを文書化しているため除外する
grep -rnE '\.raw/|aroma-insta/output/POST-|/Users/user/|Rave Culture KB' \
  --include="*.md" --include="*.json" \
  CLAUDE.md AGENTS.md SOUL.md Memory.md TOOLS.md HEARTBEAT.md .claude/ 2>/dev/null \
  | grep -v '\.claude/worktrees/' \
  | grep -v '\.claude/commands/vault-health\.md' \
  && echo "FAIL(A): 廃止済みパスが再登場しています" || echo "OK(A)"

# B. root の構造記述にある場合だけ誤り
#    wiki/canvases/ は /canvas skill が必要時に作る正当なパスなので .claude/ は対象外。
#    「vault の構造」として root 文書に書かれていたら、実在しないので誤り。
grep -nE 'wiki/(comparisons|canvases)/' \
  CLAUDE.md AGENTS.md SOUL.md Memory.md TOOLS.md HEARTBEAT.md 2>/dev/null \
  && echo "FAIL(B): 実在しない wiki サブフォルダが構造記述に再登場しています" || echo "OK(B)"
```

あわせて、出力先の分裂が再発していないかを検査する:

```bash
ls aroma-insta/output 2>/dev/null | grep -q '^POST' \
  && echo "FAIL: aroma-insta/ に POST ディレクトリが出現しています（出力先が戻っている）" \
  || echo "OK"
```

意図: AI は既存ファイルから素直に学習して、一度消した古い手順を再提案してくる。
**「やめたこと」を検査で固定する**ことで、同じ劣化を繰り返さない。

### 6. drift 検査

「今週生成した EP / POST は、`Memory.md` の大目標（UK 渡航 / 貯金 200 万 /
不労所得 / 音楽）とどのピラーに紐づくか。紐づかないものはどれか」を報告する。

紐づかない生成が続いているなら、**それ自体を指摘する**。生成が回っていること自体は
健康の証拠ではない。目標に向かっていない生成が毎日回るのは、むしろ問題である。

### 7. fail-soft

走査できなかった項目を「問題なし」と報告しない。

- grep が 0 件だったのか
- そもそも走らせられなかったのか（コマンドが無い / 権限が無い / パスが変わった）

この 2 つを**区別して書く**。分からなかったことは「分からなかった」と書く。

---

## レポートの形

`wiki/meta/lint-report-YYYY-MM-DD.md` に出力する。

```markdown
---
type: meta
date: YYYY-MM-DD
tags: [meta, lint]
---

# Vault Health YYYY-MM-DD

## サマリ
- hot.md: NN KB（目標 10KB 未満） / 判定
- index.md: 未掲載 N 件 / 実在しないページ N 件
- lint: orphan N / dead link N / frontmatter gap N
- 禁止パターン: OK | FAIL（該当箇所）
- drift: 今週 N 本生成、うち大目標に紐づかない N 本

## 走査できなかった項目
（無ければ「なし」と書く。空欄にしない）

## 人間の判断が要るもの
（破壊的な修正はここに列挙するだけ。実行しない）
```

---

## やらないこと

- ページの削除・マージ・大量リネーム（レポートに書くだけ）
- `raw/` への書き込み
- wiki コンテンツ本文の書き換え（構造・frontmatter・参照のみ）
- 「たぶん大丈夫」で OK を出すこと
