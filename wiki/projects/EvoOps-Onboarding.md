---
type: project
title: "EvoOps 参画前 オンボーディングTODO"
created: 2026-06-03
status: in-progress
tags:
  - project
  - develop
  - onboarding
  - evoops
related:
  - "[[AWS Infrastructure]]"
  - "[[AI Driven Development]]"
  - "[[ChocoPLAi]]"
---

# EvoOps 参画前 オンボーディングTODO

## プロジェクト概要

**目的**: システム障害発生時に AI が自律的に原因分析 → 改善案提示 → IaC 生成まで行う

**スケジュール**:

| 期間 | マイルストーン |
|---|---|
| 6〜7月 | MCPサーバー構築 |
| 8月 | POC → 顧客フィードバック |
| 10月 | リリース |

**技術スタック**: Claude / Copilot（LLM） / Orama（neo4jアクセス） / Neo4j（グラフDB） / Qdrant（RAG・ベクトルDB） / Terraform（IaC） / AWS / Python

---

## 🔴 WEEK 1 — 2026/6/4

### ① Neo4j を触る
> このプロジェクトの核心技術。グラフDBの概念を理解する。

- [x] Neo4j Sandbox（無料）を作成 → https://sandbox.neo4j.com/
- [x] Cypher クエリ言語の基本を学ぶ
  - MATCH・CREATE・RETURN の基本構文
  - ノード・リレーションシップの概念
- [x] 「なぜグラフDBをインフラ管理に使うか」を理解する
  - インフラの依存関係（A→B→C が連鎖する）をグラフで表現するのが適している

### ② Qdrant（RAGのベクトルDB）を理解する

- [ ] RAGの仕組みを整理する
  - 「ドキュメントをベクトル化して保存」
  - 「質問と類似したドキュメントを検索」
  - 「検索結果をLLMのコンテキストに渡す」
- [ ] Qdrant 公式ドキュメントを読む → https://qdrant.tech/documentation/
- [ ] Python で Qdrant に接続するサンプルを動かす（`pip install qdrant-client`）

### ③ Orama を理解する

- [ ] Orama とは何かを調べる
  - 全文検索・ベクトル検索を組み合わせたエンジン
  - Neo4j へのアクセスに使われている
- [ ] 公式ドキュメントを確認する → https://oramasearch.com/

---

## 🔴 WEEK 1 — 優先度：高

### ④ MCPサーバーの構築方法を理解する
> 6〜7月の目標が MCPサーバー構築なので最優先で学ぶ。

- [ ] MCP（Model Context Protocol）公式ドキュメントを読む → https://modelcontextprotocol.io/
- [ ] MCPサーバーをローカルで立てる（Claude Desktop に MCP を接続する練習）
- [ ] シンプルな MCPサーバーを Python で自作する
  - AWS の CloudWatch と繋ぐ MCPサーバーのイメージをつかむ
- [ ] Claude Code と MCP の連携を手元で試す

### ⑤ AWS CloudWatch を理解する
> 障害検知のトリガーになる重要なサービス。

- [ ] CloudWatch の主要機能を整理する
  - Alarms：しきい値超えでアラート
  - Logs：ログの収集・検索
  - Metrics：メトリクスの可視化
  - Events：イベント駆動の自動化
- [ ] CloudWatch → Lambda のトリガー設定を理解する
- [ ] CloudWatch Logs Insights のクエリを練習する → https://docs.aws.amazon.com/cloudwatch/

---

## 🟡 WEEK 2 — 優先度：中

### ⑥ LangChain / LangGraph を触る

- [ ] LangGraph の概念を理解する
  - エージェントの「状態遷移」をグラフで管理するフレームワーク
  - → https://langchain-ai.github.io/langgraph/
- [ ] シンプルな Agent を Python で作ってみる
  - 「CloudWatch のアラートを受け取る」→「原因を分析する」→「Terraform コードを提案する」という簡単なフロー

### ⑦ EvoOps とは何かを理解する

- [ ] EvoOps の概念を調べる（Evolution + Ops = AI が継続的にインフラを改善するフレームワーク）
- [ ] NTTドコモの関連資料を確認する
  - https://information.nttdocomo-fresh.jp/fresh/internship/on-site-internship/B37-S2028.html

### ⑧ Terraform の復習

- [ ] `terraform plan` の出力を読む練習
- [ ] AWS リソースのモジュール設計を復習
- [ ] `terraform validate` でコードを検証する方法

---

## 🟢 WEEK 2〜3 — 優先度：低

### ⑨ Neo4j × Python 連携を実装する

- [ ] neo4j Python ドライバーを使ってノード・リレーションシップを作成する
- [ ] インフラの依存関係を Neo4j で表現する練習
  - 例：「EC2 → RDS → S3」の依存グラフを作る

### ⑩ Copilot の使い方を整理する

- [ ] GitHub Copilot の設定を確認
- [ ] Copilot Chat の使い方を確認
- [ ] Claude Code との使い分けを整理する

---

## 学習ロードマップ

```
今日〜1週間：
├── Neo4j の Sandbox を触る（2時間）
├── Qdrant で RAG を理解する（2時間）
├── MCPサーバーをローカルで立てる（3時間）
└── CloudWatch の主要機能を整理（1時間）

1〜2週間：
├── LangGraph でシンプルな Agent を作る（3時間）
├── EvoOps の概念を理解する（1時間）
├── Terraform の復習（2時間）
└── Neo4j × Python 連携を実装（2時間）

参画直前：
├── プロジェクトのスケジュールを再確認
├── Slack の情報共有文化への準備
│   （最新LLM情報を積極的に共有する）
└── 自己紹介・貢献できることの整理
```

---

## 参画初日に言えると印象が良いこと

> 「MCPサーバーの構築を手元で試してきました。Neo4j の Cypher クエリも触れています。6〜7月の MCPサーバー構築に早速貢献できると思っています。」

---

## 参考リンクまとめ

| 技術 | URL |
|---|---|
| MCP 公式 | https://modelcontextprotocol.io/ |
| Neo4j Sandbox | https://sandbox.neo4j.com/ |
| Qdrant 公式 | https://qdrant.tech/documentation/ |
| LangGraph | https://langchain-ai.github.io/langgraph/ |
| CloudWatch | https://docs.aws.amazon.com/cloudwatch/ |
| EvoOps (NTTドコモ) | https://information.nttdocomo-fresh.jp/fresh/internship/on-site-internship/B37-S2028.html |
