# TECHNICAL_TEST_RESULTS.md

Updated: 2026-09-08 (final regression pass)

## Local verification

| Check | Result |
|-------|--------|
| `scripts/_audit_7urls.py` | 0 CURSOR issues (6 USUARIO: intentional `noindex`) |
| `scripts/_verify_audit_fixes.py` | 36/36 PASS |
| PL Spanish leak (`Seguimiento`, `Incluye`, etc.) | 0 matches |
| PL terms currency | PLN ✓ |
| CZ terms currency | Kč ✓ |
| Smartwatch fake discount / 4100 / HOY (local) | Removed ✓ |
| Casa Fuego fake discount / 3200 / verified (local) | Removed ✓ |
| Home Zero risk / 50% / verified counts | Removed ✓ |

---

## HTTP (AdsBot-Google-Mobile) — production

| URL | HTTP | Redirect | Final URL | Result |
|-----|------|----------|-----------|--------|
| `/es/smartwatch/landing.html` | 200 | none | same | PASS |
| `/pl/smartwatch/landing.html` | 200 | none | same | PASS |
| `/gr/smartwatch/landing.html` | 200 | none | same | PASS |
| `/` | 200 | none | same | PASS |
| `/pl/casa-fuego/landing.html` | 200 | none | same | PASS |
| `/cz/casa-fuego/landing.html` | 200 | none | same | PASS |
| `/sk/casa-fuego/landing.html` | 200 | none | same | PASS |

**GR stability:** 5/5 consecutive requests → 200 (502 NOT REPRODUCIBLE)

---

## Content checks (production, post-conservative pass)

| URL | Promo/urgency | i18n | Currency | Notes |
|-----|---------------|------|----------|-------|
| ES CoreSync | PASS (no 98€/4100/HOY) | ES ✓ | EUR 49 € | offer 3137 / lp 3171 |
| PL CoreSync | PASS | PL ✓ (no Spanish) | 199 zł only | offer 3141 / lp 3175 |
| GR CoreSync | PASS | EL ✓ | EUR | offer 1842 / lp 1862 |
| Home | PASS | EN ✓ | — | ES/PL/GR picker present |
| PL Casa Fuego | PASS | PL ✓ | PLN | 30 dni, offer 3179/3213 |
| CZ Casa Fuego | PASS | CS ✓ | Kč | 30 dní, offer 3251/3285 |
| SK Casa Fuego | PASS | SK ✓ | EUR | 30 dní, offer 3702/3742 |

---

## Per-URL detail

### ES CoreSync — `/es/smartwatch/landing.html`

- **HTTP:** 200
- **Final URL:** `https://trendtopia-store.com/es/smartwatch/landing.html`
- **Browser:** Not automated (static + HTTP only)
- **Mobile:** Not automated
- **Console:** NOT VERIFIED (no browser automation)
- **Network:** Essential assets load over HTTPS; no 5xx observed
- **Form:** POST AdRice; offer=3137, lp=3171; anti-double-submit present
- **Consent:** `consent-default.js` before gtag — PASS (code)
- **Cookies:** NOT VERIFIED runtime (accept/reject/persist)
- **SEO:** lang=es, canonical `/es/smartwatch/landing.html`, noindex intentional
- **Responsive:** NOT VERIFIED (manual viewports)
- **Legal links:** Footer links to `/es/*` policies — present
- **Result:** TECHNICALLY READY

### PL CoreSync — `/pl/smartwatch/landing.html`

- **HTTP:** 200
- **Form:** offer=3141, lp=3175
- **i18n:** H1 and specs fully Polish — VERIFIED
- **Terms:** PLN in `pl/terms-conditions.html` — VERIFIED
- **Result:** TECHNICALLY READY

### GR CoreSync — `/gr/smartwatch/landing.html`

- **HTTP:** 200 × 5 stable
- **Form:** offer=1842, lp=1862
- **Result:** TECHNICALLY READY

### Home — `/`

- **HTTP:** 200
- **Routing:** Country picker ES / PL / GR — no forced ES-only CTA
- **Claims:** Zero risk, 50% off, verified counts removed
- **Result:** TECHNICALLY READY

### PL Casa Fuego — `/pl/casa-fuego/landing.html`

- **HTTP:** 200
- **Returns:** 30 dni consistent with policy
- **Form:** offer=3179, lp=3213; js-v2 ×1; anti-submit
- **Result:** TECHNICALLY READY

### CZ Casa Fuego — `/cz/casa-fuego/landing.html`

- **HTTP:** 200
- **Terms:** Kč in `cz/terms-conditions.html`
- **Thank-you:** gtag currency CZK
- **Result:** TECHNICALLY READY

### SK Casa Fuego — `/sk/casa-fuego/landing.html`

- **HTTP:** 200
- **Currency:** EUR consistent
- **Result:** TECHNICALLY READY

---

## Consent Mode v2 (code order)

| Step | Status |
|------|--------|
| dataLayer created | PASS |
| gtag defined | PASS |
| consent default (denied) before tags | PASS |
| ad_storage / analytics_storage / ad_user_data / ad_personalization | Present in consent-default.js |

**Runtime banner test:** NOT VERIFIED

---

## robots.txt

- Does not block AdsBot or landing paths — PASS (static review)

---

## Tests executed

1. `scripts/_audit_7urls.py`
2. `scripts/_verify_audit_fixes.py`
3. `scripts/_prod_check_7urls.py` (production HTTP + content)
4. GR 5× HTTP stability
5. grep regression: PL Spanish strings, EUR in PL/CZ terms, promo remnants

---

## Limitations (external)

- No Playwright/Cypress in repo
- Consent accept/reject/persistence not browser-tested
- Responsive viewports not manually tested in this pass
- AdsBot HTML vs browser HTML not diffed byte-for-byte
