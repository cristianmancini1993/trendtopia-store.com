# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "scripts" / "_vortek_cro.css").read_text(encoding="utf-8")

COMPANY = "GLOBAL INTEGRATED MARKETING COMMUNICATION GROUP HOLDINGS LIMITED"
ADDR = "RM 01, 15/F, Goldsland Building, 22-26 Minden Avenue, Tsim Sha Tsui, Kowloon, Hong Kong"
UID = "019e5f4e-b178-7d63-91e1-6fda72088957"
WEBHOOK_DEFAULT = "https://hook.eu2.make.com/otlkouarqencnd3tdlobo9xhdex1wcei"
WEBHOOK_SK = "https://hook.eu2.make.com/cds3apkdon1odprbssp1g3pujadvbx1l"

PHONE_ES = r"""
  function isValidLocalPhone(val) {
    if (!val || !/\d/.test(val)) return false;
    if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
    var compact = val.replace(/[\s\-().]/g, '');
    if (compact.indexOf('+34') === 0) compact = compact.slice(3);
    else if (compact.indexOf('0034') === 0) compact = compact.slice(4);
    var digits = compact.replace(/\D/g, '');
    if (!/^[6-9]\d{8}$/.test(digits)) return false;
    if (/^(\d)\1+$/.test(digits)) return false;
    return true;
  }"""

PHONE_SK = r"""
  function isValidLocalPhone(val) {
    if (!val || !/\d/.test(val)) return false;
    if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
    var compact = val.replace(/[\s\-().]/g, '');
    if (compact.indexOf('+421') === 0) compact = compact.slice(1);
    if (compact.indexOf('00421') === 0) compact = '421' + compact.slice(5);
    var digits = compact.replace(/\D/g, '');
    var national = '';
    if (digits.indexOf('421') === 0) {
      if (digits.length > 12) return false;
      national = digits.slice(3);
    } else if (digits.charAt(0) === '0') {
      if (digits.length !== 10) return false;
      national = digits.slice(1);
    } else {
      national = digits;
    }
    if (national.length !== 9) return false;
    if (/^(\d)\1{8}$/.test(national)) return false;
    return true;
  }"""

PHONE_PL = r"""
  function isValidLocalPhone(val) {
    if (!val || !/\d/.test(val)) return false;
    if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
    var compact = val.replace(/[\s\-().]/g, '');
    if (compact.indexOf('+48') === 0) compact = compact.slice(3);
    else if (compact.indexOf('0048') === 0) compact = compact.slice(4);
    var digits = compact.replace(/\D/g, '');
    if (!/^[1-9]\d{8}$/.test(digits)) return false;
    if (/^(\d)\1+$/.test(digits)) return false;
    return true;
  }"""

PHONE_LT = r"""
  function isValidLocalPhone(val) {
    if (!val || !/\d/.test(val)) return false;
    if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
    var compact = val.replace(/[\s\-().]/g, '');
    if (compact.indexOf('+370') === 0) compact = compact.slice(4);
    else if (compact.indexOf('00370') === 0) compact = compact.slice(5);
    var digits = compact.replace(/\D/g, '');
    if (/^[08]\d{8}$/.test(digits)) digits = digits.slice(1);
    if (!/^[2-9]\d{7}$/.test(digits)) return false;
    if (/^(\d)\1+$/.test(digits)) return false;
    return true;
  }"""

PHONE_LV = r"""
  function isValidLocalPhone(val) {
    if (!val || !/\d/.test(val)) return false;
    if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
    var compact = val.replace(/[\s\-().]/g, '');
    if (compact.indexOf('+371') === 0) compact = compact.slice(4);
    else if (compact.indexOf('00371') === 0) compact = compact.slice(5);
    var digits = compact.replace(/\D/g, '');
    if (!/^[2-7]\d{7}$/.test(digits)) return false;
    if (/^(\d)\1+$/.test(digits)) return false;
    return true;
  }"""

LOCALES = {
  "es": {
    "lang": "es", "locale": "es-ES", "geo": "es", "slug": "vortek-1013",
    "currency": "EUR", "price_num": 69.00, "offer_id": "1013", "lp": "1032",
    "offer_name": "Iron Oak Pro ES 1013 (CPL)", "lp_id": "es-vortek-1013",
    "key": "e05d73a2a29281b9774064a5a48f51a293ee9682", "webhook": WEBHOOK_DEFAULT,
    "price": "69,00 €", "old": "138,00 €", "save": "AHORRAS 69 €",
    "submitting": "Enviando…",
    "cookie_text": "Utilizamos cookies técnicas y de terceros para mejorar tu experiencia y con fines analíticos.",
    "cookie_accept": "Aceptar", "cookie_learn": "Más información",
    "title": "Iron Oak Pro™ — Kit completo con 50 % de descuento",
    "desc": "Iron Oak Pro: motosierra a batería con motor sin escobillas, dos baterías y kit completo. Oferta del 50 % y pago contra reembolso.",
    "announce": "<strong>50 % DE DESCUENTO</strong> · 138,00 € → 69,00 € · PAGO AL RECIBIR",
    "ship": "Envío 24–48 h*", "cod": "Contra reembolso",
    "rating": "Valoración de clientes*",
    "eyebrow": "Motosierra profesional a batería",
    "h1": "TERMINA EL TRABAJO. <em>NO LA BATERÍA.</em>",
    "lead": "Motor sin escobillas de 1.500 W, dos baterías y kit completo para cortar troncos y ramas sin depender de cables ni gasolina.",
    "p1": "<strong>Hasta 8 horas combinadas*</strong> con las dos baterías incluidas.",
    "p2": "<strong>Capacidad declarada de hasta 40 cm*</strong> según madera y condiciones de uso.",
    "p3": "<strong>Solo 2,4 kg*</strong> incluyendo espada y batería.",
    "p4": "<strong>Lubricación y tensado automáticos*</strong> para reducir interrupciones.",
    "p5": "<strong>Guantes de regalo</strong> incluidos en el kit.",
    "hero_alt": "Kit completo de motosierra Iron Oak Pro con baterías, cadenas, cargador, maletín y guantes de regalo",
    "hero_alt": "Kit completo de motosierra Iron Oak Pro con baterías, cadenas, cargador, maletín y guantes",
    "badge_small": "OFERTA",
    "pack_label": "KIT COMPLETO INCLUIDO",
    "pack_small": "2 baterías · 2 cadenas · maletín · guantes de regalo",
    "form_eye": "Oferta de lanzamiento",
    "form_h2": "PIDE TU IRON OAK PRO",
    "form_p": "No pagas ahora. Confirmamos el pedido por teléfono y pagas al recibirlo.",
    "step1": "Paso 1 de 2", "step2": "Paso 2 de 2", "secure": "Pedido seguro",
    "err": "Revisa los campos señalados para continuar.",
    "lbl_name": "Nombre y apellidos", "ph_name": "Ej. Carlos Martínez",
    "lbl_tel": "Teléfono", "ph_tel": "Ej. 612 345 678",
    "next": "CONTINUAR CON MI PEDIDO →",
    "micro1": "Te llamaremos una sola vez para confirmar los datos y la dirección.",
    "lbl_addr": "Dirección de entrega", "ph_addr": "Calle, número, piso y puerta",
    "lbl_postal": "Código postal", "ph_postal": "28001", "postal_pattern": ' pattern="[0-9]{5}"',
    "lbl_city": "Ciudad", "ph_city": "Madrid",
    "lbl_prov": "Provincia", "ph_prov": "Madrid",
    "submit": "CONFIRMAR PEDIDO · 69,00 €",
    "back": "← Volver",
    "micro2": "Al confirmar aceptas las <a href=\"/es/terms-conditions.html\">condiciones de compra</a> y la <a href=\"/es/privacy-policy.html\">política de privacidad</a>.",
    "t1b": "Oferta −50%", "t1s": "138,00 € → 69,00 €",
    "t2b": "Pago al recibir", "t2s": "Sin pago previo",
    "t3b": "Entrega 24–48 h*", "t3s": "Tras confirmar por teléfono",
    "t4b": "30 días*", "t4s": "Política de devolución",
    "prob_eye": "Trabaja sin las limitaciones de siempre",
    "prob_h2": "UNA SOLA HERRAMIENTA. TODA LA JORNADA.",
    "prob_p": "Iron Oak Pro combina un motor sin escobillas con dos baterías intercambiables. Cuando una se agota, colocas la otra y continúas.",
    "m1b": "1.500 W*", "m1s": "Potencia declarada del motor sin escobillas.",
    "m2b": "2 BATERÍAS", "m2s": "Incluidas para alternar durante el trabajo.",
    "m3b": "40 CM*", "m3s": "Capacidad máxima declarada según tipo de madera.",
    "feat_eye": "Diseñada para avanzar",
    "feat_h2": "MENOS PARADAS. MÁS TRABAJO HECHO.",
    "feat_p": "Tres razones por las que el kit Iron Oak Pro está pensado para trabajos de poda y corte en jardines y terrenos.",
    "f1t": "MOTOR SIN ESCOBILLAS DE 1.500 W*",
    "f1p": "Diseñado para ofrecer un corte constante y reducir el sobrecalentamiento durante usos prolongados. La potencia real de corte depende de la madera, la cadena y el estado de carga.",
    "f1c1": "Motor brushless", "f1c2": "Disipación térmica", "f1c3": "Uso en jardín",
    "f1alt": "Persona cortando un tronco con la motosierra Iron Oak Pro",
    "f2t": "DOS BATERÍAS PARA SEGUIR CORTANDO",
    "f2p": "Las dos baterías incluidas suman hasta ocho horas combinadas y una carga completa en aproximadamente una hora. La autonomía real depende del tipo y el grosor de la madera.",
    "f2c1": "2 baterías", "f2c2": "Cambio rápido", "f2c3": "Cargador incluido",
    "f2alt": "Cambio de batería en la motosierra Iron Oak Pro junto al cargador",
    "f3t": "LUBRICACIÓN Y TENSADO AUTOMÁTICOS*",
    "f3p": "Depósito de aceite y sistema que ajusta la tensión de la cadena para reducir las paradas manuales. Sigue siempre las instrucciones de mantenimiento del fabricante.",
    "f3c1": "2 cadenas", "f3c2": "Depósito de aceite", "f3c3": "Ajuste automático*",
    "f3alt": "Mantenimiento y cadena de la motosierra Iron Oak Pro",
    "cmp_eye": "Comparación objetiva",
    "cmp_h2": "IRON OAK PRO FRENTE A UN MODELO BÁSICO",
    "cmp_p": "Comparación del kit Iron Oak Pro frente a una motosierra básica de jardín.",
    "cmp_h": "Característica", "cmp_a": "Iron Oak Pro", "cmp_b": "Modelo básico",
    "c1": "Baterías incluidas", "c1a": "✓ 2 unidades", "c1b": "Habitualmente 1",
    "c2": "Cargador", "c2a": "✓ Incluido", "c2b": "Variable",
    "c3": "Cadenas incluidas", "c3a": "✓ 2 unidades", "c3b": "Habitualmente 1",
    "c4": "Maletín y protección", "c4a": "✓ Incluidos", "c4b": "Variable",
    "c5": "Pago contra reembolso", "c5a": "✓ Disponible", "c5b": "Variable",
    "pack_eye": "Todo incluido",
    "pack_h2": "ABRE EL MALETÍN Y PONTE A TRABAJAR.",
    "pack_alt": "Contenido completo del pack Iron Oak Pro",
    "li1": "1 motosierra Iron Oak Pro", "li2": "2 baterías de litio", "li3": "1 cargador rápido",
    "li4": "2 cadenas y accesorios de montaje", "li5": "1 maletín de transporte",
    "li6": "Guantes de regalo, gafas y manual",
    "safety": "<strong>Seguridad:</strong> usa siempre protección ocular, guantes y equipo adecuado. Lee el manual completo y no utilices la herramienta si no estás capacitado para manejar una motosierra.",
    "rev_eye": "Opiniones", "rev_h2": "LO QUE CUENTAN QUIENES YA LA USAN.",
    "rev_note": "Opiniones de clientes sobre el uso de Iron Oak Pro. La autonomía y el corte dependen de la madera y las condiciones de trabajo.",
    "q1": "“Pude cortar la leña y terminar el trabajo del jardín sin detenerme a esperar otra carga.”",
    "q2": "“Me sorprendió que pudiera trabajar con troncos más gruesos manteniendo un manejo sencillo.”",
    "q3": "“El peso hace que resulte más manejable durante trabajos largos que otras herramientas que he utilizado.”",
    "r1n": "Carlos M.", "r1c": "Valencia",
    "r2n": "Elena V.", "r2c": "Sevilla",
    "r3n": "Javier S.", "r3c": "Zaragoza",
    "ph1": "Kit Iron Oak Pro sobre la mesa al desembalar",
    "ph2": "Pedido Iron Oak Pro al abrirlo en casa",
    "ph3": "Montaje de la motosierra Iron Oak Pro",
    "faq_eye": "Preguntas frecuentes", "faq_h2": "ANTES DE PEDIRLA, DEBES SABER…",
    "faq_p": "Respuestas sobre baterías, corte, pago, envío, devoluciones y garantía.",
    "faq": [
      ("¿Cuánto duran las baterías?", "Juntas ofrecen hasta ocho horas combinadas. El cargador rápido las carga en aproximadamente una hora. La autonomía real depende del grosor y tipo de madera, la presión de corte, la temperatura y el estado de las baterías."),
      ("¿Puede cortar troncos de 40 cm?", "La capacidad máxima declarada es de hasta 40 cm. La dureza de la madera, la técnica y el mantenimiento influyen en el resultado."),
      ("¿Tengo que pagar ahora?", "No. El pago es contra reembolso: se confirma el pedido por teléfono y se paga al transportista al recibirlo."),
      ("¿Qué incluye exactamente?", "Motosierra, dos baterías, cargador, dos cadenas, herramientas, maletín, gafas, manual y guantes de regalo."),
      ("¿Puedo devolverla?", "Sí, durante 30 días según la <a href=\"/es/refund-policy.html\">política de reembolso</a>."),
      ("¿Qué garantía tiene?", "Los productos nuevos están cubiertos por una garantía legal de conformidad de 3 años desde la entrega. La garantía cubre las faltas de conformidad en los términos establecidos por la legislación española de consumidores."),
    ],
    "cta_h2": "IRON OAK PRO POR 69,00 €",
    "cta_p": "Kit completo, 50 % de descuento y pago al recibir. Oferta sujeta a disponibilidad y confirmación.",
    "cta_btn": "PEDIR AHORA →",
    "foot_p": "Herramienta a batería para trabajos de corte y mantenimiento exterior.",
    "help": "Ayuda", "legal": "Legal",
    "a_order": "Realizar pedido", "a_ship": "Envíos", "a_contact": "Contacto",
    "a_priv": "Privacidad", "a_cook": "Cookies", "a_terms": "Condiciones de compra",
    "a_about": "Aviso legal", "cookie_btn": "Cambiar preferencias de cookies",
    "rights": "Todos los derechos reservados. *La autonomía, el corte y los plazos dependen del tipo de madera y de la confirmación del pedido.",
    "sticky": "PEDIR IRON OAK PRO · 69,00 €",
    "msg_name": "Introduce tu nombre y apellidos.",
    "msg_addr": "Introduce la dirección de entrega.",
    "msg_tel": "Introduce un número de teléfono español válido.",
    "msg_generic": "No se ha podido enviar el pedido. Inténtalo de nuevo.",
    "phone_js": PHONE_ES,
    "form_extra": "",
    "tmfp": False,
    "href_about": "/es/about-us.html", "href_contact": "/es/contact-us.html",
    "href_ship": "/es/shipping-policy.html", "href_refund": "/es/refund-policy.html",
    "href_priv": "/es/privacy-policy.html", "href_cook": "/es/cookie-policy.html",
    "href_terms": "/es/terms-conditions.html",
  },
  "sk": {
    "lang": "sk", "locale": "sk-SK", "geo": "sk", "slug": "vortek-3228",
    "currency": "EUR", "price_num": 79.00, "offer_id": "3228", "lp": "3262",
    "offer_name": "Iron Oak Pro SK 3228 (CPL)", "lp_id": "sk-vortek-3228",
    "key": "06c97b438709e68194eda1c79870739da3c83220", "webhook": WEBHOOK_SK,
    "price": "79,00 €", "old": "158,00 €", "save": "UŠETRÍTE 79 €",
    "submitting": "Odosielanie…",
    "cookie_text": "Používame technické cookies a cookies tretích strán na zlepšenie vášho zážitku a na analytické účely.",
    "cookie_accept": "Prijať", "cookie_learn": "Zistiť viac",
    "title": "Iron Oak Pro™ — Kompletný kit so zľavou 50 %",
    "desc": "Iron Oak Pro: akumulátorová reťazová píla s bezkefovým motorom, dvoma batériami a kompletným kitom. Zľava 50 % a platba na dobierku.",
    "announce": "<strong>ZĽAVA 50 %</strong> · 158,00 € → 79,00 € · PLATBA NA DOBIERKU",
    "ship": "Doručenie 24–48 h*", "cod": "Na dobierku",
    "rating": "Hodnotenie zákazníkov*",
    "eyebrow": "Profesionálna akumulátorová reťazová píla",
    "h1": "DOKONČITE PRÁCU. <em>NIE BATÉRIU.</em>",
    "lead": "Bezkefový motor 1 500 W, dve batérie a kompletný kit na rezanie kmeňov a konárov bez kábla a benzínu.",
    "p1": "<strong>Až 8 hodín spolu*</strong> s dvoma batériami v balení.",
    "p2": "<strong>Deklarovaná kapacita až 40 cm*</strong> podľa dreva a podmienok použitia.",
    "p3": "<strong>Len 2,4 kg*</strong> vrátane lišty a batérie.",
    "p4": "<strong>Automatické mazanie a napínanie*</strong> na menej prestávok.",
    "p5": "<strong>Rukavice zadarmo</strong> v balení ako darček.",
    "hero_alt": "Kompletný kit reťazovej píly Iron Oak Pro s batériami, reťazami, nabíjačkou, kufríkom a rukavicami",
    "badge_small": "PONUKA",
    "pack_label": "KOMPLETNÝ KIT V CENE",
    "pack_small": "2 batérie · 2 reťaze · kufrík · rukavice zadarmo",
    "form_eye": "Úvodná ponuka",
    "form_h2": "OBJEDNAJTE SI IRON OAK PRO",
    "form_p": "Teraz neplatíte. Objednávku potvrdíme telefonicky a zaplatíte pri prevzatí.",
    "step1": "Krok 1 z 2", "step2": "Krok 2 z 2", "secure": "Bezpečná objednávka",
    "err": "Skontrolujte označené polia a pokračujte.",
    "lbl_name": "Meno a priezvisko", "ph_name": "Napr. Peter Kovács",
    "lbl_tel": "Telefón", "ph_tel": "Napr. 0901 123 456",
    "next": "POKRAČOVAŤ V OBJEDNÁVKE →",
    "micro1": "Zavoláme vám raz na potvrdenie údajov a adresy.",
    "lbl_addr": "Adresa doručenia", "ph_addr": "Ulica, číslo, poschodie",
    "lbl_postal": "PSČ", "ph_postal": "811 01", "postal_pattern": "",
    "lbl_city": "Mesto", "ph_city": "Bratislava",
    "lbl_prov": "Kraj", "ph_prov": "Bratislavský kraj",
    "submit": "POTVRDIŤ OBJEDNÁVKU · 79,00 €",
    "back": "← Späť",
    "micro2": "Potvrdením súhlasíte s <a href=\"/sk/terms-conditions.html\">obchodnými podmienkami</a> a <a href=\"/sk/privacy-policy.html\">ochranou údajov</a>.",
    "t1b": "Zľava −50%", "t1s": "158,00 € → 79,00 €",
    "t2b": "Platba na dobierku", "t2s": "Bez platby vopred",
    "t3b": "Doručenie 24–48 h*", "t3s": "Po telefonickom potvrdení",
    "t4b": "30 dní*", "t4s": "Vrátenie tovaru",
    "prob_eye": "Práca bez obvyklých obmedzení",
    "prob_h2": "JEDEN NÁSTROJ. CELÝ DEŇ.",
    "prob_p": "Iron Oak Pro spája bezkefový motor s dvoma výmennými batériami. Keď jedna dojde, vložíte druhú a pokračujete.",
    "m1b": "1 500 W*", "m1s": "Deklarovaný výkon bezkefového motora.",
    "m2b": "2 BATÉRIE", "m2s": "V balení na striedanie pri práci.",
    "m3b": "40 CM*", "m3s": "Maximálna deklarovaná kapacita podľa dreva.",
    "feat_eye": "Navrhnutá, aby ste pokročili",
    "feat_h2": "MENEJ PRESTÁVOK. VIAC HOTOVEJ PRÁCE.",
    "feat_p": "Tri dôvody, prečo je kit Iron Oak Pro určený na rez a údržbu záhrady.",
    "f1t": "BEZKEFOVÝ MOTOR 1 500 W*",
    "f1p": "Navrhnutý na stály rez a nižšie prehrievanie pri dlhšom použití. Skutočný výkon rezu závisí od dreva, reťaze a stavu nabitia.",
    "f1c1": "Bezkefový motor", "f1c2": "Odvod tepla", "f1c3": "Práca v záhrade",
    "f1alt": "Rezanie kmeňa pílou Iron Oak Pro",
    "f2t": "DVE BATÉRIE, ABY STE MOHLI REZAŤ ĎALEJ",
    "f2p": "Dve batérie v balení spolu až osem hodín a plné nabitie približne za hodinu. Reálna výdrž závisí od druhu a hrúbky dreva.",
    "f2c1": "2 batérie", "f2c2": "Rýchla výmena", "f2c3": "Nabíjačka v balení",
    "f2alt": "Výmena batérie Iron Oak Pro pri nabíjačke",
    "f3t": "AUTOMATICKÉ MAZANIE A NAPÍNANIE*",
    "f3p": "Nádržka na olej a systém, ktorý upraví napnutie reťaze, aby ste nemuseli tak často zastavovať. Vždy dodržujte pokyny výrobcu.",
    "f3c1": "2 reťaze", "f3c2": "Nádržka na olej", "f3c3": "Automatické nastavenie*",
    "f3alt": "Údržba a reťaz píly Iron Oak Pro",
    "cmp_eye": "Objektívne porovnanie",
    "cmp_h2": "IRON OAK PRO VOČI ZÁKLADNÉMU MODELU",
    "cmp_p": "Porovnanie kitu Iron Oak Pro so základnou záhradnou pílou.",
    "cmp_h": "Vlastnosť", "cmp_a": "Iron Oak Pro", "cmp_b": "Základný model",
    "c1": "Batérie v balení", "c1a": "✓ 2 kusy", "c1b": "Zvyčajne 1",
    "c2": "Nabíjačka", "c2a": "✓ V balení", "c2b": "Rôzne",
    "c3": "Reťaze v balení", "c3a": "✓ 2 kusy", "c3b": "Zvyčajne 1",
    "c4": "Kufrík a ochrana", "c4a": "✓ V balení", "c4b": "Rôzne",
    "c5": "Platba na dobierku", "c5a": "✓ Dostupné", "c5b": "Rôzne",
    "pack_eye": "Všetko v balení",
    "pack_h2": "OTVORTE KUFRÍK A PUSŤTE SA DO PRÁCE.",
    "pack_alt": "Kompletný obsah balenia Iron Oak Pro",
    "li1": "1 reťazová píla Iron Oak Pro", "li2": "2 lítiové batérie", "li3": "1 rýchlonabíjačka",
    "li4": "2 reťaze a montážne príslušenstvo", "li5": "1 prepravný kufrík",
    "li6": "Rukavice zadarmo, okuliare a návod",
    "safety": "<strong>Bezpečnosť:</strong> vždy používajte ochranu očí, rukavice a vhodnú výbavu. Prečítajte si celý návod a pílu nepoužívajte, ak nie ste spôsobilí obsluhovať reťazovú pílu.",
    "rev_eye": "Recenzie", "rev_h2": "ČO HOVORIA TÍ, KTORÍ JU UŽ POUŽÍVAJÚ.",
    "rev_note": "Skúsenosti zákazníkov s Iron Oak Pro. Výdrž a rez závisia od dreva a podmienok práce.",
    "q1": "“Narezal som drevo na zimu a dokončil záhradu bez čakania na ďalšie nabitie.”",
    "q2": "“Prekvapilo ma, že zvládla hrubšie kmene a stále sa ľahko ovládala.”",
    "q3": "“Vďaka hmotnosti sa pri dlhšej práci ovláda ľahšie ako iné nástroje, ktoré som používal.”",
    "r1n": "Peter K.", "r1c": "Nitra",
    "r2n": "Elena V.", "r2c": "Prešov",
    "r3n": "Marek S.", "r3c": "Banská Bystrica",
    "ph1": "Súprava Iron Oak Pro na stole po vybalení",
    "ph2": "Objednávka Iron Oak Pro po otvorení doma",
    "ph3": "Montáž reťazovej píly Iron Oak Pro",
    "faq_eye": "Často kladené otázky", "faq_h2": "PRED OBJEDNÁVKOU BY STE MALI VEDIEŤ…",
    "faq_p": "Odpovede o batériách, reze, platbe, doručení, vrátení a záruke.",
    "faq": [
      ("Ako dlho vydržia batérie?", "Spolu až osem hodín. Rýchlonabíjačka ich nabije približne za hodinu. Reálna výdrž závisí od hrúbky a druhu dreva, tlaku rezu, teploty a stavu batérií."),
      ("Zvládne kmene 40 cm?", "Maximálna deklarovaná kapacita je až 40 cm. Tvrdosť dreva, technika a údržba ovplyvňujú výsledok."),
      ("Musím platiť teraz?", "Nie. Platba je na dobierku: objednávku potvrdíme telefonicky a zaplatíte kuriérovi pri prevzatí."),
      ("Čo presne obsahuje?", "Pílu, dve batérie, nabíjačku, dve reťaze, náradie, kufrík, okuliare, návod a rukavice zadarmo."),
      ("Môžem ju vrátiť?", "Áno, do 30 dní podľa <a href=\"/sk/refund-policy.html\">pravidiel vrátenia peňazí</a>."),
      ("Aká je záruka?", "Zákonná záruka 24 mesiacov od dodania."),
    ],
    "cta_h2": "IRON OAK PRO ZA 79,00 €",
    "cta_p": "Kompletný kit, zľava 50 % a platba pri prevzatí. Ponuka platí do vypredania zásob a po potvrdení.",
    "cta_btn": "OBJEDNAŤ TERAZ →",
    "foot_p": "Akumulátorový nástroj na rezanie a údržbu exteriéru.",
    "help": "Pomoc", "legal": "Právne info",
    "a_order": "Objednať", "a_ship": "Doprava", "a_contact": "Kontakt",
    "a_priv": "Ochrana údajov", "a_cook": "Cookies", "a_terms": "Obchodné podmienky",
    "a_about": "O nás", "cookie_btn": "Zmeniť nastavenia cookies",
    "rights": "Všetky práva vyhradené. *Výdrž, rez a dodanie závisia od dreva a telefonického potvrdenia objednávky.",
    "sticky": "OBJEDNAŤ IRON OAK PRO · 79,00 €",
    "msg_name": "Zadajte meno a priezvisko.",
    "msg_addr": "Zadajte adresu doručenia.",
    "msg_tel": "Zadajte platné slovenské telefónne číslo.",
    "msg_generic": "Objednávku sa nepodarilo odoslať. Skúste to znova.",
    "phone_js": PHONE_SK,
    "form_extra": '<input name="subid" id="subid" type="hidden" value="">\n          <input name="tmfp" id="tmfp" type="hidden" value="">',
    "tmfp": True,
    "href_about": "/sk/about-us.html", "href_contact": "/sk/contact-us.html",
    "href_ship": "/sk/shipping-policy.html", "href_refund": "/sk/refund-policy.html",
    "href_priv": "/sk/privacy-policy.html", "href_cook": "/sk/cookie-policy.html",
    "href_terms": "/sk/terms-conditions.html",
  },
  "pl": {
    "lang": "pl", "locale": "pl-PL", "geo": "pl", "slug": "vortek-1429",
    "currency": "PLN", "price_num": 299.00, "offer_id": "3231", "lp": "3265",
    "offer_name": "Iron Oak Pro PL 3231 (CPL)", "lp_id": "pl-vortek-1429",
    "key": "1055c1f6b7009e802d0e7b9d23d7f5ba7155307e", "webhook": WEBHOOK_DEFAULT,
    "price": "299,00 zł", "old": "598,00 zł", "save": "OSZCZĘDZASZ 299 zł",
    "submitting": "Wysyłanie…",
    "cookie_text": "Używamy technicznych plików cookie i plików cookie podmiotów trzecich, aby poprawić wygodę korzystania z serwisu i prowadzić analizy.",
    "cookie_accept": "Akceptuję", "cookie_learn": "Dowiedz się więcej",
    "title": "Iron Oak Pro™ — kompletny zestaw z 50% rabatu",
    "desc": "Iron Oak Pro: pilarka łańcuchowa akumulatorowa z silnikiem bezszczotkowym, dwoma akumulatorami i kompletnym zestawem. 50% rabatu i płatność przy odbiorze.",
    "announce": "<strong>50% RABATU</strong> · 598,00 zł → 299,00 zł · PŁATNOŚĆ PRZY ODBIORZE",
    "ship": "Dostawa 24–48 h*", "cod": "Płatność przy odbiorze",
    "rating": "Ocena klientów*",
    "eyebrow": "Profesjonalna pilarka akumulatorowa",
    "h1": "SKOŃCZ PRACĘ. <em>NIE BATERII.</em>",
    "lead": "Silnik bezszczotkowy 1500 W, dwa akumulatory i kompletny zestaw do cięcia pni i gałęzi bez kabla i benzyny.",
    "p1": "<strong>Do 8 godzin łącznie*</strong> z dwoma akumulatorami w zestawie.",
    "p2": "<strong>Deklarowana średnica do 40 cm*</strong> w zależności od drewna i warunków.",
    "p3": "<strong>Tylko 2,4 kg*</strong> z prowadnicą i akumulatorem.",
    "p4": "<strong>Automatyczne smarowanie i napinanie*</strong>, mniej przerw.",
    "p5": "<strong>Rękawice w prezencie</strong> w zestawie.",
    "hero_alt": "Kompletny zestaw pilarki Iron Oak Pro z akumulatorami, łańcuchami, ładowarką, walizką i rękawicami",
    "badge_small": "OFERTA",
    "pack_label": "KOMPLETNY ZESTAW W CENIE",
    "pack_small": "2 akumulatory · 2 łańcuchy · walizka · rękawice w prezencie",
    "form_eye": "Oferta startowa",
    "form_h2": "ZAMÓW IRON OAK PRO",
    "form_p": "Nie płacisz teraz. Potwierdzimy zamówienie telefonicznie i zapłacisz przy odbiorze.",
    "step1": "Krok 1 z 2", "step2": "Krok 2 z 2", "secure": "Bezpieczne zamówienie",
    "err": "Sprawdź zaznaczone pola, aby kontynuować.",
    "lbl_name": "Imię i nazwisko", "ph_name": "Np. Jan Kowalski",
    "lbl_tel": "Telefon", "ph_tel": "Np. 600 123 456",
    "next": "KONTYNUUJ ZAMÓWIENIE →",
    "micro1": "Zadzwonimy raz, aby potwierdzić dane i adres.",
    "lbl_addr": "Adres dostawy", "ph_addr": "Ulica, numer, mieszkanie",
    "lbl_postal": "Kod pocztowy", "ph_postal": "00-001", "postal_pattern": "",
    "lbl_city": "Miejscowość", "ph_city": "Warszawa",
    "lbl_prov": "Województwo", "ph_prov": "mazowieckie",
    "submit": "POTWIERDŹ ZAMÓWIENIE · 299,00 zł",
    "back": "← Wstecz",
    "micro2": "Potwierdzając, akceptujesz <a href=\"/pl/terms-conditions.html\">regulamin</a> i <a href=\"/pl/privacy-policy.html\">politykę prywatności</a>.",
    "t1b": "Rabat −50%", "t1s": "598,00 zł → 299,00 zł",
    "t2b": "Płatność przy odbiorze", "t2s": "Bez płatności z góry",
    "t3b": "Dostawa 24–48 h*", "t3s": "Po potwierdzeniu telefonicznym",
    "t4b": "30 dni*", "t4s": "Zwrot towaru",
    "prob_eye": "Praca bez zwykłych ograniczeń",
    "prob_h2": "JEDNO NARZĘDZIE. CAŁY DZIEŃ.",
    "prob_p": "Iron Oak Pro łączy silnik bezszczotkowy z dwoma wymiennymi akumulatorami. Gdy jeden się wyczerpie, wkładasz drugi i jedziesz dalej.",
    "m1b": "1 500 W*", "m1s": "Deklarowana moc silnika bezszczotkowego.",
    "m2b": "2 AKUMULATORY", "m2s": "W zestawie do zmiany podczas pracy.",
    "m3b": "40 CM*", "m3s": "Maksymalna deklarowana średnica w zależności od drewna.",
    "feat_eye": "Zaprojektowana, by iść do przodu",
    "feat_h2": "MNIEJ PRZESTOJÓW. WIĘCEJ ZROBIONEJ PRACY.",
    "feat_p": "Trzy powody, dla których zestaw Iron Oak Pro jest do cięcia i pielęgnacji ogrodu.",
    "f1t": "SILNIK BEZSZCZOTKOWY 1 500 W*",
    "f1p": "Do stałego cięcia i mniejszego przegrzewania przy dłuższym użyciu. Rzeczywista moc cięcia zależy od drewna, łańcucha i stanu naładowania.",
    "f1c1": "Silnik bezszczotkowy", "f1c2": "Odprowadzanie ciepła", "f1c3": "Praca w ogrodzie",
    "f1alt": "Cięcie pnia pilarką Iron Oak Pro",
    "f2t": "DWA AKUMULATORY, ŻEBY CIĄĆ DALEJ",
    "f2p": "Dwa akumulatory w zestawie dają łącznie do ośmiu godzin i pełne ładowanie w około godzinę. Rzeczywista praca zależy od rodzaju i grubości drewna.",
    "f2c1": "2 akumulatory", "f2c2": "Szybka wymiana", "f2c3": "Ładowarka w zestawie",
    "f2alt": "Wymiana akumulatora Iron Oak Pro przy ładowarce",
    "f3t": "AUTOMATYCZNE SMAROWANIE I NAPINANIE*",
    "f3p": "Zbiornik oleju i układ, który koryguje napięcie łańcucha, żeby rzadziej się zatrzymywać. Zawsze stosuj się do instrukcji producenta.",
    "f3c1": "2 łańcuchy", "f3c2": "Zbiornik oleju", "f3c3": "Regulacja automatyczna*",
    "f3alt": "Konserwacja i łańcuch pilarki Iron Oak Pro",
    "cmp_eye": "Rzetelne porównanie",
    "cmp_h2": "IRON OAK PRO WOBEC MODELU PODSTAWOWEGO",
    "cmp_p": "Porównanie zestawu Iron Oak Pro z podstawową pilarką ogrodową.",
    "cmp_h": "Cecha", "cmp_a": "Iron Oak Pro", "cmp_b": "Model podstawowy",
    "c1": "Akumulatory w zestawie", "c1a": "✓ 2 sztuki", "c1b": "Zazwyczaj 1",
    "c2": "Ładowarka", "c2a": "✓ W zestawie", "c2b": "Różnie",
    "c3": "Łańcuchy w zestawie", "c3a": "✓ 2 sztuki", "c3b": "Zazwyczaj 1",
    "c4": "Walizka i ochrona", "c4a": "✓ W zestawie", "c4b": "Różnie",
    "c5": "Płatność przy odbiorze", "c5a": "✓ Dostępna", "c5b": "Różnie",
    "pack_eye": "Wszystko w zestawie",
    "pack_h2": "OTWÓRZ WALIZKĘ I ZACZNIJ PRACĘ.",
    "pack_alt": "Pełna zawartość zestawu Iron Oak Pro",
    "li1": "1 pilarka Iron Oak Pro", "li2": "2 akumulatory litowe", "li3": "1 szybka ładowarka",
    "li4": "2 łańcuchy i akcesoria montażowe", "li5": "1 walizka transportowa",
    "li6": "Rękawice w prezencie, okulary i instrukcja",
    "safety": "<strong>Bezpieczeństwo:</strong> zawsze używaj ochrony oczu, rękawic i odpowiedniego sprzętu. Przeczytaj całą instrukcję i nie używaj narzędzia, jeśli nie jesteś przygotowany do obsługi pilarki łańcuchowej.",
    "rev_eye": "Opinie", "rev_h2": "CO MÓWIĄ OSOBY, KTÓRE JUŻ JEJ UŻYWAJĄ.",
    "rev_note": "Opinie klientów o użytkowaniu Iron Oak Pro. Czas pracy i cięcie zależą od drewna i warunków.",
    "q1": "“Pociąłem drewno na zimę i skończyłem ogród bez czekania na kolejne ładowanie.”",
    "q2": "“Zaskoczyło mnie, że radzi sobie z grubszymi pniami przy prostym prowadzeniu.”",
    "q3": "“Waga sprawia, że przy dłuższej pracy jest wygodniejsza niż inne narzędzia, których używałem.”",
    "r1n": "Piotr K.", "r1c": "Kraków",
    "r2n": "Ewa W.", "r2c": "Wrocław",
    "r3n": "Marek S.", "r3c": "Poznań",
    "ph1": "Zestaw Iron Oak Pro na stole po rozpakowaniu",
    "ph2": "Zamówienie Iron Oak Pro po otwarciu w domu",
    "ph3": "Montaż pilarki Iron Oak Pro",
    "faq_eye": "Najczęstsze pytania", "faq_h2": "ZANIM ZAMÓWISZ, MUSISZ WIEDZIEĆ…",
    "faq_p": "Odpowiedzi o akumulatorach, cięciu, płatności, dostawie, zwrotach i gwarancji.",
    "faq": [
      ("Jak długo działają akumulatory?", "Razem do ośmiu godzin. Szybka ładowarka ładuje je w około godzinę. Rzeczywisty czas zależy od grubości i rodzaju drewna, nacisku cięcia, temperatury i stanu akumulatorów."),
      ("Czy przetnie pnie 40 cm?", "Maksymalna deklarowana średnica to do 40 cm. Twardość drewna, technika i konserwacja wpływają na efekt."),
      ("Czy muszę płacić teraz?", "Nie. Płatność przy odbiorze: potwierdzamy zamówienie telefonicznie i płacisz kurierowi przy odbiorze."),
      ("Co dokładnie zawiera zestaw?", "Pilarkę, dwa akumulatory, ładowarkę, dwa łańcuchy, narzędzia, walizkę, okulary, instrukcję i rękawice w prezencie."),
      ("Czy mogę zwrócić?", "Tak, w ciągu 30 dni zgodnie z <a href=\"/pl/refund-policy.html\">polityką zwrotów</a>."),
      ("Jaka jest gwarancja?", "24-miesięczna gwarancja zgodności od dostawy."),
    ],
    "cta_h2": "IRON OAK PRO ZA 299,00 ZŁ",
    "cta_p": "Kompletny zestaw, 50% rabatu i płatność przy odbiorze. Oferta do wyczerpania zapasów i po potwierdzeniu.",
    "cta_btn": "ZAMÓW TERAZ →",
    "foot_p": "Narzędzie akumulatorowe do cięcia i prac na zewnątrz.",
    "help": "Pomoc", "legal": "Informacje prawne",
    "a_order": "Złóż zamówienie", "a_ship": "Dostawa", "a_contact": "Kontakt",
    "a_priv": "Prywatność", "a_cook": "Cookies", "a_terms": "Regulamin",
    "a_about": "O nas", "cookie_btn": "Zmień ustawienia cookies",
    "rights": "Wszelkie prawa zastrzeżone. *Czas pracy, cięcie i dostawa zależą od drewna i potwierdzenia zamówienia.",
    "sticky": "ZAMÓW IRON OAK PRO · 299,00 zł",
    "msg_name": "Wpisz imię i nazwisko.",
    "msg_addr": "Wpisz adres dostawy.",
    "msg_tel": "Wpisz prawidłowy polski numer telefonu.",
    "msg_generic": "Nie udało się wysłać zamówienia. Spróbuj ponownie.",
    "phone_js": PHONE_PL,
    "form_extra": "",
    "tmfp": False,
    "href_about": "/pl/about-us.html", "href_contact": "/pl/contact-us.html",
    "href_ship": "/pl/shipping-policy.html", "href_refund": "/pl/refund-policy.html",
    "href_priv": "/pl/privacy-policy.html", "href_cook": "/pl/cookie-policy.html",
    "href_terms": "/pl/terms-conditions.html",
  },
  "lt": {
    "lang": "lt", "locale": "lt-LT", "geo": "lt", "slug": "vortek-1427",
    "currency": "EUR", "price_num": 64.00, "offer_id": "1427", "lp": "1447",
    "offer_name": "Iron Oak Pro LT 1427 (CPL)", "lp_id": "lt-vortek-1427",
    "key": "cf9544082451f75dbf9e71e33c8f842f15fdbfb9", "webhook": WEBHOOK_DEFAULT,
    "price": "64,00 €", "old": "128,00 €", "save": "SUTAUPOTE 64 €",
    "submitting": "Siunčiama…",
    "cookie_text": "Naudojame techninius ir trečiųjų šalių slapukus jūsų patirčiai gerinti bei analitikos tikslais.",
    "cookie_accept": "Sutikti", "cookie_learn": "Sužinoti daugiau",
    "title": "Iron Oak Pro™ — visas rinkinys su 50 % nuolaida",
    "desc": "Iron Oak Pro: akumuliatorinis grandininis pjūklas su bešepetėliu varikliu, dviem akumuliatoriais ir visu rinkiniu. 50 % nuolaida ir apmokėjimas pristatymo metu.",
    "announce": "<strong>50 % NUOLAIDA</strong> · 128,00 € → 64,00 € · APMOKĖJIMAS GAVUS",
    "ship": "Pristatymas 24–48 val.*", "cod": "Apmokėjimas gavus",
    "rating": "Klientų įvertinimas*",
    "eyebrow": "Profesionalus akumuliatorinis grandininis pjūklas",
    "h1": "BAIKITE DARBĄ. <em>NE AKUMULIATORIŲ.</em>",
    "lead": "1 500 W bešepetėlis variklis, du akumuliatoriai ir visas rinkinys kamienams ir šakoms pjauti be laido ir benzino.",
    "p1": "<strong>Iki 8 valandų kartu*</strong> su dviem akumuliatoriais rinkinyje.",
    "p2": "<strong>Deklaruojamas pjovimas iki 40 cm*</strong> pagal medieną ir naudojimo sąlygas.",
    "p3": "<strong>Tik 2,4 kg*</strong> su juosta ir akumuliatoriumi.",
    "p4": "<strong>Automatinis tepimas ir įtempimas*</strong>, mažiau pertraukų.",
    "p5": "<strong>Pirštinės dovanų</strong> rinkinyje.",
    "hero_alt": "Visas Iron Oak Pro pjūklo rinkinys su akumuliatoriais, grandinėmis, krovikliu, lagaminu ir pirštinėmis",
    "badge_small": "PASIŪLYMAS",
    "pack_label": "VISAS RINKINYS ĮSKAIČIUOTAS",
    "pack_small": "2 akumuliatoriai · 2 grandinės · lagaminas · pirštinės dovanų",
    "form_eye": "Įvadinis pasiūlymas",
    "form_h2": "UŽSISAKYKITE IRON OAK PRO",
    "form_p": "Dabar nemokate. Užsakymą patvirtinsime telefonu, o mokėsite gavę.",
    "step1": "1 žingsnis iš 2", "step2": "2 žingsnis iš 2", "secure": "Saugus užsakymas",
    "err": "Patikrinkite pažymėtus laukus ir tęskite.",
    "lbl_name": "Vardas Pavardė", "ph_name": "Pvz. Jonas Kazlauskas",
    "lbl_tel": "Telefonas", "ph_tel": "Pvz. 612 34567",
    "next": "TĘSTI UŽSAKYMĄ →",
    "micro1": "Paskambinsime vieną kartą duomenims ir adresui patvirtinti.",
    "lbl_addr": "Pristatymo adresas", "ph_addr": "Gatvė, numeris, butas",
    "lbl_postal": "Pašto kodas", "ph_postal": "01100", "postal_pattern": "",
    "lbl_city": "Miestas", "ph_city": "Vilnius",
    "lbl_prov": "Apskritis", "ph_prov": "Vilniaus apskritis",
    "submit": "PATVIRTINTI UŽSAKYMĄ · 64,00 €",
    "back": "← Atgal",
    "micro2": "Patvirtindami sutinkate su <a href=\"/lt/terms-conditions.html\">sąlygomis</a> ir <a href=\"/lt/privacy-policy.html\">privatumo politika</a>.",
    "t1b": "Nuolaida −50%", "t1s": "128,00 € → 64,00 €",
    "t2b": "Apmokėjimas gavus", "t2s": "Be išankstinio mokėjimo",
    "t3b": "Pristatymas 24–48 val.*", "t3s": "Po patvirtinimo telefonu",
    "t4b": "30 dienų*", "t4s": "Grąžinimo politika",
    "prob_eye": "Dirbkite be įprastų apribojimų",
    "prob_h2": "VIENAS ĮRANKIS. VISA DIENA.",
    "prob_p": "Iron Oak Pro jungia bešepetėlį variklį su dviem keičiamais akumuliatoriais. Vienam išsekus, įstatote kitą ir tęsiate.",
    "m1b": "1 500 W*", "m1s": "Deklaruojama bešepetėlio variklio galia.",
    "m2b": "2 AKUMULIATORIAI", "m2s": "Rinkinyje keisti darbo metu.",
    "m3b": "40 CM*", "m3s": "Didžiausias deklaruojamas skersmuo pagal medieną.",
    "feat_eye": "Sukurta judėti pirmyn",
    "feat_h2": "MAŽIAU SUSTOJIMŲ. DAUGIAU ATLIKTO DARBO.",
    "feat_p": "Trys priežastys, kodėl Iron Oak Pro rinkinys skirtas sodo pjovimui ir priežiūrai.",
    "f1t": "BEŠEPETĖLIS VARIKLIS 1 500 W*",
    "f1p": "Skirtas pastoviam pjovimui ir mažesniam perkaitimui ilgai naudojant. Tikroji pjovimo galia priklauso nuo medienos, grandinės ir įkrovos.",
    "f1c1": "Bešepetėlis variklis", "f1c2": "Šilumos nuvedimas", "f1c3": "Darbas sode",
    "f1alt": "Kamieno pjovimas Iron Oak Pro pjūklu",
    "f2t": "DU AKUMULIATORIAI, KAD PJAUTUMĖTE TOLIAU",
    "f2p": "Du akumuliatoriai rinkinyje kartu iki aštuonių valandų, o pilnas įkrovimas apie valandą. Tikroji trukmė priklauso nuo medienos rūšies ir storio.",
    "f2c1": "2 akumuliatoriai", "f2c2": "Greitas keitimas", "f2c3": "Kroviklis rinkinyje",
    "f2alt": "Iron Oak Pro akumuliatoriaus keitimas prie kroviklio",
    "f3t": "AUTOMATINIS TEPIMAS IR ĮTEMPIMAS*",
    "f3p": "Alyvos bakelis ir sistema, reguliuojanti grandinės įtempimą, kad rečiau stabdytumėte. Visada laikykitės gamintojo nurodymų.",
    "f3c1": "2 grandinės", "f3c2": "Alyvos bakelis", "f3c3": "Automatinis reguliavimas*",
    "f3alt": "Iron Oak Pro priežiūra ir grandinė",
    "cmp_eye": "Objektyvus palyginimas",
    "cmp_h2": "IRON OAK PRO PRIEŠ PAGRINDINĮ MODELĮ",
    "cmp_p": "Iron Oak Pro rinkinio palyginimas su paprastu sodo pjūklu.",
    "cmp_h": "Savybė", "cmp_a": "Iron Oak Pro", "cmp_b": "Pagrindinis modelis",
    "c1": "Akumuliatoriai rinkinyje", "c1a": "✓ 2 vnt.", "c1b": "Paprastai 1",
    "c2": "Kroviklis", "c2a": "✓ Įskaičiuotas", "c2b": "Skirtingai",
    "c3": "Grandinės rinkinyje", "c3a": "✓ 2 vnt.", "c3b": "Paprastai 1",
    "c4": "Lagaminas ir apsauga", "c4a": "✓ Įskaičiuota", "c4b": "Skirtingai",
    "c5": "Apmokėjimas gavus", "c5a": "✓ Galima", "c5b": "Skirtingai",
    "pack_eye": "Viskas įskaičiuota",
    "pack_h2": "ATIDARYKITE LAGAMINĄ IR PRADĖKITE DIRBTI.",
    "pack_alt": "Visas Iron Oak Pro rinkinio turinys",
    "li1": "1 Iron Oak Pro grandininis pjūklas", "li2": "2 ličio akumuliatoriai", "li3": "1 greitasis kroviklis",
    "li4": "2 grandinės ir montavimo priedai", "li5": "1 transportavimo lagaminas",
    "li6": "Pirštinės dovanų, akiniai ir vadovas",
    "safety": "<strong>Sauga:</strong> visada naudokite akių apsaugą, pirštines ir tinkamą įrangą. Perskaitykite visą vadovą ir nenaudokite įrankio, jei nesate pasirengę valdyti grandininio pjūklo.",
    "rev_eye": "Atsiliepimai", "rev_h2": "KĄ SAKO JAU NAUDOJANTYS.",
    "rev_note": "Klientų patirtis su Iron Oak Pro. Veikimo laikas ir pjovimas priklauso nuo medienos ir sąlygų.",
    "q1": "“Sukapojau malkas žiemai ir baigiau sodą nelaukdamas kito įkrovimo.”",
    "q2": "“Nustebino, kad susitvarko su storesniais kamienais ir vis tiek paprasta valdyti.”",
    "q3": "“Dėl svorio ilgesniame darbe valdyti lengviau nei kitus įrankius, kuriuos naudojau.”",
    "r1n": "Petras K.", "r1c": "Kaunas",
    "r2n": "Rasa V.", "r2c": "Klaipėda",
    "r3n": "Marius S.", "r3c": "Šiauliai",
    "ph1": "Iron Oak Pro rinkinys ant stalo išpakavus",
    "ph2": "Iron Oak Pro užsakymas atidarius namie",
    "ph3": "Iron Oak Pro pjūklo surinkimas",
    "faq_eye": "Dažnai užduodami klausimai", "faq_h2": "PRIEŠ UŽSAKYDAMI TURITE ŽINOTI…",
    "faq_p": "Atsakymai apie akumuliatorius, pjovimą, mokėjimą, pristatymą, grąžinimą ir garantiją.",
    "faq": [
      ("Kiek veikia akumuliatoriai?", "Kartu iki aštuonių valandų. Greitasis kroviklis įkrauna apie valandą. Tikroji trukmė priklauso nuo medienos storio ir rūšies, pjovimo spaudimo, temperatūros ir akumuliatorių būklės."),
      ("Ar pjauna 40 cm kamienus?", "Didžiausias deklaruojamas skersmuo – iki 40 cm. Medienos kietumas, technika ir priežiūra turi įtakos rezultatui."),
      ("Ar turiu mokėti dabar?", "Ne. Mokama pristatymo metu: užsakymą patvirtiname telefonu, o kurjeriui mokate gavę."),
      ("Kas tiksliai įeina?", "Pjūklas, du akumuliatoriai, kroviklis, dvi grandinės, įrankiai, lagaminas, akiniai, vadovas ir pirštinės dovanų."),
      ("Ar galiu grąžinti?", "Taip, per 30 dienų pagal <a href=\"/lt/refund-policy.html\">grąžinimo politiką</a>."),
      ("Kokia garantija?", "24 mėnesių atitikties garantija nuo pristatymo."),
    ],
    "cta_h2": "IRON OAK PRO UŽ 64,00 €",
    "cta_p": "Visas rinkinys, 50 % nuolaida ir apmokėjimas gavus. Pasiūlymas galioja, kol yra atsargų, ir po patvirtinimo.",
    "cta_btn": "UŽSISAKYTI DABAR →",
    "foot_p": "Akumuliatorinis įrankis pjovimui ir lauko priežiūrai.",
    "help": "Pagalba", "legal": "Teisinė informacija",
    "a_order": "Užsakyti", "a_ship": "Pristatymas", "a_contact": "Kontaktai",
    "a_priv": "Privatumas", "a_cook": "Slapukai", "a_terms": "Sąlygos",
    "a_about": "Apie mus", "cookie_btn": "Keisti slapukų nuostatas",
    "rights": "Visos teisės saugomos. *Veikimo laikas, pjovimas ir pristatymas priklauso nuo medienos ir užsakymo patvirtinimo.",
    "sticky": "UŽSISAKYKITE IRON OAK PRO · 64,00 €",
    "msg_name": "Įveskite vardą ir pavardę.",
    "msg_addr": "Įveskite pristatymo adresą.",
    "msg_tel": "Įveskite galiojantį Lietuvos telefono numerį.",
    "msg_generic": "Užsakymo pateikti nepavyko. Bandykite dar kartą.",
    "phone_js": PHONE_LT,
    "form_extra": "",
    "tmfp": False,
    "href_about": "/lt/about-us.html", "href_contact": "/lt/contact-us.html",
    "href_ship": "/lt/shipping-policy.html", "href_refund": "/lt/refund-policy.html",
    "href_priv": "/lt/privacy-policy.html", "href_cook": "/lt/cookie-policy.html",
    "href_terms": "/lt/terms-conditions.html",
  },
  "lv": {
    "lang": "lv", "locale": "lv-LV", "geo": "lv", "slug": "vortek-3518",
    "currency": "EUR", "price_num": 79.00, "offer_id": "3518", "lp": "3555",
    "offer_name": "Iron Oak Pro LV 3518 (CPL)", "lp_id": "lv-vortek-3518",
    "key": "1e5c10c79722473d548820a5fff1b60448ebb926", "webhook": WEBHOOK_DEFAULT,
    "price": "79,00 €", "old": "158,00 €", "save": "IEETAUPAT 79 €",
    "submitting": "Nosūta…",
    "cookie_text": "Mēs izmantojam tehniskās un trešo pušu sīkdatnes, lai uzlabotu tavu pieredzi un analītikas nolūkos.",
    "cookie_accept": "Pieņemt", "cookie_learn": "Uzzināt vairāk",
    "title": "Iron Oak Pro™ — pilns komplekts ar 50 % atlaidi",
    "desc": "Iron Oak Pro: akumulatora ķēdes zāģis ar bezsuku motoru, diviem akumulatoriem un pilnu komplektu. 50 % atlaide un apmaksa saņemot.",
    "announce": "<strong>50 % ATLAIDE</strong> · 158,00 € → 79,00 € · APMAKSA SAŅEMOT",
    "ship": "Piegāde 24–48 h*", "cod": "Apmaksa saņemot",
    "rating": "Klientu vērtējums*",
    "eyebrow": "Profesionāls akumulatora ķēdes zāģis",
    "h1": "PAVEIC DARBŪ. <em>NE AKUMULATORU.</em>",
    "lead": "1500 W bezsuku motors, divi akumulatori un pilns komplekts stumbru un zaru zāģēšanai bez vada un benzīna.",
    "p1": "<strong>Līdz 8 stundām kopā*</strong> ar abiem akumulatoriem komplektā.",
    "p2": "<strong>Deklarētais griezums līdz 40 cm*</strong> atkarībā no koksnes un lietošanas.",
    "p3": "<strong>Tikai 2,4 kg*</strong> ar sliedi un akumulatoru.",
    "p4": "<strong>Automātiska eļļošana un spriegošana*</strong>, mazāk paužu.",
    "p5": "<strong>Cimdi dāvanā</strong> komplektā.",
    "hero_alt": "Pilns Iron Oak Pro ķēdes zāģa komplekts ar akumulatoriem, ķēdēm, lādētāju, koferi un cimdiem",
    "badge_small": "PIEDĀVĀJUMS",
    "pack_label": "PILNS KOMPLEKTS IEKĻAUTS",
    "pack_small": "2 akumulatori · 2 ķēdes · koferis · cimdi dāvanā",
    "form_eye": "Ievada piedāvājums",
    "form_h2": "PASŪTI IRON OAK PRO",
    "form_p": "Tagad nemaksā. Pasūtījumu apstiprināsim pa tālruni, un maksāsi saņemot.",
    "step1": "1. solis no 2", "step2": "2. solis no 2", "secure": "Drošs pasūtījums",
    "err": "Pārbaudi iezīmētos laukus, lai turpinātu.",
    "lbl_name": "Vārds Uzvārds", "ph_name": "Piem. Jānis Bērziņš",
    "lbl_tel": "Tālrunis", "ph_tel": "Piem. 2612 3456",
    "next": "TURPINĀT PASŪTĪJUMU →",
    "micro1": "Piezvanīsim vienreiz, lai apstiprinātu datus un adresi.",
    "lbl_addr": "Piegādes adrese", "ph_addr": "Iela, numurs, dzīvoklis",
    "lbl_postal": "Pasta indekss", "ph_postal": "LV-1050", "postal_pattern": "",
    "lbl_city": "Pilsēta", "ph_city": "Rīga",
    "lbl_prov": "Novads", "ph_prov": "Rīga",
    "submit": "APSTIPRINĀT PASŪTĪJUMU · 79,00 €",
    "back": "← Atpakaļ",
    "micro2": "Apstiprinot, tu piekrīti <a href=\"/lv/terms-conditions.html\">noteikumiem</a> un <a href=\"/lv/privacy-policy.html\">privātuma politikai</a>.",
    "t1b": "Atlaide −50%", "t1s": "158,00 € → 79,00 €",
    "t2b": "Apmaksa saņemot", "t2s": "Bez priekšapmaksas",
    "t3b": "Piegāde 24–48 h*", "t3s": "Pēc apstiprinājuma pa tālruni",
    "t4b": "30 dienas*", "t4s": "Atgriešanas politika",
    "prob_eye": "Strādā bez ierastajiem ierobežojumiem",
    "prob_h2": "VIENS RĪKS. VISA DIENA.",
    "prob_p": "Iron Oak Pro apvieno bezsuku motoru ar diviem maināmiem akumulatoriem. Kad viens izsīkst, ieliec otru un turpini.",
    "m1b": "1 500 W*", "m1s": "Deklarētā bezsuku motora jauda.",
    "m2b": "2 AKUMULATORI", "m2s": "Komplektā, lai mainītu darba laikā.",
    "m3b": "40 CM*", "m3s": "Maksimālais deklarētais diametrs atkarībā no koksnes.",
    "feat_eye": "Radīts, lai virzītos uz priekšu",
    "feat_h2": "MAZĀK APTURĒŠANU. VAIRĀK PABEIGTA DARBA.",
    "feat_p": "Trīs iemesli, kāpēc Iron Oak Pro komplekts ir dārza zāģēšanai un kopšanai.",
    "f1t": "BEZSUKU MOTORS 1 500 W*",
    "f1p": "Paredzēts vienmērīgam griezumam un mazākai pārkaršanai ilgākā lietošanā. Reālā griešanas jauda atkarīga no koksnes, ķēdes un uzlādes.",
    "f1c1": "Bezsuku motors", "f1c2": "Siltuma novadīšana", "f1c3": "Darbs dārzā",
    "f1alt": "Stumbra zāģēšana ar Iron Oak Pro",
    "f2t": "DIVI AKUMULATORI, LAI ZĀĢĒTU TĀLĀK",
    "f2p": "Divi akumulatori komplektā kopā līdz astoņām stundām un pilna uzlāde aptuveni stundā. Reālais laiks atkarīgs no koksnes veida un biezuma.",
    "f2c1": "2 akumulatori", "f2c2": "Ātra maiņa", "f2c3": "Lādētājs komplektā",
    "f2alt": "Iron Oak Pro akumulatora maiņa pie lādētāja",
    "f3t": "AUTOMĀTISKA EĻĻOŠANA UN SPRIEGOŠANA*",
    "f3p": "Eļļas tvertne un sistēma, kas pielāgo ķēdes spriegojumu, lai retāk apstātos. Vienmēr ievēro ražotāja norādījumus.",
    "f3c1": "2 ķēdes", "f3c2": "Eļļas tvertne", "f3c3": "Automātiska regulēšana*",
    "f3alt": "Iron Oak Pro apkope un ķēde",
    "cmp_eye": "Objektīvs salīdzinājums",
    "cmp_h2": "IRON OAK PRO PRET PAMATA MODELI",
    "cmp_p": "Iron Oak Pro komplekta salīdzinājums ar pamata dārza zāģi.",
    "cmp_h": "Īpašība", "cmp_a": "Iron Oak Pro", "cmp_b": "Pamata modelis",
    "c1": "Akumulatori komplektā", "c1a": "✓ 2 gab.", "c1b": "Parasti 1",
    "c2": "Lādētājs", "c2a": "✓ Iekļauts", "c2b": "Atšķirīgi",
    "c3": "Ķēdes komplektā", "c3a": "✓ 2 gab.", "c3b": "Parasti 1",
    "c4": "Koferis un aizsardzība", "c4a": "✓ Iekļauts", "c4b": "Atšķirīgi",
    "c5": "Apmaksa saņemot", "c5a": "✓ Pieejama", "c5b": "Atšķirīgi",
    "pack_eye": "Viss iekļauts",
    "pack_h2": "ATVER KOFERI UN ĶERIES PIE DARBA.",
    "pack_alt": "Pilns Iron Oak Pro komplekta saturs",
    "li1": "1 Iron Oak Pro ķēdes zāģis", "li2": "2 litija akumulatori", "li3": "1 ātrais lādētājs",
    "li4": "2 ķēdes un montāžas piederumi", "li5": "1 transporta koferis",
    "li6": "Cimdi dāvanā, brilles un pamācība",
    "safety": "<strong>Drošība:</strong> vienmēr lieto acu aizsardzību, cimdus un piemērotu aprīkojumu. Izlasi visu pamācību un nelieto rīku, ja neesi sagatavots darbam ar ķēdes zāģi.",
    "rev_eye": "Atsauksmes", "rev_h2": "KO SAKA TIE, KAS TO JAU LIETO.",
    "rev_note": "Klientu pieredze ar Iron Oak Pro. Darbības laiks un griezums atkarīgi no koksnes un apstākļiem.",
    "q1": "“Sasagāju malku ziemai un pabeidzu dārzu, negaidot nākamo uzlādi.”",
    "q2": "“Pārsteidza, ka tiek galā ar resnākiem stumbriem un joprojām ir viegli vadāms.”",
    "q3": "“Svara dēļ ilgākā darbā tas ir ērtāks par citiem rīkiem, ko esmu lietojis.”",
    "r1n": "Pēteris K.", "r1c": "Liepāja",
    "r2n": "Elīna V.", "r2c": "Daugavpils",
    "r3n": "Māris S.", "r3c": "Jelgava",
    "ph1": "Iron Oak Pro komplekts uz galda pēc izpakošanas",
    "ph2": "Iron Oak Pro pasūtījums, atverot mājās",
    "ph3": "Iron Oak Pro zāģa montāža",
    "faq_eye": "Biežākie jautājumi", "faq_h2": "PIRMS PASŪTĪŠANAS TEV JĀZINA…",
    "faq_p": "Atbildes par akumulatoriem, griezumu, maksājumu, piegādi, atgriešanu un garantiju.",
    "faq": [
      ("Cik ilgi darbojas akumulatori?", "Kopā līdz astoņām stundām. Ātrais lādētājs tos uzlādē aptuveni stundā. Reālais laiks atkarīgs no koksnes biezuma un veida, griešanas spiediena, temperatūras un akumulatoru stāvokļa."),
      ("Vai zāģē 40 cm stumbrus?", "Maksimālais deklarētais diametrs ir līdz 40 cm. Koksnes cietība, tehnika un apkope ietekmē rezultātu."),
      ("Vai jāmaksā tagad?", "Nē. Apmaksa saņemot: pasūtījumu apstiprinām pa tālruni, un kurjeram maksā saņemot."),
      ("Kas tieši ir komplektā?", "Zāģis, divi akumulatori, lādētājs, divas ķēdes, instrumenti, koferis, brilles, pamācība un cimdi dāvanā."),
      ("Vai varu atgriezt?", "Jā, 30 dienu laikā saskaņā ar <a href=\"/lv/refund-policy.html\">atgriešanas politiku</a>."),
      ("Kāda ir garantija?", "24 mēnešu atbilstības garantija no piegādes."),
    ],
    "cta_h2": "IRON OAK PRO PAR 79,00 €",
    "cta_p": "Pilns komplekts, 50 % atlaide un apmaksa saņemot. Piedāvājums, kamēr ir krājumi, un pēc apstiprinājuma.",
    "cta_btn": "PASŪTĪT TAGAD →",
    "foot_p": "Akumulatora rīks zāģēšanai un āra kopšanai.",
    "help": "Palīdzība", "legal": "Juridiskā informācija",
    "a_order": "Pasūtīt", "a_ship": "Piegāde", "a_contact": "Kontakti",
    "a_priv": "Privātums", "a_cook": "Sīkdatnes", "a_terms": "Noteikumi",
    "a_about": "Par mums", "cookie_btn": "Mainīt sīkdatņu iestatījumus",
    "rights": "Visas tiesības aizsargātas. *Darbības laiks, griezums un piegāde atkarīgi no koksnes un pasūtījuma apstiprinājuma.",
    "sticky": "PASŪTĪT IRON OAK PRO · 79,00 €",
    "msg_name": "Ievadi vārdu un uzvārdu.",
    "msg_addr": "Ievadi piegādes adresi.",
    "msg_tel": "Ievadi derīgu Latvijas tālruņa numuru.",
    "msg_generic": "Pasūtījumu neizdevās nosūtīt. Mēģini vēlreiz.",
    "phone_js": PHONE_LV,
    "form_extra": "",
    "tmfp": False,
    "href_about": "/lv/about-us.html", "href_contact": "/lv/contact-us.html",
    "href_ship": "/lv/shipping-policy.html", "href_refund": "/lv/refund-policy.html",
    "href_priv": "/lv/privacy-policy.html", "href_cook": "/lv/cookie-policy.html",
    "href_terms": "/lv/terms-conditions.html",
  },
}


def faq_html(items):
    parts = []
    for q, a in items:
        parts.append(f"          <details><summary>{q}</summary><p>{a}</p></details>")
    return "\n".join(parts)


def render(L):
    thankyou = f"https://trendtopia-store.com/{L['geo']}/{L['slug']}/thank-you.html"
    canonical = f"https://trendtopia-store.com/{L['geo']}/{L['slug']}/landing.html"
    tmfp_js = ""
    if L["tmfp"]:
        tmfp_js = '<script src="https://offers.adricenetwork.com/forms/tmfp/" crossorigin="anonymous" defer></script>\n'
    subid_js = ""
    if L["tmfp"]:
        subid_js = """
  document.addEventListener('DOMContentLoaded', function () {
    var params = new URLSearchParams(window.location.search);
    var campaign = params.get('utm_campaign') || '';
    document.querySelectorAll('input[name="subid"]').forEach(function (el) { if (!el.value) el.value = campaign; });
  });"""
    extra = L["form_extra"]
    if extra:
        extra = "          " + extra + "\n"
    return f"""<!DOCTYPE html>
<html lang="{L['lang']}">
<head>
<!-- Google tag (gtag.js) -->
<script src="/assets/js/consent-default.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18327321473"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  window.SITE_CONFIG = window.SITE_CONFIG || {{}};
  window.SITE_CONFIG.GOOGLE_TAG_ID = window.SITE_CONFIG.GOOGLE_TAG_ID || 'AW-18327321473';
</script>
<meta charset="utf-8">
<meta name="robots" content="noindex, nofollow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#111715">
<meta name="description" content="{L['desc']}">
<meta name="contact" content="info@trendtopia-store.com">
<title>{L['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800;900&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="{L['lang']}" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<script>
window.SITE_CONFIG = {{
  GEO: '{L['geo']}',
  LOCALE: '{L['locale']}',
  PRODUCT_SLUG: '{L['slug']}',
  CURRENCY: '{L['currency']}',
  PRICE: {L['price_num']:.2f},
  OFFER_ID: '{L['offer_id']}',
  OFFER_NAME: '{L['offer_name']}',
  LP_ID: '{L['lp_id']}',
  FORM_ENDPOINT: 'https://offers.adricenetwork.com/forms/html/',
  SUBMITTING_LABEL: '{L['submitting']}',
  COOKIE_TEXT: {L['cookie_text']!r},
  COOKIE_ACCEPT: {L['cookie_accept']!r},
  COOKIE_LEARN: {L['cookie_learn']!r},
  GOOGLE_TAG_ID: 'AW-18327321473',
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
<style>
{CSS}
</style>
</head>
<body>
  <div class="announcement">{L['announce']}</div>

  <header class="hero" id="inicio">
    <div class="wrap topbar">
      <a class="logo" href="#inicio">IRON OAK <span>PRO</span></a>
      <div class="top-proof"><span><i></i>{L['ship']}</span><span>{L['cod']}</span></div>
    </div>

    <div class="wrap hero-grid">
      <div class="hero-copy">
        <div class="rating"><span class="stars">★★★★★</span><strong>4,6/5</strong><span>{L['rating']}</span></div>
        <p class="eyebrow">{L['eyebrow']}</p>
        <h1>{L['h1']}</h1>
        <p class="lead">{L['lead']}</p>
        <ul class="hero-points">
          <li><span>{L['p1']}</span></li>
          <li><span>{L['p2']}</span></li>
          <li><span>{L['p3']}</span></li>
          <li><span>{L['p4']}</span></li>
          <li><span>{L['p5']}</span></li>
        </ul>
        <div class="product-shot">
          <img src="/assets/img/products/vortek/hero.webp?v=4" alt="{L['hero_alt']}" width="1024" height="1024">
          <div class="discount-badge">−50%<small>{L['badge_small']}</small></div>
          <div class="pack-label">{L['pack_label']}<small>{L['pack_small']}</small></div>
        </div>
      </div>

      <aside class="order-card" id="pedido">
        <span class="eyebrow">{L['form_eye']}</span>
        <h2>{L['form_h2']}</h2>
        <p>{L['form_p']}</p>
        <div class="price-row"><span class="old-price">{L['old']}</span><span class="price">{L['price']}</span><span class="save">{L['save']}</span></div>
        <div class="step-top"><span id="stepLabel">{L['step1']}</span><span>{L['secure']}</span></div>
        <div class="progress"><span id="progressBar"></span></div>
        <form class="vk-form vk-order-form tm-order-form order-form" id="orderForm" action="https://offers.adricenetwork.com/forms/html/" method="post" novalidate>
          <div class="error" id="formError" role="alert">{L['err']}</div>
          <div class="form-step" id="step1">
            <div class="field"><label for="name">{L['lbl_name']}</label><input id="name" name="name" autocomplete="name" placeholder="{L['ph_name']}" required></div>
            <div class="field"><label for="tel">{L['lbl_tel']}</label><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="{L['ph_tel']}" required></div>
            <button class="btn" id="nextStep" type="button">{L['next']}</button>
            <p class="microcopy">{L['micro1']}</p>
          </div>

          <div class="form-step" id="step2" hidden>
            <div class="field"><label for="address">{L['lbl_addr']}</label><input id="address" name="street-address" autocomplete="street-address" placeholder="{L['ph_addr']}" required></div>
            <div class="fields-2"><div class="field"><label for="postal">{L['lbl_postal']}</label><input id="postal" name="postal" inputmode="numeric" autocomplete="postal-code" placeholder="{L['ph_postal']}"{L['postal_pattern']} required></div><div class="field"><label for="city">{L['lbl_city']}</label><input id="city" name="address-level2" autocomplete="address-level2" placeholder="{L['ph_city']}" required></div></div>
            <div class="field"><label for="province">{L['lbl_prov']}</label><input id="province" name="province" autocomplete="address-level1" placeholder="{L['ph_prov']}" required></div>
            <button class="btn" name="submit" type="submit">{L['submit']}</button>
            <button class="back" id="backStep" type="button">{L['back']}</button>
            <p class="microcopy">{L['micro2']}</p>
          </div>
{extra}          <input name="uid" type="hidden" value="{UID}">
          <input name="offer" type="hidden" value="{L['offer_id']}">
          <input name="lp" type="hidden" value="{L['lp']}">
          <input name="thankyoupage" type="hidden" value="{thankyou}">
          <input name="webhook" type="hidden" value="{L['webhook']}">
          <input name="_key" type="hidden" value="{L['key']}">
          <input type="hidden" name="product" value="Iron Oak Pro">
        </form>
      </aside>
    </div>
  </header>

  <div class="trust-strip" aria-label="{L['cod']}">
    <div class="wrap trust-grid">
      <div class="trust-item"><span class="trust-icon">50%</span><span><b>{L['t1b']}</b><small>{L['t1s']}</small></span></div>
      <div class="trust-item"><span class="trust-icon">€</span><span><b>{L['t2b']}</b><small>{L['t2s']}</small></span></div>
      <div class="trust-item"><span class="trust-icon">↗</span><span><b>{L['t3b']}</b><small>{L['t3s']}</small></span></div>
      <div class="trust-item"><span class="trust-icon">↩</span><span><b>{L['t4b']}</b><small>{L['t4s']}</small></span></div>
    </div>
  </div>

  <main>
    <section>
      <div class="wrap problem-grid">
        <div>
          <p class="eyebrow">{L['prob_eye']}</p>
          <h2>{L['prob_h2']}</h2>
          <p class="section-copy">{L['prob_p']}</p>
        </div>
        <div class="problem-card">
          <div class="problem-item"><b>{L['m1b']}</b><span>{L['m1s']}</span></div>
          <div class="problem-item"><b>{L['m2b']}</b><span>{L['m2s']}</span></div>
          <div class="problem-item"><b>{L['m3b']}</b><span>{L['m3s']}</span></div>
        </div>
      </div>
    </section>

    <section class="features">
      <div class="wrap">
        <p class="eyebrow">{L['feat_eye']}</p>
        <h2>{L['feat_h2']}</h2>
        <p class="section-copy">{L['feat_p']}</p>

        <article class="feature-row"><div class="feature-media"><img src="/assets/img/products/vortek/feature-battery-swap.webp?v=4" alt="{L['f1alt']}" width="1024" height="768"></div><div class="feature-body"><span class="feature-no">01</span><h3>{L['f1t']}</h3><p>{L['f1p']}</p><div class="chips"><span class="chip">{L['f1c1']}</span><span class="chip">{L['f1c2']}</span><span class="chip">{L['f1c3']}</span></div></div></article>
        <article class="feature-row"><div class="feature-media"><img src="/assets/img/products/vortek/feature-one-handed.webp?v=2" alt="{L['f2alt']}" width="1024" height="768"></div><div class="feature-body"><span class="feature-no">02</span><h3>{L['f2t']}</h3><p>{L['f2p']}</p><div class="chips"><span class="chip">{L['f2c1']}</span><span class="chip">{L['f2c2']}</span><span class="chip">{L['f2c3']}</span></div></div></article>
        <article class="feature-row"><div class="feature-media"><img src="/assets/img/products/vortek/feature-spare-chain.webp?v=1" alt="{L['f3alt']}" width="1024" height="768"></div><div class="feature-body"><span class="feature-no">03</span><h3>{L['f3t']}</h3><p>{L['f3p']}</p><div class="chips"><span class="chip">{L['f3c1']}</span><span class="chip">{L['f3c2']}</span><span class="chip">{L['f3c3']}</span></div></div></article>
      </div>
    </section>

    <section>
      <div class="wrap">
        <p class="eyebrow">{L['cmp_eye']}</p>
        <h2>{L['cmp_h2']}</h2>
        <p class="section-copy">{L['cmp_p']}</p>
        <div class="comparison" role="table" aria-label="{L['cmp_h2']}">
          <div class="compare-row compare-head"><div>{L['cmp_h']}</div><div>{L['cmp_a']}</div><div>{L['cmp_b']}</div></div>
          <div class="compare-row"><div>{L['c1']}</div><div class="yes">{L['c1a']}</div><div class="maybe">{L['c1b']}</div></div>
          <div class="compare-row"><div>{L['c2']}</div><div class="yes">{L['c2a']}</div><div>{L['c2b']}</div></div>
          <div class="compare-row"><div>{L['c3']}</div><div class="yes">{L['c3a']}</div><div>{L['c3b']}</div></div>
          <div class="compare-row"><div>{L['c4']}</div><div class="yes">{L['c4a']}</div><div>{L['c4b']}</div></div>
          <div class="compare-row"><div>{L['c5']}</div><div class="yes">{L['c5a']}</div><div>{L['c5b']}</div></div>
        </div>
      </div>
    </section>

    <section class="pack">
      <div class="wrap pack-grid">
        <div class="pack-image"><img src="/assets/img/products/vortek/hero.webp?v=4" alt="{L['pack_alt']}" width="1024" height="1024"></div>
        <div><p class="eyebrow">{L['pack_eye']}</p><h2>{L['pack_h2']}</h2><ul class="pack-list"><li>{L['li1']}</li><li>{L['li2']}</li><li>{L['li3']}</li><li>{L['li4']}</li><li>{L['li5']}</li><li>{L['li6']}</li></ul><div class="safety">{L['safety']}</div></div>
      </div>
    </section>

    <section class="reviews">
      <div class="wrap">
        <div class="review-head"><div><p class="eyebrow">{L['rev_eye']}</p><h2>{L['rev_h2']}</h2></div><div class="review-note">{L['rev_note']}</div></div>
        <div class="review-grid">
          <article class="review">
            <img class="review-photo" src="/assets/img/products/vortek/review-unbox-kit.webp?v=1" alt="{L['ph1']}" width="1024" height="768" loading="lazy">
            <div class="review-body">
              <div class="stars">★★★★★</div>
              <blockquote>{L['q1']}</blockquote>
              <div class="review-user"><img src="/assets/img/products/vortek/review-avatar-l.webp" alt="" width="92" height="92"><span><b>{L['r1n']}</b><small>{L['r1c']}</small></span></div>
            </div>
          </article>
          <article class="review">
            <img class="review-photo" src="/assets/img/products/vortek/review-unbox-box.webp?v=1" alt="{L['ph2']}" width="1024" height="768" loading="lazy">
            <div class="review-body">
              <div class="stars">★★★★★</div>
              <blockquote>{L['q2']}</blockquote>
              <div class="review-user"><img src="/assets/img/products/vortek/review-avatar-a.webp" alt="" width="92" height="92"><span><b>{L['r2n']}</b><small>{L['r2c']}</small></span></div>
            </div>
          </article>
          <article class="review">
            <img class="review-photo" src="/assets/img/products/vortek/review-unbox-hands.webp?v=1" alt="{L['ph3']}" width="1024" height="768" loading="lazy">
            <div class="review-body">
              <div class="stars">★★★★☆</div>
              <blockquote>{L['q3']}</blockquote>
              <div class="review-user"><img src="/assets/img/products/vortek/review-avatar-m.webp" alt="" width="92" height="92"><span><b>{L['r3n']}</b><small>{L['r3c']}</small></span></div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap faq-grid">
        <div><p class="eyebrow">{L['faq_eye']}</p><h2>{L['faq_h2']}</h2><p class="section-copy">{L['faq_p']}</p></div>
        <div class="faq-list">
{faq_html(L['faq'])}
        </div>
      </div>
    </section>

    <section class="final-cta">
      <div class="wrap cta-box"><div><h2>{L['cta_h2']}</h2><p>{L['cta_p']}</p></div><a class="btn" href="#pedido">{L['cta_btn']}</a></div>
    </section>
  </main>

  <footer>
    <div class="wrap">
      <div class="footer-grid">
        <div><a class="logo" href="#inicio">IRON OAK <span>PRO</span></a><p>{L['foot_p']}</p><p>{COMPANY}<br>{ADDR}<br><a href="mailto:info@trendtopia-store.com">info@trendtopia-store.com</a></p></div>
        <div><h3>{L['help']}</h3><a href="#pedido">{L['a_order']}</a><a href="{L['href_ship']}">{L['a_ship']}</a><a href="{L['href_contact']}">{L['a_contact']}</a></div>
        <div><h3>{L['legal']}</h3><a href="{L['href_priv']}">{L['a_priv']}</a><a href="{L['href_cook']}">{L['a_cook']}</a><a href="{L['href_terms']}">{L['a_terms']}</a><a href="{L['href_about']}">{L['a_about']}</a><button type="button" class="tt-cookie-change-link">{L['cookie_btn']}</button></div>
      </div>
      <p style="margin:25px 0 0">© <span id="year"></span> {COMPANY} — {L['rights']}</p>
    </div>
  </footer>

  <div class="sticky"><a class="btn" href="#pedido">{L['sticky']}</a></div>

<script>
(function () {{
  document.getElementById('year').textContent = new Date().getFullYear();
  var form = document.getElementById('orderForm');
  var step1 = document.getElementById('step1');
  var step2 = document.getElementById('step2');
  var progressBar = document.getElementById('progressBar');
  var stepLabel = document.getElementById('stepLabel');
  var error = document.getElementById('formError');
  var MSGS = {{
    name: {L['msg_name']!r},
    address: {L['msg_addr']!r},
    tel: {L['msg_tel']!r},
    generic: {L['msg_generic']!r},
    submitting: {L['submitting']!r}
  }};
{L['phone_js']}
  function errId(input) {{ return input.id + '-error'; }}
  function validateInput(input) {{
    var val = input.value.trim();
    var msg = '';
    if (input.name === 'name') {{
      if (!val || val.length < 3 || /\\d/.test(val)) msg = MSGS.name;
    }} else if (input.name === 'street-address') {{
      if (!val || val.length < 5) msg = MSGS.address;
    }} else if (input.name === 'tel') {{
      if (!isValidLocalPhone(val)) msg = MSGS.tel;
    }}
    var err = document.getElementById(errId(input));
    if (msg) {{
      input.setCustomValidity(msg);
      if (err) {{ err.textContent = msg; err.hidden = false; }}
      input.classList.add('is-invalid');
      input.setAttribute('aria-invalid', 'true');
    }} else {{
      input.setCustomValidity('');
      if (err) {{ err.textContent = ''; err.hidden = true; }}
      input.classList.remove('is-invalid');
      input.removeAttribute('aria-invalid');
    }}
    return !msg;
  }}
  form.querySelectorAll('input[name="name"], input[name="street-address"], input[name="tel"]').forEach(function (input) {{
    var err = document.createElement('span');
    err.id = errId(input);
    err.className = 'vk-field-error';
    err.hidden = true;
    input.insertAdjacentElement('afterend', err);
    input.setAttribute('aria-describedby', err.id);
    input.addEventListener('input', function () {{ if (input.classList.contains('is-invalid')) validateInput(input); }});
    input.addEventListener('blur', function () {{ validateInput(input); }});
  }});
  document.getElementById('nextStep').addEventListener('click', function () {{
    var fields = [document.getElementById('name'), document.getElementById('tel')];
    var ok = fields.every(function (field) {{ return validateInput(field) && field.reportValidity(); }});
    if (!ok) {{ error.style.display = 'block'; return; }}
    error.style.display = 'none';
    step1.hidden = true;
    step2.hidden = false;
    progressBar.style.width = '100%';
    stepLabel.textContent = {L['step2']!r};
    document.getElementById('address').focus();
  }});
  document.getElementById('backStep').addEventListener('click', function () {{
    step2.hidden = true;
    step1.hidden = false;
    progressBar.style.width = '50%';
    stepLabel.textContent = {L['step1']!r};
    document.getElementById('tel').focus();
  }});
  form.addEventListener('submit', function (e) {{
    if (form.dataset.submitting === 'true') {{ e.preventDefault(); e.stopImmediatePropagation(); return; }}
    var valid = true, firstInvalid = null;
    form.querySelectorAll('input[name="name"], input[name="street-address"], input[name="tel"]').forEach(function (input) {{
      if (!validateInput(input)) {{ valid = false; if (!firstInvalid) firstInvalid = input; }}
    }});
    if (!form.reportValidity() || !valid) {{
      e.preventDefault(); e.stopImmediatePropagation();
      error.style.display = 'block';
      error.textContent = MSGS.generic;
      if (firstInvalid) firstInvalid.focus();
      return;
    }}
    form.dataset.submitting = 'true';
    var btn = form.querySelector('button[type="submit"]');
    if (btn) {{ btn.disabled = true; btn.textContent = MSGS.submitting; }}
  }}, true);
  document.querySelectorAll('.tt-cookie-change-link').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      if (typeof window.ttOpenCookiePreferences === 'function') window.ttOpenCookiePreferences();
    }});
  }});{subid_js}
}})();
</script>
{tmfp_js}<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
</body>
</html>
"""


PATHS = {
    "es": ROOT / "es" / "vortek-1013" / "landing.html",
    "sk": ROOT / "sk" / "vortek-3228" / "landing.html",
    "pl": ROOT / "pl" / "vortek-1429" / "landing.html",
    "lt": ROOT / "lt" / "vortek-1427" / "landing.html",
    "lv": ROOT / "lv" / "vortek-3518" / "landing.html",
}


def main():
    for geo, path in PATHS.items():
        html = render(LOCALES[geo])
        path.write_text(html, encoding="utf-8", newline="\n")
        print(f"wrote {path.relative_to(ROOT)} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
