#!/usr/bin/env python3
"""Remove IBAN-via-email instructions from refund-policy pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# List-item replacements (section 2 bullets asking for IBAN in email)
LIST_REPLACEMENTS = {
    "es": "<li>Indicación de que desea recibir el reembolso por transferencia bancaria, si procede</li>",
    "en": "<li>Confirmation that you wish to receive the refund by bank transfer, if applicable</li>",
    "pl": "<li>Potwierdzenie, że chcesz otrzymać zwrot przelewem bankowym, jeśli dotyczy</li>",
    "cz": "<li>Potvrzení, že si přejete vrácení peněz bankovním převodem, pokud je to relevantní</li>",
    "sk": "<li>Potvrdenie, že si želáte vrátenie peňazí bankovým prevodom, ak je to relevantné</li>",
    "de": "<li>Bestätigung, dass Sie die Erstattung per Banküberweisung wünschen, falls zutreffend</li>",
    "fr": "<li>Confirmation que vous souhaitez recevoir le remboursement par virement bancaire, le cas échéant</li>",
    "it": "<li>Conferma che desideri ricevere il rimborso tramite bonifico bancario, se applicabile</li>",
    "pt": "<li>Confirmação de que deseja receber o reembolso por transferência bancária, se aplicável</li>",
    "gr": "<li>Επιβεβαίωση ότι επιθυμείτε επιστροφή χρημάτων μέσω τραπεζικής μεταφοράς, εφόσον ισχύει</li>",
    "hu": "<li>Megerősítés, hogy banki átutalással kéri a visszatérítést, ha alkalmazható</li>",
    "hr": "<li>Potvrda da želite povrat novca bankovnom doznakom, ako je primjenjivo</li>",
    "ro": "<li>Confirmarea că doriți rambursarea prin transfer bancar, dacă este cazul</li>",
    "bg": "<li>Потвърждение, че желаете възстановяване чрез банков превод, ако е приложимо</li>",
    "lt": "<li>Patvirtinimas, kad pageidaujate pinigų grąžinimo banko pavedimu, jei taikoma</li>",
    "lv": "<li>Apstiprinājums, ka vēlaties naudas atmaksu ar bankas pārskaitījumu, ja attiecināms</li>",
    "ee": "<li>Kinnitust, et soovite raha tagastamist pangaülekandega, kui see on asjakohane</li>",
    "si": "<li>Potrditev, da želite vračilo kupnine z bančnim nakazilom, če je to primerno</li>",
}

SECURE_PARAGRAPH = {
    "es": "<p>El reembolso se realiza dentro de los 14 días siguientes a la recepción del producto devuelto. Cuando sea necesario realizar un reembolso mediante transferencia bancaria, nuestro equipo facilitará un procedimiento seguro para proporcionar los datos bancarios. El reembolso cubre el importe total pagado, excluyendo los gastos de envío de devolución a cargo del cliente.</p>",
    "en": "<p>The refund is issued <strong>within 14 days</strong> of receiving the returned product. When a bank transfer refund is necessary, our support team will provide a secure procedure for providing bank details. The refund covers the full amount paid, excluding any return shipping costs borne by the customer.</p>",
    "pl": "<p>Zwrot środków następuje w ciągu 14 dni od otrzymania zwracanego produktu. Gdy konieczny jest zwrot przelewem bankowym, nasz zespół wsparcia przekaże bezpieczną procedurę umożliwiającą podanie danych bankowych. Zwrot obejmuje pełną zapłaconą kwotę, z wyłączeniem kosztów wysyłki zwrotnej poniesionych przez klienta.</p>",
    "cz": "<p>Vrácení peněz proběhne do 14 dnů od obdržení vráceného produktu. Je-li nutné vrácení peněz bankovním převodem, náš tým podpory poskytne bezpečný postup pro sdělení bankovních údajů. Vrácená částka pokrývá celou zaplacenou částku, bez nákladů na zpáteční dopravu hrazených zákazníkem.</p>",
    "sk": "<p>Vrátenie peňazí sa uskutoční do 14 dní od prijatia vráteného produktu. Ak je potrebné vrátenie peňazí bankovým prevodom, náš tím podpory poskytne bezpečný postup na poskytnutie bankových údajov. Vrátenie pokrýva celú zaplatenú sumu, okrem nákladov na spätnú dopravu hradených zákazníkom.</p>",
    "de": "<p>Die Rückerstattung erfolgt innerhalb von 14 Tagen nach Erhalt des zurückgegebenen Produkts. Ist eine Erstattung per Banküberweisung erforderlich, stellt unser Support-Team ein sicheres Verfahren zur Übermittlung der Bankdaten bereit. Die Rückerstattung umfasst den gesamten gezahlten Betrag, abzüglich vom Kunden zu tragender Rücksendekosten.</p>",
    "fr": "<p>Le remboursement est effectué dans les 14 jours suivant la réception du produit retourné. Lorsqu'un remboursement par virement bancaire est nécessaire, notre équipe d'assistance fournira une procédure sécurisée pour communiquer les coordonnées bancaires. Le remboursement couvre le montant total payé, hors frais de retour à la charge du client.</p>",
    "it": "<p>Il rimborso viene erogato entro 14 giorni dal ricevimento del prodotto reso. Quando è necessario un rimborso tramite bonifico bancario, il nostro team di assistenza fornirà una procedura sicura per comunicare i dati bancari. Il rimborso copre l'intero importo pagato, escluse le spese di reso a carico del cliente.</p>",
    "pt": "<p>O reembolso é emitido no prazo de 14 dias após a recepção do produto devolvido. Quando for necessário um reembolso por transferência bancária, a nossa equipa de apoio facultará um procedimento seguro para fornecer os dados bancários. O reembolso cobre o valor total pago, excluindo os custos de envio de devolução suportados pelo cliente.</p>",
    "gr": "<p>Η επιστροφή χρημάτων εκδίδεται εντός 14 ημερών από την παραλαβή του επιστρεφόμενου προϊόντος. Όταν απαιτείται επιστροφή μέσω τραπεζικής μεταφοράς, η ομάδα υποστήριξής μας θα παρέχει ασφαλή διαδικασία για την παροχή των τραπεζικών στοιχείων. Η επιστροφή καλύπτει το πλήρες ποσό που καταβλήθηκε, εξαιρουμένων των εξόδων επιστροφής που βαρύνουν τον πελάτη.</p>",
    "hu": "<p>A visszatérítés a visszaküldött termék kézhezvételétől számított 14 napon belül történik. Ha banki átutalásos visszatérítés szükséges, ügyfélszolgálatunk biztonságos eljárást biztosít a banki adatok megadásához. A visszatérítés a teljes kifizetett összeget fedezi, a vevő által viselt visszaküldési költségek kivételével.</p>",
    "hr": "<p>Povrat novca izvršava se u roku od 14 dana od primitka vraćenog proizvoda. Kada je potreban povrat bankovnom doznakom, naš tim podrške osigurat će siguran postupak za dostavu bankovnih podataka. Povrat pokriva puni plaćeni iznos, isključujući troškove povratne dostave koje snosi kupac.</p>",
    "ro": "<p>Rambursarea se face în termen de 14 zile de la primirea produsului returnat. Când este necesară rambursarea prin transfer bancar, echipa noastră de asistență va furniza o procedură sigură pentru transmiterea datelor bancare. Rambursarea acoperă întreaga sumă plătită, excluzând costurile de transport de retur suportate de client.</p>",
    "bg": "<p>Възстановяването на сумата се извършва до 14 дни от получаване на върнатия продукт. Когато е необходимо възстановяване чрез банков превод, нашият екип за поддръжка ще предостави сигурна процедура за предоставяне на банкови данни. Възстановяването покрива пълната платена сума, с изключение на разходите за връщане, поети от клиента.</p>",
    "lt": "<p>Pinigai grąžinami per 14 dienų nuo grąžinamos prekės gavimo. Kai reikalingas grąžinimas banko pavedimu, mūsų palaikymo komanda suteiks saugią procedūrą banko duomenims pateikti. Grąžinama visa sumokėta suma, neįskaitant grąžinimo siuntimo išlaidų, kurias padengia klientas.</p>",
    "lv": "<p>Naudas atmaksa tiek izsniegta 14 dienu laikā no atgrieztās preces saņemšanas. Ja nepieciešama atmaksa ar bankas pārskaitījumu, mūsu atbalsta komanda nodrošinās drošu procedūru bankas datu sniegšanai. Atmaksa sedz visu samaksāto summu, izņemot atgriešanas piegādes izmaksas, ko sedz klients.</p>",
    "ee": "<p>Raha tagastamine toimub 14 päeva jooksul alates tagastatava toote kättesaamisest. Kui on vajalik tagastamine pangaülekandega, pakub meie tugitiim turvalise protseduuri pangandmede edastamiseks. Tagasimakse katab kogu makstud summa, välja arvatud kliendi kandavad tagastamise saatmiskulud.</p>",
    "si": "<p>Vračilo kupnine se izvrši v 14 dneh po prejemu vrnjenega izdelka. Ko je potrebno vračilo z bančnim nakazilom, naša ekipa za podporo zagotovi varen postopek za posredovanje bančnih podatkov. Povračilo krije celoten plačani znesek, brez morebitnih stroškov povratnega pošiljanja, ki jih krije stranka.</p>",
}

IBAN_LIST_PATTERNS = [
    re.compile(r"<li>\s*IBAN[^<]*</li>\s*", re.IGNORECASE),
    re.compile(r"<li>\s*[^<]*IBAN[^<]*</li>\s*", re.IGNORECASE),
]

REFUND_SECTION_PATTERNS = [
    re.compile(r"<p>[^<]*IBAN[^<]*</p>\s*", re.IGNORECASE | re.DOTALL),
    re.compile(
        r"<p>[^<]*(?:bankovním převodem|bankovým prevodom|Banküberweisung|virement bancaire|bonifico|transferência bancária|bank transfer|bankovnom doznakom|bančnim nakazilom|pangaülekandega|banki átutalással|τραπεζική)[^<]*IBAN[^<]*</p>\s*",
        re.IGNORECASE | re.DOTALL,
    ),
]


def patch_file(path: Path) -> list[str]:
    geo = path.parent.name
    text = path.read_text(encoding="utf-8")
    orig = text
    changes: list[str] = []

    list_repl = LIST_REPLACEMENTS.get(geo)
    if list_repl:
        for pat in IBAN_LIST_PATTERNS:
            if pat.search(text):
                text = pat.sub(list_repl + "\n", text, count=1)
                changes.append("iban list item")
                break

    para = SECURE_PARAGRAPH.get(geo)
    if para and "procedimiento seguro" not in text and "secure procedure" not in text and "bezpieczną procedurę" not in text:
        for pat in REFUND_SECTION_PATTERNS:
            m = pat.search(text)
            if m and "IBAN" in m.group(0):
                text = text[: m.start()] + para + "\n" + text[m.end() :]
                changes.append("refund paragraph")
                break

    if text != orig:
        path.write_text(text, encoding="utf-8")
    return changes


def main() -> None:
    log: list[str] = []
    for path in sorted(ROOT.glob("*/refund-policy.html")):
        c = patch_file(path)
        if c:
            log.append(f"{path.relative_to(ROOT)}: {', '.join(c)}")
    print(f"Patched {len(log)} files")
    for line in log:
        print(line)


if __name__ == "__main__":
    main()
