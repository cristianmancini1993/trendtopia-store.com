/**
 * Home page (/) — locale selector + product offers per market.
 */
(function () {
  if (!document.body || !document.querySelector('[data-home-i18n-root]')) return;

  var STORAGE_KEY = 'tt-home-locale';
  var COOKIE_KEY = 'tt-home-locale';
  var COOKIE_MAX_AGE = 31536000;

  var CASA_FUEGO_GEOS = ['cz', 'de', 'es', 'hu', 'lt', 'pl', 'pt', 'sk'];
  var CORESYNC_GEOS = ['bg', 'cz', 'de', 'ee', 'en', 'es', 'fr', 'gr', 'hr', 'hu', 'it', 'lt', 'lv', 'pl', 'pt', 'ro', 'si', 'sk'];

  /** English home: only live campaign landings (others stay in repo for future use). */
  var EN_HOME_MARKETS = {
    setOfPots: ['es', 'pl', 'sk', 'cz'],
    coreSync: ['es', 'pl', 'gr']
  };

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

  /**
   * Header selector: English + locales that have a live product landing on site.
   * Derived from EN_HOME_MARKETS (same geos linked on the English home).
   */
  var LOCALES_WITH_LANDING = { en: true };
  EN_HOME_MARKETS.setOfPots.forEach(function (g) { LOCALES_WITH_LANDING[g] = true; });
  EN_HOME_MARKETS.coreSync.forEach(function (g) { LOCALES_WITH_LANDING[g] = true; });

  var SELECT_LOCALES = ['en'].concat(
    Object.keys(LOCALE_LABELS)
      .filter(function (k) { return k !== 'en' && LOCALES_WITH_LANDING[k]; })
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
    en: {
      setOfPots: EN_HOME_MARKETS.setOfPots.slice(),
      coreSync: EN_HOME_MARKETS.coreSync.slice()
    }
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
      page_title: 'trendtopia-store.com — Curated products. Useful design. Selected offers.',
      page_description: 'Hand-picked items for home, garden, and everyday life. 24–48h business days, cash on delivery across 18 European countries. 30-day refund, 24-month warranty.',
      logo_aria: 'trendtopia-store.com home',
      hero_eyebrow: '⭐ New products every week',
      hero_title: 'Chosen with care, <span class="site-logo__text-accent">made for you.</span>',
      hero_subtitle: 'We take care of every detail, from selection until your order reaches your door. Delivery in 24–48 business hours and cash on delivery—your peace of mind is our priority.',
      hero_cta: 'Our products',
      trust_1_label: '24–48h business days',
      trust_1_sub: 'free shipping',
      trust_2_label: 'Cash on delivery',
      trust_2_sub: 'no prepayment',
      trust_3_label: '30-day refund',
      trust_3_sub: 'see refund policy',
      trust_4_label: '24-month warranty',
      trust_4_sub: 'manufacturer defects',
      featured_eyebrow: '⭐ Novelty of the week',
      featured_title: 'Featured product',
      featured_category: 'Tech & Smart',
      featured_name: 'CoreSync™',
      featured_desc: 'A versatile smartwatch to stay connected, track daily activity and review your rest routines from one app. Up to 10 days of battery, 5ATM water resistance, iOS/Android app included. Complete kit with spare strap and screen protectors.',
      featured_img_alt: 'CoreSync — complete smartwatch kit with spare strap, charger, manual and mobile app',
      collections_title: 'Explore our collections',
      collections_subtitle: 'Offers shown for your selected country. Tap a link to open the product page.',
      product_setOfPots_title: 'Set of Pots™ — Choose your country to see price and availability',
      product_coreSync_title: 'CoreSync™ — Choose your country to see price and availability',
      why_title: 'Why trendtopia-store.com',
      why_1_heading: 'Hand-picked products',
      why_1_text: 'We aim to offer you the highest quality in every product. That is why we test them thoroughly in real-world conditions before they reach you.',
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
      footer_rights: 'All rights reserved.',
      footer_contact_heading: 'Contact',
      footer_cookie_change: 'Change cookie preferences',
      cookie_text: 'We use necessary cookies and, with your consent, analytics and advertising cookies.',
      cookie_accept_all: 'Accept all',
      cookie_reject: 'Reject non-essential',
      cookie_manage: 'Manage preferences',
      cookie_save: 'Save preferences',
      cookie_change: 'Change cookie preferences',
      cookie_learn: 'Learn more'
    },
    es: {
      lang_label: 'Idioma / país',
      page_title: 'trendtopia-store.com — Productos seleccionados. Diseño útil. Ofertas elegidas.',
      page_description: 'Artículos para hogar, jardín y día a día. Entrega en 24–48 h laborables, contra reembolso en países disponibles. Devolución 30 días, garantía 24 meses.',
      logo_aria: 'Inicio trendtopia-store.com',
      hero_eyebrow: '⭐ Productos nuevos cada semana',
      hero_title: 'Elegido con cuidado, <span class="site-logo__text-accent">pensado para ti.</span>',
      hero_subtitle: 'Cuidamos cada detalle, desde la selección hasta que el pedido llega a tu puerta. Entrega en 24–48 h laborables y pago contra reembolso, tu tranquilidad es nuestra prioridad.',
      hero_cta: 'Nuestros productos',
      trust_1_label: '24–48 h laborables',
      trust_1_sub: 'envío gratis',
      trust_2_label: 'Contra reembolso',
      trust_2_sub: 'sin prepago',
      trust_3_label: 'Devolución 30 días',
      trust_3_sub: 'ver política de reembolso',
      trust_4_label: 'Garantía 24 meses',
      trust_4_sub: 'defectos de fabricación',
      featured_eyebrow: '⭐ Novedad de la semana',
      featured_title: 'Producto destacado',
      featured_category: 'Tecnología',
      featured_name: 'CoreSync™',
      featured_desc: 'Smartwatch versátil para mantenerte conectado, seguir tu actividad diaria y consultar tus rutinas de descanso desde una app. Hasta 10 días de batería, resistencia al agua 5ATM, app iOS/Android incluida. Kit completo con correa de repuesto y protectores de pantalla.',
      featured_img_alt: 'CoreSync — kit completo de smartwatch con correa extra, cargador, manual y app móvil',
      collections_title: 'Explora nuestras colecciones',
      collections_subtitle: 'Ofertas para tu país seleccionado. Pulsa un enlace para abrir la página del producto.',
      product_setOfPots_title: 'Set of Pots™ — Elige tu país para ver precio y disponibilidad',
      product_coreSync_title: 'CoreSync™ — Elige tu país para ver precio y disponibilidad',
      why_title: 'Por qué trendtopia-store.com',
      why_1_heading: 'Productos seleccionados',
      why_1_text: 'Buscamos ofrecerte la máxima calidad en cada producto. Por eso los probamos exhaustivamente en condiciones reales de uso antes de que lleguen a ti.',
      why_2_heading: 'Sin prepago',
      why_2_text: 'Pagas al repartidor al recibir el paquete. Si no te convence, rechaza el envío. Precios y políticas claras en cada página de producto.',
      why_3_heading: 'Atención en tu idioma',
      why_3_text: 'Soporte en tu idioma en 18 países europeos. Escríbenos al correo de atención de cada página.',
      footer_info: 'Información',
      footer_about: 'Sobre nosotros',
      footer_contact: 'Contáctanos',
      footer_privacy: 'Política de privacidad',
      footer_terms: 'Términos y condiciones',
      footer_cookie: 'Política de cookies',
      footer_shipping: 'Política de envío',
      footer_refund: 'Política de reembolso',
      footer_rights: 'Todos los derechos reservados.',
      footer_contact_heading: 'Contacto',
      footer_cookie_change: 'Cambiar preferencias de cookies',
      cookie_text: 'Usamos cookies necesarias y, con tu consentimiento, cookies analíticas y publicitarias.',
      cookie_accept_all: 'Aceptar todo',
      cookie_reject: 'Rechazar no esenciales',
      cookie_manage: 'Gestionar preferencias',
      cookie_save: 'Guardar preferencias',
      cookie_change: 'Cambiar preferencias de cookies',
      cookie_learn: 'Más información'
    },
    pt: {
      lang_label: 'Idioma / região',
      hero_eyebrow: '⭐ Novos produtos todas as semanas',
      hero_title: 'Escolhido com cuidado, <span class="site-logo__text-accent">pensado para si.</span>',
      hero_subtitle: 'Cuidamos de cada pormenor, desde a seleção até a encomenda chegar à sua porta. Entrega em 24–48 h úteis e pagamento à cobrança, a sua tranquilidade é a nossa prioridade.',
      hero_cta: 'Os nossos produtos',
      trust_1_label: '24–48 h úteis',
      trust_1_sub: 'envio grátis',
      trust_2_label: 'Pagamento à cobrança',
      trust_2_sub: 'sem pré-pagamento',
      trust_3_label: 'Reembolso 30 dias',
      trust_3_sub: 'ver política de reembolso',
      trust_4_label: 'Garantia 24 meses',
      trust_4_sub: 'defeitos de fabrico',
      featured_eyebrow: '⭐ Novidade da semana',
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
      why_1_text: 'Procuramos oferecer-lhe a máxima qualidade em cada produto. Por isso testamo-los exaustivamente em condições reais de utilização antes de chegarem até si.',
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
      page_title: 'trendtopia-store.com — Wybrane produkty. Praktyczny design. Oferty.',
      page_description: 'Produkty do domu, ogrodu i codziennego życia. Dostawa zwykle w 24–48 h roboczych, płatność przy odbiorze w dostępnych krajach. Zwrot 30 dni, gwarancja 24 miesiące.',
      logo_aria: 'Strona główna trendtopia-store.com',
      hero_eyebrow: '⭐ Nowe produkty co tydzień',
      hero_title: 'Wybrane z troską, <span class="site-logo__text-accent">stworzone z myślą o Tobie.</span>',
      hero_subtitle: 'Dbamy o każdy szczegół — od wyboru po dostawę pod Twoje drzwi. Dostawa w 24–48 h roboczych i płatność przy odbiorze, Twój spokój jest dla nas priorytetem.',
      hero_cta: 'Nasze produkty',
      trust_1_label: '24–48 h robocze',
      trust_1_sub: 'darmowa dostawa',
      trust_2_label: 'Płatność przy odbiorze',
      trust_2_sub: 'bez przedpłaty',
      trust_3_label: 'Zwrot 30 dni',
      trust_3_sub: 'zobacz politykę zwrotów',
      trust_4_label: 'Gwarancja 24 miesiące',
      trust_4_sub: 'wady produkcyjne',
      featured_eyebrow: '⭐ Nowość tygodnia',
      featured_title: 'Polecany produkt',
      featured_category: 'Technologia',
      featured_name: 'CoreSync™',
      featured_desc: 'Wszechstronny smartwatch: połączenie z telefonem, śledzenie aktywności i przegląd nawyków snu w jednej aplikacji. Do 10 dni na baterii, wodoszczelność 5ATM, aplikacja na iOS/Android. Komplet z dodatkowym paskiem i foliami na ekran.',
      featured_img_alt: 'CoreSync — kompletny zestaw smartwatch z dodatkowym paskiem, ładowarką, instrukcją i aplikacją',
      collections_title: 'Poznaj nasze kolekcje',
      collections_subtitle: 'Oferty dla wybranego kraju. Kliknij link, aby otworzyć stronę produktu.',
      product_setOfPots_title: 'Set of Pots™ — Wybierz kraj, aby zobaczyć cenę i dostępność',
      product_coreSync_title: 'CoreSync™ — Wybierz kraj, aby zobaczyć cenę i dostępność',
      why_title: 'Dlaczego trendtopia-store.com',
      why_1_heading: 'Starannie wybrane produkty',
      why_1_text: 'Chcemy zapewnić Ci najwyższą jakość każdego produktu. Dlatego testujemy je dokładnie w warunkach realnego użytkowania, zanim trafią do Ciebie.',
      why_2_heading: 'Bez przedpłaty',
      why_2_text: 'Płacisz kurierowi przy odbiorze paczki. Jeśli produkt Ci nie pasuje, możesz odmówić odbioru. Jasne ceny i zasady na każdej stronie produktu.',
      why_3_heading: 'Obsługa w Twoim języku',
      why_3_text: 'Wsparcie w języku lokalnym w 18 krajach Europy. Kontakt przez adres e-mail podany na każdej stronie.',
      footer_info: 'Informacje',
      footer_about: 'O nas',
      footer_contact: 'Kontakt',
      footer_contact_heading: 'Kontakt',
      footer_privacy: 'Polityka prywatności',
      footer_terms: 'Regulamin',
      footer_cookie: 'Polityka plików cookie',
      footer_shipping: 'Polityka wysyłki',
      footer_refund: 'Polityka zwrotów',
      footer_rights: 'Wszelkie prawa zastrzeżone.',
      footer_cookie_change: 'Zmień ustawienia plików cookie',
      cookie_text: 'Używamy niezbędnych plików cookie oraz — za Twoją zgodą — analitycznych i reklamowych.',
      cookie_accept_all: 'Akceptuj wszystkie',
      cookie_reject: 'Odrzuć opcjonalne',
      cookie_manage: 'Zarządzaj ustawieniami',
      cookie_save: 'Zapisz ustawienia',
      cookie_change: 'Zmień ustawienia plików cookie',
      cookie_learn: 'Dowiedz się więcej'
    },
    gr: {
      lang_label: 'Γλώσσα / χώρα',
      page_title: 'trendtopia-store.com — Επιλεγμένα προϊόντα. Χρήσιμος σχεδιασμός. Προσφορές.',
      page_description: 'Προϊόντα για το σπίτι, τον κήπο και την καθημερινότητα. Παράδοση συνήθως σε 24–48 ώρες εργασίας, αντικαταβολή όπου διατίθεται. Επιστροφή 30 ημερών, εγγύηση 24 μηνών.',
      logo_aria: 'Αρχική trendtopia-store.com',
      hero_eyebrow: '⭐ Νέα προϊόντα κάθε εβδομάδα',
      hero_title: 'Επιλεγμένα με προσοχή, <span class="site-logo__text-accent">σκεφτόμενα για εσάς.</span>',
      hero_subtitle: 'Φροντίζουμε κάθε λεπτομέρεια, από την επιλογή μέχρι την παράδοση στην πόρτα σας. Παράδοση σε 24–48 ώρες εργασίας και αντικαταβολή, η ηρεμία σας είναι προτεραιότητά μας.',
      hero_cta: 'Τα προϊόντα μας',
      trust_1_label: '24–48 ώρες εργασίας',
      trust_1_sub: 'δωρεάν αποστολή',
      trust_2_label: 'Αντικαταβολή',
      trust_2_sub: 'χωρίς προπληρωμή',
      trust_3_label: 'Επιστροφή 30 ημερών',
      trust_3_sub: 'δείτε την πολιτική επιστροφών',
      trust_4_label: 'Εγγύηση 24 μηνών',
      trust_4_sub: 'εργοστασιακά ελαττώματα',
      featured_eyebrow: '⭐ Πρόταση της εβδομάδας',
      featured_title: 'Προτεινόμενο προϊόν',
      featured_category: 'Τεχνολογία',
      featured_name: 'CoreSync™',
      featured_desc: 'Ευέλικτο smartwatch για επικοινωνία, παρακολούθηση δραστηριότητας και ύπνου από μία εφαρμογή. Έως 10 ημέρες μπαταρίας, αντίσταση νερού 5ATM, εφαρμογή iOS/Android. Πλήρες κιτ με επιπλέον λουράκι και προστατευτικά οθόνης.',
      featured_img_alt: 'CoreSync — πλήρες κιτ smartwatch με επιπλέον λουράκι, φορτιστή, εγχειρίδιο και εφαρμογή',
      collections_title: 'Εξερευνήστε τις συλλογές μας',
      collections_subtitle: 'Προσφορές για τη χώρα που επιλέξατε. Πατήστε έναν σύνδεσμο για τη σελίδα του προϊόντος.',
      product_setOfPots_title: 'Set of Pots™ — Επιλέξτε χώρα για τιμή και διαθεσιμότητα',
      product_coreSync_title: 'CoreSync™ — Επιλέξτε χώρα για τιμή και διαθεσιμότητα',
      why_title: 'Γιατί trendtopia-store.com',
      why_1_heading: 'Επιλεγμένα προϊόντα',
      why_1_text: 'Στόχος μας είναι να σας προσφέρουμε την υψηλότερη ποιότητα σε κάθε προϊόν. Γι\' αυτό τα δοκιμάζουμε ενδελεχώς σε πραγματικές συνθήκες χρήσης πριν φτάσουν σε εσάς.',
      why_2_heading: 'Χωρίς προπληρωμή',
      why_2_text: 'Πληρώνετε τον courier κατά την παράδοση. Αν δεν σας ταιριάζει, μπορείτε να αρνηθείτε την παραλαβή. Σαφείς τιμές και πολιτικές σε κάθε σελίδα προϊόντος.',
      why_3_heading: 'Υποστήριξη στη γλώσσα σας',
      why_3_text: 'Υποστήριξη στα εθνικά 18 ευρωπαϊκών χωρών. Επικοινωνήστε μέσω του email υποστήριξης σε κάθε σελίδα.',
      footer_info: 'Πληροφορίες',
      footer_about: 'Σχετικά με εμάς',
      footer_contact: 'Επικοινωνία',
      footer_contact_heading: 'Επικοινωνία',
      footer_privacy: 'Πολιτική απορρήτου',
      footer_terms: 'Όροι και προϋποθέσεις',
      footer_cookie: 'Πολιτική cookies',
      footer_shipping: 'Πολιτική αποστολών',
      footer_refund: 'Πολιτική επιστροφών',
      footer_rights: 'Με την επιφύλαξη παντός δικαιώματος.',
      footer_cookie_change: 'Αλλαγή προτιμήσεων cookies',
      cookie_text: 'Χρησιμοποιούμε απαραίτητα cookies και, με τη συγκατάθεσή σας, αναλυτικά και διαφημιστικά cookies.',
      cookie_accept_all: 'Αποδοχή όλων',
      cookie_reject: 'Απόρριψη μη απαραίτητων',
      cookie_manage: 'Διαχείριση προτιμήσεων',
      cookie_save: 'Αποθήκευση προτιμήσεων',
      cookie_change: 'Αλλαγή προτιμήσεων cookies',
      cookie_learn: 'Περισσότερα'
    },
    sk: {
      lang_label: 'Jazyk / krajina',
      page_title: 'trendtopia-store.com — Vybrané produkty. Užitočný dizajn. Ponuky.',
      page_description: 'Produkty pre domácnosť, záhradu a každodenný život. Doručenie zvyčajne do 24–48 hodín, dobierka v dostupných krajinách. Vrátenie do 30 dní, 24-mesačná záruka.',
      logo_aria: 'Domov trendtopia-store.com',
      hero_eyebrow: '⭐ Nové produkty každý týždeň',
      hero_title: 'Vybrané s dôrazom na detail, <span class="site-logo__text-accent">premyslené pre vás.</span>',
      hero_subtitle: 'Staráme sa o každý detail — od výberu až po doručenie k vašim dverám. Doručenie do 24–48 pracovných hodín a platba na dobierku, vaša pohoda je naša priorita.',
      hero_cta: 'Naše produkty',
      trust_1_label: '24–48 prac. hodín',
      trust_1_sub: 'doprava zdarma',
      trust_2_label: 'Dobierka',
      trust_2_sub: 'bez predplatby',
      trust_3_label: 'Vrátenie do 30 dní',
      trust_3_sub: 'pozrite si pravidlá vrátenia',
      trust_4_label: '24-mesačná záruka',
      trust_4_sub: 'výrobné vady',
      featured_eyebrow: '⭐ Novinka týždňa',
      featured_title: 'Odporúčaný produkt',
      featured_category: 'Technológie',
      featured_name: 'CoreSync™',
      featured_desc: 'Univerzálne smart hodinky na prepojenie s telefónom, sledovanie aktivity a spánku v jednej aplikácii. Až 10 dní výdrž, vodotesnosť 5ATM, aplikácia pre iOS/Android. Kompletná sada s náhradným remienkom a ochrannými fóliami.',
      featured_img_alt: 'CoreSync — kompletná sada smart hodiniek s náhradným remienkom, nabíjačkou, návodom a aplikáciou',
      collections_title: 'Preskúmajte naše kolekcie',
      collections_subtitle: 'Ponuky pre vybranú krajinu. Kliknite na odkaz a otvorte stránku produktu.',
      product_setOfPots_title: 'Set of Pots™ — Vyberte krajinu pre cenu a dostupnosť',
      product_coreSync_title: 'CoreSync™ — Vyberte krajinu pre cenu a dostupnosť',
      why_title: 'Prečo trendtopia-store.com',
      why_1_heading: 'Starostlivo vybrané produkty',
      why_1_text: 'Chceme vám ponúknuť maximálnu kvalitu každého produktu. Preto ich dôkladne testujeme v reálnych podmienkach používania skôr, ako sa k vám dostanú.',
      why_2_heading: 'Bez predplatby',
      why_2_text: 'Platíte kuriérovi pri prevzatí balíka. Ak vám nevyhovuje, môžete doručenie odmietnuť. Jasné ceny a pravidlá na každej stránke produktu.',
      why_3_heading: 'Podpora vo vašom jazyku',
      why_3_text: 'Podpora v lokálnom jazyku v 18 európskych krajinách. Kontaktujte nás e-mailom uvedeným na každej stránke.',
      footer_info: 'Informácie',
      footer_about: 'O nás',
      footer_contact: 'Kontakt',
      footer_contact_heading: 'Kontakt',
      footer_privacy: 'Zásady ochrany súkromia',
      footer_terms: 'Obchodné podmienky',
      footer_cookie: 'Zásady cookies',
      footer_shipping: 'Prepravné podmienky',
      footer_refund: 'Pravidlá vrátenia',
      footer_rights: 'Všetky práva vyhradené.',
      footer_cookie_change: 'Zmeniť nastavenia súborov cookie',
      cookie_text: 'Používame nevyhnutné cookies a so súhlasom aj analytické a reklamné cookies.',
      cookie_accept_all: 'Prijať všetko',
      cookie_reject: 'Odmietnuť nepovinné',
      cookie_manage: 'Spravovať nastavenia',
      cookie_save: 'Uložiť nastavenia',
      cookie_change: 'Zmeniť nastavenia súborov cookie',
      cookie_learn: 'Viac informácií'
    },
    cz: {
      lang_label: 'Jazyk / země',
      page_title: 'trendtopia-store.com — Vybrané produkty. Užitečný design. Nabídky.',
      page_description: 'Produkty pro domácnost, zahradu a každodenní život. Doručení obvykle do 24–48 hodin, dobírka v dostupných zemích. Vrácení do 30 dnů, 24měsíční záruka.',
      logo_aria: 'Domů trendtopia-store.com',
      hero_eyebrow: '⭐ Nové produkty každý týden',
      hero_title: 'Pečlivě vybrané, <span class="site-logo__text-accent">navržené pro vás.</span>',
      hero_subtitle: 'Pečujeme o každý detail — od výběru až po doručení k vašim dveřím. Doručení do 24–48 pracovních hodin a platba na dobírku, vaše jistota je naší prioritou.',
      hero_cta: 'Naše produkty',
      trust_1_label: '24–48 prac. hodin',
      trust_1_sub: 'doprava zdarma',
      trust_2_label: 'Dobírka',
      trust_2_sub: 'bez předplatby',
      trust_3_label: 'Vrácení do 30 dnů',
      trust_3_sub: 'viz pravidla vrácení',
      trust_4_label: '24měsíční záruka',
      trust_4_sub: 'vady z výroby',
      featured_eyebrow: '⭐ Novinka týdne',
      featured_title: 'Doporučený produkt',
      featured_category: 'Technologie',
      featured_name: 'CoreSync™',
      featured_desc: 'Univerzální chytré hodinky pro propojení s telefonem, sledování aktivity a spánku v jedné aplikaci. Až 10 dní výdrž, voděodolnost 5ATM, aplikace pro iOS/Android. Kompletní sada s náhradním řemínkem a ochrannými fóliemi.',
      featured_img_alt: 'CoreSync — kompletní sada chytrých hodinek s náhradním řemínkem, nabíječkou, návodem a aplikací',
      collections_title: 'Prohlédněte si naše kolekce',
      collections_subtitle: 'Nabídky pro vybranou zemi. Klepněte na odkaz a otevřete stránku produktu.',
      product_setOfPots_title: 'Set of Pots™ — Zvolte zemi pro cenu a dostupnost',
      product_coreSync_title: 'CoreSync™ — Zvolte zemi pro cenu a dostupnost',
      why_title: 'Proč trendtopia-store.com',
      why_1_heading: 'Pečlivě vybrané produkty',
      why_1_text: 'Usilujeme se vám nabídnout maximální kvalitu každého produktu. Proto je důkladně testujeme v reálných podmínkách použití dříve, než se k vám dostanou.',
      why_2_heading: 'Bez předplatby',
      why_2_text: 'Platíte kurýrovi při převzetí balíku. Pokud vám nevyhovuje, můžete doručení odmítnout. Jasné ceny a pravidla na každé stránce produktu.',
      why_3_heading: 'Podpora ve vašem jazyce',
      why_3_text: 'Podpora v místním jazyce v 18 evropských zemích. Kontaktujte nás e-mailem uvedeným na každé stránce.',
      footer_info: 'Informace',
      footer_about: 'O nás',
      footer_contact: 'Kontakt',
      footer_contact_heading: 'Kontakt',
      footer_privacy: 'Zásady ochrany osobních údajů',
      footer_terms: 'Obchodní podmínky',
      footer_cookie: 'Zásady cookies',
      footer_shipping: 'Přepravní podmínky',
      footer_refund: 'Pravidla vrácení',
      footer_rights: 'Všechna práva vyhrazena.',
      footer_cookie_change: 'Změnit nastavení cookies',
      cookie_text: 'Používáme nezbytné cookies a se souhlasem také analytické a reklamní cookies.',
      cookie_accept_all: 'Přijmout vše',
      cookie_reject: 'Odmítnout nepovinné',
      cookie_manage: 'Spravovat předvolby',
      cookie_save: 'Uložit předvolby',
      cookie_change: 'Změnit nastavení cookies',
      cookie_learn: 'Více informací'
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

  function normalizeLocale(locale) {
    if (locale === 'el') locale = 'gr';
    if (locale === 'cs') locale = 'cz';
    return locale;
  }

  function readCookieLocale() {
    var match = document.cookie.match(/(?:^|;\s*)tt-home-locale=([^;]*)/);
    if (!match) return null;
    try {
      return decodeURIComponent(match[1].replace(/\+/g, ' '));
    } catch (e) {
      return match[1];
    }
  }

  function writeCookieLocale(locale) {
    document.cookie =
      COOKIE_KEY +
      '=' +
      encodeURIComponent(locale) +
      ';path=/;max-age=' +
      COOKIE_MAX_AGE +
      ';SameSite=Lax';
  }

  function getSsrLocale() {
    return document.documentElement.getAttribute('data-ssr-locale');
  }

  function readQueryLang() {
    var match = /[?&]lang=([^&]+)/.exec(window.location.search || '');
    if (!match) return '';
    try {
      return normalizeLocale(decodeURIComponent(match[1].replace(/\+/g, ' ')));
    } catch (e) {
      return normalizeLocale(match[1]);
    }
  }

  function detectLocale() {
    var cookieLoc = normalizeLocale(readCookieLocale() || '');
    if (cookieLoc && isSelectableLocale(cookieLoc)) return cookieLoc;
    try {
      var saved = normalizeLocale(localStorage.getItem(STORAGE_KEY) || '');
      if (saved && isSelectableLocale(saved)) return saved;
    } catch (e) {}
    var nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
    var i;
    for (i = 0; i < NAV_TO_LOCALE.length; i++) {
      if (nav.indexOf(NAV_TO_LOCALE[i][0]) === 0) {
        var detected = NAV_TO_LOCALE[i][1];
        if (isSelectableLocale(detected)) return detected;
        break;
      }
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

  function applySiteConfig(locale) {
    var geo = locale === 'en' ? 'en' : locale;
    window.SITE_CONFIG = window.SITE_CONFIG || {};
    window.SITE_CONFIG.GEO = geo;
    var map = [
      ['cookie_text', 'COOKIE_TEXT'],
      ['cookie_accept_all', 'COOKIE_ACCEPT_ALL'],
      ['cookie_reject', 'COOKIE_REJECT'],
      ['cookie_manage', 'COOKIE_MANAGE'],
      ['cookie_save', 'COOKIE_SAVE'],
      ['cookie_change', 'COOKIE_CHANGE'],
      ['cookie_learn', 'COOKIE_LEARN']
    ];
    map.forEach(function (pair) {
      var val = msg(locale, pair[0]);
      if (val) window.SITE_CONFIG[pair[1]] = val;
    });
  }

  function applyDocumentMeta(locale) {
    var title = msg(locale, 'page_title');
    if (title) document.title = title;
    var desc = msg(locale, 'page_description');
    if (desc) {
      var meta = document.querySelector('meta[name="description"]');
      if (meta) meta.setAttribute('content', desc);
      var ogDesc = document.querySelector('meta[property="og:description"]');
      if (ogDesc) ogDesc.setAttribute('content', desc);
    }
    if (title) {
      var ogTitle = document.querySelector('meta[property="og:title"]');
      if (ogTitle) ogTitle.setAttribute('content', title);
    }
    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) {
      var alt = msg(locale, el.getAttribute('data-i18n-alt'));
      if (alt) el.setAttribute('alt', alt);
    });
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
      var label = msg(locale, el.getAttribute('data-i18n-aria'));
      if (label) el.setAttribute('aria-label', label);
    });
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
    list.sort(function (a, b) {
      return codes.indexOf(a.code) - codes.indexOf(b.code);
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

    applyDocumentMeta(locale);
    applySiteConfig(locale);

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

    writeCookieLocale(locale);
    try {
      localStorage.setItem(STORAGE_KEY, locale);
    } catch (e) {}
    document.documentElement.setAttribute('data-ssr-locale', locale);
  }

  function onLocaleSelectChange(select) {
    var next = normalizeLocale(select.value);
    if (!isSelectableLocale(next)) next = 'en';
    var ssrBefore = normalizeLocale(getSsrLocale() || '');
    applyLocale(next);
    if (ssrBefore && next !== ssrBefore) {
      window.location.replace('/?lang=' + encodeURIComponent(next));
    }
  }

  function bindLocaleSelect(select) {
    if (!select || select.dataset.homeI18nBound === '1') return;
    select.dataset.homeI18nBound = '1';
    var form = select.form;
    function onPick() {
      onLocaleSelectChange(select);
    }
    select.addEventListener('change', onPick);
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        onPick();
      });
    }
  }

  function init() {
    var select = document.getElementById('home-locale-select');
    var ssr = normalizeLocale(getSsrLocale() || '');
    var locale;
    if (ssr && isSelectableLocale(ssr)) {
      var qLang = readQueryLang();
      locale = qLang && isSelectableLocale(qLang) ? qLang : ssr;
      if (qLang && isSelectableLocale(qLang) && window.history && window.history.replaceState) {
        window.history.replaceState(null, '', '/');
      }
    } else {
      populateLocaleSelect();
      locale = detectLocale();
    }
    applyLocale(locale);
    bindLocaleSelect(select);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
