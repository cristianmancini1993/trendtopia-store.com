#!/usr/bin/env python3
"""Deploy Casa Fuego stainless 6-piece landings from Downloads with compliance fixes."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DL = Path.home() / "Downloads"

PRIVACY_CSS = """
.cf-sold-by{text-align:center;font-size:12px;color:var(--cf-gray);margin:8px 0 0;padding:0 24px}
.cf-form-privacy{text-align:center;font-size:13px;color:var(--cf-gray);margin-bottom:10px;max-width:520px;margin-left:auto;margin-right:auto}
.cf-form-privacy a{color:var(--cf-orange-dark);text-decoration:underline}"""


def strip_comments(html: str) -> str:
    return re.sub(r"<!-- IMPORTANTE:[^>]*-->\s*", "", html)


def fix_common(html: str) -> str:
    html = strip_comments(html)
    if ".cf-form-privacy{" not in html:
        html = html.replace(
            ".cf-hero-img img{width:100%;aspect-ratio:1/1;object-fit:cover}",
            ".cf-hero-img img{width:100%;aspect-ratio:1/1;object-fit:cover}" + PRIVACY_CSS,
            1,
        )
    return html


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


# ES
es = fix_common((DL / "landing-es.html").read_text(encoding="utf-8"))
es = es.replace(
    '<div class="cf-topbar">OFERTA: envío rápido · pago contra reembolso · devolución en 30 días</div>',
    '<div class="cf-topbar">Envío rápido · Pago contra reembolso · Devolución 30 días</div>',
)
es = es.replace(">PEDIR CASA FUEGO<", ">Pedir Casa Fuego<")
es = es.replace(
    '<h2>Rellena tus datos y pide Casa Fuego</h2>\n<form class="cf-form',
    '<h2>Rellena tus datos y pide Casa Fuego</h2>\n'
    '<p class="cf-form-privacy">Al enviar el formulario aceptas el tratamiento de tus datos para gestionar el pedido. '
    'Consulta la <a href="/es/privacy-policy.html">Política de privacidad</a>.</p>\n'
    '<p class="sub">Haz tu pedido y <strong>paga cómodamente contra reembolso.</strong></p>\n'
    '<form class="cf-form',
    1,
)
es = es.replace(
    '\n<p class="sub">Haz tu pedido y <strong>paga cómodamente contra reembolso.</strong></p>\n'
    '<div class="cf-social-proof">\n<div class="cf-stars" style="justify-content:center"><span class="star">★★★★★</span></div>\n'
    '<p>Opiniones de clientes en la sección de abajo.</p>',
    '\n<div class="cf-social-proof">\n<div class="cf-stars" style="justify-content:center"><span class="star">★★★★★</span></div>\n'
    '<p>Opiniones de clientes en la sección de abajo.</p>',
    1,
)
es = es.replace(
    '<h2>Rellena tus datos y pide Casa Fuego</h2>\n'
    '<p class="sub">Haz tu pedido y <strong>paga cómodamente contra reembolso.</strong></p>\n'
    '<form class="cf-form tm-order-form"',
    '<h2>Rellena tus datos y pide Casa Fuego</h2>\n'
    '<p class="cf-form-privacy">Al enviar el formulario aceptas el tratamiento de tus datos para gestionar el pedido. '
    'Consulta la <a href="/es/privacy-policy.html">Política de privacidad</a>.</p>\n'
    '<p class="sub">Haz tu pedido y <strong>paga cómodamente contra reembolso.</strong></p>\n'
    '<form class="cf-form tm-order-form"',
    1,
)
write(ROOT / "es/casa-fuego/landing.html", es)

# PL
pl = fix_common((DL / "landing-pl.html").read_text(encoding="utf-8"))
pl = pl.replace(
    '<div class="cf-topbar">OFERTA: szybka dostawa · płatność przy odbiorze · zwrot w 30 dni</div>',
    '<div class="cf-topbar">Darmowa dostawa · Płatność przy odbiorze · Zwrot 30 dni</div>',
)
pl = pl.replace(">ZAMÓW CASA FUEGO<", ">Zamów Casa Fuego<")
pl = pl.replace(
    "  PRODUCT_SLUG: 'casa-fuego',",
    "  PRODUCT_SLUG: 'casa-fuego',\n"
    "  CURRENCY: 'PLN',\n"
    "  PRICE: 399.0,\n"
    "  GOOGLE_ADS_CONVERSION_SEND_TO: 'AW-18327321473/S692CKfLieocEIH3kqNE',\n"
    "  CONVERSION_VALUE: 399.0,\n"
    "  CONVERSION_CURRENCY: 'PLN',",
)
pl = pl.replace(
    '<h2>Podaj dane i zamów Casa Fuego</h2>\n<form class="cf-form',
    '<h2>Podaj dane i zamów Casa Fuego</h2>\n'
    '<p class="cf-form-privacy">Wysyłając formularz, wyrażasz zgodę na przetwarzanie danych w celu obsługi zamówienia. '
    'Zobacz <a href="/pl/privacy-policy.html">Politykę prywatności</a>.</p>\n'
    '<p class="sub">Złóż zamówienie i <strong>wygodnie zapłać przy odbiorze.</strong></p>\n'
    '<form class="cf-form',
    1,
)
pl = pl.replace(
    '\n<p class="sub">Złóż zamówienie i <strong>wygodnie zapłać przy odbiorze.</strong></p>\n'
    '<div class="cf-social-proof">\n<div class="cf-stars" style="justify-content:center"><span class="star">★★★★★</span></div>\n'
    '<p>Opinie klientów w sekcji poniżej.</p>',
    '\n<div class="cf-social-proof">\n<div class="cf-stars" style="justify-content:center"><span class="star">★★★★★</span></div>\n'
    '<p>Opinie klientów w sekcji poniżej.</p>',
    1,
)
pl = pl.replace(
    '<h2>Podaj dane i zamów Casa Fuego</h2>\n'
    '<p class="sub">Złóż zamówienie i <strong>wygodnie zapłać przy odbiorze.</strong></p>\n'
    '<form class="cf-form tm-order-form"',
    '<h2>Podaj dane i zamów Casa Fuego</h2>\n'
    '<p class="cf-form-privacy">Wysyłając formularz, wyrażasz zgodę na przetwarzanie danych w celu obsługi zamówienia. '
    'Zobacz <a href="/pl/privacy-policy.html">Politykę prywatności</a>.</p>\n'
    '<p class="sub">Złóż zamówienie i <strong>wygodnie zapłać przy odbiorze.</strong></p>\n'
    '<form class="cf-form tm-order-form"',
    1,
)
write(ROOT / "pl/casa-fuego/landing.html", pl)

# SK
sk = fix_common((DL / "landing-sk.html").read_text(encoding="utf-8"))
sk = sk.replace(
    '<div class="cf-topbar">PONUKA: rýchle doručenie · platba pri prevzatí · vrátenie do 30 dní</div>',
    '<div class="cf-topbar">Bezplatné doručenie · Platba pri prevzatí · Vrátenie 30 dní</div>',
)
sk = sk.replace(">OBJEDNAŤ CASA FUEGO<", ">Objednať Casa Fuego<")
sk = sk.replace(
    '<h2>Zadajte údaje a objednajte Casa Fuego</h2>\n<form class="cf-form',
    '<h2>Zadajte údaje a objednajte Casa Fuego</h2>\n'
    '<p class="cf-form-privacy">Odoslaním formulára súhlasíte so spracovaním údajov na vybavenie objednávky. '
    'Pozrite <a href="/sk/privacy-policy.html">Zásady ochrany osobných údajov</a>.</p>\n'
    '<p class="sub">Objednajte a <strong>pohodlne zaplaťte pri prevzatí.</strong></p>\n'
    '<form class="cf-form',
    1,
)
sk = sk.replace(
    '\n<p class="sub">Objednajte a <strong>pohodlne zaplaťte pri prevzatí.</strong></p>\n'
    '<div class="cf-social-proof">\n<div class="cf-stars" style="justify-content:center"><span class="star">★★★★★</span></div>\n'
    '<p>Recenzie zákazníkov v sekcii nižšie.</p>',
    '\n<div class="cf-social-proof">\n<div class="cf-stars" style="justify-content:center"><span class="star">★★★★★</span></div>\n'
    '<p>Recenzie zákazníkov v sekcii nižšie.</p>',
    1,
)
sk = sk.replace(
    '<h2>Zadajte údaje a objednajte Casa Fuego</h2>\n'
    '<p class="sub">Objednajte a <strong>pohodlne zaplaťte pri prevzatí.</strong></p>\n'
    '<form class="cf-form tm-order-form"',
    '<h2>Zadajte údaje a objednajte Casa Fuego</h2>\n'
    '<p class="cf-form-privacy">Odoslaním formulára súhlasíte so spracovaním údajov na vybavenie objednávky. '
    'Pozrite <a href="/sk/privacy-policy.html">Zásady ochrany osobných údajov</a>.</p>\n'
    '<p class="sub">Objednajte a <strong>pohodlne zaplaťte pri prevzatí.</strong></p>\n'
    '<form class="cf-form tm-order-form"',
    1,
)
write(ROOT / "sk/casa-fuego/landing.html", sk)

# CZ from SK with Czech copy + AdRice IDs
cz_pairs = [
    ('lang="sk"', 'lang="cs"'),
    ("/sk/", "/cz/"),
    ("sk_SK", "cs_CZ"),
    ("GEO: 'sk'", "GEO: 'cz'"),
    (
        "Súprava z nehrdzavejúcej ocele 6 kusov | platba pri prevzatí",
        "Sada z nerezové oceli 6 dílů | platba na dobírku",
    ),
    (
        "kuchynská súprava z nehrdzavejúcej ocele, 6 kusov s pokrievkou z tvrdeného skla a 5-vrstvovým dnom. "
        "Rovnomerne rozvádza teplo a je vhodná pre indukciu, plyn, sklokeramiku a elektrické platne. Platba pri prevzatí.",
        "kuchyňská sada z nerezové oceli, 6 dílů se skleněnými poklicemi a 5vrstvým dnem. "
        "Rovnoměrně rozvádí teplo a je vhodná pro indukci, plyn, sklokeramiku a elektrické desky. Platba na dobírku.",
    ),
    (
        '<div class="cf-topbar">Bezplatné doručenie · Platba pri prevzatí · Vrátenie 30 dní</div>',
        '<div class="cf-topbar">Doručení zdarma · Platba na dobírku · Vrácení 30 dní</div>',
    ),
    (
        'ROVNOMERNÉ TEPLO PO CELOM DNE: <span class="hl">CASA FUEGO</span> JE SÚPRAVA Z NEHRDZAVEJÚCEJ OCELE S 5-VRSTVOVÝM DNOM',
        'Rovnoměrné teplo po celém dně: <span class="hl">Casa Fuego</span> je sada z nerezové oceli s 5vrstvým dnem',
    ),
    (
        "Súprava 6 kusov s pokrievkou, ktorá vďaka 5-vrstvovému dnu rozvádza teplo po celej ploche — "
        "na rovnomerné varenie na indukcii, plyne, sklokeramike a elektrickej platni.",
        "Sada 6 dílů s poklicí, která díky 5vrstvému dnu rozvádí teplo po celém povrchu — "
        "pro rovnoměrné vaření na indukci, plynu, sklokeramice a elektrické desce.",
    ),
    ("Nehrdzavejúca oceľ odolná proti korózii.", "Nerezová ocel odolná proti korozi."),
    (
        "Rýchlo a rovnomerne sa zohreje a dlhšie udrží teplo, čo zaisťuje trvácny výkon každý deň.",
        "Rychle a rovnoměrně se zahřeje a déle udrží teplo pro každodenní použití.",
    ),
    ("Kompletná súprava Casa Fuego z nehrdzavejúcej ocele", "Kompletní sada Casa Fuego z nerezové oceli"),
    ("5-vrstvové dno:", "5vrstvé dno:"),
    ("rozvádza teplo po celej ploche dna pre rovnomernejšie varenie.", "rozvádí teplo po celém dně pro rovnoměrnější vaření."),
    ("Kvalitná nehrdzavejúca oceľ:", "Kvalitní nerezová ocel:"),
    ("odolná proti korózii a trvácna.", "odolná proti korozi a trvanlivá."),
    ("Vhodná pre všetky zdroje tepla:", "Vhodná pro všechny zdroje tepla:"),
    ("indukcia, plyn, sklokeramika a elektrická platňa.", "indukce, plyn, sklokeramika a elektrická deska."),
    ("Pokrievky z tvrdeného skla:", "Skleněné poklice:"),
    ("kontrolujte varenie bez odkrývania.", "kontrolujte vaření bez zvedání poklice."),
    ("Okraj proti kvapkaniu:", "Hrana proti kapání:"),
    ("špeciálne tvarovaný okraj na nalievanie bez kvapkania.", "speciálně tvarovaná hrana pro nalévání bez kapání."),
    ("Ergonomické rukoväte odolné proti teplu:", "Ergonomické úchyty odolné vůči teplu:"),
    ("pohodlný a bezpečný úchop.", "pohodlný a jistý úchop."),
    ("Súprava 6 kusov s pokrievkou:", "Sada 6 dílů s poklicí:"),
    ("4 hrnce, kastról a panvica na každý deň.", "4 hrnce, rendlík a pánev na každý den."),
    ("89,00 €", "1 999 Kč"),
    (">Objednať Casa Fuego<", ">Objednat Casa Fuego<"),
    ("Predáva trendtopia-store.com", "Prodává trendtopia-store.com"),
    ("Zadajte údaje a objednajte Casa Fuego", "Zadejte údaje a objednejte Casa Fuego"),
    (
        'Odoslaním formulára súhlasíte so spracovaním údajov na vybavenie objednávky. '
        'Pozrite <a href="/cz/privacy-policy.html">Zásady ochrany osobných údajov</a>.',
        'Odesláním formuláře souhlasíte se zpracováním údajů za účelem vyřízení objednávky. '
        'Viz <a href="/cz/privacy-policy.html">Zásady ochrany osobních údajů</a>.',
    ),
    (
        "Objednajte a <strong>pohodlne zaplaťte pri prevzatí.</strong>",
        "Objednejte a <strong>pohodlně plaťte na dobírku.</strong>",
    ),
    ("Meno a priezvisko", "Jméno a příjmení"),
    ("Objednať teraz", "Objednat nyní"),
    ('value="3702"', 'value="3251"'),
    ('value="3742"', 'value="3285"'),
    ("c9fb0b2bbaca32e82d72fae2741f14e4a388647a", "0af7749e1e5ae84ab4405c78558227e061a30b80"),
    ("Recenzie zákazníkov v sekcii nižšie.", "Hodnocení zákazníků v recenzích níže."),
    ("Tri dôvody, prečo si vybrať Casa Fuego", "Tři důvody, proč zvolit Casa Fuego"),
    ("5-vrstvové dno Casa Fuego", "5vrstvé dno Casa Fuego"),
    ("Nehrdzavejúca oceľ Casa Fuego", "Nerezová ocel Casa Fuego"),
    ("Okraj proti kvapkaniu a ergonomické rukoväte Casa Fuego", "Hrana proti kapání a ergonomické úchyty Casa Fuego"),
    ("Recenzie zákazníkov v sekcii vyššie.", "Hodnocení zákazníků v recenzích výše."),
    (
        "COOKIE_TEXT: 'Používame súbory cookie na zlepšenie fungovania stránky a analýzu návštevnosti.'",
        "COOKIE_TEXT: 'Používáme technické soubory cookie a soubory cookie třetích stran pro zlepšení vašeho zážitku a analytiku.'",
    ),
    ("COOKIE_ACCEPT: 'Súhlasím'", "COOKIE_ACCEPT: 'Přijmout'"),
    ("COOKIE_ACCEPT_ALL: 'Prijať všetko'", "COOKIE_ACCEPT_ALL: 'Přijmout vše'"),
    ("COOKIE_REJECT: 'Odmietnuť nepodstatné'", "COOKIE_REJECT: 'Odmítnout nepodstatné'"),
    ("COOKIE_MANAGE: 'Spravovať predvoľby'", "COOKIE_MANAGE: 'Spravovat preference'"),
    ("COOKIE_SAVE: 'Uložiť predvoľby'", "COOKIE_SAVE: 'Uložit preference'"),
    ("COOKIE_CHANGE: 'Zmeniť nastavenia cookies'", "COOKIE_CHANGE: 'Změnit nastavení souborů cookie'"),
    ("COOKIE_LEARN: 'Zistiť viac'", "COOKIE_LEARN: 'Více informací'"),
]
cz = sk
for old, new in cz_pairs:
    cz = cz.replace(old, new)
cz = cz.replace("name: 'Zadajte meno a priezvisko.'", "name: 'Vyplňte prosím jméno a příjmení.'")
cz = cz.replace("address: 'Zadajte adresu.'", "address: 'Vyplňte prosím adresu.'")
cz = cz.replace("tel: 'Zadajte platné telefónne číslo.'", "tel: 'Zadejte platné telefonní číslo.'")
cz = cz.replace(
    "generic: 'Objednávku sa nepodarilo odoslať. Skúste to znova.'",
    "generic: 'Objednávku se nepodařilo odeslat. Zkuste to prosím znovu.'",
)
cz = cz.replace("submitting: 'Odosielanie…'", "submitting: 'Odesílání…'")
write(ROOT / "cz/casa-fuego/landing.html", cz)
