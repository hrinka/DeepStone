---
type: concept
title: "React Deep Dive"
tags:
  - develop
  - react
  - nextjs
  - hooks
  - rendering
updated: 2026-05-29
---

# React Deep Dive

面接で「Reactわかってる人か」を判定するために聞かれる深掘り知識。[[TypeScript Frontend]] の補完。

---

## Hooks 深掘り

### useEffect の依存配列

```ts
useEffect(() => {
  fetchData(id);
}, [id]); // id が変わるたびに実行
```

- **空配列 `[]`**: マウント時に1回だけ
- **依存あり**: 依存値が変わるたびに実行
- **なし**: 毎レンダー後に実行（ほぼ使わない）
- **クリーンアップ**: `return () => { ... }` でアンマウント時に実行（イベントリスナー解除・タイマークリアなど）

よくある罠: ESLint の `exhaustive-deps` を無視して依存配列を手動管理すると無限ループや古いクロージャが発生する。

### useMemo / useCallback

```ts
// useMemo: 重い計算結果をキャッシュ
const sorted = useMemo(() => expensiveSort(items), [items]);

// useCallback: 関数参照をキャッシュ（子コンポーネントへのprop渡し時）
const handleClick = useCallback(() => { doSomething(id); }, [id]);
```

**使い所の原則**:
- 計算コストが明らかに高い場合のみ `useMemo`
- `React.memo` でラップした子コンポーネントに渡す関数は `useCallback`
- 乱用するとメモ化自体のコストが上回る → プロファイルしてから判断

### useRef

- **DOM参照**: `inputRef.current.focus()`
- **レンダーをまたぐ値の保持**: 前の値の記憶、タイマーID保存など
- **再レンダーを起こさない**（stateとの違い）

### カスタム hooks

ロジックを再利用可能な単位に分離。テンプレートをシンプルに保つ。

```ts
// useFetch.ts
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false));
  }, [url]);
  return { data, loading };
}
```

---

## レンダリング最適化

### 仮想DOM（Virtual DOM）

- Reactは UI の仮想表現（JavaScript オブジェクト）を持つ
- 状態変化 → 新しい仮想DOMを作成 → 差分（diff）を計算 → 実DOMに最小限の変更を適用（reconciliation）
- **コスト**: diffアルゴリズム自体にもコストがかかる。不要な再レンダーを減らす方が効果的なことが多い

### React.memo

```ts
const Child = React.memo(({ value }: { value: number }) => {
  return <div>{value}</div>;
});
// propsが変わらなければ再レンダーしない
```

### なぜ key が重要か

リスト描画で `key` が変わるとReactは要素を作り直す（アンマウント→マウント）。  
- index をkeyにすると並び替え時に正しく差分検知できない
- 一意なIDを使うのが正解

### Concurrent Mode / Suspense

React 18の機能。優先度の低い更新（例: 検索候補の表示）を後回しにしてUIをブロックしない。

```tsx
<Suspense fallback={<Spinner />}>
  <SlowComponent />
</Suspense>
```

---

## Next.js レンダリング戦略

| 戦略 | 仕組み | 向いているページ |
|---|---|---|
| **SSG**（Static Site Generation） | ビルド時にHTMLを生成 | ブログ・LP・静的コンテンツ |
| **SSR**（Server-Side Rendering） | リクエストごとにサーバーでHTML生成 | 認証必須・リアルタイムデータ |
| **ISR**（Incremental Static Regeneration） | 一定時間後に再ビルド | ECサイト・ニュース |
| **CSR**（Client-Side Rendering） | ブラウザでJS実行後に描画 | ダッシュボード・管理画面 |
| **Static Export** | 全ページSSGでHTMLファイルを出力 | S3+CloudFront 配信（[[ChocoPLAi]]） |

### React Server Components（RSC）

Next.js 13 App Router から標準。サーバーでレンダーしクライアントにHTMLを送る（JSバンドルを減らせる）。

```tsx
// Server Component（デフォルト）: DB直アクセスOK, hooksNG
async function Page() {
  const data = await db.query('SELECT ...');
  return <div>{data}</div>;
}

// Client Component: 'use client' を宣言, hooksOK
'use client';
function Counter() {
  const [count, setCount] = useState(0);
  ...
}
```

---

## State 管理

| ツール | 向いている規模 | 特徴 |
|---|---|---|
| useState / useReducer | コンポーネント内 | シンプル |
| Context API | 中規模・テーマ/認証情報 | prop drillを避ける、頻繁更新は非推奨 |
| Zustand | 中〜大規模 | 軽量・シンプルなグローバルstore |
| Redux Toolkit | 大規模・複雑 | 厳格なデータフロー、devtools強力 |
| React Query / SWR | サーバー状態管理 | fetch・キャッシュ・revalidate を自動化 |

---

## よくある面接質問と回答の軸

**Q: useEffectとuseLayoutEffectの違いは？**  
A: useEffect は描画後に非同期実行。useLayoutEffect は描画前に同期実行（DOM操作後の計測などに使う。通常はuseEffectで十分）。

**Q: Reactの再レンダーはいつ起きる？**  
A: ① stateが変わった時 ② 親から渡されるpropsが変わった時 ③ useContextの値が変わった時。React.memoはpropsの浅い比較でスキップ可能。

**Q: useStateとuseRefの違いは？**  
A: useStateは値変更時に再レンダーを起こす。useRefは起こさない（DOMや前回値の保持に使う）。

## 関連

- [[TypeScript Frontend]] — React の型安全実装パターン
- [[AWS Infrastructure]] — Next.js Static Export と CloudFront 配信
