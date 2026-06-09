#!/bin/bash
# 未レンダーの slides.json を全部探して画像化する。
# 背景は各フォルダの bg.jpg / bg.png があれば自動採用、なければ slides.json の color。
#
# Usage:
#   bash tools/carousel-render/render_all.sh            # リポジトリ全体をスキャン
#   bash tools/carousel-render/render_all.sh <folder>   # 特定フォルダだけ
set -e
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$HOME/.claude/skills/nano-banana/venv/bin/python"
RENDER="$REPO/tools/carousel-render/render.py"
SCAN="${1:-$REPO}"

found=0
while IFS= read -r json; do
  dir="$(dirname "$json")"
  out="$dir/slides"
  # 既にレンダー済みでjsonの方が古ければスキップ
  if [ -d "$out" ] && [ "$out/slide_01.png" -nt "$json" ]; then
    continue
  fi
  bg=""
  for cand in "$dir/bg.jpg" "$dir/bg.png" "$dir/bg.jpeg"; do
    [ -f "$cand" ] && bg="$cand" && break
  done
  echo "▶ $dir"
  if [ -n "$bg" ]; then
    "$PY" "$RENDER" "$json" --out "$out" --bg "$bg"
  else
    "$PY" "$RENDER" "$json" --out "$out"
  fi
  found=$((found+1))
done < <(find "$SCAN" -name "slides.json" -not -path "*/node_modules/*")

echo ""
if [ "$found" -eq 0 ]; then echo "レンダー対象なし（全部最新）"; else echo "✅ $found 件レンダー完了"; fi
