---
type: concept
title: "HTTP / Browser Basics"
tags:
  - develop
  - http
  - browser
  - cors
  - cache
  - web
updated: 2026-05-29
---

# HTTP / Browser Basics

フロントエンドエンジニアとして「ブラウザがやること」を説明できるか確認される知識。

---

## HTTP の基礎

### リクエスト / レスポンスの構造

```
GET /api/users HTTP/1.1
Host: example.com
Authorization: Bearer xxx
Content-Type: application/json

{"key": "value"}
```

- **メソッド**: GET（取得）/ POST（作成）/ PUT（全体更新）/ PATCH（部分更新）/ DELETE（削除）
- **ヘッダー**: メタ情報（認証・Content-Type・Cache-Controlなど）
- **ボディ**: POSTやPATCH時のデータ

### よく使うステータスコード

| コード | 意味 | よくある場面 |
|---|---|---|
| 200 | OK | 正常取得 |
| 201 | Created | POST で作成成功 |
| 204 | No Content | DELETE 成功（ボディなし） |
| 301 | Moved Permanently | 恒久リダイレクト |
| 302 | Found | 一時リダイレクト |
| 304 | Not Modified | キャッシュ有効（再取得不要） |
| 400 | Bad Request | クライアント側の入力エラー |
| 401 | Unauthorized | 認証が必要 |
| 403 | Forbidden | 認証済みだが権限なし |
| 404 | Not Found | リソースが存在しない |
| 422 | Unprocessable Entity | バリデーションエラー（FastAPIの標準） |
| 500 | Internal Server Error | サーバー側の予期せぬエラー |
| 503 | Service Unavailable | サーバー過負荷・メンテ中 |

### HTTP/1.1 vs HTTP/2

- **HTTP/1.1**: リクエストは1接続1並列。ドメインシャーディングで回避していた
- **HTTP/2**: 1接続で多重化（multiplexing）。ヘッダー圧縮。CloudFrontはHTTP/2対応

---

## CORS（Cross-Origin Resource Sharing）

ブラウザのセキュリティ機構。異なるオリジン（プロトコル+ドメイン+ポート）へのリクエストをブラウザがブロックする。

```
フロント: https://app.example.com
API:     https://api.example.com  ← 別オリジン → CORS が発生
```

### プリフライトリクエスト（OPTIONS）

POSTやカスタムヘッダーを含むリクエスト前に、ブラウザが自動でOPTIONSを投げて許可を確認する。

```
OPTIONS /api/data
Origin: https://app.example.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization
```

サーバーが `Access-Control-Allow-Origin: https://app.example.com` を返せばOK。

### FastAPI での CORS 設定（ChocoPLAi での実践）

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.example.com"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
```

`allow_origins=["*"]` は開発時のみ。本番では明示的にオリジンを列挙する。

---

## Cookie / Session / Token

### Cookie の属性

| 属性 | 意味 |
|---|---|
| `HttpOnly` | JSからアクセス不可（XSS対策） |
| `Secure` | HTTPS通信時のみ送信 |
| `SameSite=Strict` | 同一サイトのリクエストにのみ送信（CSRF対策） |
| `SameSite=Lax` | クロスサイトのGETは許可（デフォルト） |
| `Expires` / `Max-Age` | 有効期限 |
| `Domain` / `Path` | 送信するドメイン・パスを制限 |

### Session vs JWT

| | Session | JWT（JSON Web Token） |
|---|---|---|
| 状態の保存 | サーバー側（DB・Redis） | クライアント側（トークン自体） |
| スケーリング | サーバー間でセッション共有が必要 | ステートレス（どのサーバーでも検証可能） |
| 失効 | 即時無効化できる | 有効期限まで有効（Blacklistが必要） |
| サイズ | 小さい（IDのみ） | 大きい（ペイロード込み） |
| 向いている用途 | 従来のWebアプリ | SPA・マイクロサービス・API |

NextAuthはSessionとJWTの両方をサポート。[[ChocoPLAi]] では JWT を使用。

---

## キャッシュ制御

### Cache-Control ヘッダー

```
Cache-Control: max-age=3600         # 1時間キャッシュ
Cache-Control: no-cache             # 毎回再検証（使用はキャッシュでOK）
Cache-Control: no-store             # キャッシュ禁止（機密情報）
Cache-Control: public               # CDNもキャッシュ可
Cache-Control: private              # ブラウザのみキャッシュ（CDN不可）
Cache-Control: stale-while-revalidate=60  # 古いキャッシュを即返しつつ裏でrevalidate
```

### ETag / Last-Modified（条件付きリクエスト）

サーバーがETagを返し → 次のリクエストで `If-None-Match` を送る → 変更なければ 304 を返す（ボディ転送なし）。

---

## ブラウザのレンダリング過程

```
HTML取得 → DOM構築 → CSS取得 → CSSOM構築
           ↓
      Render Tree構築 → Layout（位置計算） → Paint（描画） → Composite
```

**パフォーマンスに関わるポイント**:
- **レイアウトを引き起こすCSSプロパティ**（width, height, marginなど）の変更は高コスト
- **compositeのみで済むプロパティ**（transform, opacity）はGPUで処理 → 高速
- `will-change: transform` でGPUレイヤーを事前確保できる（乱用は逆効果）

---

## よくある面接質問と回答の軸

**Q: 401と403の違いは？**  
A: 401は「誰か教えてください（未認証）」、403は「あなたに権限がありません（認証済みだが禁止）」。

**Q: CORSエラーが出た時どう対処する？**  
A: サーバー側で `Access-Control-Allow-Origin` を正しく設定する。ブラウザのセキュリティ機構なのでフロント側だけでは解決できない（プロキシで迂回する方法もある）。

**Q: JWTの問題点は？**  
A: 有効期限内は取り消せない点。対策としてアクセストークンを短命（15分）にし、長命のリフレッシュトークンで更新する構成が一般的。

## 関連

- [[Web Security]] — XSS/CSRF と Cookie の組み合わせ
- [[TypeScript Frontend]] — Next.js での認証（NextAuth）
- [[AWS Infrastructure]] — CloudFront キャッシュ戦略
