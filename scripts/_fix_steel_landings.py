#!/usr/bin/env python3
"""Post-deploy fixes: H1 sentence case, full CZ translation, feature-steel placeholder."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/img/products/casa-fuego"

H1_FIXES = {
    ROOT / "es/casa-fuego/landing.html": (
        "CALOR UNIFORME EN TODA LA BASE: <span class=\"hl\">CASA FUEGO</span> ES UN SET DE ACERO INOXIDABLE CON FONDO DE 5 CAPAS",
        "Calor uniforme en toda la base: <span class=\"hl\">Casa Fuego</span> es un set de acero inoxidable con fondo de 5 capas",
    ),
    ROOT / "pl/casa-fuego/landing.html": (
        "RÓWNOMIERNE CIEPŁO NA CAŁYM DNIE: <span class=\"hl\">CASA FUEGO</span> TO ZESTAW ZE STALI NIERDZEWNEJ Z DNEM 5-WARSTWOWYM",
        "Równomierne ciepło na całym dnie: <span class=\"hl\">Casa Fuego</span> to zestaw ze stali nierdzewnej z dnem 5-warstwowym",
    ),
    ROOT / "sk/casa-fuego/landing.html": (
        "ROVNOMERNÉ TEPLO PO CELOM DNE: <span class=\"hl\">CASA FUEGO</span> JE SÚPRAVA Z NEHRDZAVEJÚCEJ OCELE S 5-VRSTVOVÝM DNOM",
        "Rovnomerné teplo po celom dne: <span class=\"hl\">Casa Fuego</span> je súprava z nehrdzavejúcej ocele s 5-vrstvovým dnom",
    ),
}

CZ_REPLACEMENTS = [
    (
        "Odoslaním formulára súhlasíte so spracovaním údajov na vybavenie objednávky. Pozrite "
        '<a href="/cz/privacy-policy.html">Zásady ochrany osobných údajov</a>.',
        "Odesláním formuláře souhlasíte se zpracováním údajů za účelem vyřízení objednávky. Viz "
        '<a href="/cz/privacy-policy.html">Zásady ochrany osobních údajů</a>.',
    ),
    ("🚚 Doručenie do 24–48 h v pracovných dňoch po telefonickom potvrdení", "🚚 Doručení do 24–48 h v pracovní dny po telefonickém potvrzení"),
    ("💶 Platba pri prevzatí", "💶 Platba na dobírku"),
    ("↩️ Vrátenie do 30 dní", "↩️ Vrácení do 30 dní"),
    ("Telefón*", "Telefon*"),
    ('placeholder="Telefón"', 'placeholder="Telefon"'),
    ("01 — ROVNOMERNÉ TEPLO VĎAKA 5-VRSTVOVÉMU DNU", "01 — ROVNOMĚRNÉ TEPLO DÍKY 5VRSTVÉMU DNU"),
    ("🔥 5-vrstvové dno", "🔥 5vrstvé dno"),
    ("5-vrstvové dno", "5vrstvé dno"),
    ("Rovnomerné teplo", "Rovnoměrné teplo"),
    ("Vhodné na indukciu", "Vhodné na indukci"),
    (
        "5-vrstvové dno pomáha rozvádzať teplo po celej ploche dna, nielen v strede. Zohreje sa rýchlo a rovnomerne a je vhodné pre všetky zdroje tepla: indukciu, plyn, sklokeramiku a elektrickú platňu.",
        "5vrstvé dno pomáhá rozvádět teplo po celém dně, nejen uprostřed. Zahřeje se rychle a rovnoměrně a je vhodné pro všechny zdroje tepla: indukci, plyn, sklokeramiku a elektrickou desku.",
    ),
    ("02 — ODOLNÁ A TRVÁCNA NEHRDZAVEJÚCA OCEĽ", "02 — ODOLNÁ A TRVANLIVÁ NEREZOVÁ OCEL"),
    ("🛡️ Kvalitná nehrdzavejúca oceľ", "🛡️ Kvalitní nerezová ocel"),
    ("Kvalitná nehrdzavejúca oceľ", "Kvalitní nerezová ocel"),
    ("Odolná proti korózii", "Odolná proti korozi"),
    ("Udrží teplo", "Udržuje teplo"),
    (
        "Vyrobené z nehrdzavejúcej ocele odolnej proti korózii, navrhnuté s dôrazom na trvácnosť. Dlhšie udrží teplo a zachová si vzhľad pri každodennom používaní. Nehrdzavejúca oceľ je navyše recyklovateľný materiál.",
        "Vyrobeno z nerezové oceli odolné proti korozi, navrženo s důrazem na trvanlivost. Déle udrží teplo a zachová si vzhled při každodenním používání. Nerezová ocel je navíc recyklovatelný materiál.",
    ),
    ("03 — DETAILY PREMYSLENÉ NA KAŽDÝ DEŇ", "03 — DETAILY PROMYŠLENÉ NA KAŽDÝ DEN"),
    ("🖐️ Okraj proti kvapkaniu a ergonomické rukoväte", "🖐️ Hrana proti kapání a ergonomické úchyty"),
    ("Okraj proti kvapkaniu", "Hrana proti kapání"),
    ("Rukoväte odolné proti teplu", "Úchyty odolné vůči teplu"),
    ("Sklenené pokrievky", "Skleněné poklice"),
    (
        "Špeciálne tvarovaný okraj pomáha nalievať bez kvapkania a ergonomické rukoväte odolné proti teplu ponúkajú pohodlný a jistý úchop. Pokrievky z tvrdeného skla umožňujú vidieť varenie a kvalitné materiály uľahčujú čistenie.",
        "Speciálně tvarovaná hrana pomáhá nalévat bez kapání a ergonomické úchyty odolné vůči teplu nabízejí pohodlný a jistý úchop. Skleněné poklice umožňují vidět vaření a kvalitní materiály usnadňují čištění.",
    ),
    ("*Výkon sa môže líšiť podľa zdroja tepla a spôsobu používania.", "*Výkon se může lišit podle zdroje tepla a způsobu používání."),
    ("Casa Fuego vs. tradičné hrnce", "Casa Fuego vs. tradiční hrnce"),
    ("<th>Tradičné hrnce</th>", "<th>Tradiční hrnce</th>"),
    ("❌ Tenké dno, nerovnomerné teplo", "❌ Tenké dno, nerovnoměrné teplo"),
    ("✅ 5vrstvé dno: rovnomernejšie teplo po celom dne", "✅ 5vrstvé dno: rovnoměrnější teplo po celém dně"),
    ("❌ Nie vždy vhodné na indukciu", "❌ Ne vždy vhodné na indukci"),
    ("✅ Vhodné na indukciu, plyn, sklokeramiku a elektrickú platňu", "✅ Vhodné na indukci, plyn, sklokeramiku a elektrickou desku"),
    ("❌ Kvapká pri nalievaní", "❌ Kapání při nalévání"),
    ("✅ Špeciálne tvarovaný okraj proti kvapkaniu", "✅ Speciálně tvarovaná hrana proti kapání"),
    ("❌ Rozhorúčené rukoväte", "❌ Rozhřáté úchyty"),
    ("✅ Ergonomické rukoväte odolné proti teplu", "✅ Ergonomické úchyty odolné vůči teplu"),
    ("❌ Nesúrodé kusy", "❌ Nesourodé kusy"),
    ("✅ Kompletná súprava 6 kusov so zladenými pokrievkami", "✅ Kompletní sada 6 dílů se sladěnými poklicemi"),
    ("Čo hovoria tí, ktorí už varia s Casa Fuego", "Co říkají ti, kdo už vaří s Casa Fuego"),
    ("Lucia, zákazníčka Casa Fuego", "Lucie, zákaznice Casa Fuego"),
    ("Lucia M., Bratislava", "Lucie M., Praha"),
    (
        "Hľadala som súpravu, ktorá bude fungovať na mojej indukcii, a som spokojná. Zohrieva sa rovnomerne a sklenené pokrievky sú praktické, lebo nemusím stále odkrývať. Vidno, že oceľ je pevná.",
        "Hledala jsem sadu, která bude fungovat na mé indukci, a jsem spokojená. Zahřívá se rovnoměrně a skleněné poklice jsou praktické, protože nemusím pořád zvedat víko. Je vidět, že ocel je pevná.",
    ),
    ("Martin, zákazník Casa Fuego", "Martin, zákazník Casa Fuego"),
    ("Martin R., Košice", "Martin R., Brno"),
    (
        "Tvarovaný okraj na nalievanie bez kvapkania poteší viac, než som čakal. Rukoväte zostávajú pohodlné a čistenie je jednoduché. Zaplatil som pri prevzatí, všetko v poriadku.",
        "Tvarovaná hrana pro nalévání bez kapání potěší víc, než jsem čekal. Úchyty zůstávají pohodlné a čištění je jednoduché. Zaplatil jsem na dobírku, vše v pořádku.",
    ),
    ("Zuzana, zákazníčka Casa Fuego", "Zuzana, zákaznice Casa Fuego"),
    ("Zuzana G., Žilina", "Zuzana G., Ostrava"),
    (
        "Rozvod tepla vidno pri omáčkach. Uberám jednu hviezdu, lebo najväčší hrniec zaberá dosť miesta v skrinke, ale inak súprava spĺňa účel a je kompletná.",
        "Rozvod tepla je vidět u omáček. Ubírám jednu hvězdu, protože největší hrnec zabírá dost místa ve skříni, ale jinak sada splňuje účel a je kompletní.",
    ),
    ("Hlavné vlastnosti Casa Fuego™", "Hlavní vlastnosti Casa Fuego™"),
    ("<strong>Typ:</strong> kuchynská súprava z nehrdzavejúcej ocele, 6 kusov s pokrievkou.", "<strong>Typ:</strong> kuchyňská sada z nerezové oceli, 6 dílů s poklicí."),
    ("<strong>Materiál:</strong> nehrdzavejúca oceľ odolná proti korózii.", "<strong>Materiál:</strong> nerezová ocel odolná proti korozi."),
    ("<strong>Dno:</strong> 5-vrstvové pre lepšie rozvádzanie tepla.", "<strong>Dno:</strong> 5vrstvé pro lepší rozvod tepla."),
    ("<strong>Pokrievky:</strong> z tvrdeného skla, na kontrolu varenia bez odkrývania.", "<strong>Poklice:</strong> z tvrzeného skla, pro kontrolu vaření bez zvedání poklice."),
    ("<strong>Rukoväte:</strong> ergonomické a odolné proti teplu.", "<strong>Úchyty:</strong> ergonomické a odolné vůči teplu."),
    ("<strong>Okraj:</strong> špeciálne tvarovaný, uľahčuje nalievanie bez kvapkania.", "<strong>Hrana:</strong> speciálně tvarovaná, usnadňuje nalévání bez kapání."),
    ("<strong>Kusy:</strong> 4 hrnce s pokrievkou (2,1 L · 2,9 L · 3,9 L · 6,6 L), kastról s pokrievkou (2,1 L) a panvica s pokrievkou (3,4 L).", "<strong>Díly:</strong> 4 hrnce s poklicí (2,1 l · 2,9 l · 3,9 l · 6,6 l), rendlík s poklicí (2,1 l) a pánev s poklicí (3,4 l)."),
    ("<strong>Ideálne na:</strong> každodenné varenie, ľahké a zdravé jedlá a ako doplnok do modernej kuchyne.", "<strong>Ideální pro:</strong> každodenní vaření, lehká a zdravá jídla a jako doplněk do moderní kuchyně."),
    ("*Vždy si prečítajte návod a používajte podľa odporúčaní výrobcu.", "*Vždy si přečtěte návod a používejte podle doporučení výrobce."),
    ("Kompletná súprava Casa Fuego, foto produktu", "Kompletní sada Casa Fuego, foto produktu"),
    ("🎁 Všetko, čo obsahuje Casa Fuego™", "🎁 Vše, co obsahuje Casa Fuego™"),
    ("Súprava 6 kusov, každý s pokrievkou z tvrdeného skla:", "Sada 6 dílů, každý se skleněnou poklicí:"),
    ("Hrniec s pokrievkou", "Hrnec s poklicí"),
    ("Kastról s pokrievkou", "Rendlík s poklicí"),
    ("Panvica s pokrievkou", "Pánev s poklicí"),
    ("📘 Návod na použitie v balení", "📘 Návod k použití v balení"),
    ("🚚 Doručenie do 24–48 h v pracovných dňoch po telefonickom potvrdení", "🚚 Doručení do 24–48 h v pracovní dny po telefonickém potvrzení"),
    ("💳 Platba pri prevzatí", "💳 Platba na dobírku"),
    ("🔄 Na vrátenie produktu máte 30 dní.", "🔄 Na vrácení produktu máte 30 dní."),
    ("❓ Často kladené otázky", "❓ Často kladené otázky"),
    ("🍳 Je vhodná na moju indukčnú platňu?", "🍳 Je vhodná na moji indukční desku?"),
    ("Áno. Casa Fuego je vhodná na indukciu, plyn, sklokeramiku a elektrickú platňu.", "Ano. Casa Fuego je vhodná na indukci, plyn, sklokeramiku a elektrickou desku."),
    ("🛡️ Z akého materiálu je vyrobená?", "🛡️ Z jakého materiálu je vyrobená?"),
    ("Z nehrdzavejúcej ocele odolnej proti korózii, s 5-vrstvovým dnom, ktoré pomáha rozvádzať teplo po celej ploche dna.", "Z nerezové oceli odolné proti korozi, s 5vrstvým dnem, které pomáhá rozvádět teplo po celém dně."),
    ("👀 Sú pokrievky sklenené?", "👀 Jsou poklice skleněné?"),
    ("Áno, z tvrdeného skla. Umožňujú sledovať varenie bez odkrývania.", "Ano, z tvrzeného skla. Umožňují sledovat vaření bez zvedání poklice."),
    ("🖐️ Rozhorúčia sa rukoväte?", "🖐️ Rozhřátí se úchyty?"),
    ("Rukoväte sú ergonomické a navrhnuté tak, aby boli odolné proti teplu. Napriek tomu pri dlhšom varení odporúčame pre istotu použiť chňapku.", "Úchyty jsou ergonomické a navržené tak, aby byly odolné vůči teplu. Přesto při delším vaření doporučujeme pro jistotu použít chňapku."),
    ("🧽 Ľahko sa čistí?", "🧽 Snadno se čistí?"),
    ("Kvalitné materiály a povrchová úprava uľahčujú čistenie pri každodennom používaní. Vždy postupujte podľa odporúčaní výrobcu.", "Kvalitní materiály a povrchová úprava usnadňují čištění při každodenním používání. Vždy postupujte podle doporučení výrobce."),
    ("💰 Môžem zaplatiť pri prevzatí?", "💰 Mohu zaplatit na dobírku?"),
    ("Áno. Platíte v hotovosti kuriérovi pri prevzatí objednávky.", "Ano. Platíte v hotovosti kurýrovi při převzetí objednávky."),
]


def main() -> None:
    for path, (old, new) in H1_FIXES.items():
        text = path.read_text(encoding="utf-8")
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")
            print(f"Fixed H1: {path.relative_to(ROOT)}")

    cz_path = ROOT / "cz/casa-fuego/landing.html"
    cz = cz_path.read_text(encoding="utf-8")
    for old, new in CZ_REPLACEMENTS:
        cz = cz.replace(old, new)
    cz_path.write_text(cz, encoding="utf-8")
    print("Fixed CZ translations")

    steel = ASSETS / "feature-steel.webp"
    if not steel.exists():
        src = ASSETS / "feature-lid.webp"
        if src.exists():
            shutil.copy2(src, steel)
            print(f"Created placeholder: {steel.relative_to(ROOT)} (from feature-lid.webp)")
        else:
            print("WARN: feature-steel.webp missing and no source to copy")


if __name__ == "__main__":
    main()
