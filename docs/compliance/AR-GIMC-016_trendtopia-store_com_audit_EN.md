AR-GIMC-016 · trendtopia-store.com · EN

FULL COMPLIANCE AUDIT
AR-GIMC-016 — trendtopia-store.com

Account
AR-GIMC-016

Customer ID
232-720-5786

Domain
trendtopia-store.com

Stated suspension reason
Account: Unacceptable business practices. Ads: Destination not working (HTTP: Unknown DNS error).

Audit date
8 October 2026 (Google Ads review session; prior pass 6 October 2026)

Verdict: ❌ NOT APPEAL READY
The destination still does not load from the owner's network (ERR_CONNECTION_TIMED_OUT). Google Ads reports Unknown DNS error on 14 disapproved final URLs. Do not submit account or URL appeals until hosting/DNS is restored and verified.

Legend: 🔴 critical / blocks appeal · 🟠 high / fix before appeal · ✅ verified clean · ❌ not appeal ready

Method and coverage
Live load from owner browser (8 Oct 2026): ERR_CONNECTION_TIMED_OUT on https://trendtopia-store.com.
Google Ads Policy Manager / destination troubleshooting: 14 disapproved final URLs, all Destination not working — Unknown DNS error (Desktop and iOS samples).
Account banner: suspended for Unacceptable business practices (egregious; separate from ad-level destination errors).
Pages audited on live site: 0 (site unreachable). Landing HTML exists in repository / GitHub Pages; custom domain does not serve it.
Domain registered 2026-05-23. DNS: Cloudflare nameservers (leo / tia). Repo deploy target: VPS 72.62.34.234 (timeout Oct 2026). Owner has no Cloudflare panel access; registrar: Cloudflare, Inc.
Last spend recorded (sheet): 2026-09-20. Ads had impressions/clicks before disapproval (site worked, then failed).

Root cause vs stated reason
Immediate technical cause: DNS/hosting — domain points to a non-responding host; Google reports Unknown DNS error / destination not working.
Account suspension: Unacceptable business practices — Policy Manager does not show a sub-reason beyond policy family (phishing, impersonation, other). No dedicated suspension email found in this session.
Relationship: Outage drives destination disapprovals; account suspension may be parallel or downstream. Cannot rule out cloaking/geo/IP filtering until the site loads. Confidence: LOW while offline.

Part 1 — Must fix

🔴 CRITICAL — Destination not reachable
ERR_CONNECTION_TIMED_OUT from owner network (8 Oct 2026).
Google Ads: 14 URLs, Unknown DNS error (list below).
Infrastructure must restore trendtopia-store.com globally and allow AdsBot-Google / AdsBot-Google-Mobile (no geo or IP blocking of crawlers).

Disapproved final URLs (8 Oct 2026):
https://trendtopia-store.com/pl/smartwatch/landing.html
https://trendtopia-store.com/cz/casa-fuego/landing.html
https://trendtopia-store.com/ (iOS)
https://trendtopia-store.com/sk/casa-fuego/landing.html
https://trendtopia-store.com/pl/vortek-1429/landing.html
https://trendtopia-store.com/es/terravolt/
https://trendtopia-store.com/es/vortek-1013/landing.html (2 ads)
https://trendtopia-store.com/ro/terravolt/
https://trendtopia-store.com/pl/terravolt/
https://trendtopia-store.com/lt/vortek-1427/landing.html
https://trendtopia-store.com/sk/smartwatch/landing.html
https://trendtopia-store.com/gr/smartwatch/landing.html
https://trendtopia-store.com/pl/casa-fuego/landing.html
https://trendtopia-store.com/es/smartwatch/landing.html

🔴 CRITICAL — Hosting / DNS ownership
Restore trendtopia-store.com (confirm with infra: 72.62.34.234 / “server 7” vs repoint DNS to GitHub Pages per repo).
Obtain Cloudflare/registrar access for Netmart LLC operations.

🔴 CRITICAL — Do not appeal yet
Repeated appeals within 7 days without fixes may be flagged unfounded.
Order: fix destination → verify HTTP 200 + AdsBot → per-URL appeals → account appeal last with evidence.

🟠 HIGH — Entity cross-check
Google Ads payments profile: Netmart LLC, County of Sussex, 16192 Coastal Hwy, Lewes, DE 19958-3608, US. Profile ID 2381-5531-0115. Email: marketing@netmart-llc.net.
Project sheet listed GIMC — reconcile with site footer and Netmart LLC once live.

Part 2 — Verified clean (do not break)
Nothing on the live domain could be verified — site did not load.
Prior repo audit (AUDIT_REPORT_GOOGLE_ADS.md, Sep 2026) reported technical fixes on seven URLs; re-run full live audit after restore before relying on it.

Part 3 — Fix priority order
Infrastructure/DNS: site online; no geo/IP blocks; allowlist AdsBot.
Verify: owner browser, external fetch, Google destination check on home + sample landing + thank-you.
Keep sheet aligned with Policy Manager.
Appeals only after errors clear; account appeal last.
Full compliance audit on live pages before scaling spend.

Cross-account notes
Confirm organization on site matches Netmart LLC payments profile.
Appeal history: older Health in personalized advertising appeals Successful (2025); not related to current suspension.

Limitations of this audit
Order forms were not submitted; submit payload not captured.
AdsBot-vs-browser user-agent comparison not run (site down).
Pre-consent network capture and countdown reload test not run.
Phone and mailbox liveness not tested.
About 50 mp4 videos not frame-checked (including "togliere-logo1…" and "recensone.mp4").
OCR/visual review from prior pass not repeated on live site (0 pages loaded).
trendtopia-store.com could not be reached; konadevices.com not re-tested this session.

Confidential — internal compliance audit
