#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "es/smartwatch/landing.html",
    "pl/smartwatch/landing.html",
    "gr/smartwatch/landing.html",
    "es/casa-fuego/landing.html",
    "pt/casa-fuego/landing.html",
    "de/casa-fuego/landing.html",
    "lt/casa-fuego/landing.html",
    "pl/casa-fuego/landing.html",
    "cz/casa-fuego/landing.html",
    "sk/casa-fuego/landing.html",
    "hu/casa-fuego/landing.html",
]
OLD = (
    '      <a href="/" class="site-logo">\n'
    '        <span class="site-logo__text" style="display:inline">'
    '<span class="site-logo__text-primary">trendtopia-store</span>'
    '<span class="site-logo__text-accent">.com</span></span>\n'
    "      </a>"
)
NEW = (
    OLD
    + '\n      <img class="site-logo__mark" src="/assets/img/site/logo.png" '
    'alt="trendtopia-store.com" width="72" height="72" loading="lazy" decoding="async">'
)

for rel in FILES:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if "site-logo__mark" in text:
        print("skip", rel)
        continue
    if OLD not in text:
        print("MISSING", rel)
        continue
    path.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
    print("patched", rel)
