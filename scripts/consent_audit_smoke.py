#!/usr/bin/env python3
"""Static + HTTP consent-mode smoke checks (no Playwright required)."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1:8080"

CHECKS: list[dict] = []


def fetch(path: str) -> str:
    with urllib.request.urlopen(BASE + path, timeout=10) as resp:
        return resp.read().decode("utf-8", errors="replace")


def add(name: str, ok: bool, detail: str) -> None:
    CHECKS.append({"check": name, "pass": ok, "detail": detail})


def main() -> None:
    # --- Static file order ---
    consent = (ROOT / "assets/js/consent-default.js").read_text(encoding="utf-8")
    add(
        "consent-default.js has denied defaults",
        all(x in consent for x in ("ad_storage: 'denied'", "analytics_storage: 'denied'")),
        "consent-default.js",
    )

    index = (ROOT / "index.html").read_text(encoding="utf-8")
    consent_pos = index.find("consent-default.js")
    gtag_async_pos = index.find("googletagmanager.com/gtag/js")
    add(
        "index.html loads consent-default before gtag async",
        consent_pos != -1 and gtag_async_pos != -1 and consent_pos < gtag_async_pos,
        "index.html head order",
    )
    add(
        "index.html has no inline gtag config",
        "gtag('config'" not in index,
        "index.html",
    )
    add(
        "index.html CoreSync copy without VitalSync",
        "VitalSync" not in index and "blood oxygen" not in index,
        "index.html featured__desc",
    )

    main_js = (ROOT / "assets/js/main.js").read_text(encoding="utf-8")
    add(
        "main.js defers gtag config until consent",
        "gtag('config', window.SITE_CONFIG.GOOGLE_TAG_ID)" in main_js and "__ttGtagConfigured" in main_js,
        "assets/js/main.js",
    )
    add(
        "main.js footer cookie change button",
        "tt-cookie-change-link" in main_js and 'type = \'button\'' in main_js.replace('"', "'") or 'type = "button"' in main_js,
        "assets/js/main.js injectFooterPreferencesLink",
    )

    geos = sorted({p.parent.name for p in ROOT.glob("*/refund-policy.html")})
    iban_bad = []
    for geo in geos:
        text = (ROOT / geo / "refund-policy.html").read_text(encoding="utf-8")
        if re.search(r"<li>[^<]*IBAN[^<]*</li>", text, re.I):
            iban_bad.append(geo)
        if re.search(r"facilitado por el cliente|provided by the customer|podany przez|poskytnuté zákazníkom|furnizat de client|navede kupec", text, re.I):
            iban_bad.append(geo + " (paragraph)")
    add(
        "refund policies do not request IBAN by email",
        len(iban_bad) == 0,
        "none" if not iban_bad else ", ".join(iban_bad),
    )

    # --- Live local server (optional) ---
    try:
        live_index = fetch("/")
        add("local server index reachable", True, BASE + "/")
        add(
            "live index includes consent-default.js",
            "consent-default.js" in live_index,
            BASE + "/",
        )
        live_es = fetch("/es/smartwatch/landing.html")
        add(
            "ES landing form POST to AdRice",
            'method="post"' in live_es and "offers.adricenetwork.com/forms/html/" in live_es,
            BASE + "/es/smartwatch/landing.html",
        )
        add(
            "ES landing has privacy notice near form",
            "cf-form-privacy" in live_es,
            BASE + "/es/smartwatch/landing.html",
        )
    except Exception as exc:
        add("local server reachable", False, str(exc))

    out = ROOT / "scripts" / "consent_audit_results.json"
    out.write_text(json.dumps(CHECKS, indent=2), encoding="utf-8")
    passed = sum(1 for c in CHECKS if c["pass"])
    print(json.dumps({"passed": passed, "total": len(CHECKS), "results": CHECKS}, indent=2))


if __name__ == "__main__":
    main()
