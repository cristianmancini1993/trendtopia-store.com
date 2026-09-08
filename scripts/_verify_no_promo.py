#!/usr/bin/env python3
"""Verify no discount/urgency on target Trendtopia landings."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = {
    "es/smartwatch/landing.html": {"price": "49", "offer": "3137", "lp": "3171"},
    "pl/smartwatch/landing.html": {"price": "199", "offer": "3141", "lp": "3175"},
    "gr/smartwatch/landing.html": {"price": "69", "offer": "1842", "lp": "1862"},
    "pl/casa-fuego/landing.html": {"price": "399", "offer": "3179", "lp": "3213"},
    "cz/casa-fuego/landing.html": {"price": "1999", "offer": "3251", "lp": "3285"},
    "sk/casa-fuego/landing.html": {"price": "89", "offer": "3702", "lp": "3742"},
}

# Patterns that must NOT appear in visible/business HTML (exclude CSS layout 50%).
FORBIDDEN = [
    (r"-50\s*%", "discount -50%"),
    (r"\b50\s*%\s*(OFF|off|de descuento|zniżk)", "50% promo"),
    (r"\b98[,.]?\s*00?\s*€", "old price ES 98€"),
    (r"\b398[,.]?\s*00?\s*zł", "old price PL 398zł"),
    (r"\b138[,.]?\s*00?\s*€", "old price GR 138€"),
    (r"\b798[,.]?\s*00?\s*zł", "old price CF PL 798zł"),
    (r"3\s*998", "old price CF CZ 3998"),
    (r"\b178[,.]?\s*00?\s*€", "old price CF SK 178€"),
    (r"class=\"old\"", "strikethrough old price"),
    (r"class=\"disc\"", "discount badge"),
    (r"cf-save-line", "savings line"),
    (r"cf-badge-save", "save badge"),
    (r"data-countdown", "countdown element"),
    (r"countdown\.js", "countdown script"),
    (r"df_countdown", "countdown storage key"),
    (r"\bHOY\b", "urgency HOY"),
    (r"\bDZIŚ\b", "urgency DZIŚ"),
    (r"\bDNES\b", "urgency DNES"),
    (r"ΣΗΜΕΡΑ", "urgency Greek today"),
    (r"Ahorras?\s+\d", "savings ES"),
    (r"Oszczędz", "savings PL"),
    (r"Ušetř", "savings CZ"),
    (r"Ušetr", "savings SK"),
    (r"Κερδί", "savings GR"),
    (r"limited.?time", "limited time"),
    (r"priceValidUntil", "promo JSON-LD expiry"),
    (r"highPrice", "compare high price JSON-LD"),
    (r"listPrice", "list price JSON-LD"),
]

COOKIE_GEOS = ["es", "pl", "gr", "cz", "sk"]


def main() -> int:
    fails = 0
    for rel, expect in TARGETS.items():
        html = (ROOT / rel).read_text(encoding="utf-8")
        body = html.split("</style>", 1)[-1] if "</style>" in html else html
        for pat, label in FORBIDDEN:
            if re.search(pat, body, re.I):
                print(f"FAIL {rel}: {label}")
                fails += 1
        if expect["price"].replace(" ", "") not in body.replace(" ", "").replace("\u00a0", ""):
            print(f"FAIL {rel}: missing current price {expect['price']}")
            fails += 1
        if f'value="{expect["offer"]}"' not in html or f'value="{expect["lp"]}"' not in html:
            print(f"FAIL {rel}: offer/lp changed")
            fails += 1
        else:
            print(f"PASS {rel}")

    for geo in COOKIE_GEOS:
        cp = (ROOT / f"{geo}/cookie-policy.html").read_text(encoding="utf-8")
        if "df_countdown_end" in cp.lower():
            print(f"FAIL {geo}/cookie-policy.html: df_countdown_end still documented")
            fails += 1
        else:
            print(f"PASS {geo}/cookie-policy.html")

    home = (ROOT / "index.html").read_text(encoding="utf-8")
    for pat in (r"-50\s*%", r"\b50\s*%\s*off", r"limited.?time", r"offer ends soon", r"until stock runs out"):
        if re.search(pat, home, re.I):
            print(f"FAIL index.html: {pat}")
            fails += 1
    print("PASS index.html promo scan")

    print("---")
    if fails:
        print(f"{fails} FAILURES")
        return 1
    print("ALL PROMO CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
