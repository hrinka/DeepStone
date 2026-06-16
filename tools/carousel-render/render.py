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
import json, sys, argparse, math, random, re
from pathlib import Path

# フォントが表示できない絵文字・記号を除去（tofu □ 防止）。em-dash(—)や中黒(·)は残す。
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000026FF\U00002700-\U000027BF"
    "\U0001F1E6-\U0001F1FF\U00002B00-\U00002BFF️‍]+")
def _san(s):
    return EMOJI.sub("", str(s)).rstrip()
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops, ImageOps

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
        "bg": "#F4EFE6", "main": "#33403A", "strobe": "#2C2A26",
        "sub": "#8C8276", "rule": "#C9A86A",
        "font_head": "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc",  # 明朝（詩的）
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

def _break_token(draw, word, font, max_w):
    """長すぎる語を文字単位で割る（CJK＝スペース無し・長い英単語の両方に対応）"""
    if draw.textlength(word, font=font) <= max_w:
        return [word]
    out, piece = [], ""
    for ch in word:
        if draw.textlength(piece + ch, font=font) <= max_w or not piece:
            piece += ch
        else:
            out.append(piece); piece = ch
    if piece: out.append(piece)
    return out

_KINSOKU_START = "、。，．・,.)）」』】〕｝!?！？ー~〜ゃゅょっぁぃぅぇぉ゛゜"  # 行頭禁止
def _kinsoku(lines):
    """行頭に来てはいけない文字を前の行末へ送る（日本語の見栄え）"""
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in _KINSOKU_START and lines[i-1]:
            lines[i-1] += lines[i][0]
            lines[i] = lines[i][1:]
    return [l for l in lines if l]

def greedy_wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for w in text.split(" "):
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur); cur = ""
            parts = _break_token(draw, w, font, max_w)  # 語自体が長ければ文字割り
            lines.extend(parts[:-1])
            cur = parts[-1]
    if cur:
        lines.append(cur)
    return _kinsoku(lines)

def as_lines(value, draw, font, max_w):
    """配列→そのまま / "\\n"入り文字列→分割 / 普通の文字列→必要時のみ折返し"""
    if value is None:
        return []
    if isinstance(value, list):
        raw = [_san(x) for x in value]
    elif "\n" in value:
        raw = [_san(x) for x in value.split("\n")]
    else:
        return greedy_wrap(draw, _san(value), font, max_w)
    out = []
    for ln in raw:
        if not ln:
            continue
        if draw.textlength(ln, font=font) > max_w:
            out.extend(greedy_wrap(draw, ln, font, max_w))  # 長すぎる行だけ救済
        else:
            out.append(ln)
    return out

def _raw_lines(value):
    """配列 or \\n → そのまま分割（再折返ししない・作者の改行を尊重）"""
    if value is None:
        return []
    if isinstance(value, list):
        return [_san(x) for x in value if _san(x)]
    if "\n" in value:
        return [_san(x) for x in value.split("\n") if _san(x)]
    return None  # ただの文字列 → 呼び出し側で折返し

def fit_font(draw, value, font_path, maxw, maxh, hi, lo=44):
    """配列/改行入りは作者の行を尊重しフォント縮小で収める。素の文字列は折返し。"""
    raw = _raw_lines(value)
    for size in range(hi, lo-1, -5):
        f = F(font_path, size)
        lines = raw if raw is not None else greedy_wrap(draw, _san(value), f, maxw)
        asc, desc = f.getmetrics(); lh = int((asc+desc)*1.18)
        widest = max((draw.textlength(l, font=f) for l in lines), default=0)
        if widest <= maxw and lh*len(lines) <= maxh:
            return f, lines
    f = F(font_path, lo)
    return f, (raw if raw is not None else greedy_wrap(draw, _san(value), f, maxw))

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

def draw_colored_block(draw, items, font, cy, line_gap=1.18):
    """(行, 色) のリストを均等な行間で1ブロックとして中央描画"""
    asc, desc = font.getmetrics(); lh = int((asc+desc)*line_gap)
    total = lh * len(items)
    y = cy - total // 2
    for ln, col in items:
        tw = draw.textlength(ln, font=font)
        draw.text(((W - tw) // 2, y), ln, font=font, fill=col)
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

def make_bg(theme, src, darken, bw=False):
    if src and Path(src).exists():
        im = Image.open(src).convert("RGB")
        if bw:  # 白黒化（PLURのモノクロ世界に合わせる）
            im = ImageOps.grayscale(im).convert("RGB")
        r = max(W/im.width, H/im.height)
        im = im.resize((int(im.width*r), int(im.height*r)))
        x = (im.width-W)//2; y = (im.height-H)//2
        im = im.crop((x, y, x+W, y+H))
        return ImageEnhance.Brightness(im).enhance(darken)
    base = Image.new("RGB", (W, H), theme["bg"])
    return add_grain(base, theme["grain"])  # フラット地にグレインを乗せて単調回避

def _resolve(base_dir, p):
    if not p:
        return None
    pp = Path(p)
    if pp.is_absolute() or pp.exists():
        return str(pp)
    return str(Path(base_dir) / pp)  # slides.json の隣を基準に解決

def render_slide(slide, theme, cover_bg, base_dir="."):
    typ = slide.get("type", "body")
    per_bg = _resolve(base_dir, slide.get("bg"))
    bw = bool(slide.get("bw", False))
    if typ == "cover":
        # 表紙：cover.jpg があればそれ、無ければテーマ地
        src = cover_bg or per_bg
        darken = 0.45 if theme["bg"] == "#0A0A0A" else 0.82
    elif per_bg:
        # 2〜8枚目で写真を個別指定：文字を読ませるため強めに暗くする
        src = per_bg
        darken = 0.5 if theme["bg"] == "#0A0A0A" else 0.8
    else:
        # ブランド共通テクスチャ > 単色グレイン
        src = theme.get("body_texture")
        darken = theme.get("body_dark", 0.8)
    img = make_bg(theme, src, darken, bw=bw)
    d = ImageDraw.Draw(img)
    pad = 110
    mw = W - 2*pad

    m = theme["motif"]  # PLUR は大きく詰めて目を引く / FLAVA は余白を活かす
    if typ == "cover":
        cap, band = (270, 0.56) if m else (230, 0.46)
        bigf, lines = fit_font(d, slide.get("main"), theme["font_head"], mw, int(H*band), cap)
        yb = draw_block(d, lines, bigf, theme["strobe"], int(H*(0.40 if m else 0.40)))
        if slide.get("sub"):
            subf = F(theme["font_body"], 44 if m else 40)
            draw_block(d, as_lines(slide["sub"], d, subf, mw), subf, theme["sub"], yb + 70)
    elif typ == "quote":
        cap, band = (138, 0.54) if m else (96, 0.42)
        qf, qlines = fit_font(d, slide.get("quote"), theme["font_head"], mw, int(H*band), cap)
        note = F(theme["font_body"], 36 if m else 34)
        y = draw_block(d, qlines, qf, theme["strobe"], int(H*0.42))
        if slide.get("note"):
            draw_block(d, as_lines(slide["note"], d, note, mw), note, theme["sub"], y+70)
    elif typ == "cta":
        cap, band = (160, 0.52) if m else (96, 0.40)
        bigf, tlines = fit_font(d, slide.get("text"), theme["font_head"], mw, int(H*band), cap)
        cta = F(theme["font_body"], 34)
        items = [(l, theme["main"]) for l in tlines]
        items += [(l, theme["strobe"]) for l in (_raw_lines(slide.get("strobe")) or ([_san(slide["strobe"])] if slide.get("strobe") else []))]
        draw_colored_block(d, items, bigf, int(H*0.44))
        if slide.get("cta"):
            draw_block(d, as_lines(slide["cta"], d, cta, mw), cta, theme["sub"], int(H*0.82))
    else:  # body
        cap, band = (164, 0.56) if m else (84, 0.42)
        headf, blines = fit_font(d, slide.get("text"), theme["font_head"], mw, int(H*band), cap)
        sub = F(theme["font_body"], 40 if m else 38)
        y = draw_block(d, blines, headf, theme["main"], int(H*(0.46 if m else 0.44)))
        if slide.get("sub"):
            draw_block(d, as_lines(slide["sub"], d, sub, mw), sub, theme["sub"], y+58)

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
    account = spec.get("account", "plur")
    theme = dict(THEMES[account])
    bgc = spec.get("background", {}).get("color")
    if bgc:
        theme["bg"] = bgc

    base_dir = Path(a.slides_json).parent  # 個別bgはjsonの隣を基準に解決
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    slides = spec["slides"]
    for i, s in enumerate(slides, 1):
        # フォルダに slide_N.(png/jpg) があれば、そのスライドの背景に自動採用（名前の通り）
        if "bg" not in s:
            for e in (".png", ".jpg", ".jpeg"):
                cand = base_dir / f"slide_{i}{e}"
                if cand.exists():
                    s["bg"] = str(cand)
                    if account == "plur" and "bw" not in s:
                        s["bw"] = True  # PLURはモノクロ統一
                    break
        img = render_slide(s, theme, a.cover_bg, base_dir)
        p = out / f"slide_{i:02d}.png"
        img.save(p, "PNG")
        print("saved", p)
    print(f"\n✅ {len(slides)} slides → {out}")

if __name__ == "__main__":
    main()
