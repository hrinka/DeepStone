---
type: concept
title: "AI Driven Development"
tags:
  - develop
  - AI
  - claude
  - claude-code
  - v0
updated: 2026-05-29
---

# AI Driven Development

Rinka がエンジニアとして実践・体系化したAI駆動開発。「AIを使う」から「AIをフローに組み込む」へのシフトが中心思想。

## 3レイヤー活用モデル

### Layer 1｜プロダクトへのAI機能組み込み（Claude API）

**ChocoPLAi での実装**:
- Claude API でキャッシュフロー分析コメント機能を実装
- プロンプト設計・ストリーミングレスポンス処理・エラーハンドリング・UX設計を一気通貫

**ハルシネーション対策3原則**:
1. **根拠を制約するプロンプト** — 「提供データのみ根拠にしてください」とシステムプロンプトに明示
2. **出力の構造化とバリデーション** — JSONレスポンス + Python側で実データと自動照合
3. **確信度の出力** — `confidence: low` を返させてフロントで警告UXを実現

### Layer 2｜開発効率化（Claude Code / v0）

**Claude Code 活用**:
- 設計レビュー・リファクタリング・ドキュメント生成・デバッグに日常的活用
- AGENTS.md を整備し、AIエージェントが自律的にコードを書ける環境を構築（ChocoPLAi）
- 「詰まったらClaude Codeで壁打ち → 自分でレビュー採用 → 前進」サイクルの定着

**v0 活用**:
- Figmaの仕様からUIモックアップを即生成
- 製造業サイト案件で工数約40%削減

### Layer 3｜知識管理・ルーティン自動化

- Obsidian × Claude Code = DeepStone（自動コードレビュー・知識管理）
- 日々のルーティンタスクのAI自律実行
- このVaultそのものが Layer 3 の実践

## AI出力に対する姿勢

> AIの出力をそのまま使わず、型安全性・パフォーマンス・保守性の観点でレビューしてから採用する。

AIは「生成器」でなく「協業相手」として扱う。最終判断は常に人間側。

## 関連

- [[ChocoPLAi]] — Claude API統合の実装事例
- [[AWS Infrastructure]] — Lambda + Claude API のサーバーレス構成
- [[TypeScript Frontend]] — v0 によるUI高速生成との組み合わせ
