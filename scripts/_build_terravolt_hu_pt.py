# -*- coding: utf-8 -*-
"""Clone es/terravolt to HU and PT with literal translation and photo prices."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ES_LANDING = ROOT / "es" / "terravolt" / "landing.html"
ES_TY = ROOT / "es" / "terravolt" / "thank-you.html"


def replace_all(text: str, mapping: dict[str, str]) -> str:
    missing = []
    for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
        if old not in text:
            missing.append(old[:90])
            continue
        text = text.replace(old, new)
    if missing:
        raise SystemExit("missing fragments:\n" + "\n".join(missing))
    return text


HU_LANDING = {
    'lang="es"': 'lang="hu"',
    "Terravolt™ — El jardín con el que siempre has soñado | -50%": "Terravolt™ — A kert, amelyről mindig is álmodott | -50%",
    "SUBMITTING_LABEL: 'Enviando…'": "SUBMITTING_LABEL: 'Küldés…'",
    "COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'": "COOKIE_TEXT: 'Technikai és harmadik felek cookie-jait használjuk a felhasználói élmény javítására és elemzésre.'",
    "COOKIE_ACCEPT: 'Aceptar'": "COOKIE_ACCEPT: 'Elfogadom'",
    "COOKIE_LEARN: 'Más información'": "COOKIE_LEARN: 'Tudjon meg többet'",
    "🔥 50 % DE DESCUENTO – SOLO HOY · 🚚 Envío gratuito en 24/48 h · 💵 Pago contra reembolso": "🔥 50% KEDVEZMÉNY – CSAK MA · 🚚 Ingyenes szállítás 24/48 órán belül · 💵 Utánvétes fizetés",
    "— + 1790 opiniones": "— + 1790 vélemény",
    "Kit completo · 2 baterías 60 V · Motor Brushless™ 3000 W": "Teljes készlet · 2 db 60 V-os akkumulátor · Brushless™ 3000 W motor",
    "El jardín con el que siempre has soñado, en pocos minutos y sin esfuerzo": "A kert, amelyről mindig is álmodott, néhány perc alatt és erőfeszítés nélkül",
    "Recorta, perfila y da forma con precisión milimétrica. Olvídate del esfuerzo de las herramientas antiguas: gracias a su peso de solo 1,2 kg y a la potencia de 2 baterías de ion de litio de 60 V, cuidar el césped se convierte en una tarea rápida, fácil y agradable. Potencia pura, sin complicaciones.": "Nyírjon, szegélyezzen és formázzon milliméteres pontossággal. Felejtse el a régi szerszámok erőlködését: csupán 1,2 kg-os súlya és 2 darab 60 V-os lítiumion-akkumulátorának köszönhetően a gyepápolás gyors, egyszerű és kellemes feladat lesz. Tiszta teljesítmény, komplikációk nélkül.",
    "Kit Terravolt™ completo": "Teljes Terravolt™ készlet",
    "Kit completo Terravolt™": "Teljes Terravolt™ készlet",
    "PEDIR AHORA →": "RENDELÉS MOST →",
    "¡Hoy ahorras 74 €! · ✅ 4 años de garantía": "Ma 24.900 Ft-ot spórol! · ✅ 4 év garancia",
    "🔒 Sin pago por adelantado · Pago contra reembolso": "🔒 Nincs előre fizetés · Utánvétes fizetés",
    "Envío gratuito en 24/48 h": "Ingyenes szállítás 24/48 órán belül",
    "ENVÍO GRATUITO EN 48 HORAS": "INGYENES SZÁLLÍTÁS 48 ÓRÁN BELÜL",
    "Pago contra reembolso": "Utánvétes fizetés",
    "Sin pago por adelantado": "Nincs előre fizetés",
    "Satisfecho o te devolvemos el dinero": "Elégedett, vagy visszaadjuk a pénzét",
    "Sin preguntas si no te convence": "Kérdések nélkül, ha nem győzi meg",
    "4 años de garantía GRATIS": "4 év INGYENES garancia",
    "Incluida en el precio": "Az árban benne van",
    "⏰ ¡ATENCIÓN! ¡Las existencias se están agotando!": "⏰ FIGYELEM! A készlet fogyóban van!",
    '<div class="lbl">Hrs</div>': '<div class="lbl">Óra</div>',
    '<div class="lbl">Min</div>': '<div class="lbl">Perc</div>',
    '<div class="lbl">Seg</div>': '<div class="lbl">Mp</div>',
    "Disponibilidad en almacén": "Raktárkészlet",
    "¡SOLO QUEDAN 3 UNIDADES!": "MÁR CSAK 3 DARAB MARADT!",
    "👀 En este momento hay más de <strong>16 personas</strong> en la página y ya se ha confirmado 1 pedido.": "👀 Jelenleg több mint <strong>16 ember</strong> van az oldalon, és már 1 rendelést megerősítettek.",
    "⚠️ En este momento hay más de 16 personas en la página y ya se ha confirmado 1 pedido.": "⚠️ Jelenleg több mint 16 ember van az oldalon, és már 1 rendelést megerősítettek.",
    "RELLENA EL FORMULARIO PARA REALIZAR EL PEDIDO": "TÖLTSE KI AZ ŰRLAPOT A RENDELÉSHEZ",
    "¡Haz tu pedido ahora y asegúrate una de las últimas unidades disponibles con un 50 % de descuento!": "Rendelje meg most, és biztosítsa be az egyik utolsó, 50% kedvezménnyel elérhető darabot!",
    "Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.": "Adja le a rendelést 10 percen belül, hogy 48 órán belül megérkezzen. 1. lépés: Töltse ki az alábbi űrlapot a kért adatokkal. 2. lépés: Csapatunk egyik tagja felveszi Önnel a kapcsolatot a rendelés megerősítéséhez és kérdéseinek megválaszolásához.",
    "Al enviar el formulario aceptas que usemos tus datos para gestionar el pedido. Consulta la <a href=\"/es/privacy-policy.html\">Política de privacidad</a>.": "Az űrlap elküldésével elfogadja, hogy adatait a rendelés kezeléséhez használjuk. Lásd az <a href=\"/hu/privacy-policy.html\">adatvédelmi irányelveket</a>.",
    'placeholder="Carlos García"': 'placeholder="Kovács Péter"',
    'placeholder="+34612345678"': 'placeholder="+36201234567"',
    'placeholder="Calle Mayor 25, 28013 Madrid, España"': 'placeholder="Fő utca 25, 1051 Budapest, Magyarország"',
    "🔒 Sin pago por adelantado · 4 años de garantía GRATIS": "🔒 Nincs előre fizetés · 4 év INGYENES garancia",
    "Ingeniería de precisión para tus espacios verdes": "Precíziós mérnöki munka a zöldfelületeihez",
    "Si buscas un dispositivo que combine rendimiento, ligereza y movilidad para cualquier temporada, <strong>Terravolt™ es la elección definitiva.</strong>": "Ha olyan eszközt keres, amely teljesítményt, könnyűséget és mozgékonyságot ötvöz bármely évszakban, <strong>a Terravolt™ a végleges választás.</strong>",
    "Tres formas de cuidar todo el jardín con <span class=\"hl\">Terravolt™</span>": "Három módja annak, hogy az egész kertet a <span class=\"hl\">Terravolt™</span> segítségével ápolja",
    "Diseñada conforme a los estándares más altos del cuidado inalámbrico del jardín: potencia de una desbrozadora profesional de gasolina, con una fracción de su peso y total libertad de movimiento.": "A vezeték nélküli kertápolás legmagasabb szabványai szerint tervezve: egy professzionális benzines fűkasza teljesítménye, annak súlyának töredékével és teljes mozgásszabadsággal.",
    "Terravolt™ — potencia pura de 3000 W": "Terravolt™ — tiszta 3000 W-os teljesítmény",
    "POTENCIA PURA DE 3000 W: EL CORAZÓN TECNOLÓGICO DE 60 V": "TISZTA 3000 W-OS TELJESÍTMÉNY: A 60 V-OS TECHNOLÓGIAI SZÍV",
    "El corazón de Terravolt™ es el innovador motor Brushless™ de 3000 W: rendimiento comparable al de los motores de gasolina, sin las molestias del combustible; diseñado para durar años sin necesidad de intervenciones técnicas; máxima duración de la batería para sesiones de trabajo largas y sin fatiga.": "A Terravolt™ szíve az innovatív 3000 W-os Brushless™ motor: a benzinmotorokkal összevethető teljesítmény üzemanyag-kellemetlenségek nélkül; évekig tartó működésre tervezve műszaki beavatkozás nélkül; maximális akkumulátor-üzemidő hosszú, fáradságmentes munkamenetekhez.",
    "Terravolt™ — corte y perfilado 4 en 1": "Terravolt™ — vágás és szegélyezés 4 az 1-ben",
    "CORTE Y PERFILADO · SISTEMA DE CORTE 4 EN 1": "VÁGÁS ÉS SZEGÉLYEZÉS · 4 AZ 1-BEN VÁGÓRENDSZER",
    "En pocos segundos puedes pasar de desbrozadora a cortabordes. El cabezal inclinable a 90° y 180° permite perfilar los bordes de las aceras con precisión milimétrica. Sistema de corte 4 en 1: cuchillas de acero, cepillos de hierro o discos giratorios para el césped convencional.": "Néhány másodperc alatt fűkaszából szegélynyíróvá alakíthatja. A 90°-ban és 180°-ban dönthető fej milliméteres pontossággal szegélyezi a járdákat. 4 az 1-ben vágórendszer: acélkések, vaskefék vagy forgó tárcsák a hagyományos gyephez.",
    "Terravolt™ — ergonomía y cepillo de acero": "Terravolt™ — ergonómia és acélkefe",
    "ERGONOMÍA ADAPTADA A TI · ADIÓS A LAS MALAS HIERBAS ENTRE LAS BALDOSAS": "AZ ÖNHÖZ IGAZODÓ ERGONÓMIA · BÚCSÚ A JÁRÓLAPOK KÖZÖTTI GYOMTÓL",
    "Ajusta la altura del tubo entre 99 cm y 145 cm según tu estatura. Trabaja siempre en la postura correcta, protegiendo tu espalda del cansancio. Con el cepillo giratorio de acero incluido, limpias juntas y caminos eliminando musgo y malas hierbas sin productos químicos.": "Állítsa a cső magasságát 99 cm és 145 cm között a testmagasságának megfelelően. Mindig helyes testtartásban dolgozzon, és kímélje a hátát. A mellékelt forgó acélkefével illesztéseket és utakat tisztít, mohát és gyomot távolít el vegyszerek nélkül.",
    "Comparativa": "Összehasonlítás",
    "Potencia silenciosa · Potencia Eco sin emisiones": "Csendes teljesítmény · Kibocsátásmentes Eco teljesítmény",
    "Herramientas antiguas ❌": "Régi szerszámok ❌",
    "Peso": "Súly",
    "Pesadas y ruidosas": "Nehezek és hangosak",
    "1,2 kg — una sola mano": "1,2 kg — egy kézzel",
    "Coste": "Költség",
    "Autonomía": "Üzemidő",
    "Paradas a media faena": "Megállások a munka közepén",
    "2 baterías de 60 V": "2 db 60 V-os akkumulátor",
    "Ruido": "Zaj",
    "Molesta a los vecinos": "Zavarja a szomszédokat",
    "Potencia silenciosa": "Csendes teljesítmény",
    "Emisiones": "Kibocsátás",
    "Gases y gasolina": "Gázok és benzin",
    "Cero emisiones": "Zéró kibocsátás",
    "Arranque": "Indítás",
    "Esperas y complicaciones": "Várakozás és bonyodalmak",
    "Listo en 3 segundos": "3 másodperc alatt kész",
    "Más de 15.000 clientes satisfechos en España. Estas son las razones:": "Több mint 15 000 elégedett ügyfél Magyarországon. Íme az okok:",
    "★ 4,8/5 · + 1790 opiniones": "★ 4,8/5 · + 1790 vélemény",
    "Cliente con Terravolt™": "Ügyfél a Terravolt™ készülékkel",
    "Terravolt™ en uso": "Terravolt™ használat közben",
    "«Estaba cansado de sufrir con mi antigua desbrozadora de gasolina, pesada y ruidosa. Decidí probar Terravolt™ y me quedé sorprendido: pesa muy poco —¡la levanto con una sola mano!— y corta la hierba alta sin esfuerzo. El mango telescópico permite trabajar erguido, sin tener que agacharse. ¡Una compra que repetiría mil veces!»": "«Belefáradtam, hogy a régi, nehéz és hangos benzines fűkaszámmal küzdjek. Kipróbáltam a Terravolt™-ot, és meglepődtem: alig nyom valamit —egy kézzel felemelem!— és erőlködés nélkül vágja a magas füvet. A teleszkópos nyél egyenesen tartva dolgoztat, guggolás nélkül. Ez olyan vásárlás, amelyet ezerszer megismételnék!»",
    "«Vivo en una casa adosada y no quería molestar a los vecinos un domingo por la mañana. Esta recortadora es increíblemente silenciosa, pero tiene una potencia que no esperarías de una herramienta a batería. Se monta en un instante y las cuchillas de plástico son perfectas para recortar alrededor de mis flores sin dañarlas. ¡La recomiendo totalmente a cualquiera que quiera un jardín cuidado sin estrés!»": "«Sorházban lakom, és nem akartam zavarni a szomszédokat vasárnap reggel. Ez a nyíró hihetetlenül csendes, de olyan teljesítménye van, amit nem várna egy akkumulátoros szerszámtól. Pillanatok alatt összeszerelhető, a műanyag kések pedig tökéletesek a virágaim körüli nyíráshoz, anélkül, hogy megsértenék őket. Teljes szívemből ajánlom mindenkinek, aki stressz nélkül gondozott kertet szeretne!»",
    "«Lo mejor son las dos baterías incluidas: utilizo una mientras la otra se carga, así que nunca tengo que detenerme. Con el cepillo de acero limpié el camino de malas hierbas entre las baldosas y ha quedado como nuevo. También resulta muy práctico el cabezal giratorio para perfilar el borde del césped junto a la acera. Una relación calidad-precio inigualable.»": "«A legjobb a két mellékelt akkumulátor: az egyiket használom, amíg a másik töltődik, így soha nem kell megállnom. Az acélkefével kitisztítottam a járólapok közötti gyomot az ösvényről, és olyan, mint új. Nagyon praktikus a forgó fej is a járda melletti gyepszegély kialakításához. Páratlan ár-érték arány.»",
    "Cliente verificado": "Ellenőrzött vásárló",
    "Todas las opiniones publicadas en nuestro sitio web son reales y auténticas y proceden exclusivamente de clientes verificados que han comprado nuestros productos. Después de recibir su pedido, cada cliente recibe automáticamente una invitación para participar en una encuesta de satisfacción, donde puede compartir su opinión real sobre nuestros productos y sobre su experiencia de compra en general. Recopilamos y gestionamos tanto opiniones positivas como negativas. Las opiniones no se modifican, cumplen con la normativa de protección de datos y pueden ser verificadas por el vendedor.": "A weboldalunkon közzétett összes vélemény valós és hiteles, és kizárólag ellenőrzött vásárlóktól származik, akik megvásárolták termékeinket. A rendelés átvétele után minden vásárló automatikusan meghívást kap egy elégedettségi felmérésre, ahol megoszthatja valódi véleményét termékeinkről és a vásárlási élményéről. Pozitív és negatív véleményeket is gyűjtünk és kezelünk. A véleményeket nem módosítjuk, megfelelnek az adatvédelmi szabályoknak, és az eladó ellenőrizheti őket.",
    "📦 TU KIT COMPLETO Terravolt™ INCLUYE:": "📦 AZ ÖN TELJES Terravolt™ KÉSZLETE TARTALMAZZA:",
    "TODO INCLUIDO. NO NECESITAS COMPRAR NADA MÁS.": "MINDEN BENNE VAN. NEM KELL MÁST VÁSÁROLNIA.",
    "1x Terravolt™ Professional: Cuerpo ultraligero de la máquina (1,2 kg) con motor Brushless de alto rendimiento.": "1x Terravolt™ Professional: A gép ultrakönnyű teste (1,2 kg) nagy teljesítményű Brushless motorral.",
    "2x baterías de ion de litio de 60 V de alto rendimiento (1 GRATIS): Recibes una batería adicional para disfrutar de doble autonomía.": "2x nagy teljesítményű 60 V-os lítiumion-akkumulátor (1 INGYEN): További akkumulátort kap a dupla üzemidőhöz.",
    "1x cargador ultrarrápido + 1x disco dentado de acero endurecido + 2x cuchillas Precision-Cut de acero inoxidable.": "1x ultragyors töltő + 1x edzett acél fogazott tárcsa + 2x Precision-Cut rozsdamentes acélkés.",
    "1x cabezal multihilo para perfilado + 1x cepillo giratorio de acero (GRATIS) + Garantía oficial de 4 años.": "1x többszálas fej szegélyezéshez + 1x forgó acélkefe (INGYEN) + Hivatalos 4 év garancia.",
    "Hoy: 74 € + envío gratis · -50% de descuento · ¡Hoy ahorras 74 €!": "Ma: 24.900 Ft + ingyenes szállítás · -50% kedvezmény · Ma 24.900 Ft-ot spórol!",
    "🚚 Envío gratuito en 24/48 h · 💰 Pago contra reembolso · ✅ 4 años de garantía": "🚚 Ingyenes szállítás 24/48 órán belül · 💰 Utánvétes fizetés · ✅ 4 év garancia",
    "Preguntas frecuentes": "Gyakori kérdések",
    "1. ¿Cuánto dura la batería de Terravolt™?": "1. Meddig bírja a Terravolt™ akkumulátora?",
    "Doble autonomía: 2 baterías de ion de litio de 60 V incluidas para trabajar sin interrupciones. Mientras utilizas una, la otra se carga.": "Dupla üzemidő: 2 darab 60 V-os lítiumion-akkumulátor a megszakítás nélküli munkához. Amíg az egyiket használja, a másik töltődik.",
    "2. ¿Es difícil de montar o utilizar?": "2. Nehéz összeszerelni vagy használni?",
    "Listo para trabajar en 3 segundos: inserta la batería, pulsa el botón y ya estás listo. Sin esperas, máxima eficiencia.": "3 másodperc alatt munkára kész: helyezze be az akkumulátort, nyomja meg a gombot, és kész. Várakozás nélkül, maximális hatékonyság.",
    "3. ¿También puede cortar ramas pequeñas o solamente césped?": "3. Kis ágakat is vág, vagy csak gyepet?",
    "Potencia de 3000 W: toda la fuerza que necesitas para cortar arbustos y malas hierbas sin esfuerzo. Incluye disco dentado de acero endurecido, ideal para cortar ramas, arbustos y matorrales más resistentes.": "3000 W-os teljesítmény: minden erő, amire szüksége van a bokrok és a gyom erőlködés nélküli vágásához. Edzett acél fogazott tárcsát tartalmaz, ideális ágak, bokrok és ellenállóbb bozótok vágásához.",
    "4. ¿Es ruidosa? ¿Puedo utilizarla si vivo en un bloque de pisos?": "4. Hangos? Használhatom, ha társasházban lakom?",
    "Sí, ¡esa es precisamente una de sus ventajas! El motor Brushless es extraordinariamente silencioso en comparación con los modelos tradicionales de gasolina o eléctricos. Puedes cuidar tu jardín a cualquier hora sin molestar a los vecinos.": "Igen, pont ez az egyik előnye! A Brushless motor rendkívül csendes a hagyományos benzines vagy elektromos modellekhez képest. Bármikor gondozhatja a kertjét anélkül, hogy zavarná a szomszédokat.",
    "5. ¿Qué ocurre si tengo algún problema con el producto?": "5. Mi történik, ha problémám van a termékkel?",
    "Garantía oficial de 4 años: asistencia especializada y protección completa para tu total tranquilidad. Satisfecho o te devolvemos el dinero.": "Hivatalos 4 év garancia: szakértő segítség és teljes védelem a teljes nyugalmáért. Elégedett, vagy visszaadjuk a pénzét.",
    "6. ¿Cuáles son los plazos y los costes de entrega?": "6. Mik a szállítási határidők és költségek?",
    "Envío gratuito en 24/48 h. Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Pago contra reembolso, sin pago por adelantado.": "Ingyenes szállítás 24/48 órán belül. Adja le a rendelést 10 percen belül, hogy 48 órán belül megérkezzen. Utánvétes fizetés, előleg nélkül.",
    "Ya me he decidido. ¿Cómo hago el pedido?": "Döntöttem. Hogyan adom le a rendelést?",
    "Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.": "1. lépés: Töltse ki az alábbi űrlapot a kért adatokkal. 2. lépés: Csapatunk egyik tagja felveszi Önnel a kapcsolatot a rendelés megerősítéséhez és kérdéseinek megválaszolásához.",
    "Inicio de trendtopia-store.com": "A trendtopia-store.com kezdőlapja",
    "Productos útiles para el día a día, envío en 24-48 h con pago contra reembolso.": "Hasznos termékek a mindennapokra, szállítás 24–48 órán belül utánvéttel.",
    "Información": "Információ",
    "Sobre nosotros": "Rólunk",
    "Contacto": "Kapcsolat",
    "Política de privacidad": "Adatvédelmi irányelvek",
    "Términos y condiciones": "Általános szerződési feltételek",
    "Política de cookies": "Cookie szabályzat",
    "Política de envíos": "Szállítási feltételek",
    "Política de devoluciones": "Visszatérítési szabályzat",
    "Todos los derechos reservados.": "Minden jog fenntartva.",
    "el.innerHTML = `👀 En este momento hay más de <strong>${count} personas</strong> en la página y ya se ha confirmado 1 pedido.`;": "el.innerHTML = `👀 Jelenleg több mint <strong>${count} ember</strong> van az oldalon, és már 1 rendelést megerősítettek.`;",
    "· -50% HOY:": "· -50% MA:",
}

PT_LANDING = {
    'lang="es"': 'lang="pt"',
    "Terravolt™ — El jardín con el que siempre has soñado | -50%": "Terravolt™ — O jardim com que sempre sonhou | -50%",
    "SUBMITTING_LABEL: 'Enviando…'": "SUBMITTING_LABEL: 'A enviar…'",
    "COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'": "COOKIE_TEXT: 'Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análise.'",
    "COOKIE_ACCEPT: 'Aceptar'": "COOKIE_ACCEPT: 'Aceitar'",
    "COOKIE_LEARN: 'Más información'": "COOKIE_LEARN: 'Saber mais'",
    "🔥 50 % DE DESCUENTO – SOLO HOY · 🚚 Envío gratuito en 24/48 h · 💵 Pago contra reembolso": "🔥 50 % DE DESCONTO – SÓ HOJE · 🚚 Envio gratuito em 24/48 h · 💵 Pagamento contra reembolso",
    "— + 1790 opiniones": "— + 1790 opiniões",
    "Kit completo · 2 baterías 60 V · Motor Brushless™ 3000 W": "Kit completo · 2 baterias de 60 V · Motor Brushless™ de 3000 W",
    "El jardín con el que siempre has soñado, en pocos minutos y sin esfuerzo": "O jardim com que sempre sonhou, em poucos minutos e sem esforço",
    "Recorta, perfila y da forma con precisión milimétrica. Olvídate del esfuerzo de las herramientas antiguas: gracias a su peso de solo 1,2 kg y a la potencia de 2 baterías de ion de litio de 60 V, cuidar el césped se convierte en una tarea rápida, fácil y agradable. Potencia pura, sin complicaciones.": "Corte, perfil e forme com precisão milimétrica. Esqueça o esforço das ferramentas antigas: graças ao peso de apenas 1,2 kg e à potência de 2 baterias de iões de lítio de 60 V, cuidar do relvado torna-se uma tarefa rápida, fácil e agradável. Potência pura, sem complicações.",
    "Kit Terravolt™ completo": "Kit Terravolt™ completo",
    "Kit completo Terravolt™": "Kit completo Terravolt™",
    "PEDIR AHORA →": "ENCOMENDAR AGORA →",
    "¡Hoy ahorras 74 €! · ✅ 4 años de garantía": "Hoje poupa 79 €! · ✅ 4 anos de garantia",
    "🔒 Sin pago por adelantado · Pago contra reembolso": "🔒 Sem pagamento adiantado · Pagamento contra reembolso",
    "Envío gratuito en 24/48 h": "Envio gratuito em 24/48 h",
    "ENVÍO GRATUITO EN 48 HORAS": "ENVIO GRATUITO EM 48 HORAS",
    "Pago contra reembolso": "Pagamento contra reembolso",
    "Sin pago por adelantado": "Sem pagamento adiantado",
    "Satisfecho o te devolvemos el dinero": "Satisfeito ou devolvemos o dinheiro",
    "Sin preguntas si no te convence": "Sem perguntas se não o convencer",
    "4 años de garantía GRATIS": "4 anos de garantia GRÁTIS",
    "Incluida en el precio": "Incluída no preço",
    "⏰ ¡ATENCIÓN! ¡Las existencias se están agotando!": "⏰ ATENÇÃO! As existências estão a esgotar-se!",
    '<div class="lbl">Hrs</div>': '<div class="lbl">Hrs</div>',
    '<div class="lbl">Min</div>': '<div class="lbl">Min</div>',
    '<div class="lbl">Seg</div>': '<div class="lbl">Seg</div>',
    "Disponibilidad en almacén": "Disponibilidade em armazém",
    "¡SOLO QUEDAN 3 UNIDADES!": "SÓ RESTAM 3 UNIDADES!",
    "👀 En este momento hay más de <strong>16 personas</strong> en la página y ya se ha confirmado 1 pedido.": "👀 Neste momento há mais de <strong>16 pessoas</strong> na página e já foi confirmada 1 encomenda.",
    "⚠️ En este momento hay más de 16 personas en la página y ya se ha confirmado 1 pedido.": "⚠️ Neste momento há mais de 16 pessoas na página e já foi confirmada 1 encomenda.",
    "RELLENA EL FORMULARIO PARA REALIZAR EL PEDIDO": "PREENCHA O FORMULÁRIO PARA FAZER A ENCOMENDA",
    "¡Haz tu pedido ahora y asegúrate una de las últimas unidades disponibles con un 50 % de descuento!": "Faça já a sua encomenda e garanta uma das últimas unidades disponíveis com 50 % de desconto!",
    "Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.": "Faça a encomenda no prazo de 10 minutos para a receber em 48 h. Passo 1: Preencha o formulário seguinte com os dados pedidos. Passo 2: Um membro da nossa equipa contactá-lo-á para confirmar a encomenda e responder a qualquer pergunta.",
    "Al enviar el formulario aceptas que usemos tus datos para gestionar el pedido. Consulta la <a href=\"/es/privacy-policy.html\">Política de privacidad</a>.": "Ao enviar o formulário, aceita que usemos os seus dados para gerir a encomenda. Consulte a <a href=\"/pt/privacy-policy.html\">Política de privacidade</a>.",
    'placeholder="Carlos García"': 'placeholder="João Silva"',
    'placeholder="+34612345678"': 'placeholder="+351912345678"',
    'placeholder="Calle Mayor 25, 28013 Madrid, España"': 'placeholder="Rua Augusta 25, 1100-048 Lisboa, Portugal"',
    "🔒 Sin pago por adelantado · 4 años de garantía GRATIS": "🔒 Sem pagamento adiantado · 4 anos de garantia GRÁTIS",
    "Ingeniería de precisión para tus espacios verdes": "Engenharia de precisão para os seus espaços verdes",
    "Si buscas un dispositivo que combine rendimiento, ligereza y movilidad para cualquier temporada, <strong>Terravolt™ es la elección definitiva.</strong>": "Se procura um dispositivo que combine desempenho, leveza e mobilidade em qualquer estação, <strong>Terravolt™ é a escolha definitiva.</strong>",
    "Tres formas de cuidar todo el jardín con <span class=\"hl\">Terravolt™</span>": "Três formas de cuidar de todo o jardim com a <span class=\"hl\">Terravolt™</span>",
    "Diseñada conforme a los estándares más altos del cuidado inalámbrico del jardín: potencia de una desbrozadora profesional de gasolina, con una fracción de su peso y total libertad de movimiento.": "Concebida segundo os padrões mais altos do cuidado sem fios do jardim: potência de um corta-mato profissional a gasolina, com uma fração do seu peso e total liberdade de movimento.",
    "Terravolt™ — potencia pura de 3000 W": "Terravolt™ — potência pura de 3000 W",
    "POTENCIA PURA DE 3000 W: EL CORAZÓN TECNOLÓGICO DE 60 V": "POTÊNCIA PURA DE 3000 W: O CORAÇÃO TECNOLÓGICO DE 60 V",
    "El corazón de Terravolt™ es el innovador motor Brushless™ de 3000 W: rendimiento comparable al de los motores de gasolina, sin las molestias del combustible; diseñado para durar años sin necesidad de intervenciones técnicas; máxima duración de la batería para sesiones de trabajo largas y sin fatiga.": "O coração da Terravolt™ é o inovador motor Brushless™ de 3000 W: desempenho comparável ao dos motores a gasolina, sem os incómodos do combustível; concebido para durar anos sem necessidade de intervenções técnicas; máxima duração da bateria para sessões de trabalho longas e sem fadiga.",
    "Terravolt™ — corte y perfilado 4 en 1": "Terravolt™ — corte e perfilamento 4 em 1",
    "CORTE Y PERFILADO · SISTEMA DE CORTE 4 EN 1": "CORTE E PERFILAMENTO · SISTEMA DE CORTE 4 EM 1",
    "En pocos segundos puedes pasar de desbrozadora a cortabordes. El cabezal inclinable a 90° y 180° permite perfilar los bordes de las aceras con precisión milimétrica. Sistema de corte 4 en 1: cuchillas de acero, cepillos de hierro o discos giratorios para el césped convencional.": "Em poucos segundos passa de corta-mato a aparador. A cabeça inclinável a 90° e 180° permite perfilar os rebordos dos passeios com precisão milimétrica. Sistema de corte 4 em 1: lâminas de aço, escovas de ferro ou discos rotativos para o relvado convencional.",
    "Terravolt™ — ergonomía y cepillo de acero": "Terravolt™ — ergonomia e escova de aço",
    "ERGONOMÍA ADAPTADA A TI · ADIÓS A LAS MALAS HIERBAS ENTRE LAS BALDOSAS": "ERGONOMIA ADAPTADA A SI · ADEUS ÀS ERVAS DANINHAS ENTRE AS LADRILHAS",
    "Ajusta la altura del tubo entre 99 cm y 145 cm según tu estatura. Trabaja siempre en la postura correcta, protegiendo tu espalda del cansancio. Con el cepillo giratorio de acero incluido, limpias juntas y caminos eliminando musgo y malas hierbas sin productos químicos.": "Ajuste a altura do tubo entre 99 cm e 145 cm segundo a sua estatura. Trabalhe sempre na postura correta, protegendo as costas do cansaço. Com a escova rotativa de aço incluída, limpa juntas e caminhos, eliminando musgo e ervas daninhas sem produtos químicos.",
    "Comparativa": "Comparativo",
    "Potencia silenciosa · Potencia Eco sin emisiones": "Potência silenciosa · Potência Eco sem emissões",
    "Herramientas antiguas ❌": "Ferramentas antigas ❌",
    "Peso": "Peso",
    "Pesadas y ruidosas": "Pesadas e ruidosas",
    "1,2 kg — una sola mano": "1,2 kg — uma só mão",
    "Coste": "Custo",
    "Autonomía": "Autonomia",
    "Paradas a media faena": "Paragens a meio do trabalho",
    "2 baterías de 60 V": "2 baterias de 60 V",
    "Ruido": "Ruído",
    "Molesta a los vecinos": "Incomoda os vizinhos",
    "Potencia silenciosa": "Potência silenciosa",
    "Emisiones": "Emissões",
    "Gases y gasolina": "Gases e gasolina",
    "Cero emisiones": "Zero emissões",
    "Arranque": "Arranque",
    "Esperas y complicaciones": "Esperas e complicações",
    "Listo en 3 segundos": "Pronto em 3 segundos",
    "Más de 15.000 clientes satisfechos en España. Estas son las razones:": "Mais de 15.000 clientes satisfeitos em Portugal. Estas são as razões:",
    "★ 4,8/5 · + 1790 opiniones": "★ 4,8/5 · + 1790 opiniões",
    "Cliente con Terravolt™": "Cliente com Terravolt™",
    "Terravolt™ en uso": "Terravolt™ em utilização",
    "«Estaba cansado de sufrir con mi antigua desbrozadora de gasolina, pesada y ruidosa. Decidí probar Terravolt™ y me quedé sorprendido: pesa muy poco —¡la levanto con una sola mano!— y corta la hierba alta sin esfuerzo. El mango telescópico permite trabajar erguido, sin tener que agacharse. ¡Una compra que repetiría mil veces!»": "«Estava cansado de sofrer com o meu antigo corta-mato a gasolina, pesado e ruidoso. Decidi experimentar a Terravolt™ e fiquei surpreendido: pesa muito pouco —levo-a com uma só mão!— e corta a erva alta sem esforço. O cabo telescópico permite trabalhar direito, sem ter de se baixar. Uma compra que repetiria mil vezes!»",
    "«Vivo en una casa adosada y no quería molestar a los vecinos un domingo por la mañana. Esta recortadora es increíblemente silenciosa, pero tiene una potencia que no esperarías de una herramienta a batería. Se monta en un instante y las cuchillas de plástico son perfectas para recortar alrededor de mis flores sin dañarlas. ¡La recomiendo totalmente a cualquiera que quiera un jardín cuidado sin estrés!»": "«Vivo numa moradia geminada e não queria incomodar os vizinhos num domingo de manhã. Este aparador é incrivelmente silencioso, mas tem uma potência que não esperaria de uma ferramenta a bateria. Monta-se num instante e as lâminas de plástico são perfeitas para aparar à volta das minhas flores sem as danificar. Recomendo totalmente a quem quiser um jardim cuidado sem stresse!»",
    "«Lo mejor son las dos baterías incluidas: utilizo una mientras la otra se carga, así que nunca tengo que detenerme. Con el cepillo de acero limpié el camino de malas hierbas entre las baldosas y ha quedado como nuevo. También resulta muy práctico el cabezal giratorio para perfilar el borde del césped junto a la acera. Una relación calidad-precio inigualable.»": "«O melhor são as duas baterias incluídas: uso uma enquanto a outra carrega, por isso nunca tenho de parar. Com a escova de aço limpei o caminho das ervas daninhas entre os ladrilhos e ficou como novo. Também é muito prático o cabeçote rotativo para perfilar o rebordo do relvado junto ao passeio. Uma relação qualidade-preço inigualável.»",
    "Cliente verificado": "Cliente verificado",
    "Todas las opiniones publicadas en nuestro sitio web son reales y auténticas y proceden exclusivamente de clientes verificados que han comprado nuestros productos. Después de recibir su pedido, cada cliente recibe automáticamente una invitación para participar en una encuesta de satisfacción, donde puede compartir su opinión real sobre nuestros productos y sobre su experiencia de compra en general. Recopilamos y gestionamos tanto opiniones positivas como negativas. Las opiniones no se modifican, cumplen con la normativa de protección de datos y pueden ser verificadas por el vendedor.": "Todas as opiniões publicadas no nosso sítio são reais e autênticas e provêm exclusivamente de clientes verificados que compraram os nossos produtos. Depois de receber a encomenda, cada cliente recebe automaticamente um convite para participar num inquérito de satisfação, onde pode partilhar a sua opinião real sobre os nossos produtos e sobre a experiência de compra em geral. Recolhemos e gerimos opiniões positivas e negativas. As opiniões não são alteradas, cumprem a regulamentação de proteção de dados e podem ser verificadas pelo vendedor.",
    "📦 TU KIT COMPLETO Terravolt™ INCLUYE:": "📦 O SEU KIT COMPLETO Terravolt™ INCLUI:",
    "TODO INCLUIDO. NO NECESITAS COMPRAR NADA MÁS.": "TUDO INCLUÍDO. NÃO PRECISA DE COMPRAR MAIS NADA.",
    "1x Terravolt™ Professional: Cuerpo ultraligero de la máquina (1,2 kg) con motor Brushless de alto rendimiento.": "1x Terravolt™ Professional: Corpo ultraleve da máquina (1,2 kg) com motor Brushless de alto desempenho.",
    "2x baterías de ion de litio de 60 V de alto rendimiento (1 GRATIS): Recibes una batería adicional para disfrutar de doble autonomía.": "2x baterias de iões de lítio de 60 V de alto desempenho (1 GRÁTIS): Recebe uma bateria adicional para desfrutar de dupla autonomia.",
    "1x cargador ultrarrápido + 1x disco dentado de acero endurecido + 2x cuchillas Precision-Cut de acero inoxidable.": "1x carregador ultrarrápido + 1x disco dentado de aço endurecido + 2x lâminas Precision-Cut de aço inoxidável.",
    "1x cabezal multihilo para perfilado + 1x cepillo giratorio de acero (GRATIS) + Garantía oficial de 4 años.": "1x cabeça multifios para perfilamento + 1x escova rotativa de aço (GRÁTIS) + Garantia oficial de 4 anos.",
    "Hoy: 74 € + envío gratis · -50% de descuento · ¡Hoy ahorras 74 €!": "Hoje: 79 € + envio grátis · -50% de desconto · Hoje poupa 79 €!",
    "🚚 Envío gratuito en 24/48 h · 💰 Pago contra reembolso · ✅ 4 años de garantía": "🚚 Envio gratuito em 24/48 h · 💰 Pagamento contra reembolso · ✅ 4 anos de garantia",
    "Preguntas frecuentes": "Perguntas frequentes",
    "1. ¿Cuánto dura la batería de Terravolt™?": "1. Quanto dura a bateria da Terravolt™?",
    "Doble autonomía: 2 baterías de ion de litio de 60 V incluidas para trabajar sin interrupciones. Mientras utilizas una, la otra se carga.": "Dupla autonomia: 2 baterias de iões de lítio de 60 V incluídas para trabalhar sem interrupções. Enquanto usa uma, a outra carrega.",
    "2. ¿Es difícil de montar o utilizar?": "2. É difícil de montar ou utilizar?",
    "Listo para trabajar en 3 segundos: inserta la batería, pulsa el botón y ya estás listo. Sin esperas, máxima eficiencia.": "Pronto a trabalhar em 3 segundos: insira a bateria, prima o botão e está pronto. Sem esperas, máxima eficiência.",
    "3. ¿También puede cortar ramas pequeñas o solamente césped?": "3. Também corta ramos pequenos ou só relvado?",
    "Potencia de 3000 W: toda la fuerza que necesitas para cortar arbustos y malas hierbas sin esfuerzo. Incluye disco dentado de acero endurecido, ideal para cortar ramas, arbustos y matorrales más resistentes.": "Potência de 3000 W: toda a força de que precisa para cortar arbustos e ervas daninhas sem esforço. Inclui disco dentado de aço endurecido, ideal para cortar ramos, arbustos e mato mais resistente.",
    "4. ¿Es ruidosa? ¿Puedo utilizarla si vivo en un bloque de pisos?": "4. É ruidosa? Posso utilizá-la se vivo num prédio?",
    "Sí, ¡esa es precisamente una de sus ventajas! El motor Brushless es extraordinariamente silencioso en comparación con los modelos tradicionales de gasolina o eléctricos. Puedes cuidar tu jardín a cualquier hora sin molestar a los vecinos.": "Sim, essa é precisamente uma das suas vantagens! O motor Brushless é extraordinariamente silencioso em comparação com os modelos tradicionais a gasolina ou elétricos. Pode cuidar do jardim a qualquer hora sem incomodar os vizinhos.",
    "5. ¿Qué ocurre si tengo algún problema con el producto?": "5. O que acontece se tiver algum problema com o produto?",
    "Garantía oficial de 4 años: asistencia especializada y protección completa para tu total tranquilidad. Satisfecho o te devolvemos el dinero.": "Garantia oficial de 4 anos: assistência especializada e proteção completa para a sua total tranquilidade. Satisfeito ou devolvemos o dinheiro.",
    "6. ¿Cuáles son los plazos y los costes de entrega?": "6. Quais são os prazos e os custos de entrega?",
    "Envío gratuito en 24/48 h. Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Pago contra reembolso, sin pago por adelantado.": "Envio gratuito em 24/48 h. Faça a encomenda no prazo de 10 minutos para a receber em 48 h. Pagamento contra reembolso, sem pagamento adiantado.",
    "Ya me he decidido. ¿Cómo hago el pedido?": "Já me decidi. Como faço a encomenda?",
    "Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.": "Passo 1: Preencha o formulário seguinte com os dados pedidos. Passo 2: Um membro da nossa equipa contactá-lo-á para confirmar a encomenda e responder a qualquer pergunta.",
    "Inicio de trendtopia-store.com": "Início de trendtopia-store.com",
    "Productos útiles para el día a día, envío en 24-48 h con pago contra reembolso.": "Produtos úteis para o dia a dia, envio em 24-48 h com pagamento contra reembolso.",
    "Información": "Informação",
    "Sobre nosotros": "Sobre nós",
    "Contacto": "Contacto",
    '<a href="/es/privacy-policy.html">Política de privacidad</a>': '<a href="/es/privacy-policy.html">Política de privacidade</a>',
    "Términos y condiciones": "Termos e condições",
    "Política de cookies": "Política de cookies",
    "Política de envíos": "Política de envios",
    "Política de devoluciones": "Política de devoluções",
    "Todos los derechos reservados.": "Todos os direitos reservados.",
    "el.innerHTML = `👀 En este momento hay más de <strong>${count} personas</strong> en la página y ya se ha confirmado 1 pedido.`;": "el.innerHTML = `👀 Neste momento há mais de <strong>${count} pessoas</strong> na página e já foi confirmada 1 encomenda.`;",
    "· -50% HOY:": "· -50% HOJE:",
}

HU_TY = {
    'lang="es"': 'lang="hu"',
    "Pedido recibido — Espera la llamada de confirmación | Terravolt™": "Rendelés rögzítve — Várja a visszaigazoló hívást | Terravolt™",
    "Tu pedido Terravolt™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.": "Terravolt™ rendelése rögzítve. Már csak egy utolsó lépés van hátra: vegye fel a visszaigazoló hívást.",
    "COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'": "COOKIE_TEXT: 'Technikai és harmadik felek cookie-jait használjuk a felhasználói élmény javítására és elemzésre.'",
    "COOKIE_ACCEPT: 'Aceptar'": "COOKIE_ACCEPT: 'Elfogadom'",
    "COOKIE_LEARN: 'Más información'": "COOKIE_LEARN: 'Tudjon meg többet'",
    "¡Tu pedido se ha registrado correctamente!": "Rendelését sikeresen rögzítettük!",
    "Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.": "Remek — rendelése feldolgozás alatt van. Már csak <strong>egy utolsó lépés</strong> van hátra a véglegesítéshez és a szállításhoz.",
    "El equipo trendtopia-store trabajando: call center y logística contra reembolso": "A trendtopia-store csapat munka közben: call center és utánvétes logisztika",
    "👇 Qué debes hacer ahora": "👇 Mit tegyen most",
    "📞 Responde a la llamada de confirmación": "📞 Vegye fel a visszaigazoló hívást",
    "Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido.": "Operátorunk <strong>a következő órákban</strong> felhívja Önt a rendelés megerősítéséhez.",
    "Si no respondes a la llamada, el pedido se cancelará automáticamente.": "Ha nem veszi fel a telefont, a rendelés automatikusan törlődik.",
    "🕒 Horario de contacto": "🕒 Kapcsolattartási idő",
    "<strong>Lunes – Sábado</strong> · 9:00 – 18:00": "<strong>Hétfő – Szombat</strong> · 9:00 – 18:00",
    "📋 Qué ocurre después": "📋 Mi történik ezután",
    "Responde a la llamada y <strong>confirma tus datos</strong>": "Vegye fel a hívást és <strong>erősítse meg adatait</strong>",
    "Tu pedido se enviará en un plazo de <strong>24–48 horas</strong>": "Rendelése <strong>24–48 órán belül</strong> elindul",
    "Entrega a domicilio y <strong>pago contra reembolso</strong>": "Házhoz szállítás és <strong>utánvét</strong>",
    "🔒 Pago contra reembolso": "🔒 Utánvét",
    "🛡️ Garantía 4 años": "🛡️ 4 év garancia",
    "🔐 Protección SSL": "🔐 SSL védelem",
    "Información": "Információ",
    "Sobre nosotros": "Rólunk",
    "Contacto": "Kapcsolat",
    "Política de privacidad": "Adatvédelmi irányelvek",
    "Términos y condiciones": "Általános szerződési feltételek",
    "Política de cookies": "Cookie szabályzat",
    "Política de envíos": "Szállítási feltételek",
    "Política de devoluciones": "Visszatérítési szabályzat",
    "Todos los derechos reservados.": "Minden jog fenntartva.",
    ">Contact</h4>": ">Elérhetőségek</h4>",
}

PT_TY = {
    'lang="es"': 'lang="pt"',
    "Pedido recibido — Espera la llamada de confirmación | Terravolt™": "Encomenda recebida — Aguarde a chamada de confirmação | Terravolt™",
    "Tu pedido Terravolt™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.": "A sua encomenda Terravolt™ foi registada. Falta apenas um último passo: atenda a chamada de confirmação.",
    "COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'": "COOKIE_TEXT: 'Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análise.'",
    "COOKIE_ACCEPT: 'Aceptar'": "COOKIE_ACCEPT: 'Aceitar'",
    "COOKIE_LEARN: 'Más información'": "COOKIE_LEARN: 'Saber mais'",
    "¡Tu pedido se ha registrado correctamente!": "A sua encomenda foi registada com sucesso!",
    "Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.": "Perfeito — a sua encomenda está a ser processada. Falta apenas <strong>um último passo</strong> para a concluir e iniciar o envio.",
    "El equipo trendtopia-store trabajando: call center y logística contra reembolso": "A equipa trendtopia-store a trabalhar: centro de atendimento e logística contra reembolso",
    "👇 Qué debes hacer ahora": "👇 O que deve fazer agora",
    "📞 Responde a la llamada de confirmación": "📞 Atenda a chamada de confirmação",
    "Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido.": "Um operador irá contactá-lo <strong>nas próximas horas</strong> para confirmar a sua encomenda.",
    "Si no respondes a la llamada, el pedido se cancelará automáticamente.": "Se não atender a chamada, a encomenda será automaticamente cancelada.",
    "🕒 Horario de contacto": "🕒 Horário de contacto",
    "<strong>Lunes – Sábado</strong> · 9:00 – 18:00": "<strong>Segunda – Sábado</strong> · 9:00 – 18:00",
    "📋 Qué ocurre después": "📋 O que acontece a seguir",
    "Responde a la llamada y <strong>confirma tus datos</strong>": "Atenda a chamada e <strong>confirme os seus dados</strong>",
    "Tu pedido se enviará en un plazo de <strong>24–48 horas</strong>": "A sua encomenda será enviada no prazo de <strong>24–48 horas</strong>",
    "Entrega a domicilio y <strong>pago contra reembolso</strong>": "Entrega ao domicílio e <strong>pagamento contra reembolso</strong>",
    "🔒 Pago contra reembolso": "🔒 Pagamento contra reembolso",
    "🛡️ Garantía 4 años": "🛡️ Garantia 4 anos",
    "🔐 Protección SSL": "🔐 Proteção SSL",
    "Información": "Informação",
    "Sobre nosotros": "Sobre nós",
    "Contacto": "Contacto",
    "Política de privacidad": "Política de privacidade",
    "Términos y condiciones": "Termos e condições",
    "Política de cookies": "Política de cookies",
    "Política de envíos": "Política de envios",
    "Política de devoluciones": "Política de devoluções",
    "Todos los derechos reservados.": "Todos os direitos reservados.",
    ">Contact</h4>": ">Contacto</h4>",
}

SPECS = [
    {
        "geo": "hu",
        "currency": "HUF",
        "price_num": "24900",
        "offer": "1520",
        "cpa": "17.0",
        "old": "48.800 Ft",
        "now": "24.900 Ft",
        "compare_now": "24.900 Ft (−50 %)",
        "landing_map": HU_LANDING,
        "ty_map": HU_TY,
    },
    {
        "geo": "pt",
        "currency": "EUR",
        "price_num": "79",
        "offer": "1816",
        "cpa": "17.0",
        "old": "158 €",
        "now": "79 €",
        "compare_now": "79 € (−50 %)",
        "landing_map": PT_LANDING,
        "ty_map": PT_TY,
    },
]


def write_index(geo: str, dest: Path) -> None:
    dest.write_text(
        f"""<!DOCTYPE html>
<html lang="{geo}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/terravolt/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/terravolt/landing.html">
<link rel="canonical" href="https://trendtopia-store.com/{geo}/terravolt/landing.html">
</head>
<body>
<p><a href="/{geo}/terravolt/landing.html">Terravolt™</a></p>
</body>
</html>
""",
        encoding="utf-8",
        newline="\n",
    )


def configure_landing(text: str, spec: dict) -> str:
    geo = spec["geo"]
    text = text.replace("GEO: 'es'", f"GEO: '{geo}'")
    text = text.replace("CURRENCY: 'EUR'", f"CURRENCY: '{spec['currency']}'")
    text = text.replace("PRICE: 74", f"PRICE: {spec['price_num']}")
    text = text.replace("OFFER_NAME: 'Terravolt ES'", f"OFFER_NAME: 'Terravolt {geo.upper()}'")
    text = text.replace("LP_ID: 'es-terravolt'", f"LP_ID: '{geo}-terravolt'")
    text = text.replace("OFFER_ID: '1815'", f"OFFER_ID: '{spec['offer']}'")
    text = text.replace("CPA: 17.0", f"CPA: {spec['cpa']}")
    text = text.replace('value="1815"', f'value="{spec["offer"]}"')
    text = text.replace('value="1835"', 'value=""')
    text = text.replace('value="41670e1a6896bbe651bbd071b6c14aa706334999"', 'value=""')
    text = text.replace("/es/terravolt/", f"/{geo}/terravolt/")
    text = text.replace('href="/es/', f'href="/{geo}/')
    text = text.replace("74 € (−50 %)", spec["compare_now"])
    text = text.replace("148 €", spec["old"])
    text = text.replace("74 €", spec["now"])
    return text


def configure_ty(text: str, spec: dict) -> str:
    geo = spec["geo"]
    text = text.replace(" GEO: 'es',", f" GEO: '{geo}',")
    text = text.replace(" CURRENCY: 'EUR',", f" CURRENCY: '{spec['currency']}',")
    text = text.replace(" PRICE: 74,", f" PRICE: {spec['price_num']},")
    text = text.replace(" OFFER_ID: '1815',", f" OFFER_ID: '{spec['offer']}',")
    text = text.replace("'value': 17.0,", f"'value': {spec['cpa']},")
    text = text.replace('href="/es/', f'href="/{geo}/')
    return text


def leftover_es(text: str, geo: str) -> list[str]:
    needles = [
        "El jardín",
        "PEDIR AHORA",
        "Pago contra reembolso",
        "Rellena",
        "desbrozadora",
        "Más de 15.000 clientes satisfechos en España",
        "¡Hoy ahorras 74",
        "148 €",
        "74 €",
        'href="/es/',
        "GEO: 'es'",
        "OFFER_ID: '1815'",
    ]
    return [n for n in needles if n in text]


def main() -> None:
    src_landing = ES_LANDING.read_text(encoding="utf-8")
    src_ty = ES_TY.read_text(encoding="utf-8")
    for spec in SPECS:
        geo = spec["geo"]
        folder = ROOT / geo / "terravolt"
        folder.mkdir(parents=True, exist_ok=True)
        landing = configure_landing(replace_all(src_landing, spec["landing_map"]), spec)
        ty = configure_ty(replace_all(src_ty, spec["ty_map"]), spec)
        bad_l = leftover_es(landing, geo)
        bad_t = leftover_es(ty, geo)
        if bad_l:
            raise SystemExit(f"{geo} landing leftover: {bad_l}")
        if bad_t:
            raise SystemExit(f"{geo} thank-you leftover: {bad_t}")
        (folder / "landing.html").write_text(landing, encoding="utf-8", newline="\n")
        (folder / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")
        write_index(geo, folder / "index.html")
        print(f"wrote {folder.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
