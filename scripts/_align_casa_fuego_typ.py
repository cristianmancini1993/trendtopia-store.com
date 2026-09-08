#!/usr/bin/env python3
"""Align ES/PL/SK/CZ Casa Fuego landings: hero grid, sticky CTA, package split, typography. No image changes."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = subprocess.check_output(["git", "show", "c3a8060:pl/casa-fuego/landing.html"], encoding="utf-8")

HERO_CSS = REF[REF.find("/* ---------- HERO ---------- */") : REF.find("/* ---------- ESTRELLAS ---------- */")]

EXTRA_CSS = """
.cf-package-note{text-align:center;font-size:13px;color:var(--cf-gray);margin:-8px 0 16px;line-height:1.5}
.cf-package-items{display:grid;gap:8px;margin-bottom:8px}
.cf-package-items li{background:var(--cf-light);border-radius:10px;padding:10px 12px;border-bottom:none;font-size:14px}
.cf-package-meta li{font-size:13px;color:var(--cf-gray);border-bottom:none;padding:6px 0}
.cf-sticky-cta{
  display:none;position:fixed;left:0;right:0;bottom:0;z-index:900;
  background:#fff;border-top:1px solid #ece0d8;padding:10px 16px calc(10px + env(safe-area-inset-bottom));
  box-shadow:0 -8px 24px rgba(0,0,0,.08);
}
.cf-sticky-cta__inner{max-width:520px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px}
.cf-sticky-cta__price{font-size:18px;font-weight:800;color:var(--cf-orange);white-space:nowrap}
.cf-sticky-cta .cf-cta{margin:0;padding:12px 22px;font-size:15px;flex:1;text-align:center;max-width:220px}
@media(min-width:900px){
  .cf-hero-grid{grid-template-columns:1.05fr .95fr;gap:40px}
  .cf-hero-copy{text-align:left}
  .cf-feats,.cf-price-box{margin-left:0;margin-right:0}
  .cf-stars{justify-content:flex-start}
  .cf-price-box{text-align:left}
  .cf-trust{justify-content:flex-start}
}
"""

EYEBROW_FIXES = {
    "es": [
        ("01 — CALOR UNIFORME GRACIAS AL FONDO DE 5 CAPAS", "01 — Calor uniforme gracias al fondo de 5 capas"),
        ("02 — ACERO INOXIDABLE RESISTENTE Y DURADERO", "02 — Acero inoxidable resistente y duradero"),
        ("03 — DETALLES PENSADOS PARA EL DÍA A DÍA", "03 — Detalles pensados para el día a día"),
    ],
    "pl": [
        ("01 — RÓWNOMIERNE CIEPŁO DZIĘKI DNU 5-WARSTWOWEMU", "01 — Równomierne ciepło dzięki dnu 5-warstwowemu"),
        ("02 — TRWAŁA I ODPORNA STAL NIERDZEWNA", "02 — Trwała i odporna stal nierdzewna"),
        ("03 — DETALE PRZEMYŚLANE NA CO DZIEŃ", "03 — Detale przemyślane na co dzień"),
    ],
    "sk": [
        ("01 — ROVNOMERNÉ TEPLO VĎAKA 5-VRSTVOVÉMU DNU", "01 — Rovnomerné teplo vďaka 5-vrstvovému dnu"),
        ("02 — ODOLNÁ A TRVÁCNA NEHRDZAVEJÚCA OCEĽ", "02 — Odolná a trvácna nehrdzavejúca oceľ"),
        ("03 — DETAILY PREMYSLENÉ NA KAŽDÝ DEŇ", "03 — Detaily premyslené na každý deň"),
    ],
    "cz": [
        ("01 — ROVNOMĚRNÉ TEPLO DÍKY 5VRSTVÉMU DNU", "01 — Rovnoměrné teplo díky 5vrstvému dnu"),
        ("02 — ODOLNÁ A TRVANLIVÁ NEREZOVÁ OCEL", "02 — Odolná a trvanlivá nerezová ocel"),
        ("03 — DETAILY PROMYŠLENÉ NA KAŽDÝ DEN", "03 — Detaily promyšlené na každý den"),
    ],
}

STICKY = {
    "es": ('89,00 €', "Pedir", "#cf-formulario"),
    "pl": ("399,00 zł", "Zamów", "#cf-formulario"),
    "sk": ("89,00 €", "Objednať", "#cf-formulario"),
    "cz": ("1 999 Kč", "Objednat", "#cf-formulario"),
}


def patch_css(html: str) -> str:
    html = re.sub(
        r"/\* ---------- HERO ---------- \*/.*?\.cf-form-privacy a\{color:var\(--cf-orange-dark\);text-decoration:underline\}\n",
        HERO_CSS,
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = html.replace(
        "  text-transform:uppercase;margin-bottom:10px;line-height:1.4;",
        "  margin-bottom:10px;line-height:1.4;",
    )
    if ".cf-package-note{" not in html:
        html = html.replace(
            ".cf-package .pkg-price{text-align:center;margin-top:16px;font-size:26px;font-weight:800;color:var(--cf-orange)}",
            ".cf-package .pkg-price{text-align:center;margin-top:16px;font-size:26px;font-weight:800;color:var(--cf-orange)}"
            + EXTRA_CSS,
            1,
        )
    if "@media(max-width:600px){\n  .cf-wrap{padding:0 16px}" in html and ".cf-sticky-cta{display:block}" not in html:
        html = html.replace(
            "@media(max-width:600px){\n  .cf-wrap{padding:0 16px}",
            "@media(max-width:600px){\n  .cf-sticky-cta{display:block}\n  .cf-lp{padding-bottom:76px}\n  .cf-wrap{padding:0 16px}",
            1,
        )
    return html


def restructure_hero(html: str) -> str:
    if "cf-hero-copy" in html:
        return html
    start = html.find('<section class="cf-hero">')
    if start == -1:
        return html
    end = html.find("</section>", start) + len("</section>")
    hero = html[start:end]

    hero = hero.replace(
        '<section class="cf-hero">\n<div class="cf-wrap">',
        '<section class="cf-hero">\n<div class="cf-wrap cf-hero-grid">\n<div class="cf-hero-copy">',
        1,
    )
    img_m = re.search(r"\n<div class=\"cf-hero-img\">.*?</div>\n", hero, re.DOTALL)
    if not img_m:
        return html
    img_block = img_m.group(0)
    hero = hero[: img_m.start()] + "\n" + hero[img_m.end() :]
    hero = hero.replace(
        "</div>\n</section>",
        "</div>" + img_block + "</div>\n</section>",
        1,
    )
    return html[:start] + hero + html[end:]


def split_package(html: str) -> str:
    if '<ul class="cf-package-items">' in html:
        return html

    def repl(m: re.Match) -> str:
        intro, items_block = m.group(1), m.group(2)
        lines = [ln.strip() for ln in items_block.splitlines() if ln.strip()]
        products, meta = [], []
        for ln in lines:
            if any(x in ln for x in ("🚚", "💳", "🔄", "💶", "↩")):
                meta.append(ln)
            else:
                products.append(ln)
        intro = re.sub(
            r'<p style="text-align:center;font-size:14px;margin-bottom:12px">',
            '<p class="cf-package-note">',
            intro,
        )
        return (
            intro
            + '<ul class="cf-package-items">\n'
            + "\n".join(products)
            + "\n</ul>\n<ul class=\"cf-package-meta\">\n"
            + "\n".join(meta)
            + "\n</ul>"
        )

    return re.sub(
        r'(<div class="cf-package">\s*<h3>.*?</h3>\s*<p[^>]*>.*?</p>\s*)<ul>(.*?)</ul>',
        repl,
        html,
        count=1,
        flags=re.DOTALL,
    )


def add_sticky(html: str, geo: str) -> str:
    price, label, href = STICKY[geo]
    block = f"""
<div class="cf-sticky-cta">
<div class="cf-sticky-cta__inner">
<span class="cf-sticky-cta__price">{price}</span>
<a class="cf-cta" href="{href}">{label}</a>
</div>
</div>
"""
    if '<div class="cf-sticky-cta">' in html:
        return html.replace('<div class="cf-sticky-cta" aria-hidden="true">', '<div class="cf-sticky-cta">')
    marker = "\n(function () {"
    if marker in html:
        return html.replace(marker, "\n" + block + marker, 1)
    return html.replace("</div>\n\n<footer", block + "\n</div>\n\n<footer", 1)


def patch_eyebrows(html: str, geo: str) -> str:
    for old, new in EYEBROW_FIXES.get(geo, []):
        html = html.replace(old, new)
    return html


def align_file(path: Path) -> None:
    geo = path.parent.parent.name
    html = path.read_text(encoding="utf-8")
    html = patch_css(html)
    html = restructure_hero(html)
    html = split_package(html)
    html = add_sticky(html, geo)
    html = patch_eyebrows(html, geo)
    path.write_text(html, encoding="utf-8")
    print(f"Aligned {path.relative_to(ROOT)}")


def main() -> None:
    for geo in ("es", "pl", "sk", "cz"):
        align_file(ROOT / geo / "casa-fuego" / "landing.html")


if __name__ == "__main__":
    main()
