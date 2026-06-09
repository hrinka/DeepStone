#!/usr/bin/env python3
"""
Carousel renderer — slides.json + 背景 → スライドPNG
テキストを組版してブランド準拠のカルーセル画像を吐く。AI画像生成は不要。

Usage:
  python render.py slides.json --out ./out [--cover-bg cover.jpg]

slides.json schema:
{
  "account": "plur" | "flava",
  "background": {"color":"#0A0A0A"},
  "slides": [
    {"type":"cover", "main":"PLUR", "sub":"..."},
    {"type":"body",  "text":["line1","line2"], "sub":"..."},
    {"type":"quote", "quote":["line1","line2"], "note":"..."},
    {"type":"cta",   "text":"...", "strobe":"...", "cta":"Save this."}
  ]
}

改行ルール：text/quote等は **配列で1行ずつ** 指定する（意味・カンマ・ハイフンで割る）。
文字列に "\\n" を入れてもよい。1行だけ長すぎる場合のみ自動折返しでフォールバック。
表紙(cover)の背景：--cover-bg で渡した画像を slide 1 だけに敷く（2枚目以降はテーマ地）。
"""
import json, sys, argparse, math, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops

W, H = 1080, 1350  # Instagram 4:5
TEX = Path(__file__).parent / "textures"

THEMES = {
    "plur": {
        "bg": "#0A0A0A", "main": "#ECECEC", "strobe": "#FFFFFF",
        "sub": "#9B9B9B", "rule": "#4A4A4A",
        "font_head": "/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf",
        "font_body": "/System/Library/Fonts/HelveticaNeue.ttc",
        "motif": True, "grain": 14,
        # 2〜8枚目(body)のブランド共通地。あれば自動採用＝全PLUR投稿が「日記」の質感に。
        "body_texture": str(TEX / "notebook-black.jpg"), "body_dark": 0.78,
    },
    "flava": {
        "bg": "#F4EFE6", "main": "#33403A", "strobe": "#869177",
        "sub": "#A99BC0", "rule": "#C9A86A",
        "font_head": "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "font_body": "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "motif": False, "grain": 6,
        "body_texture": str(TEX / "notebook-ivory.jpg"), "body_dark": 0.92,
    },
}

def F(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def greedy_wrap(draw, text, font, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def as_lines(value, draw, font, max_w):
    """配列→そのまま / "\\n"入り文字列→分割 / 普通の文字列→必要時のみ折返し"""
    if value is None:
        return []
    if isinstance(value, list):
        raw = value
    elif "\n" in value:
        raw = value.split("\n")
    else:
        return greedy_wrap(draw, value, font, max_w)
    out = []
    for ln in raw:
        if draw.textlength(ln, font=font) > max_w:
            out.extend(greedy_wrap(draw, ln, font, max_w))  # 長すぎる行だけ救済
        else:
            out.append(ln)
    return out

def draw_block(draw, lines, font, fill, cy, line_gap=1.18):
    asc, desc = font.getmetrics()
    lh = int((asc + desc) * line_gap)
    total = lh * len(lines)
    y = cy - total // 2
    for ln in lines:
        tw = draw.textlength(ln, font=font)
        draw.text(((W - tw) // 2, y), ln, font=font, fill=fill)
        y += lh
    return y

def waveform(draw, color, y=H-95):
    pts = []
    for x in range(80, W-80, 6):
        amp = 22 * math.sin((x-80)/38.0) * math.sin((x-80)/180.0)
        pts.append((x, y + amp))
    draw.line(pts, fill=color, width=2)

def add_grain(img, sigma):
    if sigma <= 0:
        return img
    noise = Image.effect_noise((W, H), sigma).convert("L")
    rgb = Image.merge("RGB", (noise, noise, noise))
    return ImageChops.overlay(img, rgb)

def make_bg(theme, src, darken):
    if src and Path(src).exists():
        im = Image.open(src).convert("RGB")
        r = max(W/im.width, H/im.height)
        im = im.resize((int(im.width*r), int(im.height*r)))
        x = (im.width-W)//2; y = (im.height-H)//2
        im = im.crop((x, y, x+W, y+H))
        return ImageEnhance.Brightness(im).enhance(darken)
    base = Image.new("RGB", (W, H), theme["bg"])
    return add_grain(base, theme["grain"])  # フラット地にグレインを乗せて単調回避

def render_slide(slide, theme, cover_bg):
    typ = slide.get("type", "body")
    per_bg = slide.get("bg")
    if typ == "cover":
        # 表紙：cover.jpg があればそれ、無ければテーマ地
        src = cover_bg or per_bg
        darken = 0.45 if theme["bg"] == "#0A0A0A" else 0.82
    else:
        # 2〜8枚目：個別指定 > ブランド共通テクスチャ > 単色グレイン
        src = per_bg or theme.get("body_texture")
        darken = theme.get("body_dark", 0.8)
    img = make_bg(theme, src, darken)
    d = ImageDraw.Draw(img)
    pad = 110
    mw = W - 2*pad

    if typ == "cover":
        big = F(theme["font_head"], 230)
        sub = F(theme["font_body"], 40)
        draw_block(d, as_lines(slide.get("main"), d, big, mw), big, theme["strobe"], int(H*0.42))
        if slide.get("sub"):
            draw_block(d, as_lines(slide["sub"], d, sub, mw), sub, theme["sub"], int(H*0.60))
    elif typ == "quote":
        q = F(theme["font_head"], 92)
        note = F(theme["font_body"], 34)
        y = draw_block(d, as_lines(slide.get("quote"), d, q, mw), q, theme["strobe"], int(H*0.44))
        if slide.get("note"):
            draw_block(d, as_lines(slide["note"], d, note, mw), note, theme["sub"], y+70)
    elif typ == "cta":
        big = F(theme["font_head"], 120)
        cta = F(theme["font_body"], 34)
        y = draw_block(d, as_lines(slide.get("text"), d, big, mw), big, theme["main"], int(H*0.38))
        if slide.get("strobe"):
            y = draw_block(d, as_lines(slide["strobe"], d, big, mw), big, theme["strobe"], y+40)
        if slide.get("cta"):
            draw_block(d, as_lines(slide["cta"], d, cta, mw), cta, theme["sub"], int(H*0.80))
    else:  # body
        head = F(theme["font_head"], 110) if theme["motif"] else F(theme["font_head"], 80)
        sub = F(theme["font_body"], 38)
        y = draw_block(d, as_lines(slide.get("text"), d, head, mw), head, theme["main"], int(H*0.44))
        if slide.get("sub"):
            draw_block(d, as_lines(slide["sub"], d, sub, mw), sub, theme["sub"], y+55)

    # signature motif（PLURのみ波形）。ページ番号は表示しない。
    if theme["motif"]:
        waveform(d, theme["rule"])
    return img

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slides_json")
    ap.add_argument("--out", default="./out")
    ap.add_argument("--cover-bg", default=None, help="表紙(slide1)だけに敷く画像")
    a = ap.parse_args()

    spec = json.loads(Path(a.slides_json).read_text())
    theme = dict(THEMES[spec.get("account", "plur")])
    bgc = spec.get("background", {}).get("color")
    if bgc:
        theme["bg"] = bgc

    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    slides = spec["slides"]
    for i, s in enumerate(slides, 1):
        img = render_slide(s, theme, a.cover_bg)
        p = out / f"slide_{i:02d}.png"
        img.save(p, "PNG")
        print("saved", p)
    print(f"\n✅ {len(slides)} slides → {out}")

if __name__ == "__main__":
    main()
