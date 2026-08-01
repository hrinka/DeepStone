#!/bin/bash
# 出力先の分裂を検出し、ファイルを正しい場所へ戻す。
#
# なぜ必要か:
#   日次生成は claude.ai 側のクラウド routine が行っており、この repo からは
#   設定を読むことも書き換えることもできない。routine のプロンプトに
#   `aroma-insta` が直書きされている場合、CLAUDE.md を直しても効かず、
#   毎朝 aroma-insta/output/ に POST が落ち続ける。
#
#   このスクリプトは「routine が直らなくても vault が正しい形に戻る」ための受け皿。
#
# やらないこと:
#   **commit も push もしない。** ファイルを移して stage するところまで。
#   commit / push は Obsidian Git と本人の操作に委ねる。無人で default branch へ
#   push する仕組みは、意図しない変更が外に出る経路になるため作らない。

set -uo pipefail
REPO="${REPO:-$HOME/CosmicTheta/DeepStone}"
cd "$REPO" || { echo "normalize: repo not found: $REPO"; exit 1; }

STRAY=$(find aroma-insta/output -maxdepth 1 -type d -name 'POST-*' 2>/dev/null | sort)
[ -z "$STRAY" ] && { echo "normalize: 是正対象なし"; exit 0; }

echo "normalize: ⚠️  出力先の分裂を検出しました（claude.ai 側 routine が未修正の可能性）"
MOVED=()
for d in $STRAY; do
  name=$(basename "$d")
  if [ -e "flava-fm/output/$name" ]; then
    echo "  SKIP $name — flava-fm 側に同名が既に存在。手動で確認してください"
    continue
  fi
  git mv "$d" "flava-fm/output/$name" 2>/dev/null || mv "$d" "flava-fm/output/$name"
  echo "  MOVE $name → flava-fm/output/$name"
  MOVED+=("$name")
done
[ ${#MOVED[@]} -eq 0 ] && { echo "normalize: 移動できたものなし"; exit 0; }

# 索引 flava-fm/output/posts.md に行を追加（carousel.md のメタから抽出）
for name in "${MOVED[@]}"; do
  grep -q "^| $name " flava-fm/output/posts.md 2>/dev/null && continue
  c="flava-fm/output/$name/carousel.md"
  [ -f "$c" ] || { echo "  WARN $name — carousel.md が無く索引に追加できません"; continue; }
  date=$(grep -m1 '^- 日付:'   "$c" | sed 's/^- 日付: *//')
  pil=$(grep -m1 '^- ピラー:' "$c" | sed 's/^- ピラー: *//')
  title=$(head -1 "$c" | sed 's/^# *//; s/^POST-[0-9]*: *//; s/ — Instagram カルーセル.*$//')
  row=$(printf '| %s | %s | %s | %s |' "$name" "${date:-?}" "${pil:-?}" "${title:-?}")
  # 表の最後の行の直後に挿入する。末尾に単純追記すると、表の後ろにある
  # 「索引に載っていないディレクトリ」の注記より下に落ちて表から外れるため。
  ROW="$row" perl -i -pe '
    BEGIN { $done = 0 }
    if (!$done && /^\| POST-/ .. 1) {
      if (!/^\| POST-/ && !$done) { print "$ENV{ROW}\n"; $done = 1 }
    }
  ' flava-fm/output/posts.md
  echo "  INDEX $name を索引に追加"
done

git add -A aroma-insta flava-fm 2>/dev/null

cat <<MSG

normalize: 移動と索引更新を stage しました（commit も push もしていません）。
  対象: ${MOVED[*]}
  → 次に Obsidian Git がコミットするか、手動で commit してください。
  → 根本原因は claude.ai 側 routine の出力先。直すまで毎朝これが走ります。
MSG
