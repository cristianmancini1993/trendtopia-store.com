# OWNER_EVIDENCE_REQUIRED.md

Items that **cannot** be resolved from code alone. Cursor applied conservative removals where evidence was missing; restore only when documentation exists.

Updated: 2026-09-08

---

## CoreSync (ES / PL / GR)

### Product specifications (still visible in copy — substantiation if Google asks)

| Claim | Status on landing | Evidence needed |
|-------|-------------------|-----------------|
| Battery “do 10 dni” / “hasta 10 días” | Still in hero/specs | Manufacturer battery test sheet |
| 5ATM water resistance | Still in specs | Certification / manual limits |
| 2" HD display | Still in specs | Product datasheet |
| iOS / Android compatibility | Still in copy | Minimum OS versions |
| Wellness (heart rate, sleep, steps) | Wellness wording + medical disclaimer | Confirm non-medical device classification |

### Removed conservatively — restore only with evidence

| Removed element | Was on | Restore when |
|-----------------|--------|--------------|
| Old price 98 € / 398 zł / 138 € | Hero price box | Verifiable price history |
| “-50%” / “HOY” / “DZIŚ” | Hero, topbar, meta | Dated campaign config |
| “+4100 compradores” / buyer counts | Hero, social proof | CRM or analytics export |
| “Verified buyer” badges | Reviews | Verification methodology |
| Aggregate rating in JSON-LD (if removed) | Structured data | Same as review source |

### AdRice (confirm in panel — IDs unchanged in code)

- ES: offer **3137** / lp **3171**
- PL: offer **3141** / lp **3175**
- GR: offer **1842** / lp **1862**

### Operational

- COD availability per market
- Actual shipping SLA per carrier/region (policy text updated; ops confirmation)

---

## Casa Fuego (PL / CZ / SK)

### Product (substantiation if challenged)

| Topic | Notes |
|-------|-------|
| Non-stick coating / PFOA | Material datasheet |
| Induction / oven / max temperatures | Compatibility chart |
| Handle thermal behaviour | “Zawsze chłodne” softened to descriptive copy — full claim needs test data |
| 12-piece pack contents | List vs product images |

### Removed conservatively

| Removed | Restore when |
|---------|--------------|
| Old prices (798 zł, 3 998 Kč, 178 €) | Price history |
| “-50%” / urgency | Campaign dates |
| “3200+” buyer counts | Analytics source |
| Verified review badges | Verification policy |

### AdRice

- PL: **3179** / **3213**
- CZ: **3251** / **3285**
- SK: **3702** / **3742**

---

## Home (`/`)

| Topic | Status |
|-------|--------|
| “Up to 50% off”, Zero risk, 4100/3842 counts | **REMOVED SAFELY** |
| “18 countries”, “1 hour response”, “certified suppliers” | Review `en/about-us.html` — softened; substantiate if reinstating |
| International routing | **FIXED** — ES/PL/GR picker; confirm if more locales needed |

---

## Legal / identity (not code-fixable)

- **GLOBAL INTEGRATED MARKETING COMMUNICATION GROUP HOLDINGS LIMITED** (Hong Kong) vs EU consumer jurisdiction
- GDPR international transfers (privacy policies)
- Warranty “24 months” vs statutory minimum per country

---

## SEO / Ads policy (owner decision)

- **`noindex,nofollow`** on all ad landings — intentional for paid traffic; confirm with SEO/Ads strategy before changing

---

## How to restore removed marketing

1. Provide evidence file or AdRice/campaign config in repo or shared doc
2. Request Cursor update — do not re-add without source
3. Update JSON-LD and visible DOM together
