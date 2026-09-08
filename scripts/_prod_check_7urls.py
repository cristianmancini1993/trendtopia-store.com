#!/usr/bin/env python3
"""Production HTTP + content checks for 7 Google Ads destination URLs."""
import re
import urllib.request

URLS = [
    ("ES CoreSync", "https://trendtopia-store.com/es/smartwatch/landing.html", {"offer": "3137", "lp": "3171"}),
    ("PL CoreSync", "https://trendtopia-store.com/pl/smartwatch/landing.html", {"offer": "3141", "lp": "3175"}),
    ("GR CoreSync", "https://trendtopia-store.com/gr/smartwatch/landing.html", {"offer": "1842", "lp": "1862"}),
    ("Home", "https://trendtopia-store.com/", None),
    ("PL Casa Fuego", "https://trendtopia-store.com/pl/casa-fuego/landing.html", {"offer": "3179", "lp": "3213"}),
    ("CZ Casa Fuego", "https://trendtopia-store.com/cz/casa-fuego/landing.html", {"offer": "3251", "lp": "3285"}),
    ("SK Casa Fuego", "https://trendtopia-store.com/sk/casa-fuego/landing.html", {"offer": "3702", "lp": "3742"}),
]

UA = "Mozilla/5.0 (compatible; AdsBot-Google-Mobile; +http://www.google.com/adsbot.html)"

SPANISH = re.compile(r"Seguimiento|Incluye:|actividad diaria|manual de instrucciones", re.I)
PROMO = re.compile(r"(?<![\w-])(-50%|98\s*[€$]|4100|3842|Zero risk|Up to 50%)", re.I)
URGENCY = re.compile(r"\b(HOY|DZIŚ|DNES|solo hoy|today only|limited.time)\b", re.I)


def is_css_false_positive(body: str, start: int, end: int) -> bool:
    ctx = body[max(0, start - 20) : end + 20]
    return "translate(-50%" in ctx or "left:50%" in ctx or "border-radius:50%" in ctx


def main() -> None:
    ok = 0
    for name, url, ids in URLS:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            body = resp.read().decode("utf-8", "replace")
            status = resp.status
        except Exception as exc:
            print(f"FAIL {name}: {exc}")
            continue

        issues = []
        if name == "PL CoreSync" and SPANISH.search(body):
            issues.append("spanish_leak")
        for m in PROMO.finditer(body):
            if not is_css_false_positive(body, m.start(), m.end()):
                issues.append(f"promo:{m.group()}")
        if URGENCY.search(body):
            issues.append(f"urgency:{URGENCY.search(body).group()}")

        if ids:
            om = re.search(r'name="offer"[^>]*value="(\d+)"', body)
            lm = re.search(r'name="lp"[^>]*value="(\d+)"', body)
            if not om or om.group(1) != ids["offer"]:
                issues.append(f"offer expected {ids['offer']} got {om.group(1) if om else None}")
            if not lm or lm.group(1) != ids["lp"]:
                issues.append(f"lp expected {ids['lp']} got {lm.group(1) if lm else None}")

        if issues:
            print(f"WARN {status} {name}: {issues}")
        else:
            print(f"OK   {status} {name}")
            ok += 1

    print(f"\n{ok}/{len(URLS)} URLs passed content checks")


if __name__ == "__main__":
    main()
