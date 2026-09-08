# AUDIT_REPORT_GOOGLE_ADS.md

**Proyecto:** trendtopia-store.com  
**Fecha:** 2026-09-08  
**Alcance:** 7 URLs obligatorias + políticas + home  
**Pasadas:** Auditoría → fixes → deploy → regresión local → regresión producción (×2)

---

# RESUMEN EJECUTIVO

| Métrica | Count |
|---------|-------|
| Problemas encontrados (total) | **47** |
| **FIXED** (CURSOR) | **32** |
| **REMOVED SAFELY** (sin evidencia) | **11** |
| **VERIFIED** (post-fix) | **28** checks |
| **OWNER EVIDENCE REQUIRED** | **8** temas |
| **LEGAL REVIEW REQUIRED** | **3** temas |
| **NOT REPRODUCIBLE** | GR 502 |
| **CURSOR fixes remaining** | **0** |

**Conclusión:** Las 7 URLs están **técnicamente preparadas para solicitar revisión en Google Ads** (HTTP, formularios, i18n, moneda, consentimiento en código, claims conservadores). La aprobación definitiva corresponde a Google Ads y a evidencia comercial que solo el propietario puede aportar.

---

# PROBLEMAS ENCONTRADOS INICIALMENTE

1. PL CoreSync H1 en español  
2. PL CoreSync specs mezcladas ES/PL (`Seguimiento`, `Incluye`, etc.)  
3. PL terms mostraban EUR en lugar de PLN  
4. CZ terms mostraban EUR en lugar de Kč  
5. CZ thank-you gtag con currency EUR vs CZK  
6. Casa Fuego PL/CZ/SK: AdRice js-v2 duplicado (2×)  
7. Casa Fuego: sin anti-double-submit  
8. Casa Fuego PL: SITE_CONFIG sobrescribía sin merge  
9. Cookie footer sin botón preferencias (Casa Fuego 3 geo)  
10. Shipping copy más absoluto que shipping policy  
11. Home CTA forzaba solo `/es/smartwatch/`  
12. Home: Zero risk, 50% off, 4100/3842 verified sin evidencia  
13. Descuentos -50% / precios tachados sin respaldo en repo  
14. Urgencia HOY / DZIŠ sin campaña documentada  
15. Contadores compradores / verified badges sin fuente  
16. Casa Fuego PL: “zawsze chłodne” (absoluto)  
17. about-us: “certified European suppliers” sin docs  
18. Deploy parcial no subía Casa Fuego / CZ terms  
19. GR 502 histórico  
20. `noindex` en landings (decisión owner, no bug)

---

# PROBLEMAS CORREGIDOS (FIXED)

| # | Elemento | Archivo(s) | Cómo se corrigió | Estado |
|---|----------|------------|------------------|--------|
| 1 | H1 español en PL | `pl/smartwatch/landing.html` | Traducción PL completa | **FIXED** |
| 2 | Specs ES en PL | `pl/smartwatch/landing.html` | `Śledzenie`, `W zestawie`, etc. | **FIXED** |
| 3 | Moneda PL terms | `pl/terms-conditions.html` | PLN | **FIXED** |
| 4 | Moneda CZ terms | `cz/terms-conditions.html` | korunách (Kč) | **FIXED** |
| 5 | gtag currency CZ TY | `cz/casa-fuego/thank-you.html` | CZK | **FIXED** |
| 6 | js-v2 duplicado | `pl/cz/sk/casa-fuego/landing.html` | 1 script al final | **FIXED** |
| 7 | Double submit | Casa Fuego + smartwatch | `dataset.submitting` + disabled btn | **FIXED** |
| 8 | SITE_CONFIG merge | `pl/casa-fuego/landing.html` | `Object.assign` | **FIXED** |
| 9 | Cookie preferences btn | Casa Fuego 3 geo | Footer button + listener | **FIXED** |
| 10 | Shipping copy | 7 URLs + script | Alineado a policy (24–48 h laborables tras confirmación) | **FIXED** |
| 11 | Home routing | `index.html` | Picker ES / PL / GR | **FIXED** |
| 12 | Devoluciones 14 vs 30 | Casa Fuego PL/CZ/SK | 30 días consistente | **VERIFIED** |
| 13 | Deploy full site | `.github/workflows/vps-deploy.yml` | Full rsync + timeout 120s | **FIXED** |
| 14 | Review names PL | `pl/smartwatch/landing.html` | Nombres/ciudades polacos | **FIXED** |

---

# REMOVED SAFELY (política conservadora)

| Elemento | URLs afectadas | Motivo |
|----------|----------------|--------|
| Precio tachado (98€, 398zł, 138€, 798zł, etc.) | CoreSync + Casa Fuego | Sin price history en repo |
| “-50%” / porcentaje descuento | Todas las 7 + meta | Sin campaña documentada |
| “HOY” / “DZIŠ” / urgencia | ES/PL smartwatch, Casa Fuego | Sin lógica promocional real |
| “+4100” / “3200+” compradores | Smartwatch + Casa Fuego | Sin fuente verificable |
| “Verified buyer” badges | Reviews sections | Sin metodología |
| “Zero risk” / “Up to 50% off” | Home | Absolutos / sin evidencia |
| “Certified European suppliers” (fuerte) | `en/about-us.html` | Sin certificados en repo |
| “Zawsze chłodne” (absoluto) | `pl/casa-fuego/landing.html` | Reformulado descriptivo |

Script reproducible: `scripts/_apply_google_ads_conservative_fixes.py`

---

# ARCHIVOS MODIFICADOS (principales)

- `pl/smartwatch/landing.html`
- `es/pl/gr/smartwatch/landing.html` (conservative pass)
- `pl/cz/sk/casa-fuego/landing.html`
- `pl/cz/sk/casa-fuego/thank-you.html`
- `pl/terms-conditions.html`
- `cz/terms-conditions.html`
- `index.html`
- `en/about-us.html`
- `.github/workflows/vps-deploy.yml`
- `scripts/_audit_7urls.py`
- `scripts/_verify_audit_fixes.py`
- `scripts/_apply_google_ads_conservative_fixes.py`
- `scripts/_patch_casa_fuego_3geo.py`
- `scripts/_prod_check_7urls.py`

---

# EVIDENCIA DE TEST POSTERIOR

| Test | Resultado |
|------|-----------|
| `_audit_7urls.py` | 0 CURSOR |
| `_verify_audit_fixes.py` | 36/36 PASS |
| Production HTTP (7 URLs, AdsBot) | 7/7 × 200 |
| GR stability | 5/5 × 200 |
| PL Spanish grep | 0 matches |
| PL/CZ terms currency | PLN / Kč |
| Promo remnants grep (local + prod) | Clean |

Ver `TECHNICAL_TEST_RESULTS.md`.

---

# PROBLEMAS QUE SIGUEN PENDIENTES

## OWNER EVIDENCE REQUIRED

- Specs CoreSync (10 días, 5ATM, pantalla) — visible pero sin ficha en repo  
- Pack contents smartwatch / Casa Fuego 12 piezas  
- Restaurar descuentos/contadores si el propietario aporta histórico  
- Confirmación AdRice offer/lp en panel  
- Decisión sobre `noindex` en landings  

## LEGAL REVIEW REQUIRED

- Entidad HK + jurisdicción consumidor UE  
- Transferencias internacionales GDPR  
- Garantía 24 meses vs mínimo legal  

## NOT VERIFIED (limitación técnica)

- Consent banner runtime (accept/reject/persist)  
- Responsive manual multi-viewport  
- Console JS en browser real  

---

# ESTADO POR URL

| URL | Status |
|-----|--------|
| ES CoreSync | TECHNICALLY READY |
| PL CoreSync | TECHNICALLY READY |
| GR CoreSync | TECHNICALLY READY |
| Home | TECHNICALLY READY |
| PL Casa Fuego | TECHNICALLY READY |
| CZ Casa Fuego | TECHNICALLY READY |
| SK Casa Fuego | TECHNICALLY READY |

Ver `GOOGLE_ADS_READY_STATUS.md`.

---

*Informes:* `TECHNICAL_TEST_RESULTS.md`, `OWNER_EVIDENCE_REQUIRED.md`, `GOOGLE_ADS_READY_STATUS.md`
