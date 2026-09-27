"""Extract ArcForce template from gadgethive dump and build ro/arcforce landing."""
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "_tmp_arcforce.html"
OUT_DIR = ROOT / "ro" / "arcforce"
IMG_DIR = ROOT / "assets" / "img" / "products" / "arcforce"

raw = SRC.read_text(encoding="utf-8")
start = raw.find("<!DOCTYPE html>\n<html lang=\"ro\">")
end = raw.find("</html>", start)
if start < 0 or end < 0:
    raise SystemExit("inner template not found")
inner = raw[start : end + len("</html>")]

replacements = {
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-hero.webp": "/assets/img/products/arcforce/hero.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-desc-1.webp": "/assets/img/products/arcforce/use-1.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-desc-2.webp": "/assets/img/products/arcforce/use-2.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-desc-3.webp": "/assets/img/products/arcforce/use-3.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-review-1.webp": "/assets/img/products/arcforce/review-1.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-review-2.webp": "/assets/img/products/arcforce/review-2.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-review-3.webp": "/assets/img/products/arcforce/review-3.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-1.webp": "/assets/img/products/arcforce/reviewer-1.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-2.webp": "/assets/img/products/arcforce/reviewer-2.webp?v=1",
    "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-3.webp": "/assets/img/products/arcforce/reviewer-3.webp?v=1",
}
for old, new in replacements.items():
    inner = inner.replace(old, new)

inner = inner.replace(
    '<input name="uid" type="hidden" value="019c7158-9ae4-737e-8d04-502baa35da6c" />',
    '<input name="uid" type="hidden" value="019e5f4e-b178-7d63-91e1-6fda72088957" />',
)
inner = re.sub(
    r'<input name="offer" type="hidden" value="[^"]*" />',
    '<input name="offer" type="hidden" value="PENDING" />',
    inner,
)
inner = re.sub(
    r'<input name="lp" type="hidden" value="[^"]*" />',
    '<input name="lp" type="hidden" value="PENDING" />',
    inner,
)
inner = inner.replace(
    '<input name="thankyoupage" type="hidden" value="https://gadgetvistapro.com/saldatrice-portatile-romania-thank-you-page/"/>',
    '<input name="thankyoupage" type="hidden" value="https://trendtopia-store.com/ro/arcforce/thank-you.html" />',
)
inner = inner.replace(
    '<input name="webhook" type="hidden" value="https://hook.eu2.make.com/rk3me12plkw5ubpcoxb9nrx4utnc862q"/>',
    '<input name="webhook" type="hidden" value="https://hook.eu2.make.com/bkg6tbg3vdknomqb2n4kdat1fe1tp271" />',
)
inner = re.sub(
    r'<input name="_key" type="hidden" value="[^"]*" />',
    '<input name="_key" type="hidden" value="PENDING" />',
    inner,
)

head_inject = """<!-- Google tag (gtag.js) -->
<script src="/assets/js/consent-default.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18327321473"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  window.SITE_CONFIG = window.SITE_CONFIG || {};
  window.SITE_CONFIG.GOOGLE_TAG_ID = window.SITE_CONFIG.GOOGLE_TAG_ID || 'AW-18327321473';
</script>
<meta name="robots" content="noindex, nofollow">
<meta name="contact" content="info@trendtopia-store.com">
<link rel="canonical" href="https://trendtopia-store.com/ro/arcforce/landing.html">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<script>
window.SITE_CONFIG = Object.assign(window.SITE_CONFIG || {}, {
  GEO: 'ro',
  PRODUCT_SLUG: 'arcforce',
  CURRENCY: 'RON',
  PRICE: 597,
  OFFER_NAME: 'ArcForce RO',
  LP_ID: 'ro-arcforce',
  OFFER_ID: '',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: 'Se trimite...',
  COOKIE_TEXT: 'Folosim cookie-uri tehnice și de terți pentru a îmbunătăți experiența ta și pentru analiză.',
  COOKIE_ACCEPT: 'Acceptă',
  COOKIE_LEARN: 'Află mai multe'
});
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/form-handler.js" defer></script>
"""

inner = inner.replace("<head>\n", "<head>\n" + head_inject, 1)

footer = """
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="trendtopia-store.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">trendtopia-store</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb" style="margin-top:10px;font-size:13px;color:#6b7280">Produse utile pentru viața de zi cu zi, livrare în 24-48 de ore cu ramburs la livrare.</p>
      </div>
      <div>
        <h4 class="site-footer__heading">Informaţii</h4>
        <ul class="site-footer__list">
          <li><a href="/ro/about-us.html">Despre noi</a></li>
          <li><a href="/ro/contact-us.html">Contactaţi-ne</a></li>
          <li><a href="/ro/privacy-policy.html">Politica de confidențialitate</a></li>
          <li><a href="/ro/terms-conditions.html">Termeni și condiții</a></li>
          <li><a href="/ro/cookie-policy.html">Politica cookie</a></li>
          <li><a href="/ro/shipping-policy.html">Politica de livrare</a></li>
          <li><a href="/ro/refund-policy.html">Politica de rambursare</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">Contact</h4>
        <ul class="site-footer__list">
          <li><strong>County of Sussex</strong></li>
          <li>16192 Coastal Hwy</li>
          <li>Lewes, DE 19958-3608</li>
          <li>United States</li>
          <li><a href="mailto:info@trendtopia-store.com">info@trendtopia-store.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>County of Sussex</strong> — Toate drepturile rezervate.
      <a href="/">trendtopia-store.com</a>
    </div>
  </div>
</footer>
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
"""

inner = inner.replace("\n<script>\n  // Countdown timer", footer + "\n<script>\n  // Countdown timer", 1)

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "landing.html").write_text(inner, encoding="utf-8")

# index redirect
(OUT_DIR / "index.html").write_text(
    """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {
  var path = '/ro/arcforce/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
})();
</script>
<meta http-equiv="refresh" content="0;url=/ro/arcforce/landing.html">
<link rel="canonical" href="https://trendtopia-store.com/ro/arcforce/landing.html">
</head>
<body>
<p><a href="/ro/arcforce/landing.html">ArcForce™</a></p>
</body>
</html>
""",
    encoding="utf-8",
)

# thank-you from kemppi
ty_src = ROOT / "ro" / "kemppi-167" / "thank-you.html"
ty = ty_src.read_text(encoding="utf-8")
ty = ty.replace("Kemppi™", "ArcForce™").replace("kemppi-167", "arcforce").replace("549.0", "597.0")
ty = re.sub(r"<!-- Event snippet for Purchase.*?</script>\s*", "", ty, flags=re.S)
(OUT_DIR / "thank-you.html").write_text(ty, encoding="utf-8")

# download images
IMG_DIR.mkdir(parents=True, exist_ok=True)
url_map = {
    "hero.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-hero.webp",
    "use-1.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-desc-1.webp",
    "use-2.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-desc-2.webp",
    "use-3.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-desc-3.webp",
    "review-1.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-review-1.webp",
    "review-2.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-review-2.webp",
    "review-3.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/saldatrice-review-3.webp",
    "reviewer-1.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-1.webp",
    "reviewer-2.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-2.webp",
    "reviewer-3.webp": "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-3.webp",
}
for name, url in url_map.items():
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=60).read()
    (IMG_DIR / name).write_bytes(data)
    print("saved", name, len(data))

print("wrote", OUT_DIR / "landing.html", "bytes", (OUT_DIR / "landing.html").stat().st_size)
