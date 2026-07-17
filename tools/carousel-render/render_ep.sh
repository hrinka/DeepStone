#!/bin/bash
# 特定EPのスライドを背景画像込みで再レンダーする
#
# Usage:
#   bash tools/carousel-render/render_ep.sh EP-10
#   bash tools/carousel-render/render_ep.sh EP-10 rave-team   # アカウント指定（省略可）
#
# 背景画像の置き場所: rave-team/output/EP-XX/slides/EPXX-1.png ~ EPXX-8.png
# レンダー結果:       rave-team/output/EP-XX/slides/slide_01.png ~ slide_08.png

set -e
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$HOME/.claude/skills/nano-banana/venv/bin/python"
[ -x "$PY" ] || PY="$(command -v python3 || command -v python)"
RENDER="$REPO/tools/carousel-render/render.py"

EP="${1:?Usage: $0 EP-XX}"
ACCOUNT="${2:-rave-team}"
DIR="$REPO/$ACCOUNT/output/$EP"
JSON="$DIR/slides.json"

[ -f "$JSON" ] || { echo "❌ $JSON が見つかりません"; exit 1; }

OUT="$DIR/slides"
cover=""
for cand in "$DIR"/cover*.jpg "$DIR"/cover*.jpeg "$DIR"/cover*.png; do
  [ -f "$cand" ] && cover="$cand" && break
done

echo "▶ $EP をレンダー中..."
if [ -n "$cover" ]; then
  "$PY" "$RENDER" "$JSON" --out "$OUT" --cover-bg "$cover"
else
  "$PY" "$RENDER" "$JSON" --out "$OUT"
fi
echo "✅ 完了 → $OUT"
