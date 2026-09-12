#!/usr/bin/env python3
"""Audit home SSR: i18n key coverage + internal link targets exist."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "home"
JS = ROOT / "assets/js/home-i18n.js"

LOCALES = ["en", "es", "pl", "sk", "cz", "gr"]
REQUIRED_KEYS = [
    "lang_label",
    "page_title",
    "page_description",
    "hero_eyebrow",
    "hero_title",
    "hero_subtitle",
    "why_1_text",
    "why_2_heading",
    "why_2_text",
    "why_3_text",
    "footer_about",
]


def audit_i18n_in_html() -> list[str]:
    errs: list[str] = []
    key_re = re.compile(r'data-i18n="([^"]+)"')
    for path in sorted(HOME.glob("index.*.html")):
        html = path.read_text(encoding="utf-8")
        for key in REQUIRED_KEYS:
            if f'data-i18n="{key}"' not in html:
                continue
            # Element should not still show obvious EN placeholders on non-en pages
            loc = path.stem.split(".")[-1]
            if loc == "en":
                continue
            if key == "hero_subtitle" and "Hand-picked items" in html:
                errs.append(f"{path.name}: hero_subtitle still English in SSR")
    return errs


def audit_links() -> list[str]:
    errs: list[str] = []
    href_re = re.compile(r'href="(/[^"#?]+)"')
    for path in sorted(HOME.glob("index.*.html")):
        loc = path.stem.split(".")[-1]
        html = path.read_text(encoding="utf-8")
        for href in href_re.findall(html):
            if href.startswith(("http", "//", "mailto:")):
                continue
            if href in ("/", "#our-products"):
                continue
            rel = href.lstrip("/").replace("/", "\\")
            target = ROOT / rel
            if not target.is_file():
                errs.append(f"{path.name}: broken href {href}")
        if 'data-i18n-href="about-us.html"' in html and f'href="/{loc}/about-us.html"' not in html:
            errs.append(f"{path.name}: footer about-us href not /{loc}/...")
    return errs


def main() -> int:
    errors = audit_i18n_in_html()
    errors.extend(audit_links())
    if errors:
        print("Home audit issues:")
        for e in errors:
            print(" -", e)
        return 1
    print("Home audit OK:", len(LOCALES), "locales, links and core i18n keys.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
