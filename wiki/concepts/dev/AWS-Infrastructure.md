---
type: concept
title: "AWS Infrastructure"
tags:
  - develop
  - aws
  - terraform
  - IaC
  - devops
updated: 2026-05-29
---

# AWS Infrastructure

Rinka のインフラ設計力。フロントエンド主軸ながら、インフラ全体を一人で設計・構築した実務経験あり（[[ChocoPLAi]]）。

## 使用 AWS サービス

| サービス | 役割 | 使用案件 |
|---|---|---|
| S3 | 静的ビルド成果物の格納 / PDFストレージ | ChocoPLAi |
| CloudFront | CDN（全国高速配信） | ChocoPLAi |
| App Runner | FastAPIコンテナのマネージド実行 | ChocoPLAi |
| RDS（PostgreSQL） | プライベートDB | ChocoPLAi |
| EC2 | Railsアプリ本番運用・保守 | ファッション系EC |
| Lambda | サーバーレス処理（概念理解・設計力あり） | — |
| API Gateway | Lambda前段（設計経験あり） | — |

## Terraform（IaC）

**ChocoPLAiでの実績**:
- AWS インフラ全体をTerraformでコード化
- GitHub Actionsと連携 → PRマージをトリガーに自動テスト・自動デプロイ
- 再現性・バージョン管理・チームでの共有が可能に

**IaC の意義**:
インフラを「コード」として扱うことで、環境差異をなくし、レビュー・ロールバック・複製が容易になる。Terraform は AWS の de facto 標準。

## SRE（Site Reliability Engineering）

Googleが提唱。インフラ運用をソフトウェアエンジニアリングの手法で解決するアプローチ。
- 障害対応の自動化
- SLO（Service Level Objectives）の設定
- トイル（反復手作業）の撲滅

Rinka の CI/CD整備・Terraform IaC はSREの思想に沿った実践。

## サーバーレス構成（設計知識）

```
フロント(React/TS)
     ↓
API Gateway
     ↓
Lambda（軽量処理）
     ↓  ↘
   SQS    S3（ストレージ）
     ↓
Lambda（Claude API呼び出し）
     ↓
RDS（結果保存）
```

Lambda のタイムアウト上限（15分）対策として SQS でキューイングが必要。PoC フェーズのリクエスト課金モデルと相性良い。

## 関連

- [[TypeScript Frontend]] — Next.js Static Export + CloudFront の組み合わせ
- [[AI Driven Development]] — Lambda + Claude API によるサーバーレスAI処理
- [[ChocoPLAi]] — Terraform + App Runner + RDS の実装事例
