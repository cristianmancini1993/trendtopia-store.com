"""Apply es/terravolt copy to ro/arcforce template (Terravolt™ brand). Text only."""
from pathlib import Path

p = Path("ro/arcforce/landing.html")
html = p.read_text(encoding="utf-8")

# head meta
html = html.replace(
    "<html lang=\"ro\">",
    "<html lang=\"es\">",
)
html = html.replace(
    "<title>Terravolt™ — Aparat de Sudură Profesional 8 în 1 Fără Butelie</title>",
    "<title>Terravolt™ — El jardín con el que siempre has soñado | -50%</title>",
)
html = html.replace(
    "  PRICE: 597,\n",
    "  PRICE: 499,\n",
)
html = html.replace(
    "  CURRENCY: 'RON',\n",
    "  CURRENCY: 'PLN',\n",
)

# body blocks - from line 317 to 564
start = html.index('<div class="topbar">')
end = html.index("<footer class=\"site-footer\">")
new_body = r'''<div class="topbar">🔥 50 % DE DESCUENTO – SOLO HOY · 🚚 Envío gratuito en 24/48 h · 💵 Pago contra reembolso</div>

  <div class="rating-strip wrap">
    <div class="stars">★★★★★</div>
    <div class="rating-text"><strong>4,8/5</strong> — + 1790 opiniones</div>
  </div>

  <!-- ===== HERO ===== -->
  <section class="hero wrap">
    <div class="hero-copy">
      <span class="gift-strip">Kit completo · 2 baterías 60 V · Motor Brushless™ 3000 W</span>
      <h1 class="h1-mobile-only">El jardín con el que siempre has soñado, en pocos minutos y sin esfuerzo</h1>
      <h1 class="h1-desktop-only">El jardín con el que siempre has soñado, en pocos minutos y sin esfuerzo</h1>
      <p class="lead">Recorta, perfila y da forma con precisión milimétrica. Olvídate del esfuerzo de las herramientas antiguas: gracias a su peso de solo 1,2 kg y a la potencia de 2 baterías de ion de litio de 60 V, cuidar el césped se convierte en una tarea rápida, fácil y agradable. Potencia pura, sin complicaciones.</p>

      <div class="hero-image hero-image-mobile-only">
        <img decoding="async" src="/assets/img/products/terravolt/ro-landing/hero.jpg?v=1" alt="Kit Terravolt™ completo">
      </div>

      <div class="price-block">
        <span class="was">999 zł</span>
        <span class="now">499 zł</span>
        <span class="pct">-50%</span>
      </div>

      <a href="#order-form" class="cta-btn">PEDIR AHORA →</a>
      <p class="form-note">¡Hoy ahorras 500 zł! · ✅ 4 años de garantía</p>
      <p class="form-note">🔒 Sin pago por adelantado · Pago contra reembolso</p>
    </div>

    <div class="hero-image hero-image-desktop-only">
      <img decoding="async" src="/assets/img/products/terravolt/ro-landing/hero.jpg?v=1" alt="Kit Terravolt™ completo">
    </div>
  </section>

  <div class="wrap">
    <div class="feature-row">
      <div class="feature-item"><div class="ico">🚚</div><h4>Envío gratuito en 24/48 h</h4><p>ENVÍO GRATUITO EN 48 HORAS</p></div>
      <div class="feature-item"><div class="ico">💵</div><h4>Pago contra reembolso</h4><p>Sin pago por adelantado</p></div>
      <div class="feature-item"><div class="ico">🔄</div><h4>Satisfecho o te devolvemos el dinero</h4><p>Sin preguntas si no te convence</p></div>
      <div class="feature-item"><div class="ico">✅</div><h4>4 años de garantía GRATIS</h4><p>Incluida en el precio</p></div>
    </div>
  </div>

  <!-- ===== ORDER FORM ===== -->
  <section class="order-section" id="order-form">
    <div class="wrap">
      <div class="urgency-strip">
        <div class="countdown-row">
          <div class="countdown-label">⏰ ¡ATENCIÓN! ¡Las existencias se están agotando!</div>
          <div class="countdown-timer" id="countdownTimer">
            <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">Hrs</div></div>
            <div class="sep">:</div>
            <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">Min</div></div>
            <div class="sep">:</div>
            <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">Seg</div></div>
          </div>
        </div>

        <div class="stock-row">
          <div class="stock-label">
            <span class="left">Disponibilidad en almacén</span>
            <span class="right">¡SOLO QUEDAN 3 UNIDADES!</span>
          </div>
          <div class="stock-bar"><div class="stock-bar-fill"></div></div>
        </div>

        <div class="live-row">
          <span class="dot"></span>
          <span id="liveCount">👀 En este momento hay más de <strong>16 personas</strong> en la página y ya se ha confirmado 1 pedido.</span>
        </div>
      </div>

      <div class="order-card">
        <h2>RELLENA EL FORMULARIO PARA REALIZAR EL PEDIDO</h2>
        <p>¡Haz tu pedido ahora y asegúrate una de las últimas unidades disponibles con un 50 % de descuento!</p>
        <div class="price-block" style="margin-bottom:16px;">
          <span class="was">999 zł</span>
          <span class="now">499 zł</span>
          <span class="pct">-50%</span>
        </div>
        <p>⚠️ En este momento hay más de 16 personas en la página y ya se ha confirmado 1 pedido.</p>
        <p>Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.</p>
        <p class="form-note" style="margin-bottom:14px">Al enviar el formulario aceptas que usemos tus datos para gestionar el pedido. Consulta la <a href="/ro/privacy-policy.html">Política de privacidad</a>.</p>
        
        <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
          <input type="text" name="name" autocomplete="name" placeholder="Tomasz Kowalski" required>
          <input type="tel" name="tel" autocomplete="tel" placeholder="+4915123456789" required>
          <input type="text" name="street-address" autocomplete="street-address" placeholder="ul. Marszałkowska 25, 00-068 Warszawa, Polska" required>
          
          <input name="uid" type="hidden" value="019e5f4e-b178-7d63-91e1-6fda72088957" />
          <input name="offer" type="hidden" value="PENDING" />
          <input name="lp" type="hidden" value="PENDING" />
          <input name="subid" id="subid" type="hidden" value="" />
          <input name="tmfp" id="tmfp" type="hidden" value="" />
          <input name="thankyoupage" type="hidden" value="https://trendtopia-store.com/ro/arcforce/thank-you.html" />
          <input name="webhook" type="hidden" value="https://hook.eu2.make.com/bkg6tbg3vdknomqb2n4kdat1fe1tp271" />
          <input name="_key" type="hidden" value="PENDING" />
          
          <button type="submit" class="cta-btn">PEDIR AHORA →</button>
          <p class="form-note">🔒 Sin pago por adelantado · 4 años de garantía GRATIS</p>
          <script>
            document.addEventListener("DOMContentLoaded", function () {
              var params = new URLSearchParams(window.location.search);
              var campaign = params.get("utm_campaign") || "";
              var subidInput = document.querySelector('input[name="subid"]');
              if (subidInput) { subidInput.value = campaign; }
            });
          </script>
          <script src="https://offers.adricenetwork.com/forms/tmfp/" crossorigin="anonymous" defer></script>
          <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>
      </div>
    </div>
  </section>

  <!-- ===== USE CASES ===== -->
  <section class="usecase wrap">
    <div class="uc-head">
      <span class="uc-kicker">Ingeniería de precisión para tus espacios verdes</span>
      <p class="uc-punch">Si buscas un dispositivo que combine rendimiento, ligereza y movilidad para cualquier temporada, <strong>Terravolt™ es la elección definitiva.</strong></p>
      <h2>Tres formas de cuidar todo el jardín con <span class="hl">Terravolt™</span></h2>
      <p>Diseñada conforme a los estándares más altos del cuidado inalámbrico del jardín: potencia de una desbrozadora profesional de gasolina, con una fracción de su peso y total libertad de movimiento.</p>
    </div>

    <div class="uc-grid">
      <div class="uc-card">
        <img decoding="async" src="/assets/img/products/terravolt/ro-landing/use-1.jpg?v=1" alt="Terravolt™ — potencia pura de 3000 W">
        <h3>POTENCIA PURA DE 3000 W: EL CORAZÓN TECNOLÓGICO DE 60 V</h3>
        <p>El corazón de Terravolt™ es el innovador motor Brushless™ de 3000 W: rendimiento comparable al de los motores de gasolina, sin las molestias del combustible; diseñado para durar años sin necesidad de intervenciones técnicas; máxima duración de la batería para sesiones de trabajo largas y sin fatiga.</p>
      </div>

      <div class="uc-card">
        <img decoding="async" src="/assets/img/products/terravolt/ro-landing/use-2.jpg?v=1" alt="Terravolt™ — corte y perfilado 4 en 1">
        <h3>CORTE Y PERFILADO · SISTEMA DE CORTE 4 EN 1</h3>
        <p>En pocos segundos puedes pasar de desbrozadora a cortabordes. El cabezal inclinable a 90° y 180° permite perfilar los bordes de las aceras con precisión milimétrica. Sistema de corte 4 en 1: cuchillas de acero, cepillos de hierro o discos giratorios para el césped convencional.</p>
      </div>

      <div class="uc-card">
        <img decoding="async" src="/assets/img/products/terravolt/ro-landing/use-3.jpg?v=1" alt="Terravolt™ — ergonomía y cepillo de acero">
        <h3>ERGONOMÍA ADAPTADA A TI · ADIÓS A LAS MALAS HIERBAS ENTRE LAS BALDOSAS</h3>
        <p>Ajusta la altura del tubo entre 99 cm y 145 cm según tu estatura. Trabaja siempre en la postura correcta, protegiendo tu espalda del cansancio. Con el cepillo giratorio de acero incluido, limpias juntas y caminos eliminando musgo y malas hierbas sin productos químicos.</p>
      </div>
    </div>

    <a href="#order-form" class="cta-btn cta-inline">PEDIR AHORA →</a>
  </section>

  <!-- ===== COMPARE ===== -->
  <section class="compare wrap">
    <div class="section-label">Comparativa</div>
    <h2>Potencia silenciosa · Potencia Eco sin emisiones</h2>
    <table>
      <tr><th></th><th>Herramientas antiguas ❌</th><th class="highlight">Terravolt™ ✅</th></tr>
      <tr><td>Peso</td><td>Pesadas y ruidosas</td><td class="win">1,2 kg — una sola mano</td></tr>
      <tr><td>Coste</td><td>999 zł</td><td class="win">499 zł (−50 %)</td></tr>
      <tr><td>Autonomía</td><td>Paradas a media faena</td><td class="win">2 baterías de 60 V</td></tr>
      <tr><td>Ruido</td><td>Molesta a los vecinos</td><td class="win">Potencia silenciosa</td></tr>
      <tr><td>Emisiones</td><td>Gases y gasolina</td><td class="win">Cero emisiones</td></tr>
      <tr><td>Arranque</td><td>Esperas y complicaciones</td><td class="win">Listo en 3 segundos</td></tr>
    </table>
  </section>

  <!-- ===== TESTIMONIALS ===== -->
  <section class="testimonials">
    <div class="wrap">
      <div class="section-heading">
        <h2>Más de 15.000 clientes satisfechos en Polonia. Estas son las razones:</h2>
        <p style="margin-top:8px;font-size:14px;color:#e2231a;font-weight:600">★ 4,8/5 · + 1790 opiniones</p>
      </div>
      <div class="t-grid">
        <div class="testimonial">
          <img decoding="async" class="t-photo" src="/assets/img/products/terravolt/ro-landing/review-1.jpg?v=1" alt="Cliente con Terravolt™">
          <div class="t-body">
            <div class="stars">★★★★★</div>
            <p>«Estaba cansado de sufrir con mi antigua desbrozadora de gasolina, pesada y ruidosa. Decidí probar Terravolt™ y me quedé sorprendido: pesa muy poco —¡la levanto con una sola mano!— y corta la hierba alta sin esfuerzo. El mango telescópico permite trabajar erguido, sin tener que agacharse. ¡Una compra que repetiría mil veces!»</p>
            <div class="author-row">
              <img decoding="async" class="avatar" src="/assets/img/products/arcforce/reviewer-1.webp?v=1" alt="Tomasz W.">
              <div class="author">Tomasz W. ✅ — Cliente verificado</div>
            </div>
          </div>
        </div>
        <div class="testimonial">
          <img decoding="async" class="t-photo" src="/assets/img/products/terravolt/ro-landing/review-2.jpg?v=1" alt="Terravolt™ en uso">
          <div class="t-body">
            <div class="stars">★★★★★</div>
            <p>«Vivo en una casa adosada y no quería molestar a los vecinos un domingo por la mañana. Esta recortadora es increíblemente silenciosa, pero tiene una potencia que no esperarías de una herramienta a batería. Se monta en un instante y las cuchillas de plástico son perfectas para recortar alrededor de mis flores sin dañarlas. ¡La recomiendo totalmente a cualquiera que quiera un jardín cuidado sin estrés!»</p>
            <div class="author-row">
              <img decoding="async" class="avatar" src="/assets/img/products/arcforce/reviewer-2.webp?v=1" alt="Marek K.">
              <div class="author">Marek K. ✅ — Cliente verificado</div>
            </div>
          </div>
        </div>
        <div class="testimonial">
          <img decoding="async" class="t-photo" src="/assets/img/products/terravolt/ro-landing/review-3.jpg?v=1" alt="Kit Terravolt™ completo">
          <div class="t-body">
            <div class="stars">★★★★★</div>
            <p>«Lo mejor son las dos baterías incluidas: utilizo una mientras la otra se carga, así que nunca tengo que detenerme. Con el cepillo de acero limpié el camino de malas hierbas entre las baldosas y ha quedado como nuevo. También resulta muy práctico el cabezal giratorio para perfilar el borde del césped junto a la acera. Una relación calidad-precio inigualable.»</p>
            <div class="author-row">
              <img decoding="async" class="avatar" src="/assets/img/products/arcforce/reviewer-3.webp?v=1" alt="Anna K.">
              <div class="author">Anna K. ✅ — Cliente verificado</div>
            </div>
          </div>
        </div>
      </div>
      <p style="text-align:center;margin-top:12px;font-size:13px;color:var(--color-text-muted);max-width:640px;margin-left:auto;margin-right:auto">Todas las opiniones publicadas en nuestro sitio web son reales y auténticas y proceden exclusivamente de clientes verificados que han comprado nuestros productos. Después de recibir su pedido, cada cliente recibe automáticamente una invitación para participar en una encuesta de satisfacción, donde puede compartir su opinión real sobre nuestros productos y sobre su experiencia de compra en general. Recopilamos y gestionamos tanto opiniones positivas como negativas. Las opiniones no se modifican, cumplen con la normativa de protección de datos y pueden ser verificadas por el vendedor.</p>
      <a href="#order-form" class="cta-btn cta-inline">PEDIR AHORA →</a>
    </div>
  </section>

  <!-- ===== KIT BOX ===== -->
  <section class="kit-section wrap">
    <div class="section-heading">
      <span class="eyebrow">📦 TU KIT COMPLETO Terravolt™ INCLUYE:</span>
      <h2>TODO INCLUIDO. NO NECESITAS COMPRAR NADA MÁS.</h2>
    </div>
    <div class="kit-box">
      <img decoding="async" src="/assets/img/products/terravolt/ro-landing/kit.jpg?v=1" alt="Kit completo Terravolt™">
      <div class="kit-content">
        <div class="price-block" style="margin-bottom:16px;">
          <span class="was">999 zł</span>
          <span class="now">499 zł</span>
          <span class="pct">-50%</span>
        </div>
        <ul>
          <li>1x Terravolt™ Professional: Cuerpo ultraligero de la máquina (1,2 kg) con motor Brushless de alto rendimiento.</li>
          <li>2x baterías de ion de litio de 60 V de alto rendimiento (1 GRATIS): Recibes una batería adicional para disfrutar de doble autonomía.</li>
          <li>1x cargador ultrarrápido + 1x disco dentado de acero endurecido + 2x cuchillas Precision-Cut de acero inoxidable.</li>
          <li>1x cabezal multihilo para perfilado + 1x cepillo giratorio de acero (GRATIS) + Garantía oficial de 4 años.</li>
        </ul>
        <p class="form-note" style="margin:12px 0">Hoy: 499 zł + envío gratis · -50% de descuento · ¡Hoy ahorras 500 zł!</p>
        <a href="#order-form" class="cta-btn">PEDIR AHORA →</a>
        <p class="form-note">🚚 Envío gratuito en 24/48 h · 💰 Pago contra reembolso · ✅ 4 años de garantía</p>
      </div>
    </div>
  </section>

  <!-- ===== FAQ ===== -->
  <section class="faq wrap">
    <div class="section-heading">
      <h2>Preguntas frecuentes</h2>
    </div>
    <div class="faq-item"><button class="faq-q"><span>1. ¿Cuánto dura la batería de Terravolt™?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Doble autonomía: 2 baterías de ion de litio de 60 V incluidas para trabajar sin interrupciones. Mientras utilizas una, la otra se carga.</p></div></div>
    <div class="faq-item"><button class="faq-q"><span>2. ¿Es difícil de montar o utilizar?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Listo para trabajar en 3 segundos: inserta la batería, pulsa el botón y ya estás listo. Sin esperas, máxima eficiencia.</p></div></div>
    <div class="faq-item"><button class="faq-q"><span>3. ¿También puede cortar ramas pequeñas o solamente césped?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Potencia de 3000 W: toda la fuerza que necesitas para cortar arbustos y malas hierbas sin esfuerzo. Incluye disco dentado de acero endurecido, ideal para cortar ramas, arbustos y matorrales más resistentes.</p></div></div>
    <div class="faq-item"><button class="faq-q"><span>4. ¿Es ruidosa? ¿Puedo utilizarla si vivo en un bloque de pisos?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Sí, ¡esa es precisamente una de sus ventajas! El motor Brushless es extraordinariamente silencioso en comparación con los modelos tradicionales de gasolina o eléctricos. Puedes cuidar tu jardín a cualquier hora sin molestar a los vecinos.</p></div></div>
    <div class="faq-item"><button class="faq-q"><span>5. ¿Qué ocurre si tengo algún problema con el producto?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Garantía oficial de 4 años: asistencia especializada y protección completa para tu total tranquilidad. Satisfecho o te devolvemos el dinero.</p></div></div>
    <div class="faq-item"><button class="faq-q"><span>6. ¿Cuáles son los plazos y los costes de entrega?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Envío gratuito en 24/48 h. Haz tu pedido en un plazo de 10 minutos para recibirlo en 48 h. Pago contra reembolso, sin pago por adelantado.</p></div></div>
    <div class="faq-item"><button class="faq-q"><span>Ya me he decidido. ¿Cómo hago el pedido?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Paso 1: Rellena el siguiente formulario con los datos requeridos. Paso 2: Un miembro de nuestro equipo se pondrá en contacto contigo para confirmar el pedido y responder a cualquier pregunta.</p></div></div>
  </section>

'''

html = html[:start] + new_body + html[end:]

# footer bottom promo line
html = html.replace(
    '<a href="/">trendtopia-store.com</a>\n    </div>',
    '<a href="/">trendtopia-store.com</a>\n      · -50% HOY: <s>999 zł</s> → <strong>499 zł</strong>\n    </div>',
)

# live count script
html = html.replace(
    "let count = 38;",
    "let count = 16;",
)
html = html.replace(
    "count = Math.min(46, Math.max(32, count));",
    "count = Math.min(24, Math.max(12, count));",
)
html = html.replace(
    "el.innerHTML = `<strong>${count} de persoane</strong> se uită la acest aparat de sudură acum`;",
    "el.innerHTML = `👀 En este momento hay más de <strong>${count} personas</strong> en la página y ya se ha confirmado 1 pedido.`;",
)

p.write_text(html, encoding="utf-8")
print("updated", p)
