#!/usr/bin/env python3
"""PLUR SYSTEM DIARY ロゴ生成（2案）。Pillow + DIN Condensed。1080x1080 プロフィール対応。"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

S = 1080
BG = (10, 10, 10)
WHITE = (255, 255, 255)
ECRU = (236, 236, 236)
GREY = (74, 74, 74)
HEAD = "/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf"
OUT = Path.home() / "CosmicTheta/DeepStone/brand/logos"
OUT.mkdir(parents=True, exist_ok=True)

# 音楽波形の振幅（0-1）
HEIGHTS = [0.22,0.5,0.32,0.66,0.85,0.5,0.97,0.6,0.4,0.72,1.0,0.55,0.34,
           0.78,0.48,0.88,0.44,0.3,0.62,0.42,0.74,0.52,0.26,0.58,0.36,0.68,0.3,0.5,0.22]

def F(size): return ImageFont.truetype(HEAD, size)

def ctext(d, cx, y, text, font, fill, ls=0):
    # letter-spacing付き中央寄せ
    widths = [d.textlength(c, font=font) for c in text]
    total = sum(widths) + ls*(len(text)-1)
    x = cx - total/2
    for c, w in zip(text, widths):
        d.text((x, y), c, font=font, fill=fill)
        x += w + ls

def waveform(d, cx, cy, total_w, max_h, color, bars=HEIGHTS):
    n = len(bars)
    bw = total_w/(n*1.7)
    step = bw*1.7
    x = cx - (n*step - (step-bw))/2
    for h in bars:
        hh = max(max_h*h, bw)
        d.rounded_rectangle([x, cy-hh/2, x+bw, cy+hh/2], radius=bw/2, fill=color)
        x += step

def diary():
    img = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(img)
    # spiral binding (top)
    for i in range(11):
        x = 300 + i*50
        d.rounded_rectangle([x-7, 95, x+7, 175], radius=7, fill=ECRU)
    d.line([250, 175, 830, 175], fill=GREY, width=4)
    # soundwave
    waveform(d, S/2, 470, 620, 360, WHITE)
    # wordmark — 全語
    ctext(d, S/2, 660, "PLUR", F(190), WHITE, ls=10)
    ctext(d, S/2, 870, "SYSTEM DIARY", F(92), ECRU, ls=14)
    img.save(OUT/"plur-logo-diary.png")
    return img

def dubplate():
    img = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(img)
    cx = cy = S/2
    # record grooves
    for r, col, w in [(440, ECRU, 6), (400, (38,38,38), 2), (362, (38,38,38), 2), (324, (38,38,38), 2)]:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=col, width=w)
    # center label（大きめ・全語を収める）
    lr = 262
    d.ellipse([cx-lr, cy-lr, cx+lr, cy+lr], fill=BG, outline=ECRU, width=5)
    # 縦積み：PLUR / 波形 / SYSTEM DIARY（穴は省略＝可読性優先）
    ctext(d, cx, 358, "PLUR", F(150), WHITE, ls=6)
    waveform(d, cx, 560, 300, 130, WHITE)
    ctext(d, cx, 648, "SYSTEM DIARY", F(52), ECRU, ls=9)
    img.save(OUT/"plur-logo-dubplate.png")
    return img

if __name__ == "__main__":
    diary(); dubplate()
    print("saved:", OUT/"plur-logo-diary.png", "+", OUT/"plur-logo-dubplate.png")
