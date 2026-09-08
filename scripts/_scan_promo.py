#!/usr/bin/env python3
"""Scan target pages (local + prod) for discount/urgency patterns."""
import re
import sys
from pathlib import Path

import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    r"-50\s*%", r"50\s*%", r"\b98\b", r"\b398\b", r"\b138\b", r"\b798\b",
    r"3\s*998", r"\b178\b", r"countdown", r"df_countdown", r"\bHOY\b", r"DZIŚ",
    r"DNES", r"ΣΗΜΕΡΑ", r"cf-save-line", r"Ahorras", r"Oszczędz", r"Ušetř",
    r"Ušetr", r"Κερδί", r'class="old"', r'class="disc"', r"limited.?time",
    r"offer ends", r"priceValidUntil", r"highPrice", r"listPrice",
]

LOCAL = [
    "es/smartwatch/landing.html",
    "pl/smartwatch/landing.html",
    "gr/smartwatch/landing.html",
    "pl/casa-fuego/landing.html",
    "cz/casa-fuego/landing.html",
    "sk/casa-fuego/landing.html",
    "index.html",
]

PROD = [
    ("https://trendtopia-store.com/es/smartwatch/landing.html", "ES SW"),
    ("https://trendtopia-store.com/pl/smartwatch/landing.html", "PL SW"),
    ("https://trendtopia-store.com/gr/smartwatch/landing.html", "GR SW"),
    ("https://trendtopia-store.com/pl/casa-fuego/landing.html", "PL CF"),
    ("https://trendtopia-store.com/cz/casa-fuego/landing.html", "CZ CF"),
    ("https://trendtopia-store.com/sk/casa-fuego/landing.html", "SK CF"),
    ("https://trendtopia-store.com/", "HOME"),
]

PRICES = {
    "ES SW": "49",
    "PL SW": "199",
    "GR SW": "69",
    "PL CF": "399",
    "CZ CF": "1999",
    "SK CF": "89",
}


def scan(label: str, html: str) -> list[str]:
    hits = []
    for p in PATTERNS:
        if re.search(p, html, re.I):
            hits.append(p)
    return hits


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "replace")


def main() -> int:
    fail = 0
    print("=== LOCAL ===")
    for rel in LOCAL:
        html = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        hits = scan(rel, html)
        print(f"{rel}: {len(hits)} hits -> {hits[:8]}")
        if hits:
            fail += 1

    print("\n=== PRODUCTION ===")
    for url, label in PROD:
        try:
            html = fetch(url)
            hits = scan(label, html)
            price_ok = PRICES.get(label, "") in html.replace(" ", "").replace("\u00a0", "")
            print(f"{label}: hits={len(hits)} price_ok={price_ok} -> {hits[:8]}")
            if hits:
                fail += 1
        except Exception as ex:
            print(f"{label}: ERROR {ex}")
            fail += 1

    return fail


if __name__ == "__main__":
    sys.exit(main())
