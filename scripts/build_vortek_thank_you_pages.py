"""Generate Vortek thank-you pages from locale templates (Iron Oak Pro)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SPECS = [
    {
        "template": ROOT / "es/glacierair-1415/thank-you.html",
        "dest": ROOT / "es/vortek-1013/thank-you.html",
        "replacements": [
            ("glacierair-1415", "vortek-1013"),
            ("GlacierAir™", "Iron Oak Pro™"),
            ("PRICE: 99.0", "PRICE: 69.0"),
            ("trackPurchase(99.0, 'EUR')", "trackPurchase(69.0, 'EUR')"),
            (
                "Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.",
                "Perfecto — tu pedido <strong>Iron Oak Pro™</strong> está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.",
            ),
            ('GOOGLE_TAG_ID: \'\'', "GOOGLE_TAG_ID: 'AW-18327321473'"),
            ('meta name="theme-color" content="#16a34a"', 'meta name="theme-color" content="#201c18"'),
            ("<li><a href=\"/es/about-us.html\">Sobre nosotros</a></li>", "<li><a href=\"/es/about-us.html\">Quiénes somos</a></li>"),
            ("<li><a href=\"/es/contact-us.html\">Contáctanos</a></li>", "<li><a href=\"/es/contact-us.html\">Contacto</a></li>"),
        ],
    },
    {
        "template": ROOT / "lt/casa-fuego/thank-you.html",
        "dest": ROOT / "lt/vortek-1427/thank-you.html",
        "replacements": [
            ("casa-fuego", "vortek-1427"),
            ("Casa Fuego™", "Iron Oak Pro™"),
            ("PRICE: 89.0", "PRICE: 64.0"),
            ("trackPurchase(89.0, 'EUR')", "trackPurchase(64.0, 'EUR')"),
            (
                "Puiku — jūsų užsakymas apdorojamas. Liko tik <strong>paskutinis žingsnis</strong>, kad jį užbaigtumėte ir pradėtumėte siuntimą.",
                "Puiku — jūsų <strong>Iron Oak Pro™</strong> užsakymas apdorojamas. Liko tik <strong>paskutinis žingsnis</strong>, kad jį užbaigtumėte ir pradėtumėte siuntimą.",
            ),
            ('GOOGLE_TAG_ID: \'\'', "GOOGLE_TAG_ID: 'AW-18327321473'"),
            ('meta name="theme-color" content="#16a34a"', 'meta name="theme-color" content="#201c18"'),
        ],
    },
    {
        "template": ROOT / "pl/glacierair-3297/thank-you.html",
        "dest": ROOT / "pl/vortek-1429/thank-you.html",
        "replacements": [
            ("glacierair-3297", "vortek-1429"),
            ("GlacierAir™", "Iron Oak Pro™"),
            ("PRICE: 419.0", "PRICE: 299.0"),
            ("trackPurchase(419.0, 'PLN')", "trackPurchase(299.0, 'PLN')"),
            (
                "Świetnie — Twoje zamówienie jest przetwarzane. Pozostał już tylko <strong>ostatni krok</strong> do jego ukończenia i wysyłki.",
                "Świetnie — Twoje zamówienie <strong>Iron Oak Pro™</strong> jest przetwarzane. Pozostał już tylko <strong>ostatni krok</strong> do jego ukończenia i wysyłki.",
            ),
            ('GOOGLE_TAG_ID: \'\'', "GOOGLE_TAG_ID: 'AW-18327321473'"),
            ('meta name="theme-color" content="#16a34a"', 'meta name="theme-color" content="#201c18"'),
        ],
    },
    {
        "template": ROOT / "lv/glacierair-4243/thank-you.html",
        "dest": ROOT / "lv/vortek-3518/thank-you.html",
        "replacements": [
            ("glacierair-4243", "vortek-3518"),
            ("GlacierAir™", "Iron Oak Pro™"),
            ("PRICE: 99.0", "PRICE: 79.0"),
            ("trackPurchase(99.0, 'EUR')", "trackPurchase(79.0, 'EUR')"),
            (
                "Lieliski — jūsu pasūtījums tiek apstrādāts. Atlicis tikai <strong>pēdējais solis</strong>, lai to pabeigtu un sāktu piegādi.",
                "Lieliski — jūsu <strong>Iron Oak Pro™</strong> pasūtījums tiek apstrādāts. Atlicis tikai <strong>pēdējais solis</strong>, lai to pabeigtu un sāktu piegādi.",
            ),
            ('GOOGLE_TAG_ID: \'\'', "GOOGLE_TAG_ID: 'AW-18327321473'"),
            ('meta name="theme-color" content="#16a34a"', 'meta name="theme-color" content="#201c18"'),
        ],
    },
]


def main() -> None:
    for spec in SPECS:
        html = spec["template"].read_text(encoding="utf-8")
        for old, new in spec["replacements"]:
            if old not in html:
                raise SystemExit(f"missing pattern in {spec['template']}: {old!r}")
            html = html.replace(old, new)
        spec["dest"].write_text(html, encoding="utf-8", newline="\n")
        print("wrote", spec["dest"].relative_to(ROOT))


if __name__ == "__main__":
    main()
