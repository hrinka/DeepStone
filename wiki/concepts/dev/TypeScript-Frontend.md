---
type: concept
title: "TypeScript Frontend"
tags:
  - develop
  - typescript
  - react
  - nextjs
  - frontend
updated: 2026-05-29
---

# TypeScript Frontend

Rinka のコアスキル領域。約5年の実務経験。「型を書くだけ」でなく、チーム品質担保・APIバグゼロ設計まで責任を持つ。

## スタック

| ツール | 経験 | 代表プロジェクト |
|---|---|---|
| TypeScript | 約5年 | 全案件 |
| React / Next.js 15 | 約5年 | [[ChocoPLAi]], 家事代行マッチング |
| Nuxt.js v3 | 実務あり | 製造業コーポレートサイト |
| Three.js | 複数案件 | [[42Tokyo]]最終課題、飲食店サイト |
| shadcn/ui | 実務あり | 家事代行マッチング |
| Tailwind CSS | 実務あり | 複数案件 |

## 設計思想

**型の一貫設計**  
PydanticモデルとTypeScript型定義を「一致させる設計」。フロント・バックの API 繋ぎ目でのバグをゼロにする。

**コンポーネント設計3原則**
1. 単一責任 — 1コンポーネント・1役割
2. TypeScript型を厳格に — Props/Emitsの型を明確に
3. ロジック分離 — custom hooks / composables でテンプレートをシンプルに

**パフォーマンス意識**  
- Next.js 15 Static Export + CloudFront → LCP 大幅改善（[[ChocoPLAi]]）
- Core Web Vitals（LCP・CLS・FID）観点から設計
- Lazy Load・コード分割・バンドルサイズ最適化

## Next.js の使い分け

- **Static Export** — S3+CloudFront配信で高速化（ChocoPLAi）
- **App Router** — 認証付きフルスタック構成（家事代行マッチング）
- **Pages Router** — 旧プロジェクト対応

## 関連

- [[AWS Infrastructure]] — インフラと組み合わせたフルスタック設計
- [[AI Driven Development]] — v0でUIモックアップ生成・Claude Codeで設計レビュー
- [[ChocoPLAi]] — 最新の代表プロジェクト
