#!/usr/bin/env python3
"""
Carousel renderer — slides.json + 背景 → スライドPNG
テキストを組版してブランド準拠のカルーセル画像を吐く。AI画像生成は不要。

Usage:
  python render.py slides.json --out ./out [--bg /path/to/background.jpg]

slides.json schema:
{
  "account": "plur" | "flava",
  "background": {"color":"#0A0A0A"} | {"image":"bg.jpg"},
  "slides": [
    {"type":"cover", "main":"PLUR", "sub":"..."},
    {"type":"body",  "text":"...", "sub":"..."},
    {"type":"quote", "quote":"...", "note":"..."},
    {"type":"cta",   "text":"...", "strobe":"...", "cta":"Save this."}
  ]
}
背景は --bg で全スライド一括指定、または各slideに "bg":"path" で個別指定可。
"""
import json, sys, argparse, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

W, H = 1080, 1350  # Instagram 4:5

THEMES = {
    "plur": {
        "bg": "#0A0A0A", "main": "#ECECEC", "strobe": "#FFFFFF",
        "sub": "#9B9B9B", "rule": "#4A4A4A",
        "font_head": "/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf",
        "font_body": "/System/Library/Fonts/HelveticaNeue.ttc",
        "motif": True,
    },
    "flava": {
        "bg": "#F4EFE6", "main": "#33403A", "strobe": "#869177",
        "sub": "#A99BC0", "rule": "#C9A86A",
        "font_head": "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "font_body": "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "motif": False,
    },
}

def F(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def wrap(draw, text, font, max_w):
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

def draw_block(draw, lines, font, fill, cy, line_gap=1.2, align="center"):
    asc, desc = font.getmetrics()
    lh = int((asc + desc) * line_gap)
    total = lh * len(lines)
    y = cy - total // 2
    for ln in lines:
        tw = draw.textlength(ln, font=font)
        x = (W - tw) // 2 if align == "center" else 90
        draw.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def waveform(draw, color, y=H-90):
    pts = []
    for x in range(80, W-80, 6):
        amp = 22 * math.sin((x-80)/38.0) * math.sin((x-80)/180.0)
        pts.append((x, y + amp))
    draw.line(pts, fill=color, width=2)

def make_bg(theme, slide, global_bg):
    src = slide.get("bg") or global_bg
    if src and Path(src).exists():
        img = Image.open(src).convert("RGB")
        # cover-crop to 1080x1350
        r = max(W/img.width, H/img.height)
        img = img.resize((int(img.width*r), int(img.height*r)))
        x = (img.width-W)//2; y=(img.height-H)//2
        img = img.crop((x, y, x+W, y+H))
        # darken for legibility (PLUR strong, FLAVA light)
        f = 0.45 if theme["bg"] == "#0A0A0A" else 0.85
        img = ImageEnhance.Brightness(img).enhance(f)
        return img
    return Image.new("RGB", (W, H), theme["bg"])

def render_slide(slide, theme, idx, total, global_bg):
    img = make_bg(theme, slide, global_bg)
    d = ImageDraw.Draw(img)
    pad = 110
    typ = slide.get("type", "body")

    if typ == "cover":
        big = F(theme["font_head"], 230)
        sub = F(theme["font_body"], 40)
        draw_block(d, wrap(d, slide.get("main",""), big, W-2*pad), big, theme["strobe"], int(H*0.42))
        if slide.get("sub"):
            draw_block(d, wrap(d, slide["sub"], sub, W-2*pad), sub, theme["sub"], int(H*0.60))
    elif typ == "quote":
        q = F(theme["font_head"], 92)
        note = F(theme["font_body"], 34)
        y = draw_block(d, wrap(d, slide.get("quote",""), q, W-2*pad), q, theme["strobe"], int(H*0.44))
        if slide.get("note"):
            draw_block(d, wrap(d, slide["note"], note, W-2*pad), note, theme["sub"], y+70)
    elif typ == "cta":
        big = F(theme["font_head"], 120)
        st = F(theme["font_head"], 120)
        cta = F(theme["font_body"], 34)
        y = draw_block(d, wrap(d, slide.get("text",""), big, W-2*pad), big, theme["main"], int(H*0.38))
        if slide.get("strobe"):
            draw_block(d, wrap(d, slide["strobe"], st, W-2*pad), st, theme["strobe"], y+40)
        if slide.get("cta"):
            draw_block(d, wrap(d, slide["cta"], cta, W-2*pad), cta, theme["sub"], int(H*0.80))
    else:  # body
        head = F(theme["font_head"], 110) if theme["motif"] else F(theme["font_head"], 80)
        sub = F(theme["font_body"], 38)
        y = draw_block(d, wrap(d, slide.get("text",""), head, W-2*pad), head, theme["main"], int(H*0.44))
        if slide.get("sub"):
            draw_block(d, wrap(d, slide["sub"], sub, W-2*pad), sub, theme["sub"], y+60)

    # page counter
    cnt = F(theme["font_body"], 26)
    d.text((W-150, 70), f"{idx:02d} / {total:02d}", font=cnt, fill=theme["rule"])
    # signature motif (waveform) for PLUR
    if theme["motif"]:
        waveform(d, theme["rule"])
    return img

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slides_json")
    ap.add_argument("--out", default="./out")
    ap.add_argument("--bg", default=None, help="background image for all slides")
    a = ap.parse_args()

    spec = json.loads(Path(a.slides_json).read_text())
    theme = THEMES[spec.get("account", "plur")]
    if "background" in spec:
        if spec["background"].get("color"):
            theme = {**theme, "bg": spec["background"]["color"]}
    global_bg = a.bg or (spec.get("background", {}).get("image"))

    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    slides = spec["slides"]
    for i, s in enumerate(slides, 1):
        img = render_slide(s, theme, i, len(slides), global_bg)
        p = out / f"slide_{i:02d}.png"
        img.save(p, "PNG")
        print("saved", p)
    print(f"\n✅ {len(slides)} slides → {out}")

if __name__ == "__main__":
    main()
