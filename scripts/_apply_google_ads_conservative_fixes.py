#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conservative Google Ads compliance fixes for 7 target URLs + home + terms."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SHIPPING = {
    "es": "🚚 Envío gratis en 24–48 h laborables tras confirmación telefónica",
    "pl": "🚚 Darmowa dostawa w 24–48 h roboczych po potwierdzeniu telefonicznym",
    "gr": "🚚 Δωρεάν αποστολή σε 24–48 ώρες εργασίας μετά την τηλεφωνική επιβεβαίωση",
    "cz": "🚚 Doručení zdarma do 24–48 h v pracovní dny po telefonickém potvrzení",
    "sk": "🚚 Bezplatné doručenie do 24–48 h v pracovných dňoch po telefonickej konfirmácii",
}


def strip_verified(html: str) -> str:
    html = re.sub(r'\s*<span class="rv-verif">[^<]*</span>', "", html)
    return html


def strip_discount_block(html: str) -> str:
    html = re.sub(r'\s*<span class="disc">[^<]*</span>', "", html)
    html = re.sub(r'(<span class="old">)[^<]*(</span>)', "", html)
    html = re.sub(r'\s*<div class="cf-save-line">[^<]*</div>', "", html)
    html = re.sub(r'\s*<span class="off">[^<]*</span>', "", html)
    html = re.sub(r'\s*<span class="featured__discount-badge">[^<]*</span>', "", html)
    return html


def strip_buyer_counts(html: str) -> str:
    html = re.sub(r'\s*<span class="rev">[^<]*</span>', "", html)
    html = re.sub(
        r'<p>Ocena 4,6/5 na podstawie ponad <span class="num">\d+</span>[^<]*</p>',
        "<p>Ocena klientów widoczna w sekcji opinii poniżej.</p>",
        html,
    )
    html = re.sub(
        r'<p>Valoración 4,6/5 de más de <span class="num">\d+</span>[^<]*</p>',
        "<p>Valoración de clientes disponible en las opiniones siguientes.</p>",
        html,
    )
    html = re.sub(
        r'<p>Βαθμολογία 4,6/5 από πάνω από <span class="num">\d+</span>[^<]*</p>',
        "<p>Βαθμολογίες πελατών στις κριτικές παρακάτω.</p>",
        html,
    )
    html = re.sub(
        r'<p>Ocena 4,7/5 od ponad <span class="num">\d+</span>[^<]*</p>',
        "<p>Opinie klientów w sekcji poniżej.</p>",
        html,
    )
    html = re.sub(
        r'<p>Ocena 4,6/5 od více než <span class="num">\d+</span>[^<]*</p>',
        "<p>Hodnocení zákazníků v recenzích níže.</p>",
        html,
    )
    html = re.sub(
        r'<p>Hodnotenie 4,6/5 od viac než <span class="num">\d+</span>[^<]*</p>',
        "<p>Hodnotenia zákazníkov v recenziách nižšie.</p>",
        html,
    )
    html = re.sub(r'\s*<small>Prawdziwi kupujący • Zweryfikowane zakupy</small>', "", html)
    html = re.sub(r'\s*<small>Prawdziwi klienci • Zweryfikowane zakupy</small>', "", html)
    html = re.sub(r'\s*<small>[^<]*Zweryfikowane[^<]*</small>', "", html)
    return html


def neutralize_sub_today(html: str, replacements: dict[str, str]) -> str:
    for old, new in replacements.items():
        html = html.replace(old, new)
    return html


def fix_smartwatch(geo: str) -> None:
    path = ROOT / geo / "smartwatch" / "landing.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8")
    t = strip_discount_block(t)
    t = strip_buyer_counts(t)
    t = strip_verified(t)
    ship = SHIPPING.get(geo, SHIPPING["es"])
    t = re.sub(r"<span>🚚[^<]*</span>", f"<span>{ship}</span>", t)
    subs = {
        "es": ("Pídelo hoy y", "Pide con"),
        "pl": ("Zamów dziś i", "Zamów i"),
        "gr": ("Παραγγείλτε σήμερα και", "Παραγγείλτε και"),
    }
    if geo in subs:
        t = neutralize_sub_today(t, {subs[geo][0]: subs[geo][1]})
    path.write_text(t, encoding="utf-8", newline="\n")
    print(f"fixed smartwatch {geo}")


def fix_casa_fuego(geo: str) -> None:
    path = ROOT / geo / "casa-fuego" / "landing.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8")
    t = strip_discount_block(t)
    t = strip_buyer_counts(t)
    t = strip_verified(t)
    ship = SHIPPING.get(geo, SHIPPING["pl"])
    t = re.sub(r"<span>🚚[^<]*</span>", f"<span>{ship}</span>", t)
    t = re.sub(r"<li>🚚[^<]*</li>", f"<li>{ship}</li>", t)
    # titles / topbar without -50%
    title_map = {
        "pl": (
            "Casa Fuego™ — Zestaw 12 elementów | płatność przy odbiorze",
            "OFERTA: szybka dostawa · 24 miesiące gwarancji · zwrot 30 dni",
        ),
        "cz": (
            "Casa Fuego™ — Sada 12 dílů | platba na dobírku",
            "NABÍDKA: doručení · 24měsíční záruka · vrácení 30 dní",
        ),
        "sk": (
            "Casa Fuego™ — Súprava 12 dielov | platba na dobierku",
            "PONUKA: doručenie · 24-mesačná záruka · vrátenie 30 dní",
        ),
    }
    if geo in title_map:
        new_title, new_top = title_map[geo]
        t = re.sub(r"<title>[^<]*</title>", f"<title>{new_title}</title>", t, count=1)
        t = re.sub(
            r'<meta property="og:title" content="[^"]*">',
            f'<meta property="og:title" content="{new_title}">',
            t,
            count=1,
        )
        t = re.sub(
            r'<div class="cf-topbar">[^<]*</div>',
            f'<div class="cf-topbar">{new_top}</div>',
            t,
            count=1,
        )
    t = re.sub(
        r'<p>Hodnocení 4,7/5 od více než <span class="num">\d+</span>[^<]*</p>',
        "<p>Hodnocení zákazníků v recenzích níže.</p>",
        t,
    )
    t = re.sub(
        r'<p>Hodnotenie 4,7/5 od viac ako <span class="num">\d+</span>[^<]*</p>',
        "<p>Hodnotenia zákazníkov v recenziách nižšie.</p>",
        t,
    )
    t = t.replace("🖐️ Zawsze chłodny chwyt", "🖐️ Wygodny chwyt Comfort-Grip")
    t = t.replace("✅ Uchwyty Comfort-Grip, zawsze chłodne", "✅ Uchwyty Comfort-Grip zaprojektowane dla wygody")
    t = t.replace("Zamów dziś i", "Zamów i")
    t = t.replace("Objednejte dnes a", "Objednejte a")
    t = t.replace("Objednajte dnes a", "Objednajte a")
    path.write_text(t, encoding="utf-8", newline="\n")
    print(f"fixed casa-fuego {geo}")


def fix_pl_terms() -> None:
    path = ROOT / "pl" / "terms-conditions.html"
    t = path.read_text(encoding="utf-8")
    t = t.replace(
        "Ceny na stronie podane są w walucie Euro i zawierają podatek VAT.",
        "Ceny na stronie podane są w złotych polskich (PLN) i zawierają podatek VAT.",
    )
    path.write_text(t, encoding="utf-8", newline="\n")
    print("fixed pl terms currency")


def fix_home() -> None:
    path = ROOT / "index.html"
    t = path.read_text(encoding="utf-8")
    t = t.replace("Up to 50% off.", "Selected offers.")
    t = t.replace("Up to 50% off", "Selected offers")
    t = t.replace(
        "Hand-picked items for home, garden, and everyday life. Delivered in 24-48h with cash on delivery across 18 European countries.",
        "Hand-picked items for home, garden, and everyday life. Delivery typically in 24–48 business hours after order confirmation, with cash on delivery in supported European countries.",
    )
    t = t.replace('<h2 class="featured__title">Limited-time offer ends soon</h2>',
                  '<h2 class="featured__title">Featured product</h2>')
    t = t.replace('<span class="featured__discount-badge">-50%</span>', "")
    t = re.sub(
        r'<div class="featured__rating"><span class="stars">★★★★★</span> <strong>4\.6/5</strong> — 4,100\+ verified buyers</div>',
        '<div class="featured__rating"><span class="stars">★★★★★</span> Customer reviews on product pages</div>',
        t,
    )
    t = t.replace('no questions asked', 'see refund policy')
    t = t.replace('24-48h delivery', '24–48h business days')
    # Hero CTA -> country picker section
    picker = '''<div class="hero__markets" style="display:flex;flex-wrap:wrap;gap:0.75rem;justify-content:center;margin-top:0.5rem">
    <a href="/es/smartwatch/landing.html" class="hero__cta" style="font-size:0.95rem;padding:0.75rem 1.25rem">CoreSync — España</a>
    <a href="/pl/smartwatch/landing.html" class="hero__cta" style="font-size:0.95rem;padding:0.75rem 1.25rem;background:var(--color-primary)">CoreSync — Polska</a>
    <a href="/gr/smartwatch/landing.html" class="hero__cta" style="font-size:0.95rem;padding:0.75rem 1.25rem;background:#2563eb">CoreSync — Ελλάδα</a>
  </div>'''
    t = t.replace(
        '<a href="/es/smartwatch/landing.html" class="hero__cta">See this week\'s deal →</a>',
        picker,
    )
    t = t.replace('href="/es/smartwatch/landing.html" class="featured__photo"',
                  'href="/es/smartwatch/landing.html" class="featured__photo"')
    t = t.replace(
        '<a href="/es/smartwatch/landing.html" class="featured__cta">Get the deal →</a>',
        '''<p style="margin:0 0 0.75rem;font-size:0.95rem;color:var(--color-text-muted)">Available in: <a href="/es/smartwatch/landing.html">ES</a> · <a href="/pl/smartwatch/landing.html">PL</a> · <a href="/gr/smartwatch/landing.html">GR</a></p>
          <a href="/es/smartwatch/landing.html" class="featured__cta">View CoreSync →</a>''',
    )
    # categories tile
    t = re.sub(
        r'(<a href="/es/smartwatch/landing.html" class="cat-tile cat-tile--available">)',
        r'\1',
        t,
    )
    # why section zero risk
    t = t.replace("Zero risk, zero surprises.", "Clear pricing and policies on every product page.")
    t = re.sub(r'We respond within 1 hour[^<]*', 'Contact us via the support email on each page', t)
    t = re.sub(r'\s*<div class="reviews-summary__count">[^<]*</div>', "", t)
    t = t.replace(
        '<title>trendtopia-store.com — Curated products. Useful design. Up to 50% off.</title>',
        '<title>trendtopia-store.com — Curated products. Useful design.</title>',
    )
    t = t.replace(
        'content="trendtopia-store.com — Curated products. Useful design. Up to 50% off."',
        'content="trendtopia-store.com — Curated products. Useful design."',
    )
    path.write_text(t, encoding="utf-8", newline="\n")
    print("fixed home")


if __name__ == "__main__":
    for g in ("es", "pl", "gr"):
        fix_smartwatch(g)
    for g in ("pl", "cz", "sk"):
        fix_casa_fuego(g)
    fix_pl_terms()
    fix_home()
