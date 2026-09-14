#!/usr/bin/env python3
"""Build sk/vortek-3228/landing.html from user HTML (transcript) adapted for trendtopia-store.com."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPT = Path(
    r"C:\Users\otger\.cursor\projects\c-Users-otger-trendtopia-store-com-1"
    r"\agent-transcripts\6163995b-977f-468a-8dfe-b6d970002c0a"
    r"\6163995b-977f-468a-8dfe-b6d970002c0a.jsonl"
)
OUT_DIR = ROOT / "sk" / "vortek-3228"
OUT_LANDING = OUT_DIR / "landing.html"

GTAG_HEAD = """<!-- Google tag (gtag.js) -->
<script src="/assets/js/consent-default.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18327321473"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  window.SITE_CONFIG = window.SITE_CONFIG || {};
  window.SITE_CONFIG.GOOGLE_TAG_ID = window.SITE_CONFIG.GOOGLE_TAG_ID || 'AW-18327321473';
</script>
"""

def extract_html() -> str:
    html = None
    for line in TRANSCRIPT.open(encoding="utf-8"):
        if "Iron Oak Pro" not in line or "offer reference: 3228" not in line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("role") != "user":
            continue
        for part in obj.get("message", {}).get("content", []):
            text = part.get("text", "")
            if "<!DOCTYPE html>" not in text or "3228" not in text:
                continue
            if "<user_query>" in text:
                text = text.split("<user_query>", 1)[1]
                if "</user_query>" in text:
                    text = text.split("</user_query>", 1)[0]
            start = text.find("<!DOCTYPE html>")
            end = text.find("</html>")
            if end == -1:
                continue
            html = text[start : end + len("</html>")]
    if not html:
        raise SystemExit("Iron Oak SK source HTML not found in transcript")
    return html


def adapt(html: str) -> str:
    html = re.sub(
        r"<!-- Internal offer reference:.*?-->\s*<!-- Google tag \(gtag\.js\) -->.*?</script>\s*",
        "<!-- Iron Oak Pro SK — offer 3228 · lp 3262 · 79,00 EUR -->\n" + GTAG_HEAD + "\n",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r"</script>\s*<script>\s*window\.dataLayer.*?AW-18376580748.*?</script>\s*",
        "</script>\n\n",
        html,
        count=1,
        flags=re.S,
    )
    html = html.replace("devicepathhub.com", "trendtopia-store.com")
    html = html.replace("devicepathhub<span>", "trendtopia-store<span>")
    html = html.replace("info@devicepathhub.com", "info@trendtopia-store.com")
    html = html.replace(
        "https://devicepathhub.com/sk/vortek-3228/",
        "https://trendtopia-store.com/sk/vortek-3228/",
    )
    if "<meta name=\"robots\"" not in html:
        html = html.replace(
            '<meta charset="utf-8">',
            '<meta charset="utf-8">\n<meta name="robots" content="noindex, nofollow">',
            1,
        )
    html = html.replace(
        "COOKIE_LEARN: 'Zistiť viac'\n};",
        "COOKIE_LEARN: 'Zistiť viac',\n  GOOGLE_TAG_ID: 'AW-18327321473',\n};",
    )
    if 'src="/assets/js/tracking.js"' not in html:
        html = html.replace(
            "</script>\n<script crossorigin=\"anonymous\" defer src=\"https://offers.adricenetwork.com/forms/tmfp/\"></script>",
            "</script>\n<script src=\"/assets/js/tracking.js\" defer></script>\n<script src=\"/assets/js/main.js\" defer></script>",
        )
    html = html.replace(
        '<script crossorigin="anonymous" defer src="https://offers.adricenetwork.com/forms/tmfp/"></script>\n\n\n',
        "",
    )
    html = html.replace("vk-cookie-change-link", "tt-cookie-change-link")
    html = re.sub(
        r'\s*<script src="https://offers\.adricenetwork\.com/forms/html/js-v2/" async></script>\s*',
        "\n",
        html,
    )
    html = html.replace(
        "subidInput.value = campaign;",
        "if (!subidInput.value) subidInput.value = campaign;",
    )
    html = html.replace(
        'src="/assets/img/products/vortek/hero.webp?v=3"',
        'src="/assets/img/products/vortek/hero.webp?v=3" onerror="this.onerror=null;this.src=\'/assets/img/placeholder.svg\'"',
    )
    wire_cookie = """
  document.querySelectorAll('.tt-cookie-change-link').forEach(function (btn) {
    if (btn.dataset.cookiePrefsBound === '1') return;
    btn.dataset.cookiePrefsBound = '1';
    btn.addEventListener('click', function () {
      if (typeof window.ttOpenCookiePreferences === 'function') {
        window.ttOpenCookiePreferences();
      }
    });
  });
"""
    html = html.replace(
        "  document.addEventListener('DOMContentLoaded', function () {",
        wire_cookie + "\n  document.addEventListener('DOMContentLoaded', function () {",
    )
    if "forms/html/js-v2/" not in html:
        html = html.replace(
            "</body>",
            '<script src="https://offers.adricenetwork.com/forms/tmfp/" crossorigin="anonymous" defer></script>\n'
            '<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>\n'
            "</body>",
        )
    return html


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    html = adapt(extract_html())
    OUT_LANDING.write_text(html, encoding="utf-8", newline="\n")
    print("Wrote", OUT_LANDING, OUT_LANDING.stat().st_size)


if __name__ == "__main__":
    main()
