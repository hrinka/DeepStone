#!/bin/bash
# 毎朝ローカルで自動実行：最新を pull → 出力先の分裂を是正 → 未レンダーの slides.json を全部画像化。
# launchd (ai.deepstone.render) から毎日9:10 JSTに起動される。
LOG=/tmp/deepstone-render.log
REPO="$HOME/CosmicTheta/DeepStone"
echo "===== $(date) =====" >> "$LOG"
cd "$REPO" || { echo "repo not found" >> "$LOG"; exit 1; }
git pull --no-rebase origin main >> "$LOG" 2>&1
# claude.ai 側 routine が aroma-insta/ に生成した場合の受け皿（詳細は tools/normalize-output.sh）
REPO="$REPO" bash "$REPO/tools/normalize-output.sh" >> "$LOG" 2>&1
bash "$REPO/tools/carousel-render/render_all.sh" >> "$LOG" 2>&1
echo "done $(date)" >> "$LOG"
