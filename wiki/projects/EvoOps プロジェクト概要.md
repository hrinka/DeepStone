

- 組織: NTTドコモビジネス イノベーションセンター IOWN推進室 5G 2T
- 目的: 通信・クラウド運用の障害検知→原因特定→復旧を
  LLM×AIエージェントで自律化するプラットフォーム「EvoOps」
- 体制: ドコモビジネス約10名 + 富士通3名

## 自動化の4段階レベル（最重要・暗記）
1. Copilot（人主導・AI支援）
2. 自律型エージェント
3. マルチエージェントチーム
4. 組織全体の自律運用

## 3つの業務領域
- ① プロダクト評価・UI/UX改善提案
- ② 開発バックログ（FastAPI / React）
- ③ MCPサーバー設計・開発（Python）← 6〜7月の中心

## チームのMCP設計哲学（核心）
「APIをそのままMCPにするな。LLMに優しく作れ」

### 4つの設計原則
1. ユースケースを絞る（必要な機能だけツール化）
2. docstringで簡潔に説明（ツール選択を助ける）
3. パラメータを最小化（LLMが指定する値を減らす）
4. レスポンスを整理して返す（必要な値だけ構造化）

### なぜか
APIを全部変換するとコンテキストが膨大になり
LLMのパフォーマンス低下・ツール実行不能になるため

## 技術スタック
- FastMCP（Python MCP構築フレームワーク）https://gofastmcp.com/
- Claude Code（MCP利用・AI駆動開発）
- OpenStack（運用対象クラウド）※要キャッチアップ
- Neo4j（インフラ依存関係＝構造の記憶）
- Qdrant（RAG＝過去事例・知識の記憶）
- Orama（Neo4jアクセス）

## チーム文化
- AI駆動開発（AX: Agent Transformation）を実践
- コード以外もAIと協働（PJ管理・週報・設計レビュー）
- Slackで最新LLM情報を積極共有

## 自分の強み（どこで貢献するか）
- 短期: ③MCPサーバー開発（Claude Code×Python×API設計）
- 中期: ①UI/UX改善（フロント強みは希少）
- 長期: AX実践者（Obsidian×AI、Claude Code活用）

## 重要リンク
- 企画概要: [B37 EvoOps](https://information.nttdocomo-fresh.jp/fresh/internship/on-site-internship/B37-S2028.html)
- MCP設計記事: [LLMに易しいOpenStack MCP](https://engineers.ntt.com/entry/202512-advent-calendar-day13/entry)
- FastMCP: https://gofastmcp.com/

## 学びログ（随時追記）
### YYYY-MM-DD
-