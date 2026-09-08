#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick static audit for 7 Google Ads destination URLs."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "home": ROOT / "index.html",
    "es_sw": ROOT / "es/smartwatch/landing.html",
    "pl_sw": ROOT / "pl/smartwatch/landing.html",
    "gr_sw": ROOT / "gr/smartwatch/landing.html",
    "pl_cf": ROOT / "pl/casa-fuego/landing.html",
    "cz_cf": ROOT / "cz/casa-fuego/landing.html",
    "sk_cf": ROOT / "sk/casa-fuego/landing.html",
}

ES_WORDS = re.compile(
    r"\b(Seguimiento|Incluye|pasos|registros de descanso|cargador|manual de instrucciones|"
    r"Actividad diaria|Introduce|Comprar|Nombre y apellidos|Teléfono|Dirección|España|Pídelo|Enviando|"
    r"Política de privacidad|Devolución en|Compradores reales)\b",
    re.I,
)

issues: list[dict] = []


def add(page: str, cat: str, prio: str, msg: str, detail: str = "") -> None:
    issues.append({"page": page, "cat": cat, "prio": prio, "msg": msg, "detail": detail})


def audit_file(key: str, path: Path) -> None:
    if not path.exists():
        add(key, "CURSOR", "CRÍTICO", "Archivo no existe", str(path))
        return
    t = path.read_text(encoding="utf-8")

    if "consent-default.js" in t:
        pos_c = t.find("consent-default.js")
        pos_g = t.find("googletagmanager.com/gtag/js")
        if pos_g != -1 and pos_c > pos_g:
            add(key, "CURSOR", "ALTO", "consent-default.js después de gtag async")
    else:
        if key != "home":
            add(key, "CURSOR", "ALTO", "Falta consent-default.js")

    if "AW-18327321473" not in t:
        add(key, "CURSOR", "ALTO", "Falta GOOGLE_TAG_ID AW-18327321473")

    if key == "pl_sw":
        for m in ES_WORDS.finditer(t):
            add(key, "CURSOR", "ALTO", f"Español residual: {m.group()}", f"pos ~{m.start()}")
        h1 = t.split("<h1>")[1].split("</h1>")[0] if "<h1>" in t else ""
        if re.search(r"\b(llamadas|notificaciones|muñeca|actividad y hasta)\b", h1, re.I):
            add(key, "CURSOR", "ALTO", "H1 en español", h1[:80])
        if re.search(r"\b(Javier|Pilar|Cristina|Valencia|Madrid|Bilbao|Walencja|Madryt)\b", t):
            add(key, "CURSOR", "MEDIO", "Nombres/ciudades españolas en reviews PL")

    if "tm-order-form" in t or 'class="cf-form tm-order-form"' in t:
        n_tmfp = t.count("forms/tmfp/")
        n_js = t.count("forms/html/js-v2/")
        if n_tmfp > 1 or n_js > 1:
            add(key, "CURSOR", "ALTO", f"Scripts AdRice duplicados tmfp={n_tmfp} js-v2={n_js}")
        if "form.dataset.submitting" not in t:
            add(key, "CURSOR", "MEDIO", "Sin protección dataset.submitting")
        if "tt-cookie-change-link" not in t or 'class="site-footer__link-btn tt-cookie-change-link"' not in t:
            add(key, "CURSOR", "MEDIO", "Sin botón cambiar preferencias cookies")

    if key.endswith("_sw"):
        if "window.SITE_CONFIG = {" in t and "Object.assign(window.SITE_CONFIG" not in t:
            add(key, "CURSOR", "ALTO", "SITE_CONFIG sobrescrito sin Object.assign")

    if "14 dni" in t or "14 dní" in t or "14 d" in t.lower():
        if "30" not in t[max(0, t.find("14") - 50) : t.find("14") + 50]:
            add(key, "CURSOR", "ALTO", "Posible referencia 14 días devolución")

    if 'noindex' in t and key.endswith(("_sw", "_cf")):
        add(key, "USUARIO", "MEDIO", "Landing con noindex (puede ser intencional Ads)")

    if key == "home" and "/es/smartwatch/landing.html" in t:
        add(key, "USUARIO", "MEDIO", "Home CTA apunta solo a ES smartwatch")


for k, p in PAGES.items():
    audit_file(k, p)

# CZ terms euros
terms = ROOT / "cz/terms-conditions.html"
if terms.exists():
    tx = terms.read_text(encoding="utf-8")
    if "v eurech" in tx.lower() or "eurech" in tx.lower():
        add("cz_terms", "CURSOR", "ALTO", "Términos CZ dicen precios en euros", str(terms))

print(f"ISSUES: {len(issues)}")
for i in issues:
    print(f"[{i['prio']}] {i['page']} ({i['cat']}): {i['msg']} {i['detail']}")
