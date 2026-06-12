#!/usr/bin/env python3
"""2枚の画像を黒地に白黒ミックスして1枚の背景を作る。EP-07: smiley + TB-303。"""
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageChops, ImageEnhance

W, H = 1080, 1350
d = Path.home() / "CosmicTheta/DeepStone/rave-team/output/EP-07"
smiley = d / "スクリーンショット 2026-06-12 17.59.36.png"
tb303 = d / "スクリーンショット 2026-06-12 18.04.20.png"
out = d / "slide_1.png"

def fit_w(im, w):
    r = w / im.width
    return im.resize((w, int(im.height * r)))

base = Image.new("L", (W, H), 0)

# スマイリー：反転して「白い線画」に（黄色背景→黒、黒線→白）
sm = ImageOps.grayscale(Image.open(smiley))
sm = ImageOps.invert(sm)
sm = sm.point(lambda p: 0 if p < 60 else p)      # 反転した黄色地を黒に落とす
sm = fit_w(sm, 760)
sm = ImageEnhance.Brightness(sm).enhance(1.0)
layer = Image.new("L", (W, H), 0)
layer.paste(sm, ((W - sm.width) // 2, 150))
base = ImageChops.lighter(base, layer)

# TB-303：白背景を黒に落として、実機だけ黒地に浮かべる
tb = ImageOps.grayscale(Image.open(tb303))
tb = tb.point(lambda p: 0 if p > 228 else p)     # 白背景→黒
tb = fit_w(tb, 1080)
tb = ImageEnhance.Brightness(tb).enhance(1.15)
layer2 = Image.new("L", (W, H), 0)
layer2.paste(tb, ((W - tb.width) // 2, 760))
base = ImageChops.lighter(base, layer2)

Image.merge("RGB", (base, base, base)).save(out)
print("saved", out, "size", Image.open(out).size)
