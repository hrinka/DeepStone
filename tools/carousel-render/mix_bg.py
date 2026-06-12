#!/usr/bin/env python3
"""EP-07 用：3枚の素材を黒地に映える白黒背景に加工して slide_N.png を出力。
   smile_melty → slide_1（表紙） / tb303 → slide_2 / smile → slide_7"""
from pathlib import Path
from PIL import Image, ImageOps, ImageChops, ImageEnhance

W, H = 1080, 1350
d = Path.home() / "CosmicTheta/DeepStone/rave-team/output/EP-07"

def fit_w(im, w):
    return im.resize((w, int(im.height * w / im.width)))
def fit_h(im, h):
    return im.resize((int(im.width * h / im.height), h))

def on_black(layer_img, y, x=None):
    canvas = Image.new("L", (W, H), 0)
    x = (W - layer_img.width) // 2 if x is None else x
    canvas.paste(layer_img, (x, y))
    return canvas

def smiley_lineart(path, sized):
    """黄色＋黒線＋白/黄背景 → 反転して白い線画に（背景は黒へ）"""
    im = ImageOps.grayscale(Image.open(path).convert("RGB"))
    im = ImageOps.invert(im)
    im = im.point(lambda p: 0 if p < 90 else p)   # 反転した明色(元の黄/白)を黒へ
    return ImageEnhance.Contrast(sized(im)).enhance(1.2)

def knockout_white(path, sized):
    """白背景を黒に抜いて被写体だけ残す（TB-303のシルバー実機）"""
    im = ImageOps.grayscale(Image.open(path).convert("RGB"))
    im = im.point(lambda p: 0 if p > 225 else p)
    return ImageEnhance.Brightness(sized(im)).enhance(1.15)

# slide_1: melty smiley（表紙）— 縦に大きく
m = smiley_lineart(d / "smile_melty.png", lambda im: fit_h(im, 1080))
Image.merge("RGB", [on_black(m, (H - m.height)//2)]*3).save(d / "slide_1.png")

# slide_2: TB-303 — 横幅いっぱい・中央
t = knockout_white(d / "tb303.png", lambda im: fit_w(im, 1060))
Image.merge("RGB", [on_black(t, (H - t.height)//2)]*3).save(d / "slide_2.png")

# slide_7: simple smiley — 中央やや上
s = smiley_lineart(d / "smile.png", lambda im: fit_h(im, 820))
Image.merge("RGB", [on_black(s, 360)]*3).save(d / "slide_7.png")

print("saved slide_1 / slide_2 / slide_7 in", d)
