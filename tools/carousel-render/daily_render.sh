#!/bin/bash
# 毎朝ローカルで自動実行：最新を pull → 未レンダーの slides.json を全部画像化。
# launchd (ai.deepstone.render) から毎日9:10 JSTに起動される。
LOG=/tmp/deepstone-render.log
REPO="$HOME/CosmicTheta/DeepStone"
echo "===== $(date) =====" >> "$LOG"
cd "$REPO" || { echo "repo not found" >> "$LOG"; exit 1; }
git pull --no-rebase origin main >> "$LOG" 2>&1
bash "$REPO/tools/carousel-render/render_all.sh" >> "$LOG" 2>&1
echo "done $(date)" >> "$LOG"
