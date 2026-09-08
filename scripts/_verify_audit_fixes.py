#!/usr/bin/env python3
"""Verify all CURSOR fixes from Google Ads audit."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks: list[tuple[str, bool]] = []


def ok(name: str, cond: bool) -> None:
    checks.append((name, cond))


# PL smartwatch
pl = (ROOT / "pl/smartwatch/landing.html").read_text(encoding="utf-8")
h1 = pl.split("<h1>")[1].split("</h1>")[0] if "<h1>" in pl else ""
ok("PL H1 polaco", "rozmowy" in h1 and "llamadas" not in h1)
ok("PL specs sin Seguimiento/Incluye", "Seguimiento" not in pl and "Incluye:" not in pl)
ok("PL sw js-v2=1", pl.count("forms/html/js-v2/") == 1)
ok("PL sw anti-submit", "form.dataset.submitting" in pl)
ok("PL sw medical disclaimer", "nie jest wyrobem medycznym" in pl)
ok("PL sw package shipping aligned", "roboczych po potwierdzeniu telefonicznym" in pl and pl.count("roboczych po potwierdzeniu telefonicznym") >= 2)

for geo in ("pl", "cz", "sk"):
    t = (ROOT / f"{geo}/casa-fuego/landing.html").read_text(encoding="utf-8")
    ok(f"{geo} cf js-v2=1", t.count("forms/html/js-v2/") == 1)
    ok(f"{geo} cf cookie btn", "site-footer__link-btn tt-cookie-change-link" in t)
    ok(f"{geo} cf anti-submit", "form.dataset.submitting" in t)
    ok(f"{geo} cf Object.assign", "Object.assign(window.SITE_CONFIG" in t)
    ok(f"{geo} cf consent-default", "consent-default.js" in t)
    pos_c, pos_g = t.find("consent-default.js"), t.find("googletagmanager.com/gtag/js")
    ok(f"{geo} cf consent before gtag", pos_c != -1 and (pos_g == -1 or pos_c < pos_g))

czt = (ROOT / "cz/terms-conditions.html").read_text(encoding="utf-8")
ok("CZ terms korun", "korun" in czt.lower() and "eurech" not in czt.lower())

plt = (ROOT / "pl/terms-conditions.html").read_text(encoding="utf-8")
ok("PL terms PLN", "PLN" in plt and "złotych polskich" in plt.lower())

ty = (ROOT / "cz/casa-fuego/thank-you.html").read_text(encoding="utf-8")
ok("CZ TY currency CZK", "'currency': 'CZK'" in ty)

plty = (ROOT / "pl/casa-fuego/thank-you.html").read_text(encoding="utf-8")
ok("PL CF TY currency PLN", "'currency': 'PLN'" in plty)

for geo, offer, lp in (
    ("es", "3137", "3171"),
    ("pl", "3141", "3175"),
    ("gr", "1842", "1862"),
):
    t = (ROOT / f"{geo}/smartwatch/landing.html").read_text(encoding="utf-8")
    ok(f"{geo} offer/lp", f'value="{offer}"' in t and f'value="{lp}"' in t)

for geo, offer, lp in (
    ("pl", "3179", "3213"),
    ("cz", "3251", "3285"),
    ("sk", "3702", "3742"),
):
    t = (ROOT / f"{geo}/casa-fuego/landing.html").read_text(encoding="utf-8")
    ok(f"{geo} cf offer/lp", f'value="{offer}"' in t and f'value="{lp}"' in t)

for r in (
    "AUDIT_REPORT_GOOGLE_ADS.md",
    "OWNER_EVIDENCE_REQUIRED.md",
    "TECHNICAL_TEST_RESULTS.md",
    "GOOGLE_ADS_READY_STATUS.md",
    "LEGAL_REVIEW_REQUIRED.md",
):
    ok(f"report {r}", (ROOT / r).is_file())

wf = (ROOT / ".github/workflows/vps-deploy.yml").read_text(encoding="utf-8")
ok("deploy full site", "deploy-full-site" in wf or "pl/casa-fuego/**" in wf)

failed = [n for n, v in checks if not v]
for n, v in checks:
    print(("PASS" if v else "FAIL"), n)
print("---")
print(f"{len(checks) - len(failed)}/{len(checks)} PASS")
if failed:
    raise SystemExit(1)
