# AR-GIMC-016 · trendtopia-store.com · EN

## FULL COMPLIANCE AUDIT

**AR-GIMC-016 — trendtopia-store.com**

| Field | Value |
| --- | --- |
| Account | AR-GIMC-016 |
| Customer ID | 232-720-5786 |
| Domain | trendtopia-store.com |
| Stated suspension reason | **Account:** Unacceptable business practices. **Ads:** Destination not working (HTTP: Unknown DNS error). |
| Audit date | 8 October 2026 (Google Ads review session) |
| Prior audit date | 6 October 2026 |

**Verdict: ❌ NOT APPEAL READY**

The destination still does not load from the owner’s network (`ERR_CONNECTION_TIMED_OUT`). Google Ads reports **Unknown DNS error** on all checked final URLs. **Do not submit account or URL appeals until hosting/DNS is restored and verified.**

**Legend:** 🔴 critical / blocks appeal · 🟠 high / fix before appeal · ✅ verified clean · ❌ not appeal ready

---

## Method and coverage

- Live load from owner browser (8 Oct 2026): **ERR_CONNECTION_TIMED_OUT** on `https://trendtopia-store.com`.
- Google Ads Policy Manager / Ads diagnostics: **14 disapproved final URLs**, all **Destination not working** — **Unknown DNS error** (Desktop and iOS samples).
- Google Ads account banner: **suspended** for **Unacceptable business practices** (egregious; separate from ad-level destination errors).
- Pages audited on live site: **0** (site unreachable). Repository and GitHub Pages deploy contain landing HTML; custom domain does not serve them.
- Domain registered: 2026-05-23 (RDAP). DNS nameservers: Cloudflare (`leo` / `tia`). Prior deploy target in repo: VPS **72.62.34.234** (connection timeout / SSH hang Oct 2026).
- Owner **does not have Cloudflare panel access**; domain registrar of record: Cloudflare, Inc.
- Last spend recorded (sheet): 2026-09-20. Ads had impressions/clicks before disapproval (site worked previously, then failed).

---

## Root cause vs stated reason

| Layer | Finding |
| --- | --- |
| **Immediate technical cause** | DNS/hosting: domain resolves to a non-responding host; Google labels this **Unknown DNS error** / destination not working. |
| **Account suspension** | **Unacceptable business practices** — Google does not expose a sub-reason in Policy Manager beyond policy family links (phishing, impersonation, other). No dedicated suspension email located in this session. |
| **Relationship** | A prolonged or total destination outage can trigger destination disapprovals first; account-level suspension may follow or run in parallel. **Cannot rule out cloaking/geo/IP filtering until the site loads** — confidence **LOW** while offline. |

---

## Part 1 — Must fix

### 🔴 CRITICAL — Destination not reachable

- Owner network: **ERR_CONNECTION_TIMED_OUT** (8 Oct 2026).
- Google Ads: **14 URLs**, all **Unknown DNS error** (see list below).
- Infrastructure team must restore `trendtopia-store.com` globally and allow **AdsBot-Google** / **AdsBot-Google-Mobile** (no geo or IP blocking of crawlers).

**Disapproved final URLs (Google Ads, 8 Oct 2026):**

1. `https://trendtopia-store.com/pl/smartwatch/landing.html`
2. `https://trendtopia-store.com/cz/casa-fuego/landing.html`
3. `https://trendtopia-store.com/` (iOS)
4. `https://trendtopia-store.com/sk/casa-fuego/landing.html`
5. `https://trendtopia-store.com/pl/vortek-1429/landing.html`
6. `https://trendtopia-store.com/es/terravolt/`
7. `https://trendtopia-store.com/es/vortek-1013/landing.html` (2 ads)
8. `https://trendtopia-store.com/ro/terravolt/`
9. `https://trendtopia-store.com/pl/terravolt/`
10. `https://trendtopia-store.com/lt/vortek-1427/landing.html`
11. `https://trendtopia-store.com/sk/smartwatch/landing.html`
12. `https://trendtopia-store.com/gr/smartwatch/landing.html`
13. `https://trendtopia-store.com/pl/casa-fuego/landing.html`
14. `https://trendtopia-store.com/es/smartwatch/landing.html`

### 🔴 CRITICAL — Hosting / DNS ownership

- Restore service on **trendtopia-store.com** (confirm with infra whether **72.62.34.234** / “server 7” is still the intended host, or repoint DNS to **GitHub Pages** per repo workflows).
- Obtain **Cloudflare** (or registrar) access for whoever operates Netmart LLC properties.

### 🔴 CRITICAL — Do not appeal yet

- Policy Manager warns: multiple appeals within 7 days without fixes may be flagged **unfounded**.
- Fix destination first → verify HTTP 200 for sample URLs and AdsBot → then URL-level appeals → only then consider **account** appeal for Unacceptable business practices with evidence.

### 🟠 HIGH — Suspension reason now recorded

- **Account:** Unacceptable business practices (Policy Manager, “Fix it” panel, 8 Oct 2026).
- **Ads:** Destination not working — Unknown DNS error.

### 🟠 HIGH — Entity cross-check

- **Google Ads payments profile:** **Netmart LLC**, County of Sussex, 16192 Coastal Hwy, Lewes, DE 19958-3608, US. Payments profile ID 2381-5531-0115. Primary contact email: marketing@netmart-llc.net.
- **Project sheet** referenced **GIMC** entity — reconcile sheet vs live footer (County of Sussex / Netmart LLC) once site loads.

---

## Part 2 — Verified clean (do not break)

Nothing on the **live domain** could be verified — site did not load.

**Repository (not verified by Google until served on domain):**

- Prior technical audit (`AUDIT_REPORT_GOOGLE_ADS.md`, Sep 2026) reported fixes on seven mandatory URLs; **re-run full live audit after restore** before relying on that status.

---

## Part 3 — Fix priority order

1. **Infrastructure / DNS:** Bring `trendtopia-store.com` online; no geo/IP blocks; allowlist AdsBot user agents.
2. **Verify:** Owner browser + external fetch + Google “Troubleshoot destination” on 2–3 sample URLs (home, one landing, one thank-you).
3. **Record:** Keep this sheet aligned with Policy Manager (reasons above).
4. **Appeals:** Per-URL destination appeals only after HTTP errors clear; account appeal last, with written explanation if outage caused the suspension.
5. **Full compliance audit** on live pages (forms, consent, entity, legal, creatives) before scaling spend.

---

## Cross-account notes

- Confirm **organization name on site** matches **Netmart LLC** payments profile.
- Appeal history (Policy Manager): older **Health in personalized advertising** appeals marked **Successful** (2025); **not** related to current suspension. Pagination UI did not expose rows 4–7 in session — optional follow-up in Admin → Policy.

---

## Limitations of this audit

- Order forms were not submitted; submit payload not captured.
- AdsBot-vs-browser user-agent comparison not run (site down).
- Pre-consent network capture and countdown reload test not run.
- Phone and mailbox liveness not tested.
- ~50 mp4 videos not frame-checked (including “togliere-logo1…” and “recensone.mp4”).
- OCR/visual image review from prior pass not repeated on live site (0 pages loaded).
- **konadevices.com** not re-tested this session.

---

*Confidential — internal compliance audit*
