#!/usr/bin/env python3
"""
DeepStone Morning Brief — 毎朝7:30 JSTにLINEへ送信
1. git pull で最新ジャーナルを取得
2. 今日のジャーナルから🌅ブリーフセクションを読む
3. 魚座・一白水星の運勢を取得（複数ソースからフォールバック）
4. LINEに送信
"""
import subprocess, os, ssl, json, urllib.request, re
from datetime import datetime

VAULT = "/Users/user/CosmicTheta/DeepStone"
TOKEN = "YreuaqWx5Bps7UCC7nLEdJwZFnK9zhRuf1L1Tado2ehhuPWhw6GB6wv/vUhwFzZQ/H9QfVwHfV86oCuprGAlPgcW51wBT5+/cmHVKHLu20Rf0FKQn8GJJnDFTIDaQkJnpuzezKYAAJHNB7eaBI3ZKAdB04t89/1O/w1cDnyilFU="
USER_ID = "U748eb093ae185b273e0457ea593d3801"

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def git_pull():
    subprocess.run(["git", "stash"], cwd=VAULT, capture_output=True)
    result = subprocess.run(
        ["git", "pull", "--rebase", "origin", "main"],
        cwd=VAULT, capture_output=True, text=True
    )
    subprocess.run(["git", "stash", "pop"], cwd=VAULT, capture_output=True)
    print("git pull:", result.stdout.strip() or result.stderr.strip())

def fetch_url(url, timeout=8):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX, timeout=timeout) as res:
        return res.read().decode("utf-8", errors="ignore")

def strip_tags(html):
    return re.sub(r'<[^>]+>', '', html).strip()

def fetch_pisces_ja():
    """魚座の今日の運勢（日本語） — Yahoo Japan星占い"""
    try:
        html = fetch_url("https://astro.yahoo.co.jp/fortune/daily/12/")
        # 本文テキストを抽出（運勢説明の段落）
        blocks = re.findall(r'<p[^>]*>([぀-鿿][^<]{15,})</p>', html)
        if blocks:
            return blocks[0][:120]
    except Exception as e:
        print("yahoo pisces error:", e)

    try:
        # フォールバック: livedoor 占い
        html = fetch_url("https://fortune.yahoo.co.jp/byekan/type/12")
        blocks = re.findall(r'<p[^>]*>([぀-鿿][^<]{15,})</p>', html)
        if blocks:
            return blocks[0][:120]
    except Exception as e:
        print("livedoor pisces error:", e)

    # 最終フォールバック: 英語API
    try:
        url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=Pisces&day=TODAY"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=CTX, timeout=8) as res:
            data = json.loads(res.read())
            text = data.get("data", {}).get("horoscope", "")
            return text.split(".")[0] + "." if text else ""
    except Exception as e:
        print("english api error:", e)

    return ""

def fetch_kyusei_ja():
    """一白水星の今日の運勢（日本語）"""
    try:
        html = fetch_url("https://kyusei-kimon.jp/fortune/daily/1/")
        blocks = re.findall(r'<p[^>]*>([぀-鿿][^<]{15,})</p>', html)
        if blocks:
            return blocks[0][:120]
    except Exception as e:
        print("kyusei error:", e)

    try:
        # フォールバック: 別サイト
        html = fetch_url("https://uranai-ranking.com/kyusei/ichihaku/today/")
        blocks = re.findall(r'<p[^>]*>([぀-鿿][^<]{15,})</p>', html)
        if blocks:
            return blocks[0][:120]
    except Exception as e:
        print("kyusei fallback error:", e)

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
    return "\n".join(brief_lines).strip()

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
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"=== DeepStone Morning Brief {today} ===")

    git_pull()

    brief = read_brief(today)
    pisces = fetch_pisces_ja()
    kyusei = fetch_kyusei_ja()

    fortune_block = ""
    if pisces or kyusei:
        fortune_block = "\n──────────"
        if pisces:
            fortune_block += f"\n🐟 魚座\n{pisces}"
        if kyusei:
            fortune_block += f"\n\n🌙 一白水星\n{kyusei}"
        fortune_block += "\n──────────"

    if brief:
        message = f"🌅 おはよう、Rinka。\n\n{today}\n\n{brief}{fortune_block}\n\n詳細はObsidianで 📖"
    else:
        message = f"🌅 おはよう、Rinka。\n\n{today}\n\nブリーフ準備中 ☁️{fortune_block}"

    send_line(message)

if __name__ == "__main__":
    main()
