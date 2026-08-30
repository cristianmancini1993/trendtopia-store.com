#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Casa Fuego landings + thank-you pages for all campaign geos."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

from casa_fuego_i18n import LANDING_REPLACEMENTS, LT_TY, META

ROOT = Path(__file__).resolve().parents[1]
SLUG = "casa-fuego"

GEOS = {
    "1476": {"geo": "pt", "lang": "pt", "tr": "pt", "price": 99.0, "currency": "EUR", "offer": "1476"},
    "2409": {"geo": "hu", "lang": "hu", "tr": "hu", "price": 31999.0, "currency": "HUF", "offer": "2409"},
    "3176": {"geo": "es", "lang": "es", "tr": "es", "price": 89.0, "currency": "EUR", "offer": "3176"},
    "3177": {"geo": "de", "lang": "de", "tr": "de", "price": 109.0, "currency": "EUR", "offer": "3177"},
    "3178": {"geo": "lt", "lang": "lt", "tr": "lt", "price": 89.0, "currency": "EUR", "offer": "3178"},
    "3179": {"geo": "pl", "lang": "pl", "tr": "pl", "price": 399.0, "currency": "PLN", "offer": "3179"},
    "3251": {"geo": "cz", "lang": "cs", "tr": "cz", "price": 1999.0, "currency": "CZK", "offer": "3251"},
    "3702": {"geo": "sk", "lang": "sk", "tr": "sk", "price": 89.0, "currency": "EUR", "offer": "3702"},
}

INDEX_TMPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/{slug}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/{slug}/landing.html">
<link rel="canonical" href="https://trendtopia-store.com/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">Casa Fuego™</a></p>
</body>
</html>
"""

# Spanish base prices in es/casa-fuego/landing.html
ES_BASE_NOW = "79,99 €"
ES_BASE_OLD = "159,98 €"
ES_BASE_SAVE = "Hoy ahorras 79,99 €"

# Hungarian base prices in hu/casa-fuego/landing.html
HU_BASE_NOW = "31 999 Ft"
HU_BASE_OLD = "63 998 Ft"
HU_BASE_SAVE = "Ma 31 999 Ft-ot takarítasz meg"


def fmt_price(amount: float, currency: str) -> str:
    if currency == "CZK":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s},00 Kč"
    if currency == "HUF":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s} Ft"
    if currency == "PLN":
        whole = int(amount)
        frac = int(round((amount - whole) * 100))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s},{frac:02d} zł"
    s = f"{amount:.2f}".replace(".", ",")
    return f"{s} €"


def load_ga_translations() -> dict:
    tr: dict = {}
    for name in ("_ga_i18n_part1", "_ga_i18n_part2", "_ga_i18n_part3"):
        path = Path(__file__).with_name(f"{name}.py")
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(mod)
        tr.update(mod.TRANSLATIONS)
    return tr


def load_network_forms():
    path = Path(__file__).with_name("casa_fuego_network_forms.py")
    spec = importlib.util.spec_from_file_location("casa_fuego_network_forms", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def apply_replacements(html: str, pairs: list[tuple[str, str]]) -> str:
    for src, dst in sorted(pairs, key=lambda p: len(p[0]), reverse=True):
        html = html.replace(src, dst)
    return html


def patch_lang(html: str, lang: str) -> str:
    html = html.replace('<html lang="es">', f'<html lang="{lang}">', 1)
    html = html.replace('<html lang="hu">', f'<html lang="{lang}">', 1)
    html = re.sub(r'<div class="cf-lp" lang="[^"]+"', f'<div class="cf-lp" lang="{lang}"', html, count=1)
    return html


def patch_meta(html: str, tr_key: str, now: str) -> str:
    meta = META[tr_key]
    title = meta["title"]
    desc = meta["description"].format(now=now)
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content=".*?"\s*/?>',
        f'<meta name="description" content="{desc}">',
        html,
        count=1,
    )
    return html


def patch_prices(html: str, cfg: dict, tr_key: str) -> str:
    now = fmt_price(cfg["price"], cfg["currency"])
    old = fmt_price(cfg["price"] * 2, cfg["currency"])
    save = META[tr_key]["save_line"].format(now=now)
    html = re.sub(
        r'(<span class="now">)[^<]*(</span>)',
        rf"\g<1>{now}\g<2>",
        html,
    )
    html = re.sub(
        r'(<span class="old">)[^<]*(</span>)',
        rf"\g<1>{old}\g<2>",
        html,
    )
    html = re.sub(
        r'(<div class="cf-save-line">)[^<]*(</div>)',
        rf"\g<1>{save}\g<2>",
        html,
    )
    html = re.sub(
        r'(<div class="pkg-price">)[^<]*(<span class="old">)',
        rf"\g<1>{now} \g<2>",
        html,
    )
    return html


def inject_forms(html: str, geo: str, offer: str, net_mod) -> str:
    ty = f"https://trendtopia-store.com/{geo}/{SLUG}/thank-you.html"
    form = net_mod.FORMS[offer]
    html = re.sub(
        r'(<input name="uid" type="hidden" value=")[^"]*(" />)',
        rf'\g<1>{net_mod.UID}\g<2>',
        html,
    )
    html = re.sub(
        r'(<input name="offer" type="hidden" value=")[^"]*(" />)',
        rf'\g<1>{offer}\g<2>',
        html,
    )
    html = re.sub(
        r'(<input name="lp" type="hidden" value=")[^"]*(" />)',
        rf'\g<1>{form["lp"]}\g<2>',
        html,
    )
    html = re.sub(
        r'(<input name="thankyoupage" type="hidden" value=")[^"]*("/>)',
        rf'\g<1>{ty}\g<2>',
        html,
    )
    html = re.sub(
        r'(<input name="webhook" type="hidden" value=")[^"]*("/>)',
        rf'\g<1>{net_mod.WEBHOOK}\g<2>',
        html,
    )
    html = re.sub(
        r'(<input name="_key" type="hidden" value=")[^"]*(" />)',
        rf'\g<1>{form["key"]}\g<2>',
        html,
    )
    return html


def render_landing(offer: str, cfg: dict, net_mod) -> str:
    geo = cfg["geo"]
    tr_key = cfg["tr"]
    if geo == "hu":
        html = (ROOT / "hu/casa-fuego/landing.html").read_text(encoding="utf-8")
        # Strip prior generator output so Hungarian source stays the translation base.
        html = re.sub(r'(<input name="uid" type="hidden" value=")[^"]*(" />)', r'\g<1>\g<2>', html)
        html = re.sub(r'(<input name="offer" type="hidden" value=")[^"]*(" />)', r'\g<1>\g<2>', html)
        html = re.sub(r'(<input name="lp" type="hidden" value=")[^"]*(" />)', r'\g<1>\g<2>', html)
        html = re.sub(r'(<input name="thankyoupage" type="hidden" value=")[^"]*("/>)', r'\g<1>\g<2>', html)
        html = re.sub(r'(<input name="webhook" type="hidden" value=")[^"]*("/>)', r'\g<1>\g<2>', html)
        html = re.sub(r'(<input name="_key" type="hidden" value=")[^"]*(" />)', r'\g<1>\g<2>', html)
        html = patch_prices(html, cfg, tr_key)
    else:
        html = (ROOT / "es/casa-fuego/landing.html").read_text(encoding="utf-8")
        if tr_key != "es" and tr_key in LANDING_REPLACEMENTS:
            html = apply_replacements(html, LANDING_REPLACEMENTS[tr_key])
        if tr_key != "es":
            html = patch_lang(html, cfg["lang"])
        html = patch_prices(html, cfg, tr_key)
    now = fmt_price(cfg["price"], cfg["currency"])
    html = patch_meta(html, tr_key, now)
    html = inject_forms(html, geo, offer, net_mod)
    return html


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def patch_thank_you(geo: str, cfg: dict, shared: dict, es_ty: str, offer: str, cpa: float) -> str:
    html = es_ty
    html = html.replace('lang="es"', f'lang="{cfg["lang"]}"', 1)
    html = re.sub(r"GEO:\s*'[^']*'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'[^']*'", f"PRODUCT_SLUG: '{SLUG}'", html)
    html = re.sub(r"CURRENCY:\s*'[^']*'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[0-9.]+", f"PRICE: {cfg['price']}", html)
    html = re.sub(
        r"trackPurchase\([0-9.]+,\s*'[^']*'\)",
        f"trackPurchase({cfg['price']}, '{cfg['currency']}')",
        html,
    )
    html = re.sub(
        r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
        f"COOKIE_TEXT: '{esc_js(shared['cookie_text'])}',\n  COOKIE_ACCEPT: '{esc_js(shared['cookie_accept'])}',\n  COOKIE_LEARN: '{esc_js(shared['cookie_learn'])}'",
        html,
    )
    ty_title = shared["ty_title"].replace("GlacierAir™", "Casa Fuego™")
    ty_desc = shared["ty_desc"].replace("GlacierAir™", "Casa Fuego™")
    html = re.sub(r"<title>.*?</title>", f"<title>{ty_title}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content=".*?"\s*/?>',
        f'<meta name="description" content="{ty_desc}">',
        html,
        count=1,
    )
    html = html.replace("¡Tu pedido se ha registrado correctamente!", shared["ty_h1"])
    html = html.replace(
        "Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.",
        shared["ty_sub"],
    )
    html = html.replace(
        "El equipo trendtopia-store trabajando: call center y logística contra reembolso",
        shared["ty_alt"],
    )
    html = html.replace("👇 Qué debes hacer ahora", shared["ty_eyebrow"])
    html = html.replace("📞 Responde a la llamada de confirmación", shared["ty_action_title"])
    html = html.replace(
        "Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido.",
        shared["ty_action_body"],
    )
    html = html.replace(
        "Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        shared["ty_action_warn"],
    )
    html = html.replace("🕒 Horario de contacto", shared["ty_hours_h"])
    html = html.replace("<strong>Lunes – Sábado</strong> · 9:00 – 18:00", shared["ty_hours"])
    html = html.replace("📋 Qué ocurre después", shared["ty_next_h"])
    es_steps = [
        "Responde a la llamada y <strong>confirma tus datos</strong>",
        "Tu pedido se enviará en un plazo de <strong>24–48 horas</strong>",
        "Entrega a domicilio y <strong>pago contra reembolso</strong>",
    ]
    for es_step, loc_step in zip(es_steps, shared["ty_steps"]):
        html = html.replace(f"<li>{es_step}</li>", f"<li>{loc_step}</li>")
    es_badges = ("🔒 Pago contra reembolso", "🛡️ Garantía 24 meses", "🔐 Protección SSL")
    for es_b, loc_b in zip(es_badges, shared["ty_badges"]):
        html = html.replace(es_b, loc_b)
    footer_es = (
        "    <div>\n"
        '      <h4 class="site-footer__heading">Información</h4>\n'
        '      <ul class="site-footer__list">\n'
        '        <li><a href="/es/about-us.html">Sobre nosotros</a></li>\n'
        '        <li><a href="/es/contact-us.html">Contáctanos</a></li>\n'
        '        <li><a href="/es/privacy-policy.html">Política de privacidad</a></li>\n'
        '        <li><a href="/es/terms-conditions.html">Términos y condiciones</a></li>\n'
        '        <li><a href="/es/cookie-policy.html">Política de cookies</a></li>\n'
        '        <li><a href="/es/shipping-policy.html">Política de envío</a></li>\n'
        '        <li><a href="/es/refund-policy.html">Política de reembolso</a></li>\n'
        "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        '      <h4 class="site-footer__heading">Contacto</h4>'
    )
    footer_geo = (
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{shared["info"]}</h4>\n'
        '      <ul class="site-footer__list">\n'
        f'        <li><a href="/{geo}/about-us.html">{shared["about"]}</a></li>\n'
        f'        <li><a href="/{geo}/contact-us.html">{shared["contact"]}</a></li>\n'
        f'        <li><a href="/{geo}/privacy-policy.html">{shared["privacy"]}</a></li>\n'
        f'        <li><a href="/{geo}/terms-conditions.html">{shared["terms"]}</a></li>\n'
        f'        <li><a href="/{geo}/cookie-policy.html">{shared["cookie"]}</a></li>\n'
        f'        <li><a href="/{geo}/shipping-policy.html">{shared["ship"]}</a></li>\n'
        f'        <li><a href="/{geo}/refund-policy.html">{shared["refund"]}</a></li>\n'
        "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{shared["contacts"]}</h4>'
    )
    html = html.replace(footer_es, footer_geo)
    html = html.replace("Todos los derechos reservados.", shared["rights"] + ".")
    html = html.replace("/es/", f"/{geo}/")
    html = re.sub(r"'value':\s*[0-9.]+", f"'value': {cpa}", html)
    html = re.sub(
        r"<!-- Google Ads Purchase conversion[^>]*-->",
        f"<!-- Google Ads Purchase conversion — value = CPA/CPL EUR for offer #{offer} -->",
        html,
    )
    return html


def shared_for_geo(tr_key: str, ga_tr: dict) -> dict:
    if tr_key == "lt":
        return LT_TY
    return ga_tr[tr_key]


def main(only: set[str] | None = None) -> None:
    ga_tr = load_ga_translations()
    net_mod = load_network_forms()
    es_ty = (ROOT / "es/glacierair-3345/thank-you.html").read_text(encoding="utf-8")

    for offer, cfg in GEOS.items():
        if only is not None and offer not in only:
            continue
        geo = cfg["geo"]
        tr_key = cfg["tr"]
        out_dir = ROOT / geo / SLUG
        out_dir.mkdir(parents=True, exist_ok=True)

        landing = render_landing(offer, cfg, net_mod)
        (out_dir / "landing.html").write_text(landing, encoding="utf-8")

        (out_dir / "index.html").write_text(
            INDEX_TMPL.format(lang=cfg["lang"], geo=geo, slug=SLUG),
            encoding="utf-8",
        )

        shared = shared_for_geo(tr_key, ga_tr)
        cpa = net_mod.CPA[offer]
        ty = patch_thank_you(geo, cfg, shared, es_ty, offer, cpa)
        (out_dir / "thank-you.html").write_text(ty, encoding="utf-8")

        line = f"Wrote {geo}/{SLUG}/ (#{offer}) - {fmt_price(cfg['price'], cfg['currency'])}"
        print(line.encode("ascii", "replace").decode("ascii"))


if __name__ == "__main__":
    import sys

    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(only)
