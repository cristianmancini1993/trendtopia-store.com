#!/usr/bin/env python3
"""Google Ads compliance audit patches for Casa Fuego ES/PL/SK/CZ landings."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEOS = ("es", "pl", "sk", "cz")

HIGHLIGHTS = {
    "es": {
        "title": "Lo que destaca del set",
        "items": [
            "Fondo de 5 capas que ayuda a distribuir el calor por la base.",
            "Acero inoxidable resistente a la corrosión.",
            "Tapas de cristal templado incluidas en las 6 piezas.",
            "Set completo de 6 piezas con tapas a juego (4 ollas, cacerola y sartén).",
        ],
    },
    "pl": {
        "title": "Co wyróżnia ten zestaw",
        "items": [
            "Dno 5-warstwowe, które pomaga rozprowadzać ciepło po dnie naczynia.",
            "Stal nierdzewna odporna na korozję.",
            "Pokrywki ze szkła hartowanego w każdym z 6 elementów.",
            "Kompletny zestaw 6 elementów z pasującymi pokrywkami (4 garnki, rondel i patelnia).",
        ],
    },
    "sk": {
        "title": "Čo vyniká na tejto súprave",
        "items": [
            "5-vrstvové dno, ktoré pomáha rozvádzať teplo po dne nádobia.",
            "Nehrdzavejúca oceľ odolná proti korózii.",
            "Pokrievky z tvrdeného skla pri každom z 6 kusov.",
            "Kompletná súprava 6 kusov so zladenými pokrievkami (4 hrnce, kastról a panvica).",
        ],
    },
    "cz": {
        "title": "Co vyniká u této sady",
        "items": [
            "5vrstvé dno, které pomáhá rozvádět teplo po dně nádobí.",
            "Nerezová ocel odolná proti korozi.",
            "Skleněné poklice u každého ze 6 dílů.",
            "Kompletní sada 6 dílů se sladěnými poklicemi (4 hrnce, rendlík a pánev).",
        ],
    },
}

COMPARE = {
    "es": {
        "title": "Información del producto Casa Fuego",
        "h1": "Aspecto",
        "h2": "Información del producto",
        "rows": [
            ("Producto", "Set de acero inoxidable de 6 piezas con tapas de cristal templado."),
            ("Fondo", "5 capas; ayuda a distribuir el calor por la base."),
            ("Compatibilidad", "Inducción, gas, vitrocerámica y placa eléctrica."),
            ("Tapas", "Cristal templado para controlar la cocción sin destapar."),
            ("Asas", "Ergonómicas, diseñadas para resistir el calor; usa protección si se calientan."),
            ("Contenido del set", "4 ollas, 1 cacerola y 1 sartén con tapas (ver detalle más abajo)."),
        ],
    },
    "pl": {
        "title": "Informacje o produkcie Casa Fuego",
        "h1": "Aspekt",
        "h2": "Informacja o produkcie",
        "rows": [
            ("Produkt", "Zestaw ze stali nierdzewnej, 6 elementów ze szklanymi pokrywkami."),
            ("Dno", "5-warstwowe; pomaga rozprowadzać ciepło po dnie naczynia."),
            ("Kompatybilność", "Indukcja, gaz, ceramika i płyta elektryczna."),
            ("Pokrywki", "Szkło hartowane do kontroli gotowania bez zdejmowania pokrywki."),
            ("Uchwyty", "Ergonomiczne, odporne na ciepło; używaj ochrony, jeśli się nagrzewają."),
            ("Zawartość zestawu", "4 garnki, rondel i patelnia z pokrywkami (szczegóły poniżej)."),
        ],
    },
    "sk": {
        "title": "Informácie o produkte Casa Fuego",
        "h1": "Aspekt",
        "h2": "Informácia o produkte",
        "rows": [
            ("Produkt", "Súprava z nehrdzavejúcej ocele, 6 kusov so sklenenými pokrievkami."),
            ("Dno", "5-vrstvové; pomáha rozvádzať teplo po dne nádobia."),
            ("Kompatibilita", "Indukcia, plyn, sklokeramika a elektrická platňa."),
            ("Pokrievky", "Tvrdené sklo na kontrolu varenia bez odkrývania."),
            ("Rukoväte", "Ergonomické, odolné proti teplu; pri dlhšom varení použite chňapku."),
            ("Obsah súpravy", "4 hrnce, kastról a panvica s pokrievkami (podrobnosti nižšie)."),
        ],
    },
    "cz": {
        "title": "Informace o produktu Casa Fuego",
        "h1": "Aspekt",
        "h2": "Informace o produktu",
        "rows": [
            ("Produkt", "Sada z nerezové oceli, 6 dílů se skleněnými poklicemi."),
            ("Dno", "5vrstvé; pomáhá rozvádět teplo po dně nádobí."),
            ("Kompatibilita", "Indukce, plyn, sklokeramika a elektrická deska."),
            ("Poklice", "Tvrzené sklo pro kontrolu vaření bez zvedání poklice."),
            ("Úchyty", "Ergonomické, odolné vůči teplu; při delším vaření použijte chňapku."),
            ("Obsah sady", "4 hrnce, rendlík a pánev s poklicemi (podrobnosti níže)."),
        ],
    },
}

CLAIMS = {
    "es": [
        (
            "Calor uniforme en toda la base: <span class=\"hl\">Casa Fuego</span> es un set de acero inoxidable con fondo de 5 capas",
            "Ayuda a distribuir el calor por la base: <span class=\"hl\">Casa Fuego</span> es un set de acero inoxidable con fondo de 5 capas",
        ),
        (
            "Set de 6 piezas con tapa que reparte el calor por toda la base gracias a su fondo de 5 capas — pensado para cocinar de forma uniforme en inducción, gas, vitrocerámica y placa eléctrica.",
            "Set de 6 piezas con tapa; el fondo de 5 capas ayuda a distribuir el calor por la base — compatible con inducción, gas, vitrocerámica y placa eléctrica.",
        ),
        ("Calienta de forma rápida y uniforme y retiene el calor", "Se calienta con rapidez y ayuda a retener el calor"),
        ("reparte el calor por toda la base para una cocción más uniforme", "ayuda a distribuir el calor por la base"),
        ("Borde anti-goteo:", "Borde para facilitar el vertido:"),
        ("el borde con forma especial ayuda a servir sin que gotee", "el borde con forma especial está diseñado para facilitar el vertido"),
        ("Borde anti-goteo y asas ergonómicas", "Borde para facilitar el vertido y asas ergonómicas"),
        ("alt=\"Borde anti-goteo y asas ergonómicas de Casa Fuego\"", "alt=\"Borde para facilitar el vertido y asas ergonómicas de Casa Fuego\""),
        ("<span class=\"cf-feature-badge\">Borde anti-goteo</span>", "<span class=\"cf-feature-badge\">Borde para vertido</span>"),
        (
            "El borde con forma especial ayuda a servir sin que gotee, y las asas ergonómicas y resistentes al calor ofrecen un agarre cómodo y seguro.",
            "El borde con forma especial está diseñado para facilitar el vertido; las asas ergonómicas ofrecen un agarre cómodo — usa protección si se calientan.",
        ),
        ("01 — Calor uniforme gracias al fondo de 5 capas", "01 — Fondo de 5 capas para distribuir el calor"),
        ("reparte el calor por toda la base", "ayuda a distribuir el calor por la base"),
        ("Calor uniforme</span>", "Distribución del calor</span>"),
        ("para una mejor distribución del calor", "que ayuda a distribuir el calor por la base"),
        ("con forma especial que ayuda a servir sin goteo", "con forma especial diseñado para facilitar el vertido"),
    ],
    "pl": [
        (
            "Równomierne ciepło na całym dnie: <span class=\"hl\">Casa Fuego</span> to zestaw ze stali nierdzewnej z dnem 5-warstwowym",
            "Pomaga rozprowadzać ciepło po dnie: <span class=\"hl\">Casa Fuego</span> to zestaw ze stali nierdzewnej z dnem 5-warstwowym",
        ),
        (
            "który dzięki 5-warstwowemu dnu rozprowadza ciepło po całej powierzchni — do równomiernego gotowania na indukcji, gazie, ceramice i płycie elektrycznej.",
            "z pokrywką; dno 5-warstwowe pomaga rozprowadzać ciepło po dnie — kompatybilny z indukcją, gazem, ceramiką i płytą elektryczną.",
        ),
        ("Szybko i równomiernie się nagrzewa", "Szybko się nagrzewa i pomaga utrzymać ciepło"),
        ("rozprowadza ciepło po całej powierzchni dna dla równiejszego gotowania", "pomaga rozprowadzać ciepło po dnie naczynia"),
        ("Krawędź zapobiegająca kapaniu:", "Krawędź ułatwiająca nalewanie:"),
        ("specjalnie wyprofilowana, by nalewać bez kapania", "specjalnie wyprofilowana, aby ułatwić nalewanie"),
        ("Krawędź bez kapania i ergonomiczne uchwyty", "Krawędź ułatwiająca nalewanie i ergonomiczne uchwyty"),
        ("Krawędź bez kapania", "Krawędź do nalewania"),
        (
            "Specjalnie wyprofilowana krawędź ułatwia nalewanie bez kapania, a ergonomiczne uchwyty odporne na ciepło zapewniają wygodny chwyt.",
            "Specjalnie wyprofilowana krawędź ułatwia nalewanie; ergonomiczne uchwyty zapewniają wygodny chwyt — używaj ochrony, jeśli się nagrzewają.",
        ),
        ("01 — Równomierne ciepło dzięki dnu 5-warstwowemu", "01 — Dno 5-warstwowe do rozprowadzania ciepła"),
        ("dla lepszego rozprowadzania ciepła", "pomagające rozprowadzać ciepło po dnie"),
        ("ułatwia nalewanie bez kapania", "ułatwia nalewanie"),
    ],
    "sk": [
        (
            "Rovnomerné teplo po celom dne: <span class=\"hl\">Casa Fuego</span> je súprava z nehrdzavejúcej ocele s 5-vrstvovým dnom",
            "Pomáha rozvádzať teplo po dne: <span class=\"hl\">Casa Fuego</span> je súprava z nehrdzavejúcej ocele s 5-vrstvovým dnom",
        ),
        (
            "ktorá vďaka 5-vrstvovému dnu rozvádza teplo po celej ploche — na rovnomerné varenie na indukcii, plyne, sklokeramike a elektrickej platni.",
            "s pokrievkou; 5-vrstvové dno pomáha rozvádzať teplo po dne — vhodná na indukciu, plyn, sklokeramiku a elektrickú platňu.",
        ),
        ("Rýchlo a rovnomerne sa zohreje", "Rýchlo sa zohreje a pomáha udržať teplo"),
        ("rozvádza teplo po celej ploche dna pre rovnomernejšie varenie", "pomáha rozvádzať teplo po dne nádobia"),
        ("Okraj proti kvapkaniu:", "Okraj na uľahčenie nalievania:"),
        ("Okraj proti kvapkaniu", "Okraj na nalievanie"),
        (
            "Špeciálne tvarovaný okraj pomáha nalievať bez kvapkania a ergonomické rukoväte odolné proti teplu ponúkajú pohodlný a jistý úchop.",
            "Špeciálne tvarovaný okraj uľahčuje nalievanie; ergonomické rukoväte ponúkajú pohodlný úchop — pri dlhšom varení použite chňapku.",
        ),
        ("01 — Rovnomerné teplo vďaka 5-vrstvovému dnu", "01 — 5-vrstvové dno na rozvod tepla"),
        ("pre lepšie rozvádzanie tepla", "pomáhajúce rozvádzať teplo po dne"),
        ("uľahčuje nalievanie bez kvapkania", "uľahčuje nalievanie"),
    ],
    "cz": [
        (
            "Rovnoměrné teplo po celém dně: <span class=\"hl\">Casa Fuego</span> je sada z nerezové oceli s 5vrstvým dnem",
            "Pomáhá rozvádět teplo po dně: <span class=\"hl\">Casa Fuego</span> je sada z nerezové oceli s 5vrstvým dnem",
        ),
        (
            "která díky 5vrstvému dnu rozvádí teplo po celém povrchu — pro rovnoměrné vaření na indukci, plynu, sklokeramice a elektrické desce.",
            "se skleněnými poklicemi; 5vrstvé dno pomáhá rozvádět teplo po dně — vhodná pro indukci, plyn, sklokeramiku a elektrickou desku.",
        ),
        ("Rychle a rovnoměrně se zahřeje", "Rychle se zahřeje a pomáhá udržet teplo"),
        ("rozvádí teplo po celém dně pro rovnoměrnější vaření", "pomáhá rozvádět teplo po dně nádobí"),
        ("Hrana proti kapání:", "Hrana pro usnadnění nalévání:"),
        ("Hrana proti kapání", "Hrana pro nalévání"),
        (
            "Speciálně tvarovaná hrana pomáhá nalévat bez kapání a ergonomické úchyty odolné vůči teplu nabízejí pohodlný a jistý úchop.",
            "Speciálně tvarovaná hrana usnadňuje nalévání; ergonomické úchyty nabízejí pohodlný úchop — při delším vaření použijte chňapku.",
        ),
        ("01 — Rovnoměrné teplo díky 5vrstvému dnu", "01 — 5vrstvé dno pro rozvod tepla"),
        ("pro lepší rozvod tepla", "pomáhající rozvádět teplo po dně"),
        ("usnadňuje nalévání bez kapání", "usnadňuje nalévání"),
    ],
}

REVIEW_TITLES = {
    "es": "Lo que dicen quienes ya cocinan con Casa Fuego",
    "pl": "Co mówią osoby, które już gotują z Casa Fuego",
    "sk": "Čo hovoria tí, ktorí už varia s Casa Fuego",
    "cz": "Co říkají ti, kdo už vaří s Casa Fuego",
}

VS_TITLES = {
    "es": "Casa Fuego vs. una batería tradicional",
    "pl": "Casa Fuego a tradycyjne garnki",
    "sk": "Casa Fuego vs. tradičné hrnce",
    "cz": "Casa Fuego vs. tradiční hrnce",
}

HIGHLIGHTS_CSS = """
/* ---------- DESTACADOS FACTUALES ---------- */
.cf-highlights{max-width:680px;margin:0 auto;background:var(--cf-light);border-radius:16px;padding:24px 26px}
.cf-highlights li{list-style:none;padding:10px 0;border-bottom:1px solid #ece0d8;font-size:15px;display:flex;gap:10px;align-items:flex-start;line-height:1.55;color:var(--cf-gray)}
.cf-highlights li:last-child{border-bottom:none}
.cf-highlights li::before{content:"•";color:var(--cf-orange);font-weight:800;font-size:18px;flex:0 0 auto;line-height:1.2}
"""

COMPARE_CSS_OLD = """.cf-compare td:first-child{color:var(--cf-red)}
.cf-compare td:last-child{color:var(--cf-orange-dark);font-weight:600;background:#fff8f4}"""

COMPARE_CSS_NEW = """.cf-compare td:first-child{color:var(--cf-dark);font-weight:600;width:34%;vertical-align:top}
.cf-compare td:last-child{color:var(--cf-gray);font-weight:400;background:#fff;vertical-align:top}"""


def cta_label(geo: str) -> str:
    return {
        "es": "Pedir Casa Fuego",
        "pl": "Zamów Casa Fuego",
        "sk": "Objednať Casa Fuego",
        "cz": "Objednat Casa Fuego",
    }[geo]


def build_highlights(geo: str) -> str:
    h = HIGHLIGHTS[geo]
    items = "\n".join(f"<li>{x}</li>" for x in h["items"])
    return (
        f'<h2 class="cf-section-title">{h["title"]}</h2>\n'
        f'<ul class="cf-highlights">\n{items}\n</ul>\n'
        f'<div class="cf-cta-wrap"><a class="cf-cta" href="#cf-formulario">{cta_label(geo)}</a></div>'
    )


def build_compare(geo: str) -> str:
    c = COMPARE[geo]
    rows = "\n".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in c["rows"])
    return (
        f'<h2 class="cf-section-title">{c["title"]}</h2>\n'
        f'<table class="cf-compare">\n'
        f'<tr><th>{c["h1"]}</th><th>{c["h2"]}</th></tr>\n{rows}\n</table>\n'
        f'<div class="cf-cta-wrap"><a class="cf-cta" href="#cf-formulario">{cta_label(geo)}</a></div>'
    )


def patch_css(html: str) -> str:
    html = re.sub(
        r"/\* ---------- ESTRELLAS ---------- \*/\s*\.cf-stars\{.*?\}\s*\.cf-stars \.rev\{.*?\}\s*",
        "",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"\.cf-social-proof\{.*?\}\s*\.cf-social-proof \.num\{.*?\}\s*\.cf-social-proof small\{.*?\}\s*",
        "",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"/\* ---------- OPINIONES ---------- \*/\s*\.cf-reviews\{.*?\}\s*\.cf-review p\{.*?\}\s*",
        "",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(r"  \.cf-stars\{justify-content:flex-start\}\s*", "", html)
    html = re.sub(
        r"  \.cf-review\{flex-direction:column;.*?\}\s*"
        r"  \.cf-review img\{.*?\}\s*"
        r"  \.cf-review > div\{.*?\}\s*"
        r"  \.cf-review \.rv-name,\.cf-review \.rv-stars\{.*?\}\s*",
        "",
        html,
        flags=re.DOTALL,
    )
    if ".cf-highlights{" not in html:
        html = html.replace(
            "/* ---------- TABLA COMPARATIVA ---------- */",
            HIGHLIGHTS_CSS + "\n/* ---------- TABLA COMPARATIVA ---------- */",
            1,
        )
    html = html.replace(COMPARE_CSS_OLD, COMPARE_CSS_NEW)
    return html


def patch_html(html: str, geo: str) -> str:
    html = re.sub(r"\s*<div class=\"cf-stars\">.*?</div>\s*", "\n", html, flags=re.DOTALL)
    html = re.sub(r"\s*<div class=\"cf-social-proof\">.*?</div>\s*", "\n", html, flags=re.DOTALL)

    rt = REVIEW_TITLES[geo]
    html = re.sub(
        rf"<h2 class=\"cf-section-title\">{re.escape(rt)}</h2>\s*<div class=\"cf-reviews\">.*?</div>\s*"
        rf"<div class=\"cf-cta-wrap\"><a class=\"cf-cta\" href=\"#cf-formulario\">{re.escape(cta_label(geo))}</a></div>",
        build_highlights(geo),
        html,
        count=1,
        flags=re.DOTALL,
    )

    vt = VS_TITLES[geo]
    html = re.sub(
        rf"<h2 class=\"cf-section-title\">{re.escape(vt)}</h2>\s*<table class=\"cf-compare\">.*?</table>\s*"
        rf"<div class=\"cf-cta-wrap\"><a class=\"cf-cta\" href=\"#cf-formulario\">{re.escape(cta_label(geo))}</a></div>",
        build_compare(geo),
        html,
        count=1,
        flags=re.DOTALL,
    )

    for old, new in CLAIMS.get(geo, []):
        html = html.replace(old, new)

    return html


def audit_file(path: Path) -> None:
    geo = path.parent.parent.name
    html = path.read_text(encoding="utf-8")
    html = patch_css(html)
    html = patch_html(html, geo)
    path.write_text(html, encoding="utf-8")
    print(f"Patched {path.relative_to(ROOT)}")


def main() -> None:
    for geo in GEOS:
        audit_file(ROOT / geo / "casa-fuego" / "landing.html")


if __name__ == "__main__":
    main()
