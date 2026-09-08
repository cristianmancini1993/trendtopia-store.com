# TECHNICAL_TEST_RESULTS.md

Updated: 2026-09-08 (conservative compliance pass #2)

## Local verification (post-fix)

| Check | Result |
|-------|--------|
| `scripts/_audit_7urls.py` | 0 CURSOR issues |
| `scripts/_verify_audit_fixes.py` | 36/36 PASS |
| PL Spanish in smartwatch | 0 matches |
| PL terms currency | PLN ✓ |
| CZ terms currency | Kč ✓ |
| Smartwatch fake discount removed (local) | ✓ |
| Casa Fuego fake discount removed (local) | ✓ |

## HTTP (AdsBot) — run after deploy

| URL | Expected after deploy |
|-----|----------------------|
| `/es/smartwatch/landing.html` | 200, no 4100/98€/HOY |
| `/pl/smartwatch/landing.html` | 200, no Spanish/398 zł promo |
| `/gr/smartwatch/landing.html` | 200 stable |
| `/pl/casa-fuego/landing.html` | 200, no -50% topbar |
| `/cz/casa-fuego/landing.html` | 200, CZK |
| `/sk/casa-fuego/landing.html` | 200, EUR |
| `/` | 200, ES/PL/GR picker |

## Consent Mode (code)

`consent-default.js` → default denied before gtag on all 7 landings. **PASS (code)**

Runtime cookie test: **NOT VERIFIED** (no browser automation in CI).

## Forms / AdRice

| Page | offer | lp | POST | anti-submit |
|------|-------|-----|------|-------------|
| ES SW | 3137 | 3171 | ✓ | ✓ |
| PL SW | 3141 | 3175 | ✓ | ✓ |
| GR SW | 1842 | 1862 | ✓ | ✓ |
| PL CF | 3179 | 3213 | ✓ | ✓ |
| CZ CF | 3251 | 3285 | ✓ | ✓ |
| SK CF | 3702 | 3742 | ✓ | ✓ |

## Deploy

Full-site VPS workflow on every `main` push.
