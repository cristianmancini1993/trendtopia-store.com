# -*- coding: utf-8 -*-
"""Clone es/terravolt to CZ at 1 899 Kč (50% off)."""
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


CZ_LANDING = {
    'lang="es"': 'lang="cs"',
    "Terravolt™ — El jardín con el que siempre has soñado | -50%": "Terravolt™ — Zahrada, o které jste vždy snili | -50%",
    "SUBMITTING_LABEL: 'Enviando…'": "SUBMITTING_LABEL: 'Odesílání…'",
    "COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'": "COOKIE_TEXT: 'Používáme technické cookies a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.'",
    "COOKIE_ACCEPT: 'Aceptar'": "COOKIE_ACCEPT: 'Přijmout'",
    "COOKIE_LEARN: 'Más información'": "COOKIE_LEARN: 'Zjistit více'",
    "🔥 50 % DE DESCUENTO – SOLO HOY · 🚚 Envío gratuito en 24/48 h · 💵 Pago contra reembolso": "🔥 SLEVA 50 % – JEN DNES · 🚚 Doprava zdarma do 24/48 h · 💵 Platba na dobírku",
    "— + 1790 opiniones": "— + 1790 recenzí",
    "Kit completo · 2 baterías 60 V · Motor Brushless™ 3000 W": "Kompletní sada · 2 baterie 60 V · Motor Brushless™ 3000 W",
    "El jardín con el que siempre has soñado, en pocos minutos y sin esfuerzo": "Zahrada, o které jste vždy snili, během několika minut a bez námahy",
    "Recorta, perfila y da forma con precisión milimétrica. Olvídate del esfuerzo de las herramientas antiguas: gracias a su peso de solo 1,2 kg y a la potencia de 2 baterías de ion de litio de 60 V, cuidar el césped se convierte en una tarea rápida, fácil y agradable. Potencia pura, sin complicaciones.": "Stříhejte, začišťujte okraje a tvarujte s milimetrovou přesností. Zapomeňte na dřinu se starými nástroji: díky hmotnosti pouhých 1,2 kg a výkonu 2 lithium-iontových baterií 60 V se péče o trávník stane rychlou, snadnou a příjemnou prací. Čistý výkon, bez komplikací.",
    "Kit Terravolt™ completo": "Kompletní sada Terravolt™",
    "Kit completo Terravolt™": "Kompletní sada Terravolt™",
    "PEDIR AHORA →": "OBJEDNAT NYNÍ →",
    "¡Hoy ahorras 74 €! · ✅ 4 años de garantía": "Dnes ušetříte 1 899 Kč! · ✅ 4 roky záruky",
    "🔒 Sin pago por adelantado · Pago contra reembolso": "🔒 Bez platby předem · Platba na dobírku",
    "Envío gratuito en 24/48 h": "Doprava zdarma do 24/48 h",
    "ENVÍO GRATUITO EN 48 HORAS": "DOPRAVA ZDARMA DO 48 HODIN",
    "Pago contra reembolso": "Platba na dobírku",
    "Sin pago por adelantado": "Bez platby předem",
    "Satisfecho o te devolvemos el dinero": "Spokojenost, nebo peníze zpět",
    "Sin preguntas si no te convence": "Bez otázek, pokud vás to nepřesvědčí",
    "4 años de garantía GRATIS": "4 roky záruky ZDARMA",
    "Incluida en el precio": "V ceně zahrnuto",
    "⏰ ¡ATENCIÓN! ¡Las existencias se están agotando!": "⏰ POZOR! Zásoby docházejí!",
    '<div class="lbl">Hrs</div>': '<div class="lbl">Hod</div>',
    '<div class="lbl">Min</div>': '<div class="lbl">Min</div>',
    '<div class="lbl">Seg</div>': '<div class="lbl">Sek</div>',
    "Disponibilidad en almacén": "Dostupnost na skladě",
    "¡SOLO QUEDAN 3 UNIDADES!": "ZBÝVAJÍ UŽ JEN 3 KUSY!",
    "👀 En este momento hay más de <strong>16 personas</strong> en la página y ya se ha confirmado 1 pedido.": "👀 Právě teď je na stránce více než <strong>16 lidí</strong> a už byla potvrzena 1 objednávka.",
    "⚠️ En este momento hay más de 16 personas en la página y ya se ha confirmado 1 pedido.": "⚠️ Právě teď je na stránce více než 16 lidí a už byla potvrzena 1 objednávka.",
    "RELLENA EL FORMULARIO PARA REALIZAR EL PEDIDO": "VYPLŇTE FORMULÁŘ PRO OBJEDNÁVKU",
    "¡Haz tu pedido ahora y asegúrate una de las últimas unidades disponibles con un 50 % de descuento!": "Objednejte hned a zajistěte si jeden z posledních kusů se slevou 50 %!",
    "Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.": "Objednejte do 10 minut, abyste zásilku obdrželi do 48 h. Krok 1: Vyplňte následující formulář požadovanými údaji. Krok 2: Člen našeho týmu vás kontaktuje, aby objednávku potvrdil a zodpověděl vaše otázky.",
    "Al enviar el formulario aceptas que usemos tus datos para gestionar el pedido. Consulta la <a href=\"/es/privacy-policy.html\">Política de privacidad</a>.": "Odesláním formuláře souhlasíte s použitím vašich údajů ke zpracování objednávky. Viz <a href=\"/cz/privacy-policy.html\">zásady ochrany osobních údajů</a>.",
    'placeholder="Carlos García"': 'placeholder="Jan Novák"',
    'placeholder="+34612345678"': 'placeholder="+420601123456"',
    'placeholder="Calle Mayor 25, 28013 Madrid, España"': 'placeholder="Václavské náměstí 1, 110 00 Praha, Česko"',
    "🔒 Sin pago por adelantado · 4 años de garantía GRATIS": "🔒 Bez platby předem · 4 roky záruky ZDARMA",
    "Ingeniería de precisión para tus espacios verdes": "Přesné inženýrství pro vaše zelené plochy",
    "Si buscas un dispositivo que combine rendimiento, ligereza y movilidad para cualquier temporada, <strong>Terravolt™ es la elección definitiva.</strong>": "Hledáte-li zařízení, které spojuje výkon, lehkost a mobilitu v každém období, <strong>Terravolt™ je definitivní volba.</strong>",
    "Tres formas de cuidar todo el jardín con <span class=\"hl\">Terravolt™</span>": "Tři způsoby, jak pečovat o celou zahradu s <span class=\"hl\">Terravolt™</span>",
    "Diseñada conforme a los estándares más altos del cuidado inalámbrico del jardín: potencia de una desbrozadora profesional de gasolina, con una fracción de su peso y total libertad de movimiento.": "Navržena podle nejvyšších standardů bezdrátové péče o zahradu: výkon profesionálního benzínového křovinořezu, se zlomkem jeho hmotnosti a naprostou volností pohybu.",
    "Terravolt™ — potencia pura de 3000 W": "Terravolt™ — čistý výkon 3000 W",
    "POTENCIA PURA DE 3000 W: EL CORAZÓN TECNOLÓGICO DE 60 V": "ČISTÝ VÝKON 3000 W: TECHNOLOGICKÉ SRDCE 60 V",
    "El corazón de Terravolt™ es el innovador motor Brushless™ de 3000 W: rendimiento comparable al de los motores de gasolina, sin las molestias del combustible; diseñado para durar años sin necesidad de intervenciones técnicas; máxima duración de la batería para sesiones de trabajo largas y sin fatiga.": "Srdcem Terravolt™ je inovativní motor Brushless™ 3000 W: výkon srovnatelný s benzínovými motory, bez starostí s palivem; navržený tak, aby vydržel roky bez technických zásahů; maximální výdrž baterie pro dlouhé pracovní relace bez únavy.",
    "Terravolt™ — corte y perfilado 4 en 1": "Terravolt™ — sekání a začišťování 4 v 1",
    "CORTE Y PERFILADO · SISTEMA DE CORTE 4 EN 1": "SEKÁNÍ A ZAČIŠŤOVÁNÍ · SYSTÉM SEKÁNÍ 4 V 1",
    "En pocos segundos puedes pasar de desbrozadora a cortabordes. El cabezal inclinable a 90° y 180° permite perfilar los bordes de las aceras con precisión milimétrica. Sistema de corte 4 en 1: cuchillas de acero, cepillos de hierro o discos giratorios para el césped convencional.": "Během několika sekund přejdete z křovinořezu na vyžínač okrajů. Hlava sklopná o 90° a 180° umožňuje začišťovat okraje chodníků s milimetrovou přesností. Systém sekání 4 v 1: ocelové nože, železné kartáče nebo rotační kotouče pro běžný trávník.",
    "Terravolt™ — ergonomía y cepillo de acero": "Terravolt™ — ergonomie a ocelový kartáč",
    "ERGONOMÍA ADAPTADA A TI · ADIÓS A LAS MALAS HIERBAS ENTRE LAS BALDOSAS": "ERGONOMIE PŘIZPŮSOBENÁ VÁM · SBOHEM PLEVELU MEZI DLAŽDICEMI",
    "Ajusta la altura del tubo entre 99 cm y 145 cm según tu estatura. Trabaja siempre en la postura correcta, protegiendo tu espalda del cansancio. Con el cepillo giratorio de acero incluido, limpias juntas y caminos eliminando musgo y malas hierbas sin productos químicos.": "Nastavte výšku trubky mezi 99 cm a 145 cm podle své výšky. Pracujte vždy ve správné poloze a chraňte záda před únavou. Součástí je otočný ocelový kartáč, kterým vyčistíte spáry a cesty a odstraníte mech a plevel bez chemie.",
    "Comparativa": "Srovnání",
    "Potencia silenciosa · Potencia Eco sin emisiones": "Tichý výkon · Eco výkon bez emisí",
    "Herramientas antiguas ❌": "Staré nástroje ❌",
    "Peso": "Hmotnost",
    "Pesadas y ruidosas": "Těžké a hlučné",
    "1,2 kg — una sola mano": "1,2 kg — jednou rukou",
    "Coste": "Cena",
    "Autonomía": "Výdrž",
    "Paradas a media faena": "Zastávky uprostřed práce",
    "2 baterías de 60 V": "2 baterie 60 V",
    "Ruido": "Hluk",
    "Molesta a los vecinos": "Ruší sousedy",
    "Potencia silenciosa": "Tichý výkon",
    "Emisiones": "Emise",
    "Gases y gasolina": "Plyny a benzín",
    "Cero emisiones": "Nulové emise",
    "Arranque": "Start",
    "Esperas y complicaciones": "Čekání a komplikace",
    "Listo en 3 segundos": "Připraveno za 3 sekundy",
    "Más de 15.000 clientes satisfechos en España. Estas son las razones:": "Více než 15 000 spokojených zákazníků v Česku. Toto jsou důvody:",
    "★ 4,8/5 · + 1790 opiniones": "★ 4,8/5 · + 1790 recenzí",
    "Cliente con Terravolt™": "Zákazník s Terravolt™",
    "Terravolt™ en uso": "Terravolt™ při použití",
    "«Estaba cansado de sufrir con mi antigua desbrozadora de gasolina, pesada y ruidosa. Decidí probar Terravolt™ y me quedé sorprendido: pesa muy poco —¡la levanto con una sola mano!— y corta la hierba alta sin esfuerzo. El mango telescópico permite trabajar erguido, sin tener que agacharse. ¡Una compra que repetiría mil veces!»": "«Už mě unavovalo trápit se se starým benzínovým křovinořezem, těžkým a hlučným. Rozhodl jsem se vyzkoušet Terravolt™ a zůstal jsem překvapený: váží velmi málo —zvednu ho jednou rukou!— a vysokou trávu seká bez námahy. Teleskopická rukojeť umožňuje pracovat vzpřímeně, bez ohýbání. Nákup, který bych zopakoval tisíckrát!»",
    "«Vivo en una casa adosada y no quería molestar a los vecinos un domingo por la mañana. Esta recortadora es increíblemente silenciosa, pero tiene una potencia que no esperarías de una herramienta a batería. Se monta en un instante y las cuchillas de plástico son perfectas para recortar alrededor de mis flores sin dañarlas. ¡La recomiendo totalmente a cualquiera que quiera un jardín cuidado sin estrés!»": "«Bydlím v řadovém domě a nechtěl jsem rušit sousedy v neděli ráno. Tento vyžínač je neuvěřitelně tichý, ale má výkon, který byste od akumulátorového nářadí nečekali. Složíte ho okamžitě a plastové nože jsou ideální k zastřihávání kolem květin, aniž byste je poškodili. Doporučuji ho každému, kdo chce upravenou zahradu bez stresu!»",
    "«Lo mejor son las dos baterías incluidas: utilizo una mientras la otra se carga, así que nunca tengo que detenerme. Con el cepillo de acero limpié el camino de malas hierbas entre las baldosas y ha quedado como nuevo. También resulta muy práctico el cabezal giratorio para perfilar el borde del césped junto a la acera. Una relación calidad-precio inigualable.»": "«Nejlepší jsou dvě přiložené baterie: jednu používám, zatímco se druhá nabíjí, takže nikdy nemusím zastavovat. Ocelovým kartáčem jsem vyčistil cestu od plevele mezi dlaždicemi a je jako nová. Velmi praktická je i otočná hlava na začištění okraje trávníku u chodníku. Nepřekonatelný poměr cena/výkon.»",
    "Cliente verificado": "Ověřený zákazník",
    "Todas las opiniones publicadas en nuestro sitio web son reales y auténticas y proceden exclusivamente de clientes verificados que han comprado nuestros productos. Después de recibir su pedido, cada cliente recibe automáticamente una invitación para participar en una encuesta de satisfacción, donde puede compartir su opinión real sobre nuestros productos y sobre su experiencia de compra en general. Recopilamos y gestionamos tanto opiniones positivas como negativas. Las opiniones no se modifican, cumplen con la normativa de protección de datos y pueden ser verificadas por el vendedor.": "Všechny recenze zveřejněné na našem webu jsou skutečné a autentické a pocházejí výhradně od ověřených zákazníků, kteří si naše produkty koupili. Po přijetí objednávky každý zákazník automaticky obdrží pozvánku k účasti v průzkumu spokojenosti, kde může sdílet svůj skutečný názor na naše produkty a na celkový nákupní zážitek. Shromažďujeme a spravujeme pozitivní i negativní recenze. Recenze se nemění, splňují předpisy o ochraně údajů a prodávající je může ověřit.",
    "📦 TU KIT COMPLETO Terravolt™ INCLUYE:": "📦 VAŠE KOMPLETNÍ SADA Terravolt™ OBSAHUJE:",
    "TODO INCLUIDO. NO NECESITAS COMPRAR NADA MÁS.": "VŠE V CENĚ. NEMUSÍTE DOKUPOVAT NIC DALŠÍHO.",
    "1x Terravolt™ Professional: Cuerpo ultraligero de la máquina (1,2 kg) con motor Brushless de alto rendimiento.": "1x Terravolt™ Professional: Ultralehké tělo stroje (1,2 kg) s vysoce výkonným motorem Brushless.",
    "2x baterías de ion de litio de 60 V de alto rendimiento (1 GRATIS): Recibes una batería adicional para disfrutar de doble autonomía.": "2x vysoce výkonné lithium-iontové baterie 60 V (1 ZDARMA): Dostanete přídavnou baterii pro dvojnásobnou výdrž.",
    "1x cargador ultrarrápido + 1x disco dentado de acero endurecido + 2x cuchillas Precision-Cut de acero inoxidable.": "1x ultrarychlá nabíječka + 1x ozubený kotouč z kalené oceli + 2x nože Precision-Cut z nerezové oceli.",
    "1x cabezal multihilo para perfilado + 1x cepillo giratorio de acero (GRATIS) + Garantía oficial de 4 años.": "1x vícežilová hlava na začišťování + 1x otočný ocelový kartáč (ZDARMA) + Oficiální záruka 4 roky.",
    "Hoy: 74 € + envío gratis · -50% de descuento · ¡Hoy ahorras 74 €!": "Dnes: 1 899 Kč + doprava zdarma · sleva -50 % · Dnes ušetříte 1 899 Kč!",
    "🚚 Envío gratuito en 24/48 h · 💰 Pago contra reembolso · ✅ 4 años de garantía": "🚚 Doprava zdarma do 24/48 h · 💰 Platba na dobírku · ✅ 4 roky záruky",
    "Preguntas frecuentes": "Časté dotazy",
    "1. ¿Cuánto dura la batería de Terravolt™?": "1. Jak dlouho vydrží baterie Terravolt™?",
    "Doble autonomía: 2 baterías de ion de litio de 60 V incluidas para trabajar sin interrupciones. Mientras utilizas una, la otra se carga.": "Dvojnásobná výdrž: 2 lithium-iontové baterie 60 V v balení pro práci bez přerušení. Zatímco jednu používáte, druhá se nabíjí.",
    "2. ¿Es difícil de montar o utilizar?": "2. Je obtížné ji sestavit nebo používat?",
    "Listo para trabajar en 3 segundos: inserta la batería, pulsa el botón y ya estás listo. Sin esperas, máxima eficiencia.": "Připraveno k práci za 3 sekundy: vložte baterii, stiskněte tlačítko a jste připraveni. Bez čekání, maximální účinnost.",
    "3. ¿También puede cortar ramas pequeñas o solamente césped?": "3. Umí sekat i malé větve, nebo jen trávník?",
    "Potencia de 3000 W: toda la fuerza que necesitas para cortar arbustos y malas hierbas sin esfuerzo. Incluye disco dentado de acero endurecido, ideal para cortar ramas, arbustos y matorrales más resistentes.": "Výkon 3000 W: veškerá síla, kterou potřebujete k sekání keřů a plevele bez námahy. Součástí je ozubený kotouč z kalené oceli, ideální k sekání větví, keřů a odolnějšího křoví.",
    "4. ¿Es ruidosa? ¿Puedo utilizarla si vivo en un bloque de pisos?": "4. Je hlučná? Mohu ji používat, když bydlím v bytovém domě?",
    "Sí, ¡esa es precisamente una de sus ventajas! El motor Brushless es extraordinariamente silencioso en comparación con los modelos tradicionales de gasolina o eléctricos. Puedes cuidar tu jardín a cualquier hora sin molestar a los vecinos.": "Ano, to je právě jedna z jejích výhod! Motor Brushless je mimořádně tichý ve srovnání s tradičními benzínovými nebo elektrickými modely. Můžete se o zahradu starat kdykoli, aniž byste rušili sousedy.",
    "5. ¿Qué ocurre si tengo algún problema con el producto?": "5. Co se stane, když budu mít s výrobkem problém?",
    "Garantía oficial de 4 años: asistencia especializada y protección completa para tu total tranquilidad. Satisfecho o te devolvemos el dinero.": "Oficiální záruka 4 roky: specializovaná podpora a kompletní ochrana pro váš klid. Spokojenost, nebo peníze zpět.",
    "6. ¿Cuáles son los plazos y los costes de entrega?": "6. Jaké jsou dodací lhůty a náklady na doručení?",
    "Envío gratuito en 24/48 h. Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Pago contra reembolso, sin pago por adelantado.": "Doprava zdarma do 24/48 h. Objednejte do 10 minut, abyste zásilku obdrželi do 48 h. Platba na dobírku, bez platby předem.",
    "Ya me he decidido. ¿Cómo hago el pedido?": "Rozhodl jsem se. Jak objednám?",
    "Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.": "Krok 1: Vyplňte následující formulář požadovanými údaji. Krok 2: Člen našeho týmu vás kontaktuje, aby objednávku potvrdil a zodpověděl vaše otázky.",
    "Inicio de trendtopia-store.com": "Úvodní stránka trendtopia-store.com",
    "Productos útiles para el día a día, envío en 24-48 h con pago contra reembolso.": "Užitečné produkty na každý den, doprava do 24–48 h s platbou na dobírku.",
    "Información": "Informace",
    "Sobre nosotros": "O nás",
    "Contacto": "Kontakt",
    '<a href="/es/privacy-policy.html">Política de privacidad</a>': '<a href="/es/privacy-policy.html">Zásady ochrany osobních údajů</a>',
    "Términos y condiciones": "Obchodní podmínky",
    "Política de cookies": "Zásady cookies",
    "Política de envíos": "Podmínky dopravy",
    "Política de devoluciones": "Podmínky vrácení",
    "Todos los derechos reservados.": "Všechna práva vyhrazena.",
    "el.innerHTML = `👀 En este momento hay más de <strong>${count} personas</strong> en la página y ya se ha confirmado 1 pedido.`;": "el.innerHTML = `👀 Právě teď je na stránce více než <strong>${count} lidí</strong> a už byla potvrzena 1 objednávka.`;",
    "· -50% HOY:": "· -50 % DNES:",
}

CZ_TY = {
    'lang="es"': 'lang="cs"',
    "Pedido recibido — Espera la llamada de confirmación | Terravolt™": "Objednávka přijata — Vyčkejte na potvrzovací hovor | Terravolt™",
    "Tu pedido Terravolt™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.": "Vaše objednávka Terravolt™ byla zaznamenána. Zbývá poslední krok: přijměte potvrzovací hovor.",
    "COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'": "COOKIE_TEXT: 'Používáme technické cookies a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.'",
    "COOKIE_ACCEPT: 'Aceptar'": "COOKIE_ACCEPT: 'Přijmout'",
    "COOKIE_LEARN: 'Más información'": "COOKIE_LEARN: 'Zjistit více'",
    "¡Tu pedido se ha registrado correctamente!": "Vaše objednávka byla úspěšně zaznamenána!",
    "Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.": "Skvělé — vaše objednávka se zpracovává. Zbývá už jen <strong>poslední krok</strong> k dokončení a odeslání.",
    "El equipo trendtopia-store trabajando: call center y logística contra reembolso": "Tým trendtopia-store při práci: call centrum a logistika na dobírku",
    "👇 Qué debes hacer ahora": "👇 Co teď udělat",
    "📞 Responde a la llamada de confirmación": "📞 Přijměte potvrzovací hovor",
    "Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido.": "Operátor vás bude kontaktovat <strong>v následujících hodinách</strong>, aby objednávku potvrdil.",
    "Si no respondes a la llamada, el pedido se cancelará automáticamente.": "Pokud hovor nepřijmete, objednávka se automaticky zruší.",
    "🕒 Horario de contacto": "🕒 Kontaktní doba",
    "<strong>Lunes – Sábado</strong> · 9:00 – 18:00": "<strong>Pondělí – Sobota</strong> · 9:00 – 18:00",
    "📋 Qué ocurre después": "📋 Co bude dál",
    "Responde a la llamada y <strong>confirma tus datos</strong>": "Přijměte hovor a <strong>potvrďte své údaje</strong>",
    "Tu pedido se enviará en un plazo de <strong>24–48 horas</strong>": "Vaše objednávka bude odeslána do <strong>24–48 hodin</strong>",
    "Entrega a domicilio y <strong>pago contra reembolso</strong>": "Doručení na adresu a <strong>platba na dobírku</strong>",
    "🔒 Pago contra reembolso": "🔒 Platba na dobírku",
    "🛡️ Garantía 4 años": "🛡️ Záruka 4 roky",
    "🔐 Protección SSL": "🔐 Ochrana SSL",
    "Información": "Informace",
    "Sobre nosotros": "O nás",
    "Contacto": "Kontakt",
    "Política de privacidad": "Zásady ochrany osobních údajů",
    "Términos y condiciones": "Obchodní podmínky",
    "Política de cookies": "Zásady cookies",
    "Política de envíos": "Podmínky dopravy",
    "Política de devoluciones": "Podmínky vrácení",
    "Todos los derechos reservados.": "Všechna práva vyhrazena.",
    ">Contact</h4>": ">Kontakt</h4>",
}


def write_index(dest: Path) -> None:
    dest.write_text(
        """<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {
  var path = '/cz/terravolt/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
})();
</script>
<meta http-equiv="refresh" content="0;url=/cz/terravolt/landing.html">
<link rel="canonical" href="https://trendtopia-store.com/cz/terravolt/landing.html">
</head>
<body>
<p><a href="/cz/terravolt/landing.html">Terravolt™</a></p>
</body>
</html>
""",
        encoding="utf-8",
        newline="\n",
    )


def leftover_es(text: str) -> list[str]:
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
        "-50% HOY",
        "site-footer__heading\">Contact</h4>",
    ]
    return [n for n in needles if n in text]


def main() -> None:
    landing = ES_LANDING.read_text(encoding="utf-8")
    ty = ES_TY.read_text(encoding="utf-8")
    landing = replace_all(landing, CZ_LANDING)
    ty = replace_all(ty, CZ_TY)
    landing = landing.replace("GEO: 'es'", "GEO: 'cz'")
    landing = landing.replace("CURRENCY: 'EUR'", "CURRENCY: 'CZK'")
    landing = landing.replace("PRICE: 74", "PRICE: 1899")
    landing = landing.replace("OFFER_NAME: 'Terravolt ES'", "OFFER_NAME: 'Terravolt CZ'")
    landing = landing.replace("LP_ID: 'es-terravolt'", "LP_ID: 'cz-terravolt'")
    landing = landing.replace("OFFER_ID: '1815'", "OFFER_ID: '2043'")
    landing = landing.replace("CPA: 17.0", "CPA: 19.0")
    landing = landing.replace('value="1815"', 'value="2043"')
    landing = landing.replace('value="1835"', 'value=""')
    landing = landing.replace('value="41670e1a6896bbe651bbd071b6c14aa706334999"', 'value=""')
    landing = landing.replace("/es/terravolt/", "/cz/terravolt/")
    landing = landing.replace('href="/es/', 'href="/cz/')
    landing = landing.replace("74 € (−50 %)", "1 899 Kč (−50 %)")
    landing = landing.replace("148 €", "3 798 Kč")
    landing = landing.replace("74 €", "1 899 Kč")
    ty = ty.replace(" GEO: 'es',", " GEO: 'cz',")
    ty = ty.replace(" CURRENCY: 'EUR',", " CURRENCY: 'CZK',")
    ty = ty.replace(" PRICE: 74,", " PRICE: 1899,")
    ty = ty.replace(" OFFER_ID: '1815',", " OFFER_ID: '2043',")
    ty = ty.replace("'value': 17.0,", "'value': 19.0,")
    ty = ty.replace('href="/es/', 'href="/cz/')
    for label, text in (("landing", landing), ("thank-you", ty)):
        bad = leftover_es(text)
        if bad:
            raise SystemExit(f"cz {label} leftover: {bad}")
    folder = ROOT / "cz" / "terravolt"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "landing.html").write_text(landing, encoding="utf-8", newline="\n")
    (folder / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")
    write_index(folder / "index.html")
    print(f"wrote {folder.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
