/**
 * Home page (/) — locale selector + product offers per market.
 */
(function () {
  if (!document.body || !document.querySelector('[data-home-i18n-root]')) return;

  var STORAGE_KEY = 'tt-home-locale';

  var CASA_FUEGO_GEOS = ['cz', 'de', 'es', 'hu', 'lt', 'pl', 'pt', 'sk'];
  var CORESYNC_GEOS = ['bg', 'cz', 'de', 'ee', 'en', 'es', 'fr', 'gr', 'hr', 'hu', 'it', 'lt', 'lv', 'pl', 'pt', 'ro', 'si', 'sk'];

  var LOCALE_LABELS = {
    bg: 'Български',
    cz: 'Čeština',
    de: 'Deutsch',
    ee: 'Eesti',
    en: 'English',
    es: 'Español',
    fr: 'Français',
    gr: 'Ελληνικά',
    hr: 'Hrvatski',
    hu: 'Magyar',
    it: 'Italiano',
    lt: 'Lietuvių',
    lv: 'Latviešu',
    pl: 'Polski',
    pt: 'Português',
    ro: 'Română',
    si: 'Slovenščina',
    sk: 'Slovenčina'
  };

  var HTML_LANG = {
    bg: 'bg', cz: 'cs', de: 'de', ee: 'et', en: 'en', es: 'es', fr: 'fr', gr: 'el',
    hr: 'hr', hu: 'hu', it: 'it', lt: 'lt', lv: 'lv', pl: 'pl', pt: 'pt', ro: 'ro', si: 'sl', sk: 'sk'
  };

  var SELECT_LOCALES = ['en'].concat(
    Object.keys(LOCALE_LABELS)
      .filter(function (k) { return k !== 'en'; })
      .sort(function (a, b) { return LOCALE_LABELS[a].localeCompare(LOCALE_LABELS[b], undefined, { sensitivity: 'base' }); })
  );

  var MARKETS = { setOfPots: [], coreSync: [] };
  CASA_FUEGO_GEOS.forEach(function (geo) {
    MARKETS.setOfPots.push({ code: geo, href: '/' + geo + '/casa-fuego/landing.html' });
  });
  CORESYNC_GEOS.forEach(function (geo) {
    MARKETS.coreSync.push({ code: geo, href: '/' + geo + '/smartwatch/landing.html' });
  });

  var LOCALE_MARKETS = {
    en: { setOfPots: CASA_FUEGO_GEOS.slice(), coreSync: CORESYNC_GEOS.slice() }
  };
  SELECT_LOCALES.forEach(function (geo) {
    if (geo === 'en') return;
    LOCALE_MARKETS[geo] = {
      setOfPots: CASA_FUEGO_GEOS.indexOf(geo) >= 0 ? [geo] : [],
      coreSync: CORESYNC_GEOS.indexOf(geo) >= 0 ? [geo] : []
    };
  });

  var LOCALE_GEO = {};
  SELECT_LOCALES.forEach(function (g) { LOCALE_GEO[g] = g; });

  /** Current offer prices from product landings (home only — do not edit landings). */
  var PRODUCT_PRICES = {
    coreSync: {
      bg: '69,00 €', cz: '1.499,00 Kč', de: '69,00 €', ee: '99,00 €', en: '99,00 €',
      es: '49,00 €', fr: '99,00 €', gr: '69,00 €', hr: '99,00 €', hu: '31.999 Ft',
      it: '99,00 €', lt: '54,00 €', lv: '69,00 €', pl: '199,00 zł', pt: '66,00 €',
      ro: '339,00 lei', si: '99,00 €', sk: '99,00 €'
    },
    setOfPots: {
      cz: '1 999 Kč', de: '109,00 €', es: '89,00 €', hu: '31.999 Ft',
      lt: '89,00 €', pl: '399,00 zł', pt: '99,00 €', sk: '89,00 €'
    }
  };

  var PRICED_LINES = {
    en: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Get it now for only {price}',
      product_coreSync_priced: 'CoreSync™ — Get it now for only {price}'
    },
    es: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Consíguelo ya por solo {price}',
      product_coreSync_priced: 'CoreSync™ — Consíguelo ya por solo {price}'
    },
    pt: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Obtenha já por apenas {price}',
      product_coreSync_priced: 'CoreSync™ — Obtenha já por apenas {price}'
    },
    pl: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Zgarnij już za jedyne {price}',
      product_coreSync_priced: 'CoreSync™ — Zgarnij już za jedyne {price}'
    },
    de: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Jetzt für nur {price}',
      product_coreSync_priced: 'CoreSync™ — Jetzt für nur {price}'
    },
    fr: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Obtenez-le dès maintenant pour seulement {price}',
      product_coreSync_priced: 'CoreSync™ — Obtenez-le dès maintenant pour seulement {price}'
    },
    it: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Ottienilo ora a soli {price}',
      product_coreSync_priced: 'CoreSync™ — Ottienilo ora a soli {price}'
    },
    gr: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Αποκτήστε το τώρα μόνο με {price}',
      product_coreSync_priced: 'CoreSync™ — Αποκτήστε το τώρα μόνο με {price}'
    },
    sk: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Zaobstarajte si ho už od {price}',
      product_coreSync_priced: 'CoreSync™ — Zaobstarajte si ho už od {price}'
    },
    cz: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Pořiďte si ho už za {price}',
      product_coreSync_priced: 'CoreSync™ — Pořiďte si ho už za {price}'
    },
    hu: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Szerezze be most mindössze {price}',
      product_coreSync_priced: 'CoreSync™ — Szerezze be most mindössze {price}'
    },
    lt: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Gaukite jau dabar tik už {price}',
      product_coreSync_priced: 'CoreSync™ — Gaukite jau dabar tik už {price}'
    },
    lv: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Iegūstiet to jau tagad tikai par {price}',
      product_coreSync_priced: 'CoreSync™ — Iegūstiet to jau tagad tikai par {price}'
    },
    ro: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Obțineți-l acum pentru doar {price}',
      product_coreSync_priced: 'CoreSync™ — Obțineți-l acum pentru doar {price}'
    },
    bg: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Вземете го сега само за {price}',
      product_coreSync_priced: 'CoreSync™ — Вземете го сега само за {price}'
    },
    hr: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Nabavite odmah za samo {price}',
      product_coreSync_priced: 'CoreSync™ — Nabavite odmah za samo {price}'
    },
    si: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Poiščite ga zdaj za samo {price}',
      product_coreSync_priced: 'CoreSync™ — Poiščite ga zdaj za samo {price}'
    },
    ee: {
      featured_name_priced: 'CoreSync™ — {price}',
      product_setOfPots_priced: 'Set of Pots™ — Hankige kohe vaid {price} eest',
      product_coreSync_priced: 'CoreSync™ — Hankige kohe vaid {price} eest'
    }
  };

  var MESSAGES = {
    en: {
      lang_label: 'Language / region',
      hero_eyebrow: '⭐ Hand-picked weekly',
      hero_title: 'Curated products. Useful design.<br><em>Selected offers.</em>',
      hero_subtitle: 'Hand-picked items for home, garden, and everyday life. Delivery typically in 24–48 business hours after order confirmation, with cash on delivery in supported European countries.',
      hero_cta: 'Our products',
      trust_1_label: '24–48h business days',
      trust_1_sub: 'free shipping',
      trust_2_label: 'Cash on delivery',
      trust_2_sub: 'no prepayment',
      trust_3_label: '30-day refund',
      trust_3_sub: 'see refund policy',
      trust_4_label: '24-month warranty',
      trust_4_sub: 'manufacturer defects',
      featured_eyebrow: "⭐ Today's novelty",
      featured_title: 'Featured product',
      featured_category: 'Tech & Smart',
      featured_name: 'CoreSync™',
      featured_desc: 'A versatile smartwatch to stay connected, track daily activity and review your rest routines from one app. Up to 10 days of battery, 5ATM water resistance, iOS/Android app included. Complete kit with spare strap and screen protectors.',
      collections_title: 'Explore our collections',
      collections_subtitle: 'Offers shown for your selected country. Tap a link to open the product page.',
      product_setOfPots_title: 'Set of Pots™ — Choose your country to see price and availability',
      product_coreSync_title: 'CoreSync™ — Choose your country to see price and availability',
      why_title: 'Why trendtopia-store.com',
      why_1_heading: 'Hand-picked products',
      why_1_text: 'We test every item before adding it to our catalog. No filler, no gadgets — only products that solve real problems.',
      why_2_heading: 'No prepayment, ever',
      why_2_text: "Pay cash to the courier when you receive the package. If you're not happy, refuse the delivery. Clear pricing and policies on every product page.",
      why_3_heading: 'Local customer service',
      why_3_text: 'Native-language support across 18 European countries. Contact us via the support email on each page.',
      footer_info: 'Information',
      footer_about: 'About us',
      footer_contact: 'Contact us',
      footer_privacy: 'Privacy Policy',
      footer_terms: 'Terms & Conditions',
      footer_cookie: 'Cookie Policy',
      footer_shipping: 'Shipping Policy',
      footer_refund: 'Refund Policy',
      footer_rights: 'All rights reserved.'
    },
    es: {
      lang_label: 'Idioma / país',
      hero_eyebrow: '⭐ Selección semanal',
      hero_title: 'Productos seleccionados. Diseño útil.<br><em>Ofertas elegidas.</em>',
      hero_subtitle: 'Artículos elegidos para hogar, jardín y día a día. Entrega habitual en 24–48 h laborables tras confirmar el pedido, con pago contra reembolso en los países disponibles.',
      hero_cta: 'Nuestros productos',
      trust_1_label: '24–48 h laborables',
      trust_1_sub: 'envío gratis',
      trust_2_label: 'Contra reembolso',
      trust_2_sub: 'sin prepago',
      trust_3_label: 'Devolución 30 días',
      trust_3_sub: 'ver política de reembolso',
      trust_4_label: 'Garantía 24 meses',
      trust_4_sub: 'defectos de fabricación',
      featured_eyebrow: '⭐ Novedad del día',
      featured_title: 'Producto destacado',
      featured_category: 'Tecnología',
      featured_name: 'CoreSync™',
      featured_desc: 'Smartwatch versátil para mantenerte conectado, seguir tu actividad diaria y consultar tus rutinas de descanso desde una app. Hasta 10 días de batería, resistencia al agua 5ATM, app iOS/Android incluida.',
      collections_title: 'Explora nuestras colecciones',
      collections_subtitle: 'Ofertas para tu país seleccionado. Pulsa un enlace para abrir la página del producto.',
      product_setOfPots_title: 'Set of Pots™ — Elige tu país para ver precio y disponibilidad',
      product_coreSync_title: 'CoreSync™ — Elige tu país para ver precio y disponibilidad',
      why_title: 'Por qué trendtopia-store.com',
      why_1_heading: 'Productos seleccionados',
      why_1_text: 'Probamos cada artículo antes de incluirlo en el catálogo.',
      why_2_heading: 'Sin prepago',
      why_2_text: 'Pagas al repartidor al recibir el paquete.',
      why_3_heading: 'Atención en tu idioma',
      why_3_text: 'Soporte en idioma local en 18 países europeos.',
      footer_info: 'Información',
      footer_about: 'Sobre nosotros',
      footer_contact: 'Contáctanos',
      footer_privacy: 'Política de privacidad',
      footer_terms: 'Términos y condiciones',
      footer_cookie: 'Política de cookies',
      footer_shipping: 'Política de envío',
      footer_refund: 'Política de reembolso',
      footer_rights: 'Todos los derechos reservados.'
    },
    pt: {
      lang_label: 'Idioma / região',
      hero_eyebrow: '⭐ Seleção semanal',
      hero_title: 'Produtos selecionados. Design útil.<br><em>Ofertas escolhidas.</em>',
      hero_subtitle: 'Artigos para casa, jardim e dia a dia. Entrega habitual em 24–48 horas úteis após confirmação do pedido, com pagamento à cobrança nos países disponíveis.',
      hero_cta: 'Os nossos produtos',
      trust_1_label: '24–48 h úteis',
      trust_1_sub: 'envio grátis',
      trust_2_label: 'Pagamento à cobrança',
      trust_2_sub: 'sem pré-pagamento',
      trust_3_label: 'Reembolso 30 dias',
      trust_3_sub: 'ver política de reembolso',
      trust_4_label: 'Garantia 24 meses',
      trust_4_sub: 'defeitos de fabrico',
      featured_eyebrow: '⭐ Novidade do dia',
      featured_title: 'Produto em destaque',
      featured_category: 'Tech & Smart',
      featured_name: 'CoreSync™',
      featured_desc: 'Smartwatch versátil para se manter conectado, acompanhar a atividade diária e consultar rotinas de descanso numa app.',
      collections_title: 'Explore as nossas coleções',
      collections_subtitle: 'Ofertas para o país selecionado. Toque num link para abrir a página do produto.',
      product_setOfPots_title: 'Set of Pots™ — Escolha o país para ver preço e disponibilidade',
      product_coreSync_title: 'CoreSync™ — Escolha o país para ver preço e disponibilidade',
      why_title: 'Porquê trendtopia-store.com',
      why_1_heading: 'Produtos selecionados',
      why_1_text: 'Testamos cada artigo antes de o incluir no catálogo.',
      why_2_heading: 'Sem pré-pagamento',
      why_2_text: 'Paga ao estafeta na entrega.',
      why_3_heading: 'Apoio no seu idioma',
      why_3_text: 'Suporte em idioma local em 18 países europeus.',
      footer_info: 'Informação',
      footer_about: 'Sobre nós',
      footer_contact: 'Contacto',
      footer_privacy: 'Política de privacidade',
      footer_terms: 'Termos e condições',
      footer_cookie: 'Política de cookies',
      footer_shipping: 'Política de envio',
      footer_refund: 'Política de reembolso',
      footer_rights: 'Todos os direitos reservados.'
    },
    pl: {
      lang_label: 'Język / kraj',
      hero_cta: 'Nasze produkty',
      collections_subtitle: 'Oferty dla wybranego kraju. Kliknij link, aby otworzyć stronę produktu.',
      product_setOfPots_title: 'Set of Pots™ — Wybierz kraj, aby zobaczyć cenę i dostępność',
      product_coreSync_title: 'CoreSync™ — Wybierz kraj, aby zobaczyć cenę i dostępność',
      footer_about: 'O nas',
      footer_contact: 'Kontakt'
    },
    gr: {
      lang_label: 'Γλώσσα / χώρα',
      hero_cta: 'Τα προϊόντα μας',
      collections_subtitle: 'Προσφορές για τη χώρα που επιλέξατε.',
      product_setOfPots_title: 'Set of Pots™ — Επιλέξτε χώρα για τιμή και διαθεσιμότητα',
      product_coreSync_title: 'CoreSync™ — Επιλέξτε χώρα για τιμή και διαθεσιμότητα',
      footer_about: 'Σχετικά με εμάς',
      footer_contact: 'Επικοινωνία'
    },
    sk: {
      lang_label: 'Jazyk / krajina',
      hero_cta: 'Naše produkty',
      product_setOfPots_title: 'Set of Pots™ — Vyberte krajinu pre cenu a dostupnosť',
      footer_about: 'O nás'
    },
    cz: {
      lang_label: 'Jazyk / země',
      hero_cta: 'Naše produkty',
      product_setOfPots_title: 'Set of Pots™ — Zvolte zemi pro cenu a dostupnost',
      footer_about: 'O nás'
    }
  };

  SELECT_LOCALES.forEach(function (loc) {
    if (!MESSAGES[loc]) {
      MESSAGES[loc] = { lang_label: LOCALE_LABELS[loc] };
    }
  });

  var NAV_TO_LOCALE = [
    ['es', 'es'], ['pt', 'pt'], ['pl', 'pl'], ['de', 'de'], ['fr', 'fr'], ['it', 'it'],
    ['hu', 'hu'], ['ro', 'ro'], ['bg', 'bg'], ['hr', 'hr'], ['lt', 'lt'], ['lv', 'lv'],
    ['et', 'ee'], ['sl', 'si'], ['sk', 'sk'], ['cs', 'cz'], ['el', 'gr'], ['gr', 'gr']
  ];

  function isSelectableLocale(locale) {
    return SELECT_LOCALES.indexOf(locale) !== -1;
  }

  function detectLocale() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'el') saved = 'gr';
      if (saved === 'cs') saved = 'cz';
      if (saved && isSelectableLocale(saved)) return saved;
    } catch (e) {}
    var nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
    var i;
    for (i = 0; i < NAV_TO_LOCALE.length; i++) {
      if (nav.indexOf(NAV_TO_LOCALE[i][0]) === 0) return NAV_TO_LOCALE[i][1];
    }
    return 'en';
  }

  function msg(locale, key) {
    var pack = MESSAGES[locale] || {};
    if (pack[key] != null) return pack[key];
    return (MESSAGES.en[key] != null ? MESSAGES.en[key] : '');
  }

  function pricedLine(locale, key, price) {
    var pack = PRICED_LINES[locale] || PRICED_LINES.en;
    var tpl = (pack && pack[key]) || (PRICED_LINES.en && PRICED_LINES.en[key]) || '{price}';
    return tpl.replace(/\{price\}/g, price);
  }

  function applyProductPricing(locale) {
    var geo = locale;
    var useChooserCopy = locale === 'en';

    var featName = document.querySelector('.featured__name[data-i18n="featured_name"]');
    if (featName) {
      if (useChooserCopy) {
        featName.textContent = msg(locale, 'featured_name');
      } else {
        var corePrice = PRODUCT_PRICES.coreSync[geo];
        featName.textContent = corePrice
          ? pricedLine(locale, 'featured_name_priced', corePrice)
          : msg(locale, 'featured_name');
      }
    }

    document.querySelectorAll('[data-i18n="product_setOfPots_title"]').forEach(function (el) {
      if (useChooserCopy) {
        el.textContent = msg(locale, 'product_setOfPots_title');
        return;
      }
      var p = PRODUCT_PRICES.setOfPots[geo];
      el.textContent = p
        ? pricedLine(locale, 'product_setOfPots_priced', p)
        : msg(locale, 'product_setOfPots_title');
    });

    document.querySelectorAll('[data-i18n="product_coreSync_title"]').forEach(function (el) {
      if (useChooserCopy) {
        el.textContent = msg(locale, 'product_coreSync_title');
        return;
      }
      var p = PRODUCT_PRICES.coreSync[geo];
      el.textContent = p
        ? pricedLine(locale, 'product_coreSync_priced', p)
        : msg(locale, 'product_coreSync_title');
    });
  }

  function marketLabel(locale, code) {
    return (code || '').toUpperCase();
  }

  function renderMarketLinks(locale, productKey, container) {
    var picker = container.closest('[data-home-product]');
    var codes = (LOCALE_MARKETS[locale] && LOCALE_MARKETS[locale][productKey]) || [];
    var list = MARKETS[productKey].filter(function (m) {
      return codes.indexOf(m.code) !== -1;
    });
    if (!picker) return;
    if (!list.length) {
      picker.hidden = true;
      return;
    }
    picker.hidden = false;
    container.innerHTML = list
      .map(function (m) {
        return '<a href="' + m.href + '">' + marketLabel(locale, m.code) + '</a>';
      })
      .join(' · ');
  }

  function populateLocaleSelect() {
    var select = document.getElementById('home-locale-select');
    if (!select || select.dataset.populated === '1') return;
    select.textContent = '';
    SELECT_LOCALES.forEach(function (loc) {
      var opt = document.createElement('option');
      opt.value = loc;
      opt.textContent = LOCALE_LABELS[loc];
      select.appendChild(opt);
    });
    select.dataset.populated = '1';
  }

  function applyLocale(locale) {
    if (locale === 'el') locale = 'gr';
    if (locale === 'cs') locale = 'cz';
    if (!isSelectableLocale(locale)) locale = 'en';
    document.documentElement.lang = HTML_LANG[locale] || 'en';

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      el.textContent = msg(locale, el.getAttribute('data-i18n'));
    });
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      el.innerHTML = msg(locale, el.getAttribute('data-i18n-html'));
    });

    var geo = LOCALE_GEO[locale] || 'en';
    document.querySelectorAll('[data-i18n-href]').forEach(function (el) {
      var page = el.getAttribute('data-i18n-href');
      el.setAttribute('href', '/' + geo + '/' + page);
    });

    document.querySelectorAll('[data-market-links]').forEach(function (el) {
      renderMarketLinks(locale, el.getAttribute('data-market-links'), el);
    });

    applyProductPricing(locale);

    var featured = document.querySelector('[data-home-feature="coresync"]');
    var coreCodes = (LOCALE_MARKETS[locale] && LOCALE_MARKETS[locale].coreSync) || [];
    if (featured) featured.hidden = coreCodes.length === 0;

    var select = document.getElementById('home-locale-select');
    if (select && select.value !== locale) select.value = locale;
    var langLabel = document.querySelector('.home-lang__label');
    var langLabelText = msg(locale, 'lang_label');
    if (langLabel) langLabel.textContent = langLabelText;
    if (select) select.setAttribute('aria-label', langLabelText);

    try {
      localStorage.setItem(STORAGE_KEY, locale);
    } catch (e) {}
  }

  function init() {
    populateLocaleSelect();
    var select = document.getElementById('home-locale-select');
    var locale = detectLocale();
    applyLocale(locale);
    if (select) {
      select.addEventListener('change', function () {
        applyLocale(select.value);
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
