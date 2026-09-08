# AUDIT_REPORT_GOOGLE_ADS.md

**Proyecto:** trendtopia-store.com  
**Fecha:** 2026-09-08  
**Alcance:** 7 URLs + políticas relacionadas  
**Metodología:** Inventario código → reproducción HTTP → auditoría estática → fixes CURSOR → segunda pasada

---

# RESUMEN EJECUTIVO

| Métrica | Count |
|---------|-------|
| **CRÍTICOS** (abiertos) | 0 |
| **ALTOS** (USUARIO / pendientes) | 12 |
| **MEDIOS** | 8 |
| **BAJOS** | 2 |
| **CURSOR corregidos** | 9 |
| **USUARIO pendientes** | 14 |
| **LEGAL/EXTERNO** | 3 |
| **PASS verificados** | 22 |

**Conclusión:** Las landings están **técnicamente preparadas para solicitar revisión** en cuanto a HTTP, formularios, consentimiento (código), AdRice e idioma. La **aprobación definitiva depende de Google Ads** y de confirmar claims comerciales/técnicos (USUARIO). No enviar campañas con claims ALTO sin evidencia del propietario.

---

# VEREDICTO POR URL

| URL | Veredicto |
|-----|-----------|
| `https://trendtopia-store.com/` | **LISTA CON RIESGOS MENORES** (no es LP Ads; CTAs solo ES) |
| `https://trendtopia-store.com/es/smartwatch/landing.html` | **LISTA CON RIESGOS MENORES** — técnico OK; claims comerciales USUARIO |
| `https://trendtopia-store.com/pl/smartwatch/landing.html` | **LISTA CON RIESGOS MENORES** — fixes idioma aplicados |
| `https://trendtopia-store.com/gr/smartwatch/landing.html` | **LISTA CON RIESGOS MENORES** — HTTP estable (502 no reproducido) |
| `https://trendtopia-store.com/pl/casa-fuego/landing.html` | **LISTA CON RIESGOS MENORES** — fixes técnicos aplicados |
| `https://trendtopia-store.com/cz/casa-fuego/landing.html` | **LISTA CON RIESGOS MENORES** |
| `https://trendtopia-store.com/sk/casa-fuego/landing.html` | **LISTA CON RIESGOS MENORES** |

**NO ENVIAR TODAVÍA** si Google Ads exige substantiation de: +4100 compradores, precios tachados, claims 5ATM/10 días, “zawsze chłodne”, etc., hasta confirmación del propietario.

---

# TABLA DE PROBLEMAS

| URL | Prioridad | Categoría | Elemento | Problema | Evidencia | Archivo | Corrección | Estado | Riesgo Ads |
|-----|-----------|-----------|----------|----------|-----------|---------|------------|--------|------------|
| GR smartwatch | CRÍTICO | PASS | HTTP | 502 histórico | 5/5×200 AdsBot 2026-09-08 | — | — | Cerrado | Bajo (ahora) |
| PL smartwatch | ALTO | CURSOR | H1 | H1 en español | Texto ES en PL | `pl/smartwatch/landing.html` ~400 | Traducido a PL | **Corregido** | Medio |
| PL smartwatch | ALTO | CURSOR | Specs | Mezcla ES/PL en specs | Seguimiento/Incluye | `pl/smartwatch/landing.html` ~575 | PL correcto | **Corregido** | Medio |
| PL/CZ/SK casa-fuego | ALTO | CURSOR | AdRice js-v2 | Script duplicado 2× | 2 loads por form | `*/casa-fuego/landing.html` | 1 load al final | **Corregido** | Alto conv. |
| PL/CZ/SK casa-fuego | MEDIO | CURSOR | Submit | Sin anti doble submit | Falta dataset.submitting | `*/casa-fuego/landing.html` | Añadido | **Corregido** | Medio |
| PL casa-fuego | ALTO | CURSOR | SITE_CONFIG | Sobrescribe sin merge | Pierde GOOGLE_TAG_ID | `pl/casa-fuego/landing.html` | Object.assign | **Corregido** | Medio |
| PL/CZ/SK casa-fuego | MEDIO | CURSOR | Cookies footer | Sin botón preferencias | Solo JS listener | `*/casa-fuego/landing.html` | Botón HTML | **Corregido** | Bajo |
| CZ terms | ALTO | CURSOR | Moneda | “Ceny v eurech” vs Kč | Texto legal | `cz/terms-conditions.html` ~42 | korunách (Kč) | **Corregido** | Medio |
| CZ casa-fuego TY | MEDIO | CURSOR | gtag conversion | currency EUR vs CZK | thank-you | `cz/casa-fuego/thank-you.html` ~327 | CZK | **Corregido** | Medio |
| Casa Fuego PL/CZ/SK | — | PASS | Devolución | 14 vs 30 días | Solo 30 días | landings + refund | — | Verificado | — |
| ES/PL/GR SW | ALTO | USUARIO | Social proof | +4100 compradores | Visible hero | `es/smartwatch/landing.html` | Documentar origen | Pendiente | Alto |
| ES SW | ALTO | USUARIO | Urgencia | “-50% HOY” | Hero price box | `es/smartwatch/landing.html` ~418 | Confirmar promo | Pendiente | Alto |
| ES/PL/GR SW | ALTO | USUARIO | Claims técnicos | 10 días, 5ATM, wellness | Copy + FAQ | smartwatch landings | Ficha técnica | Pendiente | Alto |
| PL Casa Fuego | ALTO | USUARIO | Claims | “zawsze chłodne” | Feature + tabla | `pl/casa-fuego/landing.html` ~440 | Evidencia | Pendiente | Alto |
| Home | MEDIO | USUARIO | CTA | Solo `/es/smartwatch/` | 4 enlaces | `index.html` | Decisión routing | Pendiente | Medio |
| Todas LPs | MEDIO | USUARIO | robots | noindex,nofollow | meta robots | landings | Confirmar intención | Pendiente | Medio |
| Footer all | MEDIO | LEGAL/EXTERNO | Vendedor | HK entity | GLOBAL INTEGRATED… | footers | Abogado UE | Pendiente | Medio |
| Privacy | MEDIO | LEGAL/EXTERNO | GDPR | Transferencias HK | privacy policies | `*/privacy-policy.html` | DPO/abogado | Pendiente | Medio |
| Consent | MEDIO | PASS/CODE | Consent Mode v2 | Default denied antes gtag | consent-default.js | assets | — | Código OK | Bajo |
| Consent runtime | MEDIO | — | Banner | Aceptar/rechazar persistencia | — | — | QA manual | NO VERIFICADO | Medio |

---

# CAMBIOS REALIZADOS POR CURSOR

## 1. `pl/smartwatch/landing.html`

**Motivo:** Español residual en H1 y specs (hallazgo 3.1)

**Antes (H1):** `llamadas, notificaciones, actividad y hasta 10 días de batería en tu muñeca`  
**Después:** `rozmowy, powiadomienia, aktywność i do 10 dni baterii na nadgarstku`

**Antes (specs):** `Seguimiento:` / `Incluye:` / `pasos` / `registros de descanso`  
**Después:** `Śledzenie:` / `W zestawie:` / texto PL completo

**Prueba:** `grep` 0 matches español; `_audit_7urls.py` 0 CURSOR

---

## 2–4. `pl/casa-fuego/landing.html`, `cz/casa-fuego/landing.html`, `sk/casa-fuego/landing.html`

**Motivo:** Paridad técnica con ES smartwatch (AdRice, consent, submit, cookies)

**Cambios:**
- `SITE_CONFIG = Object.assign(...)` + textos cookie localizados
- Eliminado `js-v2` duplicado dentro de forms; 1 script al final
- `form.dataset.submitting` + `btn.disabled`
- Botón footer `tt-cookie-change-link`
- CSS `.site-footer__link-btn` y `:disabled`

**Prueba:** `_audit_7urls.py`; grep `js-v2` = 1 por archivo

---

## 5. `cz/terms-conditions.html`

**Motivo:** Moneda incorrecta (hallazgo 3.4)

**Antes:** `Ceny na webu jsou v eurech`  
**Después:** `Ceny na webu jsou v korunách českých (Kč)`

---

## 6. `cz/casa-fuego/thank-you.html`

**Motivo:** Bug tracking — producto en Kč, conversión en EUR

**Antes:** `'currency': 'EUR'`  
**Después:** `'currency': 'CZK'`

---

## 7. `.github/workflows/vps-deploy.yml`

**Motivo:** Casa Fuego y CZ terms no se desplegaban

**Añadido:** paths y rsync para `pl/cz/sk/casa-fuego` y `cz/terms-conditions.html`

---

## 8. `scripts/_audit_7urls.py`, `scripts/_patch_casa_fuego_3geo.py`

**Motivo:** Automatizar auditoría y parches reproducibles

---

# COSAS QUE DEBE RESOLVER EL PROPIETARIO

## [ALTO] — +4100 compradores reales (CoreSync)

**Qué ve Google/usuario:** “+4100 compradores reales”, “4,6/5”  
**Por qué problemático:** Sin evidencia = misrepresentation risk  
**Confirmar:** Origen de la cifra, metodología, fecha  
**Documento:** Export CRM, reviews verificadas, o ajustar copy  
**Cursor después:** SÍ (una vez confirmado número o texto aprobado)

## [ALTO] — Claims batería 5ATM / 10 días

**Qué ve:** Hero, FAQ, specs, meta description  
**Confirmar:** Manual fabricante, certificados  
**Cursor después:** SÍ (suavizar copy si propietario lo indica)

## [ALTO] — Casa Fuego “zawsze chłodne”

**Qué ve:** Feature title + tabla comparativa PL  
**Confirmar:** Pruebas térmicas o redacción aprobada  
**Cursor después:** SÍ

## [MEDIO] — Home CTAs → solo ES

**Qué ve:** Usuario internacional llega a ES smartwatch  
**Confirmar:** Intención de negocio  
**Cursor después:** SÍ (router geo o selector)

## [MEDIO] — noindex en landings Ads

**Qué ve:** `<meta name="robots" content="noindex, nofollow">`  
**Confirmar:** ¿Intencional para LPs pagadas?  
**Cursor después:** SÍ (si deben indexarse)

---

# LEGAL / EXTERNO

| Texto / tema | Archivo | País | Duda | Profesional | Cambio posterior |
|--------------|---------|------|------|-------------|------------------|
| Vendedor HK, consumidores UE | Footers, privacy | Todos | Ley aplicable, derechos consumidor | Abogado UE comercio electrónico | Actualizar terms/privacy |
| Transferencia datos fuera EEE | privacy-policy | EU locales | Base legal Art. 49 GDPR | DPO / abogado privacidad | Cláusulas contrato |
| Garantía legal vs “24 meses oficial” | landings + terms | PL/CZ/SK | Plazo mínimo legal vs comercial | Asesor consumo | Alinear copy |

---

# PASS CONFIRMADOS

- HTTP 200 estable (7 URLs × 5, AdsBot)
- GR 502 no reproducido
- AdRice offer/lp IDs según configuración propietario
- AdRice POST + uid presente
- js-v2 sin duplicación en 7 URLs auditadas
- Anti doble submit en formularios auditados
- Consent default denied antes de gtag (código)
- Precios coherentes internamente (-50% math)
- Devolución 30 días Casa Fuego (no 14)
- robots.txt no bloquea crawlers
- HTTPS en URLs producción
- PL smartwatch sin español visible post-fix
- CZ terms moneda Kč post-fix
- Enlaces legales footer presentes por geo

---

# RESULTADOS DE TESTS

Ver `TECHNICAL_TEST_RESULTS.md`.

| Prueba | Estado |
|--------|--------|
| HTTP AdsBot | PASS |
| Audit estático | PASS (0 CURSOR) |
| Consent Mode código | PASS |
| Consent runtime | NO VERIFICADO |
| Cookies pre-consent | NO VERIFICADO |
| Browser console | NO VERIFICADO |
| Responsive viewports | NO VERIFICADO |
| Build/lint | N/A |

---

# CHECKLIST FINAL POR URL

## ES CoreSync

- [x] HTTP 200
- [x] canonical correcto (`/es/smartwatch/landing.html`)
- [x] lang es
- [x] offer 3137 / lp 3171
- [x] formulario POST AdRice
- [x] Consent Mode (código)
- [x] precio coherente 49/98 €
- [x] refund coherente (30 días en política ES)
- [x] no double submit
- [x] cookie change footer
- [ ] claims USUARIO documentados
- [ ] noindex — confirmar intención

## PL CoreSync

- [x] HTTP 200
- [x] lang pl
- [x] offer 3141 / lp 3175
- [x] idioma PL (H1 + specs)
- [x] precio 199/398 zł
- [x] formulario + consent
- [ ] claims USUARIO
- [ ] noindex — confirmar

## GR CoreSync

- [x] HTTP 200 estable
- [x] offer 1842 / lp 1862
- [x] precio 69/138 €
- [x] formulario + consent
- [ ] claims USUARIO
- [ ] noindex — confirmar

## PL Casa Fuego

- [x] HTTP 200
- [x] offer 3179 / lp 3213
- [x] 30 dni zwrot
- [x] precio 399/798 zł
- [x] fixes AdRice/submit/cookies
- [ ] claims “zawsze chłodne” USUARIO
- [ ] noindex — confirmar

## CZ Casa Fuego

- [x] HTTP 200
- [x] offer 3251 / lp 3285
- [x] 30 dní + Kč
- [x] terms moneda Kč
- [x] thank-you currency CZK
- [ ] noindex — confirmar

## SK Casa Fuego

- [x] HTTP 200
- [x] offer 3702 / lp 3742
- [x] 89/178 € coherente
- [x] fixes técnicos
- [ ] noindex — confirmar

## Home

- [x] HTTP 200
- [ ] CTA internacional USUARIO
- [ ] claims home USUARIO

---

*Informes relacionados:* `OWNER_EVIDENCE_REQUIRED.md`, `TECHNICAL_TEST_RESULTS.md`, `TODO_BEFORE_GOOGLE_ADS_REVIEW.md`
