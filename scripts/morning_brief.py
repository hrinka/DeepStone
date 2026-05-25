#!/usr/bin/env python3
"""
DeepStone Morning Brief — 毎朝7:30 JSTにLINEへ送信
"""
import subprocess, os, ssl, json, urllib.request, re
from datetime import datetime, timezone, timedelta

VAULT = "/Users/user/CosmicTheta/DeepStone"
TOKEN = "YreuaqWx5Bps7UCC7nLEdJwZFnK9zhRuf1L1Tado2ehhuPWhw6GB6wv/vUhwFzZQ/H9QfVwHfV86oCuprGAlPgcW51wBT5+/cmHVKHLu20Rf0FKQn8GJJnDFTIDaQkJnpuzezKYAAJHNB7eaBI3ZKAdB04t89/1O/w1cDnyilFU="
USER_ID = "U748eb093ae185b273e0457ea593d3801"

JST = timezone(timedelta(hours=9))

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def git_pull():
    """fetch + checkout で競合を回避してジャーナルファイルだけ更新"""
    try:
        # fetchだけ（競合しない）
        subprocess.run(["git", "fetch", "origin", "main"],
                       cwd=VAULT, capture_output=True, timeout=15)
        # journal/ だけ origin から取得（ローカル変更を壊さない）
        subprocess.run(["git", "checkout", "origin/main", "--", "journal/"],
                       cwd=VAULT, capture_output=True, timeout=10)
        print("git pull: journal/ updated from origin")
    except Exception as e:
        print("git pull error:", e)

def clean_markdown(text):
    """markdownの書式記号を除去してLINE用プレーンテキストに変換"""
    # **太字** → 太字
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    # *斜体* → 斜体
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    # ## 見出し → 見出し
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # <!-- コメント --> → 削除
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # [[wikilink]] → wikilink
    text = re.sub(r'\[\[(.*?)\]\]', r'\1', text)
    # 3行以上の空行を2行に
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def fetch_url(url, timeout=8):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX, timeout=timeout) as res:
        return res.read().decode("utf-8", errors="ignore")

def fetch_pisces_ja():
    """魚座の今日の運勢（日本語）"""
    try:
        html = fetch_url("https://astro.yahoo.co.jp/fortune/daily/12/")
        blocks = re.findall(r'<p[^>]*>([぀-鿿ぁ-ゟ][^<]{15,})</p>', html)
        if blocks:
            return blocks[0][:120]
    except Exception as e:
        print("yahoo pisces error:", e)

    try:
        url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=Pisces&day=TODAY"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=CTX, timeout=8) as res:
            data = json.loads(res.read())
            text = data.get("data", {}).get("horoscope", "")
            return text.split(".")[0] + "." if text else ""
    except Exception as e:
        print("english horoscope error:", e)
    return ""

def fetch_kyusei_ja():
    """一白水星の今日の運勢（日本語）"""
    try:
        html = fetch_url("https://kyusei-kimon.jp/fortune/daily/1/")
        blocks = re.findall(r'<p[^>]*>([぀-鿿ぁ-ゟ][^<]{15,})</p>', html)
        if blocks:
            return blocks[0][:120]
    except Exception as e:
        print("kyusei error:", e)
    return ""

def read_brief(today):
    path = os.path.join(VAULT, "journal", f"{today}.md")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    brief_lines = []
    in_brief = False
    for line in lines:
        if "## 🌅 今朝のブリーフ" in line:
            in_brief = True
            continue
        if in_brief:
            if line.startswith("## ") or line.strip() == "---":
                break
            brief_lines.append(line)
    raw = "\n".join(brief_lines)
    return clean_markdown(raw)

def send_line(message):
    payload = json.dumps({
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        "https://api.line.me/v2/bot/message/push",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        },
        method="POST"
    )
    try:
        res = urllib.request.urlopen(req, context=CTX)
        print("LINE sent:", res.read().decode())
    except Exception as e:
        print("LINE error:", e)

def main():
    # JSTで今日の日付を取得（UTC環境でも正しく動く）
    now = datetime.now(JST)
    today = now.strftime("%Y-%m-%d")
    print(f"=== DeepStone Morning Brief {today} (JST) ===")

    git_pull()

    brief = read_brief(today)
    pisces = fetch_pisces_ja()
    kyusei = fetch_kyusei_ja()

    fortune_block = ""
    if pisces or kyusei:
        fortune_block = "\n\n──────────"
        if pisces:
            fortune_block += f"\n🐟 魚座\n{pisces}"
        if kyusei:
            fortune_block += f"\n\n🌙 一白水星\n{kyusei}"
        fortune_block += "\n──────────"

    if brief:
        message = f"🌅 おはよう、Rinka。\n\n{today}\n\n{brief}{fortune_block}\n\n📖 詳細はObsidianで"
    else:
        message = f"🌅 おはよう、Rinka。\n\n{today}\n\nブリーフ準備中 ☁️{fortune_block}"

    send_line(message)

if __name__ == "__main__":
    main()
