---
type: entity
entity_type: project
title: "New Moon Guild"
tags:
  - develop
  - project
  - metaverse
  - hackathon
  - NTTdocomo
updated: 2026-05-29
---

# New Moon Guild

NTTドコモ主催ハッカソン **最優秀賞**受賞プロジェクト。DJライブ × メタバース × AI感情解析のリアルタイム連携。Rinka が10名チームのリードを担当。

## 概要

| 項目 | 内容 |
|---|---|
| クライアント / 主催 | NTTドコモ（MetaMe メタバース） |
| 期間 | 3ヶ月 |
| チーム規模 | 10名（エンジニア・デザイナー・音響スタッフ） |
| 受賞 | **NTTドコモ主催ハッカソン 最優秀賞** |
| Rinka の役割 | チームリード、React / Node.js 実装 |

## 技術構成

```
DJ機材（BPM・楽曲情報）
        ↓ OSCプロトコル
Unreal Engine 5（メタバース空間）
        ↓
React / Node.js（演出連動ダッシュボード）
        ↓
AIリアルタイム感情解析
        ↓
照明・エフェクト動的制御
```

- **OSC プロトコル**: DJ機材とUnreal Engine 5をリアルタイム連携
- **感情解析**: ユーザーコメントをAIで解析し、演出を動的制御
- **Node.js**: TypeScriptでOSCプロトコル処理・感情解析ロジック実装

## リードとしての取り組み

職種バラバラ（エンジニア・デザイナー・音響）のチームで共通言語を作ることが課題。

**解決策**:
- Figma・Miroで技術仕様を視覚化し、非エンジニアも理解できる共有方法を設計
- 毎朝のショートスタンドアップ（今日やること + 詰まっていること）を制度化

## Rinka にとっての意味

「技術・演出・チームマネジメントの3つを同時に回した、エンジニアとして一番成長を感じたプロジェクト」

DJカルチャーとエンジニアリングが交差する点でもあり、[[Rt3mis]] としてのアーティスト活動とシナジーを持つ。

## 関連

- [[TypeScript Frontend]] — React / Node.js 実装
- [[AI Driven Development]] — AIリアルタイム感情解析
