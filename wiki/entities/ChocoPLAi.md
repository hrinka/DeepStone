---
type: entity
entity_type: project
title: "ChocoPLAi"
tags:
  - develop
  - project
  - fintech
  - aws
  - claude-api
updated: 2026-05-29
---

# ChocoPLAi

FinTech 系 Web アプリ。Rinka が設計・実装した代表作。フロントエンド・バックエンド・インフラ・Claude API統合まで一人で担当。

## 概要

| 項目 | 内容 |
|---|---|
| 種別 | キャッシュフロー分析 SaaS |
| 担当 | フロント全体 + バックエンド + インフラ + AI機能 |
| フロント | Next.js 15（Static Export）/ TypeScript / Zod |
| バックエンド | FastAPI / Python 3.11 / SQLAlchemy / Alembic / Pydantic |
| インフラ | AWS（S3 + CloudFront + App Runner + RDS / Terraform） |
| AI | Claude API（キャッシュフロー分析コメント機能） |
| CI/CD | GitHub Actions（PRマージトリガー） |

## アーキテクチャ

```
フロント（Next.js 15 Static Export）
         ↓
  S3 + CloudFront（CDN・高速配信）
         ↓
    App Runner（FastAPI コンテナ）
         ↓
    RDS PostgreSQL（プライベート接続）
         ↓
  Claude API（分析コメント生成）
```

## 技術的特徴

**型の一貫設計**: Pydantic（バックエンド）と Zod + TypeScript（フロントエンド）でスキーマを同期させ、API繋ぎ目のバグをゼロに。

**AI統合**: ハルシネーション3対策（プロンプト制約・JSON出力バリデーション・確信度返却）を実装済み。

**AGENTS.md**: AIエージェントが自律的にコードを書ける環境を整備。

**IaC**: Terraform でAWSインフラ全体をコード管理。

## 課題と解決

TerraformでのAWSインフラ構築とClaude API組み込みを同時並行する必要があった。  
→ タスクを「ブロッカー」と「後回し可能」に分解し、インフラ先行→AI機能接続の順で整理。Claude Codeで設計の壁打ちしながら前進。期限内リリース達成。

## 関連

- [[TypeScript Frontend]] — Next.js 15 実装
- [[AWS Infrastructure]] — Terraform + App Runner 構成
- [[AI Driven Development]] — Claude API 統合
