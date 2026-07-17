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
[ -x "$PY" ] || PY="$(command -v python3 || command -v python)"
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
  # 表紙(slide1)だけに敷く背景。cover*.jpg / cover(1).jpg / cover 2.png 等を拾う（最初の1枚）。
  cover=""
  for cand in "$dir"/cover*.jpg "$dir"/cover*.jpeg "$dir"/cover*.png "$dir"/cover*.JPG "$dir"/cover*.PNG; do
    [ -f "$cand" ] && cover="$cand" && break
  done
  echo "▶ $dir"
  if [ -n "$cover" ]; then
    "$PY" "$RENDER" "$json" --out "$out" --cover-bg "$cover"
  else
    "$PY" "$RENDER" "$json" --out "$out"
  fi
  found=$((found+1))
done < <(find "$SCAN" -name "slides.json" -not -path "*/node_modules/*" -not -path "*/_archive/*")

echo ""
if [ "$found" -eq 0 ]; then echo "レンダー対象なし（全部最新）"; else echo "✅ $found 件レンダー完了"; fi
