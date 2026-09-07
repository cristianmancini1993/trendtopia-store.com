// ============================================================
// MAIN — site-wide bootstrap (cookie consent, year, smooth scroll)
// ============================================================

(function () {
  var CONSENT_KEY = 'tt_cookie_consent_v2';
  var CONSENT_VERSION = '2026-09-07';

  var I18N = {
    es: {
      accept: 'Aceptar todo',
      reject: 'Rechazar no esenciales',
      manage: 'Gestionar preferencias',
      save: 'Guardar preferencias',
      change: 'Cambiar preferencias de cookies',
      necessary: 'Cookies necesarias',
      necessaryDesc: 'Imprescindibles para el funcionamiento del sitio. Siempre activas.',
      analytics: 'Analítica',
      analyticsDesc: 'Nos ayudan a entender el uso del sitio de forma agregada.',
      ads: 'Publicidad y medición',
      adsDesc: 'Permiten medir conversiones y la eficacia de campañas (p. ej. Google Ads).',
      personalization: 'Personalización publicitaria',
      personalizationDesc: 'Permite anuncios más relevantes según tu actividad.',
      googleData: 'Información sobre el tratamiento de datos por Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    en: {
      accept: 'Accept all',
      reject: 'Reject non-essential',
      manage: 'Manage preferences',
      save: 'Save preferences',
      change: 'Change cookie preferences',
      necessary: 'Necessary cookies',
      necessaryDesc: 'Required for the site to work. Always active.',
      analytics: 'Analytics',
      analyticsDesc: 'Help us understand site usage in aggregate form.',
      ads: 'Advertising and measurement',
      adsDesc: 'Allow conversion measurement and campaign effectiveness (e.g. Google Ads).',
      personalization: 'Ad personalization',
      personalizationDesc: 'Enables more relevant ads based on your activity.',
      googleData: 'How Google processes data',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    cz: {
      accept: 'Přijmout vše',
      reject: 'Odmítnout nepovinné',
      manage: 'Spravovat předvolby',
      save: 'Uložit předvolby',
      change: 'Změnit nastavení cookies',
      necessary: 'Nezbytné cookies',
      necessaryDesc: 'Nutné pro fungování webu. Vždy aktivní.',
      analytics: 'Analytika',
      analyticsDesc: 'Pomáhají pochopit využití webu v souhrnné podobě.',
      ads: 'Reklama a měření',
      adsDesc: 'Umožňují měření konverzí a efektivity kampaní (např. Google Ads).',
      personalization: 'Personalizace reklamy',
      personalizationDesc: 'Umožňuje relevantnější reklamy podle vaší aktivity.',
      googleData: 'Informace o zpracování dat společností Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    pl: {
      accept: 'Akceptuj wszystkie',
      reject: 'Odrzuć opcjonalne',
      manage: 'Zarządzaj ustawieniami',
      save: 'Zapisz ustawienia',
      change: 'Zmień ustawienia plików cookie',
      necessary: 'Niezbędne pliki cookie',
      necessaryDesc: 'Wymagane do działania strony. Zawsze aktywne.',
      analytics: 'Analityka',
      analyticsDesc: 'Pomagają zrozumieć korzystanie ze strony w formie zbiorczej.',
      ads: 'Reklama i pomiar',
      adsDesc: 'Umożliwiają pomiar konwersji i skuteczności kampanii (np. Google Ads).',
      personalization: 'Personalizacja reklam',
      personalizationDesc: 'Umożliwia bardziej trafne reklamy na podstawie aktywności.',
      googleData: 'Informacje o przetwarzaniu danych przez Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    sk: {
      accept: 'Prijať všetko',
      reject: 'Odmietnuť nepovinné',
      manage: 'Spravovať nastavenia',
      save: 'Uložiť nastavenia',
      change: 'Zmeniť nastavenia súborov cookie',
      necessary: 'Nevyhnutné cookies',
      necessaryDesc: 'Potrebné na fungovanie webu. Vždy aktívne.',
      analytics: 'Analytika',
      analyticsDesc: 'Pomáhajú pochopiť využitie webu v súhrnnej podobe.',
      ads: 'Reklama a meranie',
      adsDesc: 'Umožňujú meranie konverzií a efektivity kampaní (napr. Google Ads).',
      personalization: 'Personalizácia reklamy',
      personalizationDesc: 'Umožňuje relevantnejšie reklamy podľa vašej aktivity.',
      googleData: 'Informácie o spracovaní údajov spoločnosťou Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    de: {
      accept: 'Alle akzeptieren',
      reject: 'Optionale ablehnen',
      manage: 'Einstellungen verwalten',
      save: 'Einstellungen speichern',
      change: 'Cookie-Einstellungen ändern',
      necessary: 'Notwendige Cookies',
      necessaryDesc: 'Erforderlich für den Betrieb der Website. Immer aktiv.',
      analytics: 'Analyse',
      analyticsDesc: 'Helfen uns, die Nutzung der Website in aggregierter Form zu verstehen.',
      ads: 'Werbung und Messung',
      adsDesc: 'Ermöglichen Conversion-Messung und Kampagnenwirksamkeit (z. B. Google Ads).',
      personalization: 'Werbepersonalisierung',
      personalizationDesc: 'Ermöglicht relevantere Werbung basierend auf Ihrer Aktivität.',
      googleData: 'Informationen zur Datenverarbeitung durch Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    fr: {
      accept: 'Tout accepter',
      reject: 'Refuser les non essentiels',
      manage: 'Gérer les préférences',
      save: 'Enregistrer les préférences',
      change: 'Modifier les préférences cookies',
      necessary: 'Cookies nécessaires',
      necessaryDesc: 'Indispensables au fonctionnement du site. Toujours actifs.',
      analytics: 'Analytique',
      analyticsDesc: 'Nous aident à comprendre l\'utilisation du site de manière agrégée.',
      ads: 'Publicité et mesure',
      adsDesc: 'Permettent la mesure des conversions et l\'efficacité des campagnes (p. ex. Google Ads).',
      personalization: 'Personnalisation publicitaire',
      personalizationDesc: 'Permet des annonces plus pertinentes selon votre activité.',
      googleData: 'Informations sur le traitement des données par Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    it: {
      accept: 'Accetta tutto',
      reject: 'Rifiuta non essenziali',
      manage: 'Gestisci preferenze',
      save: 'Salva preferenze',
      change: 'Modifica preferenze cookie',
      necessary: 'Cookie necessari',
      necessaryDesc: 'Essenziali per il funzionamento del sito. Sempre attivi.',
      analytics: 'Analitica',
      analyticsDesc: 'Ci aiutano a comprendere l\'uso del sito in forma aggregata.',
      ads: 'Pubblicità e misurazione',
      adsDesc: 'Consentono la misurazione delle conversioni e l\'efficacia delle campagne (es. Google Ads).',
      personalization: 'Personalizzazione pubblicitaria',
      personalizationDesc: 'Consente annunci più pertinenti in base alla tua attività.',
      googleData: 'Informazioni sul trattamento dei dati da parte di Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    pt: {
      accept: 'Aceitar tudo',
      reject: 'Rejeitar não essenciais',
      manage: 'Gerir preferências',
      save: 'Guardar preferências',
      change: 'Alterar preferências de cookies',
      necessary: 'Cookies necessários',
      necessaryDesc: 'Essenciais para o funcionamento do site. Sempre ativos.',
      analytics: 'Analítica',
      analyticsDesc: 'Ajudam-nos a compreender a utilização do site de forma agregada.',
      ads: 'Publicidade e medição',
      adsDesc: 'Permitem medir conversões e eficácia de campanhas (ex.: Google Ads).',
      personalization: 'Personalização publicitária',
      personalizationDesc: 'Permite anúncios mais relevantes com base na sua atividade.',
      googleData: 'Informações sobre o tratamento de dados pela Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    gr: {
      accept: 'Αποδοχή όλων',
      reject: 'Απόρριψη μη απαραίτητων',
      manage: 'Διαχείριση προτιμήσεων',
      save: 'Αποθήκευση προτιμήσεων',
      change: 'Αλλαγή προτιμήσεων cookies',
      necessary: 'Απαραίτητα cookies',
      necessaryDesc: 'Απαραίτητα για τη λειτουργία του ιστότοπου. Πάντα ενεργά.',
      analytics: 'Αναλυτικά',
      analyticsDesc: 'Μας βοηθούν να κατανοήσουμε τη χρήση του ιστότοπου σε συγκεντρωτική μορφή.',
      ads: 'Διαφήμιση και μέτρηση',
      adsDesc: 'Επιτρέπουν μέτρηση μετατροπών και αποτελεσματικότητας καμπανιών (π.χ. Google Ads).',
      personalization: 'Εξατομίκευση διαφημίσεων',
      personalizationDesc: 'Επιτρέπει πιο σχετικές διαφημίσεις βάσει της δραστηριότητάς σας.',
      googleData: 'Πληροφορίες για την επεξεργασία δεδομένων από την Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    hu: {
      accept: 'Összes elfogadása',
      reject: 'Nem szükségesek elutasítása',
      manage: 'Beállítások kezelése',
      save: 'Beállítások mentése',
      change: 'Cookie-beállítások módosítása',
      necessary: 'Szükséges sütik',
      necessaryDesc: 'A webhely működéséhez elengedhetetlenek. Mindig aktív.',
      analytics: 'Analitika',
      analyticsDesc: 'Segítenek megérteni az oldal használatát összesített formában.',
      ads: 'Hirdetés és mérés',
      adsDesc: 'Lehetővé teszi a konverziók és kampányhatékonyság mérését (pl. Google Ads).',
      personalization: 'Hirdetésszemélyesítés',
      personalizationDesc: 'Relevánsabb hirdetéseket tesz lehetővé az aktivitása alapján.',
      googleData: 'Információk a Google adatkezeléséről',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    hr: {
      accept: 'Prihvati sve',
      reject: 'Odbij nebitne',
      manage: 'Upravljaj postavkama',
      save: 'Spremi postavke',
      change: 'Promijeni postavke kolačića',
      necessary: 'Nužni kolačići',
      necessaryDesc: 'Potrebni za rad stranice. Uvijek aktivni.',
      analytics: 'Analitika',
      analyticsDesc: 'Pomažu nam razumjeti korištenje stranice u agregiranom obliku.',
      ads: 'Oglašavanje i mjerenje',
      adsDesc: 'Omogućuju mjerenje konverzija i učinkovitosti kampanja (npr. Google Ads).',
      personalization: 'Personalizacija oglasa',
      personalizationDesc: 'Omogućuje relevantnije oglase na temelju vaše aktivnosti.',
      googleData: 'Informacije o obradi podataka od strane Googlea',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    ro: {
      accept: 'Acceptă tot',
      reject: 'Respinge neesențiale',
      manage: 'Gestionează preferințele',
      save: 'Salvează preferințele',
      change: 'Schimbă preferințele cookie',
      necessary: 'Cookie-uri necesare',
      necessaryDesc: 'Esențiale pentru funcționarea site-ului. Întotdeauna active.',
      analytics: 'Analiză',
      analyticsDesc: 'Ne ajută să înțelegem utilizarea site-ului în formă agregată.',
      ads: 'Publicitate și măsurare',
      adsDesc: 'Permit măsurarea conversiilor și eficacității campaniilor (ex. Google Ads).',
      personalization: 'Personalizare publicitară',
      personalizationDesc: 'Permite anunțuri mai relevante pe baza activității dvs.',
      googleData: 'Informații despre procesarea datelor de către Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    bg: {
      accept: 'Приеми всички',
      reject: 'Отхвърли неосновни',
      manage: 'Управление на предпочитанията',
      save: 'Запази предпочитанията',
      change: 'Промяна на предпочитанията за бисквитки',
      necessary: 'Необходими бисквитки',
      necessaryDesc: 'Необходими за работата на сайта. Винаги активни.',
      analytics: 'Аналитика',
      analyticsDesc: 'Помагат ни да разберем използването на сайта в обобщен вид.',
      ads: 'Реклама и измерване',
      adsDesc: 'Позволяват измерване на конверсиите и ефективността на кампаниите (напр. Google Ads).',
      personalization: 'Рекламна персонализация',
      personalizationDesc: 'Позволява по-релевантни реклами според вашата активност.',
      googleData: 'Информация за обработката на данни от Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    lt: {
      accept: 'Priimti viską',
      reject: 'Atmesti nebūtinus',
      manage: 'Tvarkyti nustatymus',
      save: 'Išsaugoti nustatymus',
      change: 'Keisti slapukų nustatymus',
      necessary: 'Būtini slapukai',
      necessaryDesc: 'Reikalingi svetainės veikimui. Visada aktyvūs.',
      analytics: 'Analitika',
      analyticsDesc: 'Padeda suprasti svetainės naudojimą apibendrinta forma.',
      ads: 'Reklama ir matavimas',
      adsDesc: 'Leidžia matuoti konversijas ir kampanijų efektyvumą (pvz., Google Ads).',
      personalization: 'Reklamos personalizavimas',
      personalizationDesc: 'Leidžia aktualesnes reklamas pagal jūsų veiklą.',
      googleData: 'Informacija apie „Google“ duomenų tvarkymą',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    lv: {
      accept: 'Pieņemt visu',
      reject: 'Noraidīt nebūtiskos',
      manage: 'Pārvaldīt iestatījumus',
      save: 'Saglabāt iestatījumus',
      change: 'Mainīt sīkdatņu iestatījumus',
      necessary: 'Nepieciešamās sīkdatnes',
      necessaryDesc: 'Nepieciešamas vietnes darbībai. Vienmēr aktīvas.',
      analytics: 'Analītika',
      analyticsDesc: 'Palīdz saprast vietnes lietojumu apkopotā veidā.',
      ads: 'Reklāma un mērīšana',
      adsDesc: 'Ļauj mērīt konversijas un kampaņu efektivitāti (piem., Google Ads).',
      personalization: 'Reklāmas personalizācija',
      personalizationDesc: 'Ļauj atbilstošākas reklamas, pamatojoties uz jūsu aktivitāti.',
      googleData: 'Informācija par Google datu apstrādi',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    ee: {
      accept: 'Nõustu kõigega',
      reject: 'Keeldu mittevajalikest',
      manage: 'Halda eelistusi',
      save: 'Salvesta eelistused',
      change: 'Muuda küpsiste eelistusi',
      necessary: 'Vajalikud küpsised',
      necessaryDesc: 'Vajalikud saidi toimimiseks. Alati aktiivsed.',
      analytics: 'Analüütika',
      analyticsDesc: 'Aitavad mõista saidi kasutust koondatud kujul.',
      ads: 'Reklaam ja mõõtmine',
      adsDesc: 'Võimaldavad mõõta konversioone ja kampaaniate tõhusust (nt Google Ads).',
      personalization: 'Reklaami personaliseerimine',
      personalizationDesc: 'Võimaldab asjakohasemaid reklaame teie tegevuse põhjal.',
      googleData: 'Teave Google\'i andmetöötluse kohta',
      googleDataUrl: 'https://business.safety.google/privacy/'
    },
    si: {
      accept: 'Sprejmi vse',
      reject: 'Zavrni neobvezne',
      manage: 'Upravljaj nastavitve',
      save: 'Shrani nastavitve',
      change: 'Spremeni nastavitve piškotkov',
      necessary: 'Nujni piškotki',
      necessaryDesc: 'Potrebni za delovanje spletnega mesta. Vedno aktivni.',
      analytics: 'Analitika',
      analyticsDesc: 'Pomagajo razumeti uporabo spletnega mesta v agregirani obliki.',
      ads: 'Oglaševanje in merjenje',
      adsDesc: 'Omogočajo merjenje konverzij in učinkovitosti kampanj (npr. Google Ads).',
      personalization: 'Personalizacija oglasov',
      personalizationDesc: 'Omogoča bolj relevantne oglase glede na vašo dejavnost.',
      googleData: 'Informacije o obdelavi podatkov s strani Google',
      googleDataUrl: 'https://business.safety.google/privacy/'
    }
  };

  function geo() {
    return (window.SITE_CONFIG && window.SITE_CONFIG.GEO) || 'en';
  }

  function t(key) {
    var g = geo();
    var pack = I18N[g] || I18N.en;
    if (window.SITE_CONFIG) {
      var map = {
        accept: 'COOKIE_ACCEPT_ALL',
        reject: 'COOKIE_REJECT',
        manage: 'COOKIE_MANAGE',
        save: 'COOKIE_SAVE',
        change: 'COOKIE_CHANGE'
      };
      if (map[key] && window.SITE_CONFIG[map[key]]) return window.SITE_CONFIG[map[key]];
    }
    return pack[key] || I18N.en[key] || key;
  }

  function labels() {
    var g = geo();
    return I18N[g] || I18N.en;
  }

  function readConsent() {
    try {
      var raw = localStorage.getItem(CONSENT_KEY);
      if (!raw) return null;
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  function writeConsent(state) {
    try {
      localStorage.setItem(CONSENT_KEY, JSON.stringify({
        version: CONSENT_VERSION,
        analytics: !!state.analytics,
        ads: !!state.ads,
        personalization: !!state.personalization,
        ts: Date.now()
      }));
    } catch (e) {
      // ignore
    }
  }

  function applyGtagConsent(state) {
    if (typeof window.gtag !== 'function') return;
    var granted = state.ads || state.analytics || state.personalization;
    window.gtag('consent', 'update', {
      ad_storage: state.ads ? 'granted' : 'denied',
      analytics_storage: state.analytics ? 'granted' : 'denied',
      ad_user_data: state.ads ? 'granted' : 'denied',
      ad_personalization: state.personalization ? 'granted' : 'denied'
    });
    if (granted && window.SITE_CONFIG && window.SITE_CONFIG.GOOGLE_TAG_ID && !window.__ttGtagConfigured) {
      window.gtag('config', window.SITE_CONFIG.GOOGLE_TAG_ID);
      window.__ttGtagConfigured = true;
    }
  }

  function cookiePolicyUrl() {
    return '/' + geo() + '/cookie-policy.html';
  }

  function removeBanner() {
    var el = document.getElementById('tt-cookie-banner');
    if (el) el.remove();
    var modal = document.getElementById('tt-cookie-modal');
    if (modal) modal.remove();
    document.body.classList.remove('tt-cookie-modal-open');
  }

  function buildModal(onSave) {
    var L = labels();
    var modal = document.createElement('div');
    modal.id = 'tt-cookie-modal';
    modal.className = 'tt-cookie-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-labelledby', 'tt-cookie-modal-title');
    modal.innerHTML =
      '<div class="tt-cookie-modal__panel">' +
        '<h2 id="tt-cookie-modal-title" class="tt-cookie-modal__title">' + t('manage') + '</h2>' +
        '<div class="tt-cookie-pref">' +
          '<div><strong>' + L.necessary + '</strong><p>' + L.necessaryDesc + '</p></div>' +
          '<span class="tt-cookie-pref__always" aria-hidden="true">✓</span>' +
        '</div>' +
        '<label class="tt-cookie-pref"><span><strong>' + L.analytics + '</strong><p>' + L.analyticsDesc + '</p></span>' +
          '<input type="checkbox" id="tt-pref-analytics"></label>' +
        '<label class="tt-cookie-pref"><span><strong>' + L.ads + '</strong><p>' + L.adsDesc + '</p></span>' +
          '<input type="checkbox" id="tt-pref-ads"></label>' +
        '<label class="tt-cookie-pref"><span><strong>' + L.personalization + '</strong><p>' + L.personalizationDesc + '</p></span>' +
          '<input type="checkbox" id="tt-pref-personalization"></label>' +
        '<p class="tt-cookie-modal__links">' +
          '<a href="' + cookiePolicyUrl() + '">' + ((window.SITE_CONFIG && window.SITE_CONFIG.COOKIE_LEARN) || 'Cookie policy') + '</a> · ' +
          '<a href="' + L.googleDataUrl + '" target="_blank" rel="noopener noreferrer">' + L.googleData + '</a>' +
        '</p>' +
        '<div class="tt-cookie-modal__actions">' +
          '<button type="button" class="tt-cookie-btn tt-cookie-btn--secondary" id="tt-cookie-modal-close">' + t('reject') + '</button>' +
          '<button type="button" class="tt-cookie-btn tt-cookie-btn--primary" id="tt-cookie-modal-save">' + t('save') + '</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(modal);

    modal.querySelector('#tt-cookie-modal-close').addEventListener('click', function () {
      onSave({ analytics: false, ads: false, personalization: false });
    });
    modal.querySelector('#tt-cookie-modal-save').addEventListener('click', function () {
      onSave({
        analytics: modal.querySelector('#tt-pref-analytics').checked,
        ads: modal.querySelector('#tt-pref-ads').checked,
        personalization: modal.querySelector('#tt-pref-personalization').checked
      });
    });
    modal.addEventListener('click', function (e) {
      if (e.target === modal) {
        modal.remove();
        document.body.classList.remove('tt-cookie-modal-open');
      }
    });
    return modal;
  }

  function showPreferences(existing) {
    removeBanner();
    document.body.classList.add('tt-cookie-modal-open');
    var modal = buildModal(function (state) {
      writeConsent(state);
      applyGtagConsent(state);
      modal.remove();
      document.body.classList.remove('tt-cookie-modal-open');
    });
    if (existing) {
      modal.querySelector('#tt-pref-analytics').checked = !!existing.analytics;
      modal.querySelector('#tt-pref-ads').checked = !!existing.ads;
      modal.querySelector('#tt-pref-personalization').checked = !!existing.personalization;
    }
    modal.querySelector('#tt-cookie-modal-save').focus();
  }

  function showBanner() {
    if (document.getElementById('tt-cookie-banner')) return;
    var L = labels();
    var cookieText = (window.SITE_CONFIG && window.SITE_CONFIG.COOKIE_TEXT) ||
      'We use necessary cookies and, with your consent, analytics and advertising cookies.';
    var banner = document.createElement('div');
    banner.id = 'tt-cookie-banner';
    banner.className = 'tt-cookie-banner';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.innerHTML =
      '<div class="tt-cookie-banner__inner">' +
        '<p class="tt-cookie-banner__text">' + cookieText + '</p>' +
        '<div class="tt-cookie-banner__links">' +
          '<a href="' + cookiePolicyUrl() + '">' + ((window.SITE_CONFIG && window.SITE_CONFIG.COOKIE_LEARN) || 'Learn more') + '</a>' +
          '<a href="' + L.googleDataUrl + '" target="_blank" rel="noopener noreferrer">' + L.googleData + '</a>' +
        '</div>' +
        '<div class="tt-cookie-banner__actions">' +
          '<button type="button" class="tt-cookie-btn tt-cookie-btn--secondary" id="tt-cookie-reject">' + t('reject') + '</button>' +
          '<button type="button" class="tt-cookie-btn tt-cookie-btn--ghost" id="tt-cookie-manage">' + t('manage') + '</button>' +
          '<button type="button" class="tt-cookie-btn tt-cookie-btn--primary" id="tt-cookie-accept">' + t('accept') + '</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);

    banner.querySelector('#tt-cookie-accept').addEventListener('click', function () {
      var state = { analytics: true, ads: true, personalization: true };
      writeConsent(state);
      applyGtagConsent(state);
      removeBanner();
    });
    banner.querySelector('#tt-cookie-reject').addEventListener('click', function () {
      var state = { analytics: false, ads: false, personalization: false };
      writeConsent(state);
      applyGtagConsent(state);
      removeBanner();
    });
    banner.querySelector('#tt-cookie-manage').addEventListener('click', function () {
      showPreferences(readConsent());
    });
  }

  function injectFooterPreferencesLink() {
    var footers = document.querySelectorAll('.site-footer__bottom, .site-footer');
    if (!footers.length) return;
    var target = footers[footers.length - 1];
    if (target.querySelector('.tt-cookie-change-link')) return;
    var link = document.createElement('button');
    link.type = 'button';
    link.className = 'tt-cookie-change-link';
    link.textContent = t('change');
    link.addEventListener('click', function () {
      showPreferences(readConsent());
    });
    if (target.classList.contains('site-footer__bottom')) {
      target.appendChild(document.createTextNode(' · '));
      target.appendChild(link);
    } else {
      var wrap = document.createElement('p');
      wrap.className = 'site-footer__bottom';
      wrap.style.borderTop = 'none';
      wrap.style.paddingTop = '0';
      wrap.appendChild(link);
      target.appendChild(wrap);
    }
  }

  function initConsent() {
    var saved = readConsent();
    if (saved && saved.version === CONSENT_VERSION) {
      applyGtagConsent(saved);
      injectFooterPreferencesLink();
      return;
    }
    if (saved && saved.version !== CONSENT_VERSION) {
      try { localStorage.removeItem(CONSENT_KEY); } catch (e) { /* ignore */ }
    }
    showBanner();
    injectFooterPreferencesLink();
  }

  document.addEventListener('DOMContentLoaded', function () {
    var years = document.querySelectorAll('[data-year]');
    var y = new Date().getFullYear();
    years.forEach(function (el) { el.textContent = y; });

    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener('click', function (e) {
        var id = link.getAttribute('href');
        if (!id || id === '#') return;
        var target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });

    initConsent();
  });

  window.ttOpenCookiePreferences = function () {
    showPreferences(readConsent());
  };
})();
