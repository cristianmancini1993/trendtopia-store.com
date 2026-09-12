#!/usr/bin/env python3
"""Align */about-us.html 'by the numbers' blocks with en/about-us.html (3 factual bullets)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (h2 title exactly as in file, ul inner HTML for 3 bullets — matches en structure)
NUMBERS_BLOCKS = {
    "en": (
        "By the numbers",
        """
      <li><strong>18 European countries</strong> served with 24-48h delivery</li>
      <li><strong>30-day refund</strong> guaranteed (beyond the 14 days required by EU law)</li>
      <li><strong>24-month legal warranty</strong> on every product</li>""",
    ),
    "es": (
        "Por los números",
        """
<li><strong>18 países europeos</strong> con entrega en 24-48 h</li>
<li><strong>Devolución de 30 días</strong> garantizada (más allá de los 14 días exigidos por la ley de la UE)</li>
<li><strong>Garantía legal de 24 meses</strong> en cada producto</li>""",
    ),
    "pl": (
        "Według liczb",
        """
<li><strong>18 krajów europejskich</strong> z dostawą w 24–48 h</li>
<li><strong>30-dniowy zwrot</strong> gwarantowany (ponad 14 dni wymaganych przez prawo UE)</li>
<li><strong>24-miesięczna gwarancja prawna</strong> na każdy produkt</li>""",
    ),
    "gr": (
        "Με τους αριθμούς",
        """
<li><strong>18 ευρωπαϊκές χώρες</strong> με παράδοση 24–48 ώρες</li>
<li><strong>Επιστροφή χρημάτων 30 ημερών</strong> (πέρα από τις 14 ημέρες που απαιτεί η νομοθεσία της ΕΕ)</li>
<li><strong>Νομική εγγύηση 24 μηνών</strong> σε κάθε προϊόν</li>""",
    ),
    "sk": (
        "Podľa čísel",
        """
<li><strong>18 európskych krajín</strong> s doručením do 24–48 hodín</li>
<li><strong>30-dňové vrátenie peňazí</strong> (nad rámec 14 dní podľa práv EÚ)</li>
<li><strong>24-mesačná zákonná záruka</strong> na každý produkt</li>""",
    ),
    "cz": (
        "Podle čísel",
        """
<li><strong>18 evropských zemí</strong> s doručením do 24–48 hodin</li>
<li><strong>30denní vrácení peněz</strong> (nad rámec 14 dní dle práva EU)</li>
<li><strong>24měsíční zákonná záruka</strong> na každý produkt</li>""",
    ),
    "de": (
        "Anhand der Zahlen",
        """
<li><strong>18 europäische Länder</strong> mit Lieferung in 24–48 Stunden</li>
<li><strong>30 Tage Rückerstattung</strong> (über die 14 Tage der EU-Rechtsvorschriften hinaus)</li>
<li><strong>24 Monate gesetzliche Gewährleistung</strong> auf jedes Produkt</li>""",
    ),
    "fr": (
        "En chiffres",
        """
<li><strong>18 pays européens</strong> desservis avec livraison en 24–48 h</li>
<li><strong>Remboursement sous 30 jours</strong> (au-delà des 14 jours requis par la législation européenne)</li>
<li><strong>Garantie légale de 24 mois</strong> sur chaque produit</li>""",
    ),
    "it": (
        "Numeri e fiducia",
        """
      <li><strong>18 paesi europei</strong> serviti con consegna in 24–48 ore</li>
      <li><strong>Rimborso entro 30 giorni</strong> (oltre i 14 giorni richiesti dalla legge UE)</li>
      <li><strong>24 mesi di garanzia legale</strong> su ogni prodotto</li>""",
    ),
    "pt": (
        "Pelos números",
        """
<li><strong>18 países europeus</strong> com entrega em 24–48 h</li>
<li><strong>Reembolso de 30 dias</strong> garantido (além dos 14 dias exigidos pela lei da UE)</li>
<li><strong>Garantia legal de 24 meses</strong> em cada produto</li>""",
    ),
    "hu": (
        "A számok alapján",
        """
<li><strong>18 európai ország</strong> 24–48 órás kiszállítással</li>
<li><strong>30 napos visszatérítés</strong> (az EU-s jog által előírt 14 napon túl)</li>
<li><strong>24 hónapos törvényes jótállás</strong> minden termékre</li>""",
    ),
    "lt": (
        "Pagal skaičius",
        """
<li><strong>18 Europos šalių</strong> su pristatymu per 24–48 val.</li>
<li><strong>30 dienų pinigų grąžinimas</strong> (viršija ES reikalaujamas 14 dienų)</li>
<li><strong>24 mėnesių teisinė garantija</strong> kiekvienam produktui</li>""",
    ),
    "lv": (
        "Pēc skaitļiem",
        """
<li><strong>18 Eiropas valstis</strong> ar piegādi 24–48 stundu laikā</li>
<li><strong>30 dienu naudas atgriešana</strong> (papildus ES prasītajām 14 dienām)</li>
<li><strong>24 mēnešu likumīgā garantija</strong> katram produktam</li>""",
    ),
    "ee": (
        "Numbrite järgi",
        """
<li><strong>18 Euroopa riiki</strong> 24–48 tunni tarnega</li>
<li><strong>30-päevane tagastus</strong> (üle EL-i nõutava 14 päeva)</li>
<li><strong>24-kuuline seaduslik garantii</strong> igale tootele</li>""",
    ),
    "bg": (
        "По числата",
        """
<li><strong>18 европейски държави</strong> с доставка за 24–48 часа</li>
<li><strong>30-дневно възстановяване</strong> (след 14-те дни по законодателството на ЕС)</li>
<li><strong>24-месечна законова гаранция</strong> за всеки продукт</li>""",
    ),
    "ro": (
        "După cifre",
        """
<li><strong>18 țări europene</strong> cu livrare în 24–48 ore</li>
<li><strong>Rambursare în 30 de zile</strong> (peste cele 14 zile cerute de legislația UE)</li>
<li><strong>Garanție legală de 24 de luni</strong> pentru fiecare produs</li>""",
    ),
    "hr": (
        "Po brojkama",
        """
<li><strong>18 europskih zemalja</strong> s dostavom u 24–48 sati</li>
<li><strong>Povrat novca u 30 dana</strong> (iznad 14 dana propisanih EU zakonodavstvom)</li>
<li><strong>24-mjesečno zakonsko jamstvo</strong> na svaki proizvod</li>""",
    ),
    "si": (
        "Po številkah",
        """
<li><strong>18 evropskih držav</strong> z dostavo v 24–48 urah</li>
<li><strong>30-dnevno vračilo</strong> (poleg 14 dni, ki jih zahteva zakonodaja EU)</li>
<li><strong>24-mesečna zakonska garancija</strong> za vsak izdelek</li>""",
    ),
}

FAKE_STAT_PATTERNS = [
    re.compile(r"\s*<li[^>]*>[^<]*3842[^<]*</li>\s*", re.I | re.S),
    re.compile(r"\s*<li[^>]*>[^<]*4,8\s*/\s*5[^<]*</li>\s*", re.I | re.S),
    re.compile(r"\s*<li[^>]*>[^<]*4\.8\s*/\s*5[^<]*</li>\s*", re.I | re.S),
    re.compile(
        r"\s*<li[^>]*>[^<]*(?:"
        r"reviews on product|opiniones de clientes en|opinie klientów na|"
        r"Recenze zákazníků na|Κριτικές πελατών στις|avis clients vérifiés|"
        r"recensioni verificate|verified customer|preverjenih ocen"
        r")[^<]*</li>\s*",
        re.I | re.S,
    ),
]

HEAD_GTAG = """<!-- Google tag (gtag.js) -->
<script src="/assets/js/consent-default.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18327321473"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  window.SITE_CONFIG = window.SITE_CONFIG || {};
  window.SITE_CONFIG.GOOGLE_TAG_ID = window.SITE_CONFIG.GOOGLE_TAG_ID || 'AW-18327321473';
</script>"""


def strip_fake_stats(text: str) -> str:
    for pat in FAKE_STAT_PATTERNS:
        text = pat.sub("\n", text)
    return text


def replace_numbers_block(text: str, h2: str, ul_items: str) -> str:
    pattern = re.compile(
        rf"<h2>\s*{re.escape(h2)}\s*</h2>\s*<ul>.*?</ul>",
        re.I | re.S,
    )
    replacement = f"<h2>{h2}</h2>\n<ul>\n{ul_items.strip()}\n</ul>"
    new, n = pattern.subn(replacement, text, count=1)
    return new if n else text


def fix_gtag_head(text: str) -> str:
    if "consent-default.js" in text:
        return text
    # Replace broken head gtag block (no consent-default)
    pattern = re.compile(
        r"<!-- Google tag \(gtag\.js\) -->.*?<\/script>\s*\n(?=<meta)",
        re.S,
    )
    if pattern.search(text):
        return pattern.sub(HEAD_GTAG + "\n", text, count=1)
    return text


def main() -> None:
    changed = []
    for geo, (h2, ul) in NUMBERS_BLOCKS.items():
        path = ROOT / geo / "about-us.html"
        if not path.is_file():
            print("skip missing", path)
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        text = strip_fake_stats(text)
        text = replace_numbers_block(text, h2, ul)
        text = fix_gtag_head(text)
        if text != orig:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))
    print("updated", len(changed), "files")
    for p in changed:
        print(" ", p)


if __name__ == "__main__":
    main()
