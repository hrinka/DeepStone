

新しい情報源を追加

```markdown
I'm adding a new source to my knowledge base about [TOPIC].

Here is my current wiki index (so you know what already exists):
[PASTE the contents of wiki/index.md]

Here is the new source:
[PASTE the new article]

Please:
1. Write a summary of this source
2. Update my index with any new concepts
3. Note any connections to existing concepts (mark these with
   [[wikilinks]])
4. Flag anything that contradicts existing wiki content with ⚠️
```


ステップ4：AIにWikiのコンパイルを依頼する（5分）

Claude（またはお好みのAI）を開きます。以下のプロンプトをコピー＆ペーストし、括弧内の部分を置き換えてください。

```markdown
I'm building a personal knowledge base about [YOUR TOPIC].

I have [NUMBER] source articles. I'm going to paste them below.
For each source, please:

1. Write a 200-word summary capturing the key points
2. List the main concepts mentioned (as a simple list)
3. Identify any connections between this source and the others

After processing all sources, please:
4. Write a "master index" listing every concept with a one-line
   description
5. Write one "concept article" (300-500 words) for the single
   most important concept across all sources

Format everything as markdown. Use [[double brackets]] around
concept names so they work as links in Obsidian.

Here are my sources:

[PASTE YOUR RAW NOTES HERE, separated by --- between each one]
```

Claudeは構造化された出力を生成します。
各セクションを、wikiフォルダ内の新しいノートにコピーしてください。

- 要約を個別のメモとして保存してください
- （例：wiki/summary-bitcoin-halving.md）。
- マスターインデックスをwiki/index.mdとして保存します。
- コンセプト記事をwiki/に分かりやすい名前で保存してください。

ステップ5：魔法を体験しよう

Obsidianのグラフビューを開きます（左側のサイドバーにあるグラフアイコンをクリックするか、Ctrl/Cmd+Gを押します）。

メモは点として表示され、AIが作成した[[wikilinks]]で結ばれています。これは、つながり合ったアイデアのネットワークとして視覚化された、あなたの知識ベースです。

ノート内のリンクされた概念をクリックしてください。該当するページが存在する場合は、Obsidianがそのページを開きます。まだ存在しない場合は、Obsidianが作成を提案します。このようにして、Wikiは自然に成長していきます。

これで実用的な知識ベースが完成しました。ここからは、それをより大きく、より速く、より強力にするための作業です。

## 

知識基盤を拡大する（日々の習慣）

新しい情報源を追加

保存する価値のあるものを読んだときはいつでも：

1. それを切り取るか、生のフォルダに貼り付けてください。
    
2. Claudeを開いて、これを貼り付けてください。
    

```markdown
I'm adding a new source to my knowledge base about [TOPIC].

Here is my current wiki index (so you know what already exists):
[PASTE the contents of wiki/index.md]

Here is the new source:
[PASTE the new article]

Please:
1. Write a summary of this source
2. Update my index with any new concepts
3. Note any connections to existing concepts (mark these with
   [[wikilinks]])
4. Flag anything that contradicts existing wiki content with ⚠️
```

1. 出力結果をWikiフォルダに保存し、古いインデックスを更新済みのインデックスに置き換えてください。
    

質問をする

ここからが真価を発揮するところです。10件以上の記事をまとめると、次のようになります。


```markdown
Here is my knowledge base index:
[PASTE wiki/index.md]

My question: [YOUR QUESTION]

Please research the answer using the concepts and sources in my
wiki. If you need to see specific articles, tell me which ones
and I'll paste them. Cite your sources using [[wikilinks]].

After answering, save the answer as a markdown file I can add
to my wiki.
```

重要な習慣：必ず回答をWikiに書き込むこと。Wikiフォルダに保存してください。これが循環的な効果を生み出します。すべての質問が、将来の質問のための基盤を豊かにするのです。

週ごとの健康チェック


```markdown
Here is my knowledge base index:
[PASTE wiki/index.md]

Please perform a health check:
1. Which concepts are mentioned but don't have their own article
   yet? (These are gaps I should fill)
2. Are any summaries likely outdated? (Flag anything over 6 months
   old)
3. What are 3 interesting questions I could research next?
4. Are there orphan concepts with no connections to other topics?
```

週に3回のやり取り。
1、2件の情報源の追加、時折の質問、そして状態チェック。