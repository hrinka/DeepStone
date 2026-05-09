---
name: obsidian-synthesize
description: "Automatic synthesis — scans the vault for unnamed patterns across pages and writes synthesis pages. Triggers on: synthesize, find patterns, what connects, synthesize the vault, find connections, auto-synthesis."
---

# obsidian-synthesize: Automatic Pattern Discovery

vaultを自律スキャンし、まだ名前のついていないパターン・接続・進化を発見してwikiページに書き出す。

---

## 手順

1. `wiki/hot.md` → `wiki/index.md` を読む
2. `wiki/log.md` の直近20エントリを読む
3. 4つの並行エージェントでスキャン：

### Agent 1: Cross-Source（複数ソースに現れる概念）
- `wiki/sources/` の全ページを読む
- 2つ以上の無関係なソースに登場する概念を探す
- 例：Dub Production Philosophy が「RBMA記事」にも「DJ Mag記事」にも現れている → Synthesis候補

### Agent 2: Entity Convergence（一緒に登場するエンティティ）
- `wiki/entities/` をスキャン
- 複数のコンテキストで共に登場するが、接続ページがない人物・組織のペアを探す
- 例：King TubbyとAugustus Pablo → すでに接続あり。では Mad ProfessorとJah Shakaは？

### Agent 3: Concept Evolution（進化する概念）
- `wiki/concepts/` で3回以上更新されたページを探す
- その概念がどう変化したかを時系列で追う
- 「Concept Evolution」セクションを書く

### Agent 4: Orphan Rescue（孤立ページの救済）
- 被リンクがない `wiki/` ページを探す
- 内容的に既存ページとリンクすべき箇所を特定してリンクを作成

---

## 発見ごとにページ作成

`wiki/concepts/Synthesis — [タイトル].md` を作成：

```yaml
---
type: synthesis
date: YYYY-MM-DD
tags:
  - synthesis
  - auto-generated
auto_generated: true
---
```

本文：
- 発見したパターンの説明
- どのソース・ページから来たか（[[wikilink]]付き）
- 意味すること
- 推奨アクション

---

## 後処理

1. `wiki/index.md` に新しいSynthesisページを追加
2. `wiki/log.md` の先頭に追記：
   ```
   ## [YYYY-MM-DD] synthesize | X synthesis pages, Y orphans rescued, Z connections found
   ```
3. `wiki/hot.md` を更新

---

## DeepStone への適用メモ

- `wiki/concepts/Synthesis — *.md` として保存（既存のconcepts/内に）
- Rinka Content Vision と Charlotte R1nR1n Rave Dictionary への接続も探す
- 音楽知識とコンテンツ戦略の間のパターンを特に注目する
