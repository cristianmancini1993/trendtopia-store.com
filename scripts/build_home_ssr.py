#!/usr/bin/env python3
"""
Pre-render home page per locale for server-side delivery (nginx Accept-Language / cookie).
Source template: index.template.html → index.html + home/index.{locale}.html
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "index.template.html"
OUT_DIR = ROOT / "home"
DEFAULT_LOCALE = "en"


def load_data() -> dict:
    js_path = ROOT / "assets/js/home-i18n-data.js"
    code = js_path.read_text(encoding="utf-8")
    script = (
        "const fs=require('fs');const vm=require('vm');"
        "const code=fs.readFileSync('assets/js/home-i18n-data.js','utf8');"
        "const g={globalThis:{}};vm.runInNewContext(code,g);"
        "process.stdout.write(JSON.stringify(g.globalThis.HOME_I18N_DATA));"
    )
    try:
        raw = subprocess.check_output(["node", "-e", script], cwd=ROOT, text=True)
        return json.loads(raw)
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    try:
        import dukpy  # type: ignore

        raw = dukpy.evaljs(code + "\nJSON.stringify(globalThis.HOME_I18N_DATA);")
        return json.loads(raw)
    except Exception as e:
        raise SystemExit(
            "Could not load home i18n data (install Node.js or pip install dukpy)"
        ) from e


def compute_select_locales(data: dict) -> list[str]:
    labels = data["LOCALE_LABELS"]
    en_home = data["EN_HOME_MARKETS"]
    with_landing = {"en"}
    for g in en_home["setOfPots"] + en_home["coreSync"]:
        with_landing.add(g)
    rest = sorted(
        (k for k in labels if k != "en" and k in with_landing),
        key=lambda k: labels[k].casefold(),
    )
    return ["en"] + rest


def compute_locale_markets(data: dict, select_locales: list[str]) -> dict:
    casa = data["CASA_FUEGO_GEOS"]
    core = data["CORESYNC_GEOS"]
    en_home = data["EN_HOME_MARKETS"]
    markets = {
        "en": {
            "setOfPots": list(en_home["setOfPots"]),
            "coreSync": list(en_home["coreSync"]),
        }
    }
    for geo in select_locales:
        if geo == "en":
            continue
        markets[geo] = {
            "setOfPots": [geo] if geo in casa else [],
            "coreSync": [geo] if geo in core else [],
        }
    return markets


def msg(data: dict, locale: str, key: str) -> str:
    pack = data["MESSAGES"].get(locale) or {}
    if key in pack:
        return pack[key]
    en = data["MESSAGES"].get("en") or {}
    return en.get(key, "")


def priced_line(data: dict, locale: str, key: str, price: str) -> str:
    lines = data["PRICED_LINES"]
    pack = lines.get(locale) or lines.get("en") or {}
    tpl = pack.get(key) or lines.get("en", {}).get(key) or "{price}"
    return tpl.replace("{price}", price)


def market_hrefs(data: dict, locale_markets: dict, locale: str, product: str) -> list[tuple[str, str]]:
    codes = locale_markets.get(locale, {}).get(product, [])
    hrefs = []
    for code in codes:
        if product == "setOfPots":
            href = f"/{code}/casa-fuego/landing.html"
        else:
            href = f"/{code}/smartwatch/landing.html"
        hrefs.append((code.upper(), href))
    return hrefs


def links_html(pairs: list[tuple[str, str]]) -> str:
    if not pairs:
        return ""
    return " · ".join(f'<a href="{h}">{c}</a>' for c, h in pairs)


def set_attr(html: str, attr: str, key: str, value: str, *, is_html: bool = False) -> str:
    pattern = rf'(<[^>]*\bdata-{attr}="{re.escape(key)}"[^>]*>)(.*?)(</[^>]+>)'

    def repl(m: re.Match[str]) -> str:
        inner = value if is_html else escape(value)
        return m.group(1) + inner + m.group(3)

    return re.sub(pattern, repl, html, count=1, flags=re.S | re.I)


def set_logo_aria(html: str, value: str) -> str:
    safe = value.replace('"', "&quot;")
    return re.sub(
        r'(<a[^>]*class="site-logo"[^>]*aria-label=")[^"]*(")',
        rf"\1{safe}\2",
        html,
        count=1,
    )


def set_img_alt(html: str, key: str, value: str) -> str:
    safe = escape(value)
    return re.sub(
        rf'(<img[^>]*data-i18n-alt="{re.escape(key)}"[^>]*alt=")[^"]*(")',
        rf"\1{safe}\2",
        html,
        count=1,
    )


def set_i18n_html(html: str, key: str, value: str) -> str:
    """Replace inner HTML up to the element's own closing tag (not nested tags like </em>)."""
    pattern = (
        rf'(<(\w+)[^>]*\bdata-i18n-html="{re.escape(key)}"[^>]*>)'
        rf"(.*?)"
        rf"(</\2>)"
    )
    return re.sub(
        pattern,
        lambda m: m.group(1) + value + m.group(4),
        html,
        count=1,
        flags=re.S | re.I,
    )


def render_locale(template: str, locale: str, data: dict, select_locales: list[str], locale_markets: dict) -> str:
    html = template
    html_lang = data["HTML_LANG"].get(locale, locale)
    html = re.sub(
        r"<html lang=\"[^\"]*\"",
        f'<html lang="{html_lang}" data-ssr-locale="{locale}"',
        html,
        count=1,
    )

    hero_val = msg(data, locale, "hero_title")
    if hero_val:
        html = set_i18n_html(html, "hero_title", hero_val)

    i18n_keys = set(re.findall(r'data-i18n="([^"]+)"', html))
    i18n_keys.discard("hero_title")
    for key in i18n_keys:
        val = msg(data, locale, key)
        if val:
            html = set_attr(html, "i18n", key, val)

    for key in re.findall(r'data-i18n-alt="([^"]+)"', html):
        val = msg(data, locale, key)
        if val:
            html = set_img_alt(html, key, val)

    logo_aria = msg(data, locale, "logo_aria")
    if logo_aria:
        html = set_logo_aria(html, logo_aria)

    geo = locale
    html = re.sub(
        r'(<a[^>]*data-i18n-href="([^"]+)"[^>]*href=")[^"]*(")',
        lambda m: m.group(1) + f"/{geo}/{m.group(2)}" + m.group(3),
        html,
    )

    prices = data["PRODUCT_PRICES"]
    use_chooser = locale == "en"

    feat = msg(data, locale, "featured_name")
    if not use_chooser:
        cp = prices["coreSync"].get(locale)
        if cp:
            feat = priced_line(data, locale, "featured_name_priced", cp)
    html = set_attr(html, "i18n", "featured_name", feat)

    def product_title(key_priced: str, key_plain: str, price_map: dict) -> str:
        if use_chooser:
            return msg(data, locale, key_plain)
        p = price_map.get(locale)
        if p:
            return priced_line(data, locale, key_priced, p)
        return msg(data, locale, key_plain)

    pots_title = product_title("product_setOfPots_priced", "product_setOfPots_title", prices["setOfPots"])
    core_title = product_title("product_coreSync_priced", "product_coreSync_title", prices["coreSync"])
    html = re.sub(
        r'(<[^>]*data-i18n="product_setOfPots_title"[^>]*>)(.*?)(</[^>]+>)',
        lambda m: m.group(1) + escape(pots_title) + m.group(3),
        html,
        flags=re.S,
    )
    html = re.sub(
        r'(<[^>]*data-i18n="product_coreSync_title"[^>]*>)(.*?)(</[^>]+>)',
        lambda m: m.group(1) + escape(core_title) + m.group(3),
        html,
        flags=re.S,
    )

    for product, attr in (("setOfPots", "setOfPots"), ("coreSync", "coreSync")):
        pairs = market_hrefs(data, locale_markets, locale, product)
        inner = links_html(pairs)
        pattern = rf'(<span[^>]*data-market-links="{attr}"[^>]*>)(.*?)(</span>)'

        def repl(m: re.Match[str], inner=inner) -> str:
            return m.group(1) + inner + m.group(3)

        html = re.sub(pattern, repl, html, flags=re.S)
        if not pairs:
            html = re.sub(
                rf'(<div[^>]*data-home-product="{product}"[^>]*)(>)',
                r'\1 hidden>',
                html,
                count=1,
            )

    core_codes = locale_markets.get(locale, {}).get("coreSync", [])
    if not core_codes:
        html = re.sub(
            r'(<section[^>]*data-home-feature="coresync"[^>]*)(>)',
            r"\1 hidden>",
            html,
            count=1,
        )

    labels = data["LOCALE_LABELS"]
    opts = []
    for loc in select_locales:
        sel = " selected" if loc == locale else ""
        opts.append(f'<option value="{loc}"{sel}>{escape(labels[loc])}</option>')
    lang_label = msg(data, locale, "lang_label")
    html = re.sub(
        r'(<select id="home-locale-select"[^>]*aria-label=")[^"]*(")',
        lambda m: m.group(1) + lang_label.replace('"', "&quot;") + m.group(2),
        html,
        count=1,
    )
    html = re.sub(
        r'(<select id="home-locale-select"[^>]*>)(.*?)(</select>)',
        lambda m: m.group(1) + "\n        " + "\n        ".join(opts) + "\n      " + m.group(3),
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'\s*data-populated="1"',
        "",
        html,
    )

    title = msg(data, locale, "page_title")
    desc = msg(data, locale, "page_description")
    if title:
        html = re.sub(r"<title>[^<]*</title>", f"<title>{escape(title)}</title>", html, count=1)
        html = re.sub(
            r'<meta property="og:title" content="[^"]*"',
            f'<meta property="og:title" content="{escape(title)}"',
            html,
            count=1,
        )
    if desc:
        html = re.sub(
            r'<meta name="description" content="[^"]*"',
            f'<meta name="description" content="{escape(desc)}"',
            html,
            count=1,
        )
        html = re.sub(
            r'<meta property="og:description" content="[^"]*"',
            f'<meta property="og:description" content="{escape(desc)}"',
            html,
            count=1,
        )

    cfg_geo = "en" if locale == "en" else locale
    cookie_pairs = [
        ("COOKIE_TEXT", "cookie_text"),
        ("COOKIE_ACCEPT_ALL", "cookie_accept_all"),
        ("COOKIE_REJECT", "cookie_reject"),
        ("COOKIE_MANAGE", "cookie_manage"),
        ("COOKIE_SAVE", "cookie_save"),
        ("COOKIE_CHANGE", "cookie_change"),
        ("COOKIE_LEARN", "cookie_learn"),
    ]
    cfg_parts = [f"GEO: '{cfg_geo}'"]
    for cfg_key, msg_key in cookie_pairs:
        val = msg(data, locale, msg_key)
        if val:
            val_esc = val.replace("\\", "\\\\").replace("'", "\\'")
            cfg_parts.append(f"{cfg_key}: '{val_esc}'")
    cfg_js = "{ " + ", ".join(cfg_parts) + " }"
    html = re.sub(
        r"<script>window\.SITE_CONFIG = \{[^}]*\};</script>",
        f"<script>window.SITE_CONFIG = {cfg_js};</script>",
        html,
        count=1,
    )

    return html


def main() -> int:
    if not TEMPLATE.is_file():
        print("Missing index.template.html — copy index.html to index.template.html first", file=sys.stderr)
        return 1
    data = load_data()
    select_locales = compute_select_locales(data)
    locale_markets = compute_locale_markets(data, select_locales)
    template = TEMPLATE.read_text(encoding="utf-8")
    OUT_DIR.mkdir(exist_ok=True)
    for locale in select_locales:
        rendered = render_locale(template, locale, data, select_locales, locale_markets)
        out_path = OUT_DIR / f"index.{locale}.html"
        out_path.write_text(rendered, encoding="utf-8", newline="\n")
        print("Wrote", out_path.relative_to(ROOT))
        if locale == DEFAULT_LOCALE:
            (ROOT / "index.html").write_text(rendered, encoding="utf-8", newline="\n")
            print("Wrote index.html (default", DEFAULT_LOCALE + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
