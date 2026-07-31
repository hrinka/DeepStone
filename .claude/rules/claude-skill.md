---
paths:
  - ".claude/skills/**"
  - ".claude/commands/**"
---

# skill / command 作成ルール

## どちらで持つか

- **command**（`.claude/commands/<name>.md`） — 手順が 1 ファイルに収まり、参照資料を
  持たないもの。人が `/name` と打って起動する前提
- **skill**（`.claude/skills/<name>/SKILL.md`） — 参照資料（`references/`）を分割したい、
  または**発話から自動で起動させたい**もの。`description` に trigger となる言い回しを
  具体的に列挙する

## 対応関係を放置しない

command と skill が同名で両方ある場合、**手順の正典は SKILL.md** とし、command 側は
skill を呼ぶだけの薄いラッパにする。両方に手順を書くと必ず片方が古くなる。

## 存在しない前提を書かない

hook・プラグイン・ディレクトリなど、**実在を確認していないものに依存する記述を入れない**。
（過去に `/wiki-fold` が存在しない PostToolUse hook を前提に書かれていた事例がある）
