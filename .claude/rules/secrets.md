---
paths:
  - "**/*"
---

# シークレット取り扱いルール

## 平文で書かない

- API キー・アクセストークン・パスワード・webhook URL をファイルに直接書かない。
  `.env`（gitignore 済み）に置き、コードからは環境変数で読む
- ノートに貼りたくなったら、値ではなく**置き場所**を書く（「LINE のトークンは 1Password の
  〈項目名〉」）

## 検出を回避しない

gitleaks / GitHub Push Protection にブロックされた場合、**回避する行為を一切してはならない**。

- 禁止: bypass URL への誘導、`--no-verify` での commit、履歴書き換えによる回避、force push
- 必要な場合は状況を報告し、人間が判断・操作する

## この防衛線の限界（重要）

pre-commit hook は**デスクトップの CLI commit でしか走らない**。Obsidian Git のモバイル版は
native hook を実行しないため、モバイルからの commit は素通りする。
最終的な backstop は「repo を private に保つこと」と「push 先の Secret Scanning」である。

## プラグインの data.json

`.obsidian/plugins/*/data.json` は `.gitignore` 済み。端末ごとの状態であり、認証情報が入る
（実例: obsidian-local-rest-api = 自己署名 TLS 秘密鍵 + API キー、google-calendar =
Google OAuth リフレッシュトークン）。**この ignore を外さないこと。**
