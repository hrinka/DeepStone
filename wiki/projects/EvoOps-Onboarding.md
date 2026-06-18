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

# EvoOps Onboarding

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
production-onboarding-roadmap.md

・1体のエージェントを本番にデプロイしてから、フル自立稼働に至るまでの段階設計
・認識能力(observe / judge)は積極的に学習させる。制御権限(act)は段階的にしか開放しない。
・最終的に育てるべきは単体エージェントの能力ではなく、**本番環境に適応できるエージェント組織能力**。
・検証で操作を学び、本番で判断を学び、権限を段階的に与える。


・検証では静的品質を仕上げる。

・本番では段階的に権限を広げながら動的品質を積み上げる。いきなり全権限を与えず、認識(観察・判断)と制御(実行)を分離して育てる。

・事故の原因は能力不足ではなく権限の渡しすぎ。


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
