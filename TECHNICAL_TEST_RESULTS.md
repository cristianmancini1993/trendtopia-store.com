# TECHNICAL_TEST_RESULTS.md

Updated: 2026-09-08 (final pass)

---

## ES CoreSync — `https://trendtopia-store.com/es/smartwatch/landing.html`

| Field | Result |
|-------|--------|
| HTTP | 200 — **VERIFIED** |
| Final URL | Same — **VERIFIED** |
| Redirects | None — **VERIFIED** |
| Browser | NOT_VERIFIED |
| Mobile | NOT_VERIFIED |
| Console | NOT_VERIFIED |
| Network | No 5xx on main document — **VERIFIED** |
| Form | POST AdRice; offer=3137, lp=3171 — **VERIFIED** |
| Double submit | `dataset.submitting` — **VERIFIED** (code) |
| Consent Mode | default before gtag — **VERIFIED** (code) |
| Cookies runtime | NOT_VERIFIED |
| Tracking | js-v2 ×1 — **VERIFIED** |
| SEO | lang=es, canonical self — **VERIFIED** |
| Legal links | `/es/*` footer — **VERIFIED** |
| Responsive | NOT_VERIFIED |
| **Result** | **TECHNICALLY READY** |

---

## PL CoreSync — `https://trendtopia-store.com/pl/smartwatch/landing.html`

| Field | Result |
|-------|--------|
| HTTP | 200 — **VERIFIED** |
| i18n | No Spanish leak — **VERIFIED** |
| Terms PLN | PLN in terms — **VERIFIED** |
| Form | offer=3141, lp=3175 — **VERIFIED** |
| Shipping | Hero + package aligned — **VERIFIED** |
| Consent / Form / Tracking | Same as ES — **VERIFIED** (code) |
| **Result** | **TECHNICALLY READY** |

---

## GR CoreSync — `https://trendtopia-store.com/gr/smartwatch/landing.html`

| Field | Result |
|-------|--------|
| HTTP | 10/10 × 200 AdsBot — **VERIFIED** |
| 502 historical | NOT_REPRODUCIBLE |
| Form | offer=1842, lp=1862 — **VERIFIED** |
| **Result** | **TECHNICALLY READY** |

---

## Home — `https://trendtopia-store.com/`

| Field | Result |
|-------|--------|
| HTTP | 200 — **VERIFIED** |
| Routing | ES/PL/GR picker; `#coresSync-markets` — **VERIFIED** |
| Aggressive claims | Removed — **VERIFIED** |
| **Result** | **TECHNICALLY READY** |

---

## PL Casa Fuego — `https://trendtopia-store.com/pl/casa-fuego/landing.html`

| Field | Result |
|-------|--------|
| HTTP | 200 — **VERIFIED** |
| Returns | 30 dni — **VERIFIED** |
| Currency | PLN; TY gtag PLN — **VERIFIED** |
| Form | offer=3179, lp=3213 — **VERIFIED** |
| **Result** | **TECHNICALLY READY** |

---

## CZ Casa Fuego — `https://trendtopia-store.com/cz/casa-fuego/landing.html`

| Field | Result |
|-------|--------|
| HTTP | 200 — **VERIFIED** |
| Terms / TY | Kč / CZK — **VERIFIED** |
| Returns | 30 dní — **VERIFIED** |
| **Result** | **TECHNICALLY READY** |

---

## SK Casa Fuego — `https://trendtopia-store.com/sk/casa-fuego/landing.html`

| Field | Result |
|-------|--------|
| HTTP | 200 — **VERIFIED** |
| Currency | EUR — **VERIFIED** |
| Returns | 30 dní — **VERIFIED** |
| **Result** | **TECHNICALLY READY** |

---

## Automated tests executed

1. `scripts/_audit_7urls.py` — 0 CURSOR
2. `scripts/_verify_audit_fixes.py` — 40/40 PASS
3. `scripts/_prod_check_7urls.py` — 7/7 PASS
4. GR HTTP × 10 stability

## Tests NOT POSSIBLE

- Consent banner accept/reject/persist (no browser automation)
- Responsive viewports manual
- Live form POST (no real orders)
