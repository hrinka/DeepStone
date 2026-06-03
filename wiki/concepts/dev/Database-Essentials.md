---
type: concept
title: "Database Essentials"
tags:
  - develop
  - database
  - sql
  - postgresql
  - orm
updated: 2026-05-29
---

# Database Essentials

フルスタック・バックエンドエンジニアとして「DBを理解している」を示す知識。[[ChocoPLAi]] では PostgreSQL + SQLAlchemy を使用。

---

## SQL 基礎

### DDL（テーブル定義）

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### DML（データ操作）

```sql
-- SELECT
SELECT u.name, p.title
FROM users u
INNER JOIN posts p ON u.id = p.user_id
WHERE u.created_at > '2024-01-01'
ORDER BY p.created_at DESC
LIMIT 20 OFFSET 40;  -- ページネーション

-- INSERT
INSERT INTO users (email, name) VALUES ('rinka@example.com', 'Rinka');

-- UPDATE
UPDATE users SET name = 'Rinka Honma' WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;
```

### JOINの種類

| JOIN | 説明 |
|---|---|
| INNER JOIN | 両方に存在するレコードのみ |
| LEFT JOIN | 左テーブルを全件 + 右に一致するもの（NULLあり） |
| RIGHT JOIN | 右テーブルを全件 + 左に一致するもの |
| FULL OUTER JOIN | どちらかに存在する全レコード |

---

## インデックス

大量のデータから高速に検索するための仕組み（本の索引と同じ）。

```sql
-- インデックス作成
CREATE INDEX idx_users_email ON users(email);

-- 複合インデックス（検索条件の順番に合わせる）
CREATE INDEX idx_posts_user_created ON posts(user_id, created_at DESC);
```

### インデックスが効く条件・効かない条件

```sql
-- 効く
WHERE email = 'rinka@example.com'      -- 完全一致
WHERE created_at > '2024-01-01'        -- 範囲検索（先頭列のみ）
WHERE user_id = 1 AND created_at > ... -- 複合インデックスの先頭から使う

-- 効きにくい
WHERE LOWER(email) = 'rinka@...'       -- 関数をかけると効かない
WHERE email LIKE '%rinka%'             -- 前方一致以外の LIKE
```

**トレードオフ**: インデックスはSELECTを速くするが、INSERT/UPDATE/DELETEを遅くする（インデックスも更新が必要なため）。

---

## トランザクション / ACID

複数の操作を「すべて成功」か「すべて失敗（ロールバック）」にまとめる仕組み。

```sql
BEGIN;
UPDATE accounts SET balance = balance - 10000 WHERE id = 1;
UPDATE accounts SET balance = balance + 10000 WHERE id = 2;
COMMIT; -- または ROLLBACK;
```

### ACID 特性

| 特性 | 意味 |
|---|---|
| **A**tomicity（原子性） | 全部成功か全部失敗 |
| **C**onsistency（一貫性） | トランザクション前後でDB制約を満たす |
| **I**solation（分離性） | 並行トランザクションが互いに影響しない |
| **D**urability（永続性） | コミット済みデータはシステム障害でも失われない |

### SQLAlchemy でのトランザクション（ChocoPLAi で使用）

```python
async with db.begin():
    user = User(email="rinka@example.com")
    db.add(user)
    # ここでエラーが出れば自動ロールバック
```

---

## N+1 問題

最も頻出のパフォーマンス問題。

```python
# N+1 問題（ユーザー10人に対してクエリが11回走る）
users = db.query(User).all()     # クエリ1回
for user in users:
    posts = user.posts           # ユーザーごとにクエリが走る（N回）
```

**解決策: eager loading（JOIN で一括取得）**

```python
# SQLAlchemy: joinedload
users = db.query(User).options(joinedload(User.posts)).all()
# SELECT users.*, posts.* FROM users LEFT JOIN posts ON ... -- 1回で済む
```

---

## マイグレーション

スキーマ変更を履歴管理する仕組み。[[ChocoPLAi]] では **Alembic** を使用。

```bash
alembic revision --autogenerate -m "add_user_table"
alembic upgrade head   # 最新まで適用
alembic downgrade -1   # 1つ戻す
```

本番環境では `alembic upgrade head` をデプロイの自動化（GitHub Actions）に組み込む。

---

## PostgreSQL 特有の機能

| 機能 | 用途 |
|---|---|
| `JSONB` | JSONデータをインデックス付きで保存（柔軟なスキーマ） |
| `UUID` | 主キーにUUIDを使う（分散システムでID衝突を防ぐ） |
| `ARRAY` | 配列型（タグ機能など） |
| Full Text Search | 全文検索（日本語は `pgroonga` 拡張が強力） |
| `EXPLAIN ANALYZE` | クエリの実行計画を確認（ボトルネック分析） |

---

## RDB vs NoSQL

| | RDB（PostgreSQL等） | NoSQL（MongoDB, DynamoDB等） |
|---|---|---|
| スキーマ | 固定（変更にマイグレーションが必要） | 柔軟（ドキュメント単位） |
| 一貫性 | ACID保証 | 結果整合性（設定による） |
| スケール | 垂直スケールが主 | 水平スケールしやすい |
| 向いている用途 | 金融・EC・複雑なリレーション | SNSフィード・IoT・スキーマ頻繁変更 |

[[ChocoPLAi]] はFinTechアプリのため、ACID保証のあるPostgreSQLを選択。

---

## よくある面接質問と回答の軸

**Q: インデックスとは何ですか？なぜ使いますか？**  
A: テーブルを高速に検索するためのデータ構造（B-Tree等）。フルテーブルスキャンをO(n)→O(log n)にする。ただしINSERT/UPDATE時のオーバーヘッドがあるため、頻繁に検索するカラムに絞って設定する。

**Q: トランザクションとは何ですか？**  
A: 複数のDB操作をひとかたまりとして扱う仕組み。全部成功するかロールバックするかのどちらかにする（ACID保証）。口座振り込みのように「片方だけ実行されてはいけない」操作に使う。

**Q: N+1問題を経験したことはありますか？**  
A: SQLAlchemyを使ったAPIでログを見てクエリが大量発行されていることに気づき、`joinedload`に切り替えて解決した。ORM使用時は `EXPLAIN ANALYZE` でクエリ確認を習慣にしている。

## 関連

- [[AWS Infrastructure]] — RDS PostgreSQL の運用
- [[Web Security]] — SQLインジェクション対策
- [[TypeScript Frontend]] — フロントから見てAPIレスポンス型を設計する観点
