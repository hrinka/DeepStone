---
type: concept
title: "Testing Strategy"
tags:
  - develop
  - testing
  - jest
  - vitest
  - e2e
  - tdd
updated: 2026-05-29
---

# Testing Strategy

「品質を担保できるエンジニアか」を測る面接頻出テーマ。Rinka の実務経験はユニットテスト・統合テスト（ChocoPLAi）。

---

## テストピラミッド

```
          E2Eテスト
        （少数・遅い・コスト高）
       ─────────────────────
         統合テスト
       （中程度）
      ─────────────────────
         ユニットテスト
       （多数・速い・コスト低）
```

| 種類 | テスト対象 | ツール |
|---|---|---|
| ユニットテスト | 関数・コンポーネント単体 | Jest / Vitest |
| 統合テスト | コンポーネント+API連携 | Testing Library / MSW |
| E2Eテスト | ユーザー操作フロー全体 | Playwright / Cypress |

---

## ユニットテスト（Jest / Vitest）

### React コンポーネントのテスト

```tsx
import { render, screen, fireEvent } from '@testing-library/react';

test('ボタンをクリックするとカウントが増える', () => {
  render(<Counter />);
  const button = screen.getByRole('button', { name: '+' });
  fireEvent.click(button);
  expect(screen.getByText('1')).toBeInTheDocument();
});
```

### 非同期テスト

```tsx
import { waitFor } from '@testing-library/react';

test('データ取得後にユーザー名が表示される', async () => {
  render(<UserProfile userId="1" />);
  await waitFor(() => {
    expect(screen.getByText('Rinka')).toBeInTheDocument();
  });
});
```

### モック（jest.mock / vi.mock）

```ts
// API呼び出しをモック
jest.mock('../api/users', () => ({
  fetchUser: jest.fn().mockResolvedValue({ name: 'Rinka' })
}));
```

**注意**: モックしすぎると実装の詳細に依存したテストになり、リファクタ時に壊れやすい。できるだけ振る舞い（ユーザーが見えるもの）をテストする。

---

## MSW（Mock Service Worker）

API をネットワークレベルでモックする。実際のfetchを使えるのでより実態に近い統合テストが書ける。

```ts
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users/:id', (req, res, ctx) => {
    return res(ctx.json({ name: 'Rinka' }));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

---

## E2Eテスト（Playwright）

```ts
import { test, expect } from '@playwright/test';

test('ログインしてダッシュボードが表示される', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name=email]', 'rinka@example.com');
  await page.fill('[name=password]', 'password');
  await page.click('button[type=submit]');
  await expect(page).toHaveURL('/dashboard');
  await expect(page.getByText('おかえり、Rinka')).toBeVisible();
});
```

---

## FastAPI のテスト（Python）

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Rinka"
```

pytest を使用。`conftest.py` でDBのフィクスチャを用意し、テスト用DBを使う。

---

## テスト戦略の考え方

### TDD（Test-Driven Development）

1. 失敗するテストを書く（Red）
2. テストが通る最小限の実装をする（Green）
3. リファクタリングする（Refactor）

すべてのコードにTDDが適しているわけではない。純粋な関数・ビジネスロジックに特に有効。

### テストの優先順位

1. **ビジネスロジックのユニットテスト**（バグが出ると困る計算処理・バリデーション）
2. **API エンドポイントの統合テスト**（正常系・エラー系のパターン）
3. **主要ユーザーフローのE2Eテスト**（ログイン・決済など）
4. UIの細かい見た目はスナップショットテストで

---

## CI との統合

```yaml
# .github/workflows/test.yml
name: Test
on: [pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test -- --coverage
      - run: npx playwright test  # E2Eはheadlessで
```

PRマージ前に自動テストが走る構成（[[AWS Infrastructure]] のCI/CD参照）。

---

## よくある面接質問と回答の軸

**Q: テストはどんな方針で書いていますか？**  
A: テストピラミッドを意識し、ユニットテストを土台に。ビジネスロジックとAPIエンドポイントを優先的にカバーし、主要フローはE2Eでも保護する。テストは「実装の詳細」ではなく「ユーザーが見る振る舞い」を検証するように書く（Testing Library のアプローチ）。

**Q: テストカバレッジ100%を目指しますか？**  
A: 数字を目標にするより、「壊れたら困る部分が保護されているか」を基準にする。設定ファイルや型定義のカバレッジを上げても意味が薄い。カバレッジはあくまで指標のひとつ。

**Q: モックはどこまで使いますか？**  
A: 外部APIやDBはモック（または MSW）する。内部の実装はできるだけモックしない。モックしすぎると「テストが通るが動かない」状態になりやすい。

## 関連

- [[AWS Infrastructure]] — GitHub Actions CI/CD への組み込み
- [[TypeScript Frontend]] — React Testing Library での型安全テスト
- [[Database Essentials]] — FastAPI テスト用DBフィクスチャ
