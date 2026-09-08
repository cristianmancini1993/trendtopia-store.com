#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply technical fixes to Casa Fuego PL/CZ/SK landings."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LOCALES = {
    "pl": {
        "cookie_change": "Zmień ustawienia plików cookie",
        "site_config": """window.SITE_CONFIG = Object.assign(window.SITE_CONFIG || {}, {
  GEO: 'pl',
  PRODUCT_SLUG: 'casa-fuego',
  COOKIE_TEXT: 'Używamy plików cookie, aby ulepszać działanie strony i analizować ruch.',
  COOKIE_ACCEPT: 'Akceptuję',
  COOKIE_ACCEPT_ALL: 'Akceptuj wszystko',
  COOKIE_REJECT: 'Odrzuć nieistotne',
  COOKIE_MANAGE: 'Zarządzaj preferencjami',
  COOKIE_SAVE: 'Zapisz preferencje',
  COOKIE_CHANGE: 'Zmień ustawienia plików cookie',
  COOKIE_LEARN: 'Dowiedz się więcej'
});""",
    },
    "cz": {
        "cookie_change": "Změnit nastavení souborů cookie",
        "site_config": """window.SITE_CONFIG = Object.assign(window.SITE_CONFIG || {}, {
  GEO: 'cz',
  PRODUCT_SLUG: 'casa-fuego',
  COOKIE_TEXT: 'Používáme technické soubory cookie a soubory cookie třetích stran pro zlepšení vašeho zážitku a analytiku.',
  COOKIE_ACCEPT: 'Přijmout',
  COOKIE_ACCEPT_ALL: 'Přijmout vše',
  COOKIE_REJECT: 'Odmítnout nepodstatné',
  COOKIE_MANAGE: 'Spravovat preference',
  COOKIE_SAVE: 'Uložit preference',
  COOKIE_CHANGE: 'Změnit nastavení souborů cookie',
  COOKIE_LEARN: 'Více informací'
});""",
    },
    "sk": {
        "cookie_change": "Zmeniť nastavenia súborov cookie",
        "site_config": """window.SITE_CONFIG = Object.assign(window.SITE_CONFIG || {}, {
  GEO: 'sk',
  PRODUCT_SLUG: 'casa-fuego',
  COOKIE_TEXT: 'Používame technické cookies a cookies tretích strán na zlepšenie vášho zážitku a analytiku.',
  COOKIE_ACCEPT: 'Prijať',
  COOKIE_ACCEPT_ALL: 'Prijať všetko',
  COOKIE_REJECT: 'Odmietnuť nepodstatné',
  COOKIE_MANAGE: 'Spravovať preferencie',
  COOKIE_SAVE: 'Uložiť preferencie',
  COOKIE_CHANGE: 'Zmeniť nastavenia súborov cookie',
  COOKIE_LEARN: 'Viac informácií'
});""",
    },
}

ADRICE_INLINE = '<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>\n'

OLD_SUBMIT = """    form.addEventListener('submit', function (e) {
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

NEW_SUBMIT = """    form.addEventListener('submit', function (e) {
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
})();
</script>
<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>

</body>"""

CSS_BTN = """.cf-form button:disabled{opacity:.72;cursor:not-allowed;transform:none}
"""
CSS_FOOTER = """.cf-lp .site-footer__list .site-footer__link-btn{
  background:none;border:none;padding:0;margin:0;
  font:inherit;color:inherit;text-decoration:underline;cursor:pointer;
  text-align:left;
}
.cf-lp .site-footer__list .site-footer__link-btn:focus-visible{
  outline:2px solid var(--cf-orange);outline-offset:2px;
}
"""


def patch(geo: str) -> None:
    path = ROOT / geo / "casa-fuego" / "landing.html"
    t = path.read_text(encoding="utf-8")
    loc = LOCALES[geo]

    t = re.sub(
        r"window\.SITE_CONFIG = \{[\s\S]*?\};",
        loc["site_config"],
        t,
        count=1,
    )

    t = t.replace(ADRICE_INLINE, "")

    if "form.dataset.submitting" not in t:
        t = t.replace(OLD_SUBMIT, NEW_SUBMIT)
    elif ADRICE_INLINE.strip() not in t and 'forms/html/js-v2/' not in t.split("</script>")[-1]:
        t = t.replace("</body>", '<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>\n\n</body>')

    cookie_btn = f'        <li><button type="button" class="site-footer__link-btn tt-cookie-change-link">{loc["cookie_change"]}</button></li>'
    if "tt-cookie-change-link" not in t:
        t = t.replace(
            "        <li><a href=\"/" + geo + "/refund-policy.html\">",
            cookie_btn + "\n        <li><a href=\"/" + geo + "/refund-policy.html\">",
        )

    if ".cf-form button:disabled" not in t:
        t = t.replace(
            ".cf-form button:hover{background:var(--cf-orange-dark)}",
            ".cf-form button:hover{background:var(--cf-orange-dark)}\n" + CSS_BTN.strip(),
        )

    if ".site-footer__list .site-footer__link-btn" not in t:
        t = t.replace(
            "@media (min-width:768px){\n  .cf-lp .site-footer{padding:72px 0 48px}",
            CSS_FOOTER + "@media (min-width:768px){\n  .cf-lp .site-footer{padding:72px 0 48px}",
        )

    path.write_text(t, encoding="utf-8", newline="\n")
    print(f"Patched {path.relative_to(ROOT)}")


for g in ("pl", "cz", "sk"):
    patch(g)
