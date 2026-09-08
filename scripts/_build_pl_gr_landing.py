#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build pl/gr CoreSync landings from corrected es/smartwatch/landing.html."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ES = ROOT / "es" / "smartwatch" / "landing.html"

LOCALES = {
    "pl": {
        "lang": "pl",
        "geo": "pl",
        "path_prefix": "/pl/",
        "country_name": "Polska",
        "offer": "3141",
        "lp": "3175",
        "_key": "b8326e3eb2c8bd4345a5a7b1ec4397f181131c7e",
        "thankyou": "https://trendtopia-store.com/pl/smartwatch/thank-you.html",
        "title": "CoreSync™ Smartwatch | Łączność, aktywność i autonomia | Trendtopia Polska",
        "description": "Odkryj CoreSync™, smartwatch do rozmów, powiadomień, codziennej aktywności i odpoczynku, z autonomią do 10 dni i kompatybilnością z iOS oraz Android.",
        "cookie_text": "Używamy plików cookie technicznych i stron trzecich, aby poprawić Twoje doświadczenie i do celów analitycznych.",
        "cookie_accept": "Akceptuję",
        "cookie_accept_all": "Akceptuj wszystko",
        "cookie_reject": "Odrzuć nieistotne",
        "cookie_manage": "Zarządzaj preferencjami",
        "cookie_save": "Zapisz preferencje",
        "cookie_change": "Zmień ustawienia plików cookie",
        "cookie_learn": "Dowiedz się więcej",
        "price_now": "199,00 zł",
        "price_old": "398,00 zł",
        "price_save": "199,00 zł",
        "disc": "-50% DZIŚ",
        "pkg_off": "50% zniżki!",
        "submit": "ZAMÓW CORESYNC",
        "msgs": {
            "name": "Wpisz imię i nazwisko.",
            "address": "Wpisz adres dostawy.",
            "tel": "Wpisz prawidłowy numer telefonu.",
            "generic": "Nie udało się wysłać zamówienia. Spróbuj ponownie.",
            "submitting": "Wysyłanie…",
        },
        "footer_info": "Informacje",
        "footer_about": "O nas",
        "footer_contact": "Kontakt",
        "footer_privacy": "Polityka prywatności",
        "footer_terms": "Regulamin",
        "footer_cookie": "Polityka cookies",
        "footer_ship": "Polityka wysyłki",
        "footer_refund": "Polityka zwrotów",
        "footer_rights": "Wszelkie prawa zastrzeżone",
        "footer_contacts": "Kontakt",
    },
    "gr": {
        "lang": "el",
        "geo": "gr",
        "path_prefix": "/gr/",
        "country_name": "Ελλάδα",
        "offer": "1842",
        "lp": "1862",
        "_key": "f9c80134e3e627afb228790d616668b0b70aa1c4",
        "thankyou": "https://trendtopia-store.com/gr/smartwatch/thank-you.html",
        "title": "CoreSync™ Smartwatch | Συνδεσιμότητα, δραστηριότητα και αυτονομία | Trendtopia Ελλάδα",
        "description": "Ανακαλύψτε το CoreSync™, ένα smartwatch για κλήσεις, ειδοποιήσεις, καθημερινή δραστηριότητα και ξεκούραση, με έως 10 ημέρες αυτονομίας και συμβατότητα με iOS και Android.",
        "cookie_text": "Χρησιμοποιούμε τεχνικά cookies και cookies τρίτων για να βελτιώσουμε την εμπειρία σας και για αναλυτικά στοιχεία.",
        "cookie_accept": "Αποδοχή",
        "cookie_accept_all": "Αποδοχή όλων",
        "cookie_reject": "Απόρριψη μη απαραίτητων",
        "cookie_manage": "Διαχείριση προτιμήσεων",
        "cookie_save": "Αποθήκευση προτιμήσεων",
        "cookie_change": "Αλλαγή προτιμήσεων cookies",
        "cookie_learn": "Μάθετε περισσότερα",
        "price_now": "69,00 €",
        "price_old": "138,00 €",
        "price_save": "69,00 €",
        "disc": "-50% ΣΗΜΕΡΑ",
        "pkg_off": "50% έκπτωση!",
        "submit": "ΠΑΡΑΓΓΕΙΛΕ CORESYNC",
        "msgs": {
            "name": "Συμπληρώστε το ονοματεπώνυμο.",
            "address": "Συμπληρώστε τη διεύθυνση παράδοσης.",
            "tel": "Συμπληρώστε έγκυρο αριθμό τηλεφώνου.",
            "generic": "Δεν ήταν δυνατή η αποστολή της παραγγελίας. Δοκιμάστε ξανά.",
            "submitting": "Αποστολή…",
        },
        "footer_info": "Πληροφορίες",
        "footer_about": "Σχετικά με εμάς",
        "footer_contact": "Επικοινωνήστε μαζί μας",
        "footer_privacy": "Πολιτική απορρήτου",
        "footer_terms": "Όροι και προϋποθέσεις",
        "footer_cookie": "Πολιτική cookies",
        "footer_ship": "Πολιτική αποστολής",
        "footer_refund": "Πολιτική επιστροφών",
        "footer_rights": "Όλα τα δικαιώματα διατηρούνται",
        "footer_contacts": "Επικοινωνία",
    },
}

# Spanish → target body translations (shared structure from ES reference)
BODY_TR = {
    "pl": {
        'lang="es"': 'lang="pl"',
        'CoreSync: llamadas, notificaciones, actividad y hasta 10 días de batería en tu muñeca': "CoreSync: rozmowy, powiadomienia, aktywność i do 10 dni baterii na nadgarstku",
        "Un smartwatch cómodo y versátil para mantenerte conectado, seguir tu actividad diaria y consultar tus registros desde una sola app.": "Wygodny i wszechstronny smartwatch, który utrzymuje Cię w kontakcie, śledzi codzienną aktywność i pozwala przeglądać dane z jednej aplikacji.",
        "Kit completo CoreSync: smartwatch, correas, cargador, manual y app en el móvil": "Kompletny zestaw CoreSync: smartwatch, paski, ładowarka, instrukcja i aplikacja w telefonie",
        "+4100 compradores reales": "+4100 prawdziwych kupujących",
        "<strong>Hasta 10 días de autonomía</strong> para acompañarte durante más tiempo.": "<strong>Do 10 dni autonomii</strong>, aby towarzyszyć Ci dłużej.",
        "<strong>Llamadas y notificaciones en la muñeca,</strong> compatible con iOS y Android.": "<strong>Rozmowy i powiadomienia na nadgarstku,</strong> kompatybilny z iOS i Android.",
        "<strong>Actividad diaria y descanso</strong> de un vistazo desde la app.": "<strong>Codzienna aktywność i odpoczynek</strong> na pierwszy rzut oka w aplikacji.",
        "<strong>Resistente al agua 5ATM</strong> para acompañarte en tu rutina.": "<strong>Wodoodporność 5ATM</strong> na co dzień.",
        "<strong>Correa de recambio, cargador y 2 fundas protectoras incluidas.</strong>": "<strong>Zapasowy pasek, ładowarka i 2 osłony ochronne w zestawie.</strong>",
        "Ahorras 49,00 €": "Oszczędzasz 199,00 zł",
        "Sí, quiero mi CoreSync": "Tak, chcę CoreSync",
        "🚚 Envío gratis 24–48 h": "🚚 Darmowa dostawa 24–48 h",
        "💶 Pago contra reembolso": "💶 Płatność przy odbiorze",
        "🛡️ Garantía 24 meses": "🛡️ Gwarancja 24 miesiące",
        "↩️ Devolución 30 días": "↩️ Zwrot w 30 dni",
        "Introduce tus datos para pedir tu CoreSync": "Podaj dane, aby zamówić CoreSync",
        "Al enviar el formulario, aceptas que tratemos tus datos para gestionar tu pedido. Consulta nuestra": "Wysyłając formularz, wyrażasz zgodę na przetwarzanie danych w celu obsługi zamówienia. Zobacz",
        "Política de privacidad": "Politykę prywatności",
        "Pídelo hoy y": "Zamów dziś i",
        "paga cómodamente contra reembolso.": "wygodnie zapłać przy odbiorze.",
        "Nombre y apellidos*": "Imię i nazwisko*",
        "Nombre y apellidos": "Imię i nazwisko",
        "Teléfono*": "Telefon*",
        "Teléfono": "Telefon",
        "Dirección de entrega*": "Adres dostawy*",
        "Dirección de entrega": "Adres dostawy",
        "PEDIR MI CORESYNC": "ZAMÓW CORESYNC",
        "Tus datos se utilizarán para gestionar tu solicitud. Consulta nuestra": "Twoje dane zostaną wykorzystane do obsługi zamówienia. Zobacz",
        "Valoración 4,6/5 de más de": "Ocena 4,6/5 na podstawie ponad",
        "compradores reales": "prawdziwych kupujących",
        "Compradores reales • Compras verificadas": "Prawdziwi kupujący • Zweryfikowane zakupy",
        "Tres razones para añadir CoreSync a tu día a día": "Trzy powody, by włączyć CoreSync w codzienną rutynę",
        "Hombre utilizando el smartwatch CoreSync durante el día": "Mężczyzna korzystający ze smartwatcha CoreSync w ciągu dnia",
        "01 — TU DÍA, DE UN VISTAZO": "01 — TWÓJ DZIEŃ NA PIERWSZY RZUT OKA",
        "Actividad y rutinas, sin complicaciones": "Aktywność i rutyny bez komplikacji",
        "Pasos": "Kroki",
        "Actividad": "Aktywność",
        "Descanso": "Odpoczynek",
        "Consulta tus pasos, actividad diaria y periodos de descanso desde el reloj y la app. Todo organizado de forma sencilla para que puedas revisar tu rutina de un vistazo.": "Sprawdzaj kroki, codzienną aktywność i okresy odpoczynku z zegarka i aplikacji. Wszystko uporządkowane prosto, abyś mógł przejrzeć rutynę na pierwszy rzut oka.",
        "CoreSync junto a un smartphone mostrando registros de actividad y descanso": "CoreSync obok smartfona z zapisami aktywności i odpoczynku",
        "02 — DESCANSA Y REVISA TU RUTINA": "02 — ODPOCZYNEK I PRZEGLĄD RUTYNY",
        "Información de descanso fácil de consultar": "Łatwy dostęp do informacji o odpoczynku",
        "Registro de sueño": "Rejestr snu",
        "Historial diario": "Historia dzienna",
        "App incluida": "Aplikacja w zestawie",
        "Lleva un registro de tus periodos de sueño y consulta tus datos al despertar desde la app. Así puedes observar tus rutinas de descanso a lo largo del tiempo de una forma sencilla y visual.": "Prowadź rejestr okresów snu i sprawdzaj dane po przebudzeniu w aplikacji. Możesz obserwować rutyny odpoczynku w czasie w prosty, wizualny sposób.",
        "Persona utilizando CoreSync en un entorno cotidiano": "Osoba korzystająca z CoreSync w codziennym otoczeniu",
        "03 — TODO LO QUE NECESITAS, NADA DE MÁS": "03 — WSZYSTKO, CZEGO POTRZEBUJESZ, NIC WIĘCEJ",
        "Kit completo listo para usar": "Kompletny zestaw gotowy do użycia",
        "1 correa de recambio": "1 zapasowy pasek",
        "2 protectores": "2 osłony",
        "Cargador incluido": "Ładowarka w zestawie",
        "CoreSync llega listo para acompañarte desde el primer día: smartwatch, correa de recambio, dos protectores, cargador y manual de instrucciones. Es compatible con iOS y Android, cuenta con resistencia al agua 5ATM y ofrece hasta 10 días de autonomía según el uso y la configuración.": "CoreSync jest gotowy od pierwszego dnia: smartwatch, zapasowy pasek, dwie osłony, ładowarka i instrukcja. Kompatybilny z iOS i Android, wodoodporność 5ATM i do 10 dni autonomii w zależności od użytkowania i ustawień.",
        "*La autonomía puede variar según el uso, la configuración y las funciones activadas.": "*Autonomia może się różnić w zależności od użytkowania, ustawień i aktywnych funkcji.",
        "Comprar ya CoreSync": "Kup teraz CoreSync",
        "Otras marcas vs CoreSync": "Inne marki vs CoreSync",
        "Un smartwatch convencional": "Zwykły smartwatch",
        "La carga frecuente puede acabar formando parte de tu rutina": "Częste ładowanie może stać się częścią rutyny",
        "<strong>Hasta 10 días de autonomía</strong> según el uso y la configuración": "<strong>Do 10 dni autonomii</strong> w zależności od użytkowania i ustawień",
        "Las funciones importantes pueden quedar repartidas entre distintos menús": "Ważne funkcje mogą być rozproszone w różnych menu",
        "<strong>Llamadas, notificaciones y registros diarios</strong> en una experiencia sencilla": "<strong>Rozmowy, powiadomienia i codzienne zapisy</strong> w prostej obsłudze",
        "Demasiadas métricas y opciones pueden complicar la experiencia": "Zbyt wiele metryk i opcji może utrudniać korzystanie",
        "<strong>Información esencial</strong> organizada de forma clara": "<strong>Podstawowe informacje</strong> uporządkowane przejrzyście",
        "Algunos diseños pueden resultar incómodos durante muchas horas": "Niektóre modele mogą być niewygodne przez wiele godzin",
        "<strong>Diseño pensado</strong> para acompañarte durante el día": "<strong>Przemyślany design</strong> na cały dzień",
        "Algunos modelos están muy ligados a un único ecosistema": "Niektóre modele wiążą Cię z jednym ekosystemem",
        "<strong>Compatible con iOS y Android</strong>": "<strong>Kompatybilny z iOS i Android</strong>",
        "Funciones similares pueden encontrarse en modelos con precios superiores": "Podobne funkcje często w droższych modelach",
        "<strong>Diseño, autonomía y conectividad a precio justo</strong>": "<strong>Design, autonomia i łączność w uczciwej cenie</strong>",
        "Lo que opinan quienes ya utilizan CoreSync": "Co mówią osoby, które już korzystają z CoreSync",
        "✔ Compra verificada": "✔ Zweryfikowany zakup",
        "Características principales de CoreSync™": "Główne cechy CoreSync™",
        "<strong>Tipo:</strong> Smartwatch para conectividad, actividad diaria y seguimiento de rutinas.": "<strong>Typ:</strong> Smartwatch do łączności, codziennej aktywności i śledzenia rutyn.",
        '<strong>Pantalla:</strong> Pantalla HD retroiluminada de 2".': '<strong>Wyświetlacz:</strong> Podświetlany ekran HD 2".',
        "<strong>Batería:</strong> Hasta 10 días de autonomía según el uso y la configuración.": "<strong>Bateria:</strong> Do 10 dni autonomii w zależności od użytkowania i ustawień.",
        "<strong>Resistencia:</strong> Resistencia al agua 5ATM.": "<strong>Odporność:</strong> Wodoodporność 5ATM.",
        "<strong>Compatibilidad:</strong> Compatible con iOS y Android mediante la app incluida.": "<strong>Kompatybilność:</strong> iOS i Android przez aplikację w zestawie.",
        "<strong>Conectividad:</strong> Llamadas y notificaciones directamente desde la muñeca.": "<strong>Łączność:</strong> Rozmowy i powiadomienia prosto z nadgarstka.",
        "<strong>Seguimiento:</strong> Actividad diaria, pasos y registros de descanso.": "<strong>Śledzenie:</strong> Codzienna aktywność, kroki i zapisy odpoczynku.",
        "<strong>Incluye:</strong> 1 correa de recambio, 2 protectores, cargador y manual de instrucciones.": "<strong>W zestawie:</strong> 1 zapasowy pasek, 2 osłony, ładowarka i instrukcja.",
        "<strong>Garantía:</strong> 24 meses.": "<strong>Gwarancja:</strong> 24 miesiące.",
        "Este producto no es un dispositivo médico y no está destinado al diagnóstico, prevención o tratamiento de enfermedades.": "Ten produkt nie jest wyrobem medycznym i nie jest przeznaczony do diagnozowania, zapobiegania ani leczenia chorób.",
        "*Lee siempre el manual incluido y usa el producto según las recomendaciones del fabricante.": "*Zawsze czytaj dołączoną instrukcję i używaj produktu zgodnie z zaleceniami producenta.",
        "Kit completo CoreSync, imagen final del producto": "Kompletny zestaw CoreSync, zdjęcie produktu",
        "🎁 Todo lo que incluye el pack CoreSync™": "🎁 Co zawiera pakiet CoreSync™",
        "✅ <strong>1× Smartwatch CoreSync</strong>": "✅ <strong>1× Smartwatch CoreSync</strong>",
        "✅ <strong>1× Correa de recambio</strong>": "✅ <strong>1× Zapasowy pasek</strong>",
        "✅ <strong>2× Protectores de pantalla/cuerpo</strong>": "✅ <strong>2× Osłony ekranu/korpusu</strong>",
        "✅ <strong>1× Cargador + cable</strong>": "✅ <strong>1× Ładowarka + kabel</strong>",
        "📘 Manual de instrucciones incluido": "📘 Instrukcja obsługi w zestawie",
        "📱 App compatible con iOS y Android": "📱 Aplikacja iOS/Android",
        "🚚 Envío gratis en 24–48 horas": "🚚 Darmowa dostawa w 24–48 godzin",
        "💳 Pago contra reembolso": "💳 Płatność przy odbiorze",
        "🔄 Devolución en 30 días": "🔄 Zwrot w 30 dni",
        "🛡️ Garantía de 24 meses": "🛡️ Gwarancja 24 miesiące",
        "¡50 % de descuento!": "50% zniżki!",
        "❓ Preguntas frecuentes": "❓ Najczęstsze pytania",
        "📱 ¿Es compatible con iPhone y Android?": "📱 Czy działa z iPhone i Android?",
        "Sí. CoreSync es compatible con iOS y Android. Instala la app, empareja el reloj y configura sus funciones desde el móvil.": "Tak. CoreSync działa z iOS i Android. Pobierz aplikację, sparuj zegarek i skonfiguruj funkcje z telefonu.",
        "🔋 ¿Cuánto dura la batería?": "🔋 Jak długo trzyma bateria?",
        "CoreSync puede alcanzar hasta 10 días de autonomía dependiendo del uso, la configuración, las llamadas, las notificaciones y las funciones que mantengas activadas.": "CoreSync może osiągnąć do 10 dni autonomii w zależności od użytkowania, ustawień, rozmów, powiadomień i aktywnych funkcji.",
        "💧 ¿Tiene resistencia al agua?": "💧 Czy ma wodoodporność?",
        "CoreSync cuenta con resistencia al agua 5ATM. Consulta el manual y las recomendaciones del fabricante para conocer las condiciones concretas de uso.": "CoreSync ma wodoodporność 5ATM. Sprawdź instrukcję i zalecenia producenta dotyczące warunków użytkowania.",
        "😴 ¿Puedo consultar mis registros de descanso?": "😴 Czy mogę sprawdzać zapisy odpoczynku?",
        "Sí. CoreSync puede registrar información relacionada con tus periodos de sueño para que puedas consultar tus rutinas de descanso desde la aplicación.": "Tak. CoreSync może rejestrować informacje o okresach snu, abyś mógł sprawdzać rutyny odpoczynku w aplikacji.",
        "📞 ¿Puedo recibir llamadas y notificaciones?": "📞 Czy mogę odbierać rozmowy i powiadomienia?",
        "Sí. Una vez conectado al móvil, CoreSync permite acceder a funciones de llamadas y consultar notificaciones compatibles directamente desde la muñeca.": "Tak. Po połączeniu z telefonem CoreSync umożliwia rozmowy i powiadomienia prosto z nadgarstka.",
        "💰 ¿Puedo pagar contra reembolso?": "💰 Czy mogę zapłacić przy odbiorze?",
        "Sí. Puedes pagar al repartidor cuando recibas tu pedido en casa, según las condiciones de envío disponibles para tu zona.": "Tak. Płacisz kurierowi po otrzymaniu zamówienia, zgodnie z warunkami dostawy dla Twojego regionu.",
        "Información": "Informacje",
        "Sobre nosotros": "O nas",
        "Contáctanos": "Kontakt",
        "Términos y condiciones": "Regulamin",
        "Política de cookies": "Polityka cookies",
        "Política de envío": "Polityka wysyłki",
        "Política de reembolso": "Polityka zwrotów",
        "Cambiar preferencias de cookies": "Zmień ustawienia plików cookie",
        "Contacto": "Kontakt",
        "Todos los derechos reservados.": "Wszelkie prawa zastrzeżone.",
        "Introduce tu nombre y apellidos.": "Wpisz imię i nazwisko.",
        "Introduce la dirección de entrega.": "Wpisz adres dostawy.",
        "Introduce un teléfono válido.": "Wpisz prawidłowy numer telefonu.",
        "No se pudo enviar el pedido. Inténtalo de nuevo.": "Nie udało się wysłać zamówienia. Spróbuj ponownie.",
        "Enviando…": "Wysyłanie…",
        "Javier R., Valencia": "Jan R., Kraków",
        "Javier R. usando CoreSync en una pausa laboral": "Jan R. z CoreSync w przerwie w pracy",
        "Pilar G., Madrid": "Anna G., Warszawa",
        "Pilar G. con CoreSync en ambiente hogareño": "Anna G. z CoreSync w domu",
        "Cristina F., Bilbao": "Katarzyna F., Wrocław",
        "Cristina F. mirando la app de sueño con CoreSync": "Katarzyna F. ogląda aplikację snu z CoreSync",
        "/* ---------- LISTA DE VENTAJAS ---------- */": "/* ---------- LISTA ZALET ---------- */",
        "/* ---------- CAJA DE PRECIO ---------- */": "/* ---------- SEKCJA CENY ---------- */",
        "49,00 €": "199,00 zł",
        "98,00 €": "398,00 zł",
        "-50% HOY": "-50% DZIŚ",
    },
    "gr": {
        'lang="es"': 'lang="el"',
        "Introduce tus datos para pedir tu CoreSync": "Εισαγάγετε τα στοιχεία σας για να παραγγείλετε το CoreSync",
        "Al enviar el formulario, aceptas que tratemos tus datos para gestionar tu pedido. Consulta nuestra": "Με την αποστολή της φόρμας, αποδέχεστε την επεξεργασία των δεδομένων σας για τη διαχείριση της παραγγελίας. Δείτε την",
        "Política de privacidad": "Πολιτική απορρήτου",
        "PEDIR MI CORESYNC": "ΠΑΡΑΓΓΕΙΛΕ CORESYNC",
        "Tus datos se utilizarán para gestionar tu solicitud. Consulta nuestra": "Τα δεδομένα σας θα χρησιμοποιηθούν για τη διαχείριση της παραγγελίας. Δείτε την",
        "Este producto no es un dispositivo médico y no está destinado al diagnóstico, prevención o tratamiento de enfermedades.": "Το προϊόν αυτό δεν αποτελεί ιατροτεχνολογικό προϊόν και δεν προορίζεται για τη διάγνωση, την πρόληψη ή τη θεραπεία ασθενειών.",
        "Cambiar preferencias de cookies": "Αλλαγή προτιμήσεων cookies",
        "Introduce tu nombre y apellidos.": "Συμπληρώστε το ονοματεπώνυμο.",
        "Introduce la dirección de entrega.": "Συμπληρώστε τη διεύθυνση παράδοσης.",
        "Introduce un teléfono válido.": "Συμπληρώστε έγκυρο αριθμό τηλεφώνου.",
        "No se pudo enviar el pedido. Inténtalo de nuevo.": "Δεν ήταν δυνατή η αποστολή της παραγγελίας. Δοκιμάστε ξανά.",
        "Enviando…": "Αποστολή…",
        "49,00 €": "69,00 €",
        "98,00 €": "138,00 €",
        "-50% HOY": "-50% ΣΗΜΕΡΑ",
        "Ahorras 49,00 €": "Εξοικονομείτε 69,00 €",
        "¡50 % de descuento!": "50% έκπτωση!",
        " included": " που περιλαμβάνεται",
        " included.": " που περιλαμβάνεται.",
        "App incluida": "Εφαρμογή που περιλαμβάνεται",
        "Cargador incluido": "Φορτιστής που περιλαμβάνεται",
        "Εισάγετε τα στοιχεία σας για περισσότερες πληροφορίες σχετικά με το CoreSync": "Εισαγάγετε τα στοιχεία σας για να παραγγείλετε το CoreSync",
        "Ναι, θέλω το CoreSync μου": "ΠΑΡΑΓΓΕΙΛΕ CORESYNC",
        "Θέλω να μάθω περισσότερα": "ΠΑΡΑΓΓΕΙΛΕ CORESYNC",
    },
}


def patch_meta(html: str, loc: dict) -> str:
    html = html.replace('lang="es"', f'lang="{loc["lang"]}"')
    html = html.replace("GEO: 'es'", f"GEO: '{loc['geo']}'")
    html = html.replace("/es/", loc["path_prefix"])
    html = html.replace("Trendtopia España", f"Trendtopia {loc['country_name']}")
    html = html.replace("es_ES", "pl_PL" if loc["geo"] == "pl" else "el_GR")
    html = re.sub(r"<title>.*?</title>", f"<title>{loc['title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{loc["description"]}">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{loc["title"]}">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{loc["description"]}">',
        html,
        count=1,
    )
    site_config = f"""window.SITE_CONFIG = Object.assign(window.SITE_CONFIG || {{}}, {{
  GEO: '{loc["geo"]}',
  PRODUCT_SLUG: 'smartwatch',
  COOKIE_TEXT: '{loc["cookie_text"]}',
  COOKIE_ACCEPT: '{loc["cookie_accept"]}',
  COOKIE_ACCEPT_ALL: '{loc["cookie_accept_all"]}',
  COOKIE_REJECT: '{loc["cookie_reject"]}',
  COOKIE_MANAGE: '{loc["cookie_manage"]}',
  COOKIE_SAVE: '{loc["cookie_save"]}',
  COOKIE_CHANGE: '{loc["cookie_change"]}',
  COOKIE_LEARN: '{loc["cookie_learn"]}'
}});"""
    html = re.sub(
        r"window\.SITE_CONFIG = Object\.assign\(window\.SITE_CONFIG \|\| \{\}, \{[\s\S]*?\}\);",
        site_config,
        html,
        count=1,
    )
    html = html.replace('value="3137"', f'value="{loc["offer"]}"')
    html = html.replace('value="3171"', f'value="{loc["lp"]}"')
    html = html.replace(
        'value="e4902d24a201fe03eb3c43937bbcef784ded5f43"',
        f'value="{loc["_key"]}"',
    )
    html = html.replace(
        "https://trendtopia-store.com/es/smartwatch/thank-you.html",
        loc["thankyou"],
    )
    html = html.replace("<!-- CoreSync™ — Landing ES (slug: smartwatch) -->", f"<!-- CoreSync™ — Landing {loc['geo'].upper()} (slug: smartwatch) -->")
    return html


def apply_body_translations(html: str, geo: str) -> str:
    for src, dst in BODY_TR[geo].items():
        html = html.replace(src, dst)
    return html


def patch_gr_from_existing(gr_html: str, loc: dict) -> str:
    """Patch existing GR landing with ES technical fixes."""
    html = gr_html
    # SITE_CONFIG
    site_config = f"""window.SITE_CONFIG = Object.assign(window.SITE_CONFIG || {{}}, {{
  GEO: '{loc["geo"]}',
  PRODUCT_SLUG: 'smartwatch',
  COOKIE_TEXT: '{loc["cookie_text"]}',
  COOKIE_ACCEPT: '{loc["cookie_accept"]}',
  COOKIE_ACCEPT_ALL: '{loc["cookie_accept_all"]}',
  COOKIE_REJECT: '{loc["cookie_reject"]}',
  COOKIE_MANAGE: '{loc["cookie_manage"]}',
  COOKIE_SAVE: '{loc["cookie_save"]}',
  COOKIE_CHANGE: '{loc["cookie_change"]}',
  COOKIE_LEARN: '{loc["cookie_learn"]}'
}});"""
    html = re.sub(
        r"window\.SITE_CONFIG = \{[\s\S]*?\};",
        site_config,
        html,
        count=1,
    )
    # CSS from ES
    if ".cf-form button:disabled" not in html:
        html = html.replace(
            ".cf-form button:hover{background:var(--cf-orange-dark)}",
            ".cf-form button:hover{background:var(--cf-orange-dark)}\n.cf-form button:disabled{opacity:.72;cursor:not-allowed;transform:none}",
        )
    if ".site-footer__link-btn" not in html:
        html = html.replace(
            ".cf-lp .site-footer__brand-mark{\n  display:block;\n  width:75px;\n  height:auto;\n  margin:0 auto 1rem;\n}",
            ".cf-lp .site-footer__brand-mark{\n  display:block;\n  width:75px;\n  height:auto;\n  margin:0 auto 1rem;\n}\n.cf-lp .site-footer__list .site-footer__link-btn{\n  background:none;border:none;padding:0;margin:0;\n  font:inherit;color:inherit;text-decoration:underline;cursor:pointer;\n  text-align:left;\n}\n.cf-lp .site-footer__list .site-footer__link-btn:focus-visible{\n  outline:2px solid var(--cf-orange);outline-offset:2px;\n}",
        )
    # Remove duplicate adrice scripts inside forms
    block = re.compile(
        r"<script>\s*document\.addEventListener\(\"DOMContentLoaded\"[\s\S]*?</script>\s*"
        r"<script src=\"https://offers\.adricenetwork\.com/forms/tmfp/\"[\s\S]*?"
        r"<script src=\"https://offers.adricenetwork\.com/forms/html/js-v2/\" async></script>\s*",
        re.MULTILINE,
    )
    html = block.sub("", html)
    # Footer cookie button
    if "tt-cookie-change-link" not in html:
        html = html.replace(
            '        <li><a href="/gr/refund-policy.html">Πολιτική επιστροφών</a></li>\n      </ul>',
            '        <li><a href="/gr/refund-policy.html">Πολιτική επιστροφών</a></li>\n        <li><button type="button" class="site-footer__link-btn tt-cookie-change-link">Αλλαγή προτιμήσεων cookies</button></li>\n      </ul>',
        )
    # JS submit guard + cookie + subid + adrice at end
    old_js_end = """    form.addEventListener('submit', function (e) {
      var result = validateForm(form);

      if (!result.valid) {
        e.preventDefault();
        e.stopImmediatePropagation();
        live.textContent = MSGS.generic;
        if (result.firstInvalid) result.firstInvalid.focus();
        return;
      }

      live.textContent = '';
      var btn = form.querySelector('button[type="submit"]');
      if (btn && btn.textContent.indexOf(MSGS.submitting) === -1) {
        btn.dataset.originalText = btn.textContent;
        btn.textContent = MSGS.submitting;
      }
    }, true);
  }

  document.querySelectorAll('.cf-form.tm-order-form').forEach(wireForm);
})();
</script>

</body>"""
    new_js_end = """    form.addEventListener('submit', function (e) {
      if (form.dataset.submitting === 'true') {
        e.preventDefault();
        e.stopImmediatePropagation();
        return;
      }

      var result = validateForm(form);

      if (!result.valid) {
        e.preventDefault();
        e.stopImmediatePropagation();
        live.textContent = MSGS.generic;
        if (result.firstInvalid) result.firstInvalid.focus();
        return;
      }

      form.dataset.submitting = 'true';
      live.textContent = '';
      var btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.dataset.originalText = btn.textContent;
        btn.textContent = MSGS.submitting;
      }
    }, true);
  }

  document.querySelectorAll('.cf-form.tm-order-form').forEach(wireForm);

  document.querySelectorAll('.site-footer .tt-cookie-change-link').forEach(function (btn) {
    if (btn.dataset.cookiePrefsBound === '1') return;
    btn.dataset.cookiePrefsBound = '1';
    btn.addEventListener('click', function () {
      if (typeof window.ttOpenCookiePreferences === 'function') {
        window.ttOpenCookiePreferences();
      }
    });
  });

  document.addEventListener('DOMContentLoaded', function () {
    var params = new URLSearchParams(window.location.search);
    var campaign = params.get('utm_campaign') || '';
    document.querySelectorAll('input[name="subid"]').forEach(function (subidInput) {
      subidInput.value = campaign;
    });
  });
})();
</script>
<script src="https://offers.adricenetwork.com/forms/tmfp/" crossorigin="anonymous" defer></script>
<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>

</body>"""
    html = html.replace(old_js_end, new_js_end)
    html = apply_body_translations(html, "gr")
    # Fix remaining English "included"
    html = html.replace(" included", " που περιλαμβάνεται")
    html = html.replace("Εφαρμογή included", "Εφαρμογή που περιλαμβάνεται")
    html = html.replace("Φορτιστής included", "Φορτιστής που περιλαμβάνεται")
    html = html.replace("εγχειρίδιο included", "εγχειρίδιο που περιλαμβάνεται")
    html = html.replace("εγχειρίδιο οδηγιών included", "εγχειρίδιο οδηγιών που περιλαμβάνεται")
    return html


def build_pl_from_es(es_html: str, loc: dict) -> str:
    html = es_html
    html = patch_meta(html, loc)
    html = apply_body_translations(html, "pl")
    # PL topbar: keep ES structure (already in es template)
    html = html.replace(
        '<div class="cf-lp" lang="pl">',
        '<div class="cf-lp" lang="pl">',
    )
    return html


def main() -> None:
    es_html = ES.read_text(encoding="utf-8")
    pl_out = ROOT / "pl" / "smartwatch" / "landing.html"
    gr_out = ROOT / "gr" / "smartwatch" / "landing.html"
    gr_existing = gr_out.read_text(encoding="utf-8")

    pl_html = build_pl_from_es(es_html, LOCALES["pl"])
    gr_html = patch_gr_from_existing(gr_existing, LOCALES["gr"])

    pl_out.write_text(pl_html, encoding="utf-8", newline="\n")
    gr_out.write_text(gr_html, encoding="utf-8", newline="\n")
    print(f"Wrote {pl_out.relative_to(ROOT)} ({len(pl_html)} bytes)")
    print(f"Wrote {gr_out.relative_to(ROOT)} ({len(gr_html)} bytes)")


if __name__ == "__main__":
    main()
