#!/usr/bin/env python3
"""Remove orphaned discount/urgency CSS from target landings."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LANDINGS = [
    ROOT / "es/smartwatch/landing.html",
    ROOT / "pl/smartwatch/landing.html",
    ROOT / "gr/smartwatch/landing.html",
    ROOT / "pl/casa-fuego/landing.html",
    ROOT / "cz/casa-fuego/landing.html",
    ROOT / "sk/casa-fuego/landing.html",
]

COOKIE_POLICIES = [
    ROOT / "es/cookie-policy.html",
    ROOT / "pl/cookie-policy.html",
    ROOT / "gr/cookie-policy.html",
    ROOT / "cz/cookie-policy.html",
    ROOT / "sk/cookie-policy.html",
]

# Multiline CSS rules for removed promo UI (not used in HTML anymore).
CSS_SELECTORS = [
    ".cf-topbar__product",
    ".cf-badge-save",
    ".cf-price-box .stock",
    ".cf-price-box .disc",
    ".cf-price .old",
    ".cf-save-line",
    ".cf-package .pkg-price .old",
    ".cf-package .pkg-price .off",
    ".cf-form-urgency",
]


def strip_css_rule(text: str, selector: str) -> str:
    pattern = re.compile(rf"{re.escape(selector)}\{{[^{{}}]*\}}\s*", re.MULTILINE)
    return pattern.sub("", text)


def clean_landing(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = original
    for sel in CSS_SELECTORS:
        if sel == ".cf-topbar__product" and "smartwatch" not in str(path):
            continue
        updated = strip_css_rule(updated, sel)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"cleaned CSS: {path.relative_to(ROOT)}")
        return True
    print(f"unchanged: {path.relative_to(ROOT)}")
    return False


def clean_cookie_policy(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = re.sub(
        r"\s*<li>[^<]*df_countdown_end[^<]*</li>\s*",
        "\n",
        original,
        flags=re.IGNORECASE,
    )
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"cleaned cookie policy: {path.relative_to(ROOT)}")
        return True
    print(f"cookie policy unchanged: {path.relative_to(ROOT)}")
    return False


def main() -> None:
    changed = 0
    for p in LANDINGS:
        if clean_landing(p):
            changed += 1
    for p in COOKIE_POLICIES:
        if clean_cookie_policy(p):
            changed += 1
    print(f"done — {changed} files updated")


if __name__ == "__main__":
    main()
