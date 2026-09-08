#!/usr/bin/env python3
"""Post-audit cleanup for Casa Fuego ES/PL/SK/CZ."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REMOVE_LINES = [
    "<p>Opiniones de clientes en la sección de abajo.</p>",
    "<p>Opiniones de clientes en la sección de arriba.</p>",
    "<p>Opinie klientów w sekcji poniżej.</p>",
    "<p>Opinie klientów w sekcji powyżej.</p>",
    "<p>Recenzie zákazníkov v sekcii nižšie.</p>",
    "<p>Recenzie zákazníkov v sekcii vyššie.</p>",
    "<p>Hodnocení zákazníků v recenzích níže.</p>",
    "<p>Hodnocení zákazníků v recenzích výše.</p>",
]

REPLACEMENTS = [
    (
        "Reparte el calor de forma uniforme y es compatible",
        "Ayuda a distribuir el calor por la base y es compatible",
    ),
    (
        "Rovnomerne rozvádza teplo a je vhodná",
        "Pomáha rozvádzať teplo po dne a je vhodná",
    ),
    (
        "Rovnoměrně rozvádí teplo a je vhodná",
        "Pomáhá rozvádět teplo po dně a je vhodná",
    ),
    (
        "Równomiernie rozprowadza ciepło i pasuje",
        "Pomaga rozprowadzać ciepło po dnie i pasuje",
    ),
    (
        "Calienta de forma rápida y uniforme y es compatible con todas las fuentes de calor",
        "Se calienta con rapidez y es compatible con inducción, gas, vitrocerámica y placa eléctrica",
    ),
    (
        "<span class=\"cf-feature-badge\">Równomierne ciepło</span>",
        "<span class=\"cf-feature-badge\">Rozprowadzanie ciepła</span>",
    ),
    (
        "<span class=\"cf-feature-badge\">Rovnomerné teplo</span>",
        "<span class=\"cf-feature-badge\">Rozvod tepla</span>",
    ),
    (
        "<span class=\"cf-feature-badge\">Rovnoměrné teplo</span>",
        "<span class=\"cf-feature-badge\">Rozvod tepla</span>",
    ),
    (
        "Specjalnie wyprofilowana krawędź pomaga nalewać bez kapania, a ergonomiczne, odporne na ciepło uchwyty zapewniają wygodny i pewny chwyt.",
        "Specjalnie wyprofilowana krawędź ułatwia nalewanie; ergonomiczne uchwyty zapewniają wygodny chwyt — używaj ochrony, jeśli się nagrzewają.",
    ),
    ("</form>\n</div>\n</div>\n</section>", "</form>\n</div>\n</section>"),
]


def main() -> None:
    for geo in ("es", "pl", "sk", "cz"):
        path = ROOT / geo / "casa-fuego" / "landing.html"
        html = path.read_text(encoding="utf-8")
        for line in REMOVE_LINES:
            html = html.replace(line + "\n", "")
            html = html.replace(line, "")
        for old, new in REPLACEMENTS:
            html = html.replace(old, new)
        path.write_text(html, encoding="utf-8")
        print(f"Cleaned {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
