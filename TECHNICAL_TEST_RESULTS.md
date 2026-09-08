# TECHNICAL_TEST_RESULTS.md

Auditoría ejecutada: 2026-09-08 (UTC+2)  
Repositorio: `trendtopia-store.com-1`  
Alcance: 7 URLs Google Ads + controles estáticos en código fuente

---

## 1. HTTP / AdsBot-Google

**Método:** 5 peticiones consecutivas por URL, `User-Agent: AdsBot-Google`, timeout 20s.

| URL | Resultado |
|-----|-----------|
| `/` | 5/5 × HTTP 200 |
| `/es/smartwatch/landing.html` | 5/5 × HTTP 200 |
| `/pl/smartwatch/landing.html` | 5/5 × HTTP 200 |
| `/gr/smartwatch/landing.html` | 5/5 × HTTP 200 |
| `/pl/casa-fuego/landing.html` | 5/5 × HTTP 200 |
| `/cz/casa-fuego/landing.html` | 5/5 × HTTP 200 |
| `/sk/casa-fuego/landing.html` | 5/5 × HTTP 200 |

**GR 502 histórico:** NO reproducido en esta sesión (5/5 × 200).

**Estado:** PASS

---

## 2. robots.txt

- `User-agent: *` → `Allow: /`
- No bloquea AdsBot ni rutas smartwatch/casa-fuego auditadas
- Sitemap declarado: `https://trendtopia-store.com/sitemap.xml`

**Estado:** PASS

---

## 3. Auditoría estática (`scripts/_audit_7urls.py`)

**Post-correcciones:** 7 hallazgos, todos categoría USUARIO (noindex intencional + home CTA ES).

**Estado CURSOR:** PASS (0 issues CURSOR pendientes en las 7 URLs)

---

## 4. Consent Mode v2 (código)

**Archivo:** `assets/js/consent-default.js`

```javascript
gtag('consent', 'default', {
  ad_storage: 'denied',
  analytics_storage: 'denied',
  ad_user_data: 'denied',
  ad_personalization: 'denied',
  wait_for_update: 500
});
```

**Landings auditadas:** `consent-default.js` cargado en `<head>` **antes** de `gtag/js` (ES/PL/GR smartwatch; PL/CZ/SK casa-fuego).

**Estado código:** PASS  
**Estado runtime (aceptar/rechazar/persistencia):** NO VERIFICADO — no hay Playwright/navegador automatizado en este entorno.

---

## 5. AdRice — formularios

| Página | offer | lp | uid | js-v2 loads | POST action |
|--------|-------|-----|-----|-------------|-------------|
| ES CoreSync | 3137 | 3171 | 019e5f4e-… | 1 | `https://offers.adricenetwork.com/forms/html/` |
| PL CoreSync | 3141 | 3175 | 019e5f4e-… | 1 | idem |
| GR CoreSync | 1842 | 1862 | 019e5f4e-… | 1 | idem |
| PL Casa Fuego | 3179 | 3213 | 019e5f4e-… | 1 | idem |
| CZ Casa Fuego | 3251 | 3285 | 019e5f4e-… | 1 | idem |
| SK Casa Fuego | 3702 | 3742 | 019e5f4e-… | 1 | idem |

**Anti doble submit:** `form.dataset.submitting` + `btn.disabled` en ES/PL/GR smartwatch y PL/CZ/SK casa-fuego.

**Estado:** PASS (implementación verificada en código)

---

## 6. Precios — coherencia matemática

| Landing | Actual | Anterior | Descuento declarado | Cálculo 1−(actual/anterior) |
|---------|--------|----------|---------------------|----------------------------|
| ES CoreSync | 49,00 € | 98,00 € | 50% | 50% ✓ |
| PL CoreSync | 199,00 zł | 398,00 zł | 50% | 50% ✓ |
| GR CoreSync | 69,00 € | 138,00 € | 50% | 50% ✓ |
| PL Casa Fuego | 399,00 zł | 798,00 zł | 50% | 50% ✓ |
| CZ Casa Fuego | 1 999 Kč | 3 998 Kč | 50% | 50% ✓ |
| SK Casa Fuego | 89,00 € | 178,00 € | 50% | 50% ✓ |

Representaciones hero / sticky / formulario / paquete: coherentes por landing (grep manual).

**Estado:** PASS (coherencia interna)  
**Autenticidad comercial precio tachado:** USUARIO — no verificable en repo.

---

## 7. Devoluciones Casa Fuego

Referencias **30 días** en landing PL/CZ/SK y políticas de refund enlazadas.  
No se encontró `14 dni` / `14 dní` en casa-fuego.

**Estado:** PASS

---

## 8. Moneda legal Chequia

- `cz/terms-conditions.html`: corregido a **korunách českých (Kč)**
- `cz/casa-fuego/thank-you.html`: conversión Google Ads `currency: 'CZK'` (antes EUR)

**Estado:** PASS (post-fix)

---

## 9. Idioma PL CoreSync

- H1 español residual: **corregido** a polaco
- Specs (`Śledzenie`, `W zestawie`): **corregidos** previamente
- Grep post-fix: 0 coincidencias `llamadas|Seguimiento|Incluye|…`

**Estado:** PASS

---

## 10. Cookies antes del consentimiento

**Estado:** NO VERIFICADO en navegador limpio (requiere inspección DevTools / Playwright).

---

## 11. JavaScript consola

**Estado:** NO VERIFICADO en navegador real. Código estático sin `console.log` de debug en landings auditadas.

---

## 12. Responsive

**Estado:** NO VERIFICADO viewport-by-viewport. CSS incluye breakpoints `@media (max-width:768px)` en landings.

---

## 13. Build / lint

No hay pipeline build para HTML estático.  
**Lint HTML:** NO VERIFICADO (sin herramienta configurada).

---

## 14. Deploy VPS

Workflow `.github/workflows/vps-deploy.yml` ampliado para incluir:
- `pl/casa-fuego/**`, `cz/casa-fuego/**`, `sk/casa-fuego/**`
- `cz/terms-conditions.html`

**Nota:** Los fixes locales requieren **commit + push a `main`** para llegar a producción.

---

## 16. Producción vs repositorio local (2026-09-08)

Comprobación en vivo de `trendtopia-store.com` **antes de deploy** de esta sesión:

| Recurso | Repo local | Producción |
|---------|------------|------------|
| PL smartwatch H1 | Polaco (`rozmowy…`) | **Español** (`llamadas…`) — pendiente deploy |
| PL casa-fuego js-v2 | 1× | **2×** — pendiente deploy |
| PL casa-fuego cookie btn | Presente | **Ausente** — pendiente deploy |
| PL casa-fuego anti-submit | Presente | **Ausente** — pendiente deploy |
| CZ terms moneda | Kč | **Euros** — pendiente deploy |

**Estado:** Fixes verificados en repo; **producción desactualizada** hasta push + workflow VPS.

**Verificación post-deploy:** Re-ejecutar `scripts/_verify_audit_fixes.py` y comparar HTML en vivo tras push.

---

## 15. Segunda pasada (verificación post-corrección)

| Control | Resultado |
|---------|-----------|
| `python scripts/_audit_7urls.py` | 0 CURSOR |
| HTTP 7 URLs × 5 | 35/35 × 200 |
| AdRice js-v2 duplicado en 7 URLs | 0 |
| PL español H1/specs | 0 matches |
| CZ terms euros | 0 matches |
| Cookie footer button HTML (casa-fuego) | Presente PL/CZ/SK |

**Estado segunda pasada CURSOR:** PASS
