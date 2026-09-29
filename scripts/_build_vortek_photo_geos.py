# -*- coding: utf-8 -*-
"""Build Vortek landings for HU / HR / RO / PT from the existing CRO renderer."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "scripts" / "_vortek_cro.css").read_text(encoding="utf-8")
COMPANY = "County of Sussex"
ADDR = "16192 Coastal Hwy, Lewes, DE 19958-3608, United States"
UID = "019e5f4e-b178-7d63-91e1-6fda72088957"
WEBHOOK_DEFAULT = "https://hook.eu2.make.com/otlkouarqencnd3tdlobo9xhdex1wcei"


def faq_html(items):
    parts = []
    for q, a in items:
        parts.append(f" <details><summary>{q}</summary><p>{a}</p></details>")
    return "\n".join(parts)


def render(L):
    thankyou = f"https://trendtopia-store.com/{L['geo']}/{L['slug']}/thank-you.html"
    canonical = f"https://trendtopia-store.com/{L['geo']}/{L['slug']}/landing.html"
    tmfp_js = ""
    if L["tmfp"]:
        tmfp_js = '<script src="https://offers.adricenetwork.com/forms/tmfp/" crossorigin="anonymous" defer></script>\n'
    subid_js = ""
    extra = L["form_extra"]
    if extra:
        extra = " " + extra + "\n"
    return f"""<!DOCTYPE html>
<html lang="{L['lang']}">
<head>
<!-- Google tag (gtag.js) -->
<script src="/assets/js/consent-default.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18327321473"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){{dataLayer.push(arguments);}}
 gtag('js', new Date());
 window.SITE_CONFIG = window.SITE_CONFIG || {{}};
 window.SITE_CONFIG.GOOGLE_TAG_ID = window.SITE_CONFIG.GOOGLE_TAG_ID || 'AW-18327321473';
</script>
<meta charset="utf-8">
<meta name="robots" content="noindex, nofollow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#111715">
<meta name="description" content="{L['desc']}">
<meta name="contact" content="info@trendtopia-store.com">
<title>{L['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800;900&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="{L['lang']}" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<script>
window.SITE_CONFIG = {{
 GEO: '{L['geo']}',
 LOCALE: '{L['locale']}',
 PRODUCT_SLUG: '{L['slug']}',
 CURRENCY: '{L['currency']}',
 PRICE: {L['price_num']:.2f},
 OFFER_ID: '{L['offer_id']}',
 OFFER_NAME: '{L['offer_name']}',
 LP_ID: '{L['lp_id']}',
 FORM_ENDPOINT: 'https://offers.adricenetwork.com/forms/html/',
 SUBMITTING_LABEL: '{L['submitting']}',
 COOKIE_TEXT: {L['cookie_text']!r},
 COOKIE_ACCEPT: {L['cookie_accept']!r},
 COOKIE_LEARN: {L['cookie_learn']!r},
 GOOGLE_TAG_ID: 'AW-18327321473',
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
<style>
{CSS}
</style>
</head>
<body>
 <div class="announcement">{L['announce']}</div>

 <header class="hero" id="inicio">
 <div class="wrap topbar">
 <a class="logo" href="#inicio">{L.get("logo_html", "VOR<span>TEK</span>")}</a>
 <div class="top-proof"><span><i></i>{L['ship']}</span><span>{L['cod']}</span></div>
 </div>

 <div class="wrap hero-grid">
 <div class="hero-copy">
 <div class="rating"><span class="stars">★★★★★</span><strong>4,6/5</strong><span>{L['rating']}</span></div>
 <p class="eyebrow">{L['eyebrow']}</p>
 <h1>{L['h1']}</h1>
 <p class="lead">{L['lead']}</p>
 <ul class="hero-points">
 <li><span>{L['p1']}</span></li>
 <li><span>{L['p2']}</span></li>
 <li><span>{L['p3']}</span></li>
 <li><span>{L['p4']}</span></li>
 <li><span>{L['p5']}</span></li>
 </ul>
 <div class="product-shot">
 <img src="/assets/img/products/vortek/hero.webp?v=6" alt="{L['hero_alt']}" width="1200" height="1200">
 <div class="discount-badge">−50%<small>{L['badge_small']}</small></div>
 <div class="pack-label">{L['pack_label']}<small>{L['pack_small']}</small></div>
 </div>
 </div>

 <aside class="order-card" id="pedido">
 <span class="eyebrow">{L['form_eye']}</span>
 <h2>{L['form_h2']}</h2>
 <p>{L['form_p']}</p>
 <div class="price-row"><span class="old-price">{L['old']}</span><span class="price">{L['price']}</span><span class="save">{L['save']}</span></div>
 <div class="step-top"><span id="stepLabel">{L['step1']}</span><span>{L['secure']}</span></div>
 <div class="progress"><span id="progressBar"></span></div>
 <form class="vk-form vk-order-form tm-order-form order-form" id="orderForm" action="https://offers.adricenetwork.com/forms/html/" method="post" novalidate>
 <div class="error" id="formError" role="alert">{L['err']}</div>
 <div class="form-step" id="step1">
 <div class="field"><label for="name">{L['lbl_name']}</label><input id="name" name="name" autocomplete="name" placeholder="{L['ph_name']}" required></div>
 <div class="field"><label for="tel">{L['lbl_tel']}</label><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="{L['ph_tel']}" required></div>
 <button class="btn" id="nextStep" type="button">{L['next']}</button>
 <p class="microcopy">{L['micro1']}</p>
 </div>

 <div class="form-step" id="step2" hidden>
 <div class="field"><label for="address">{L['lbl_addr']}</label><input id="address" name="street-address" autocomplete="street-address" placeholder="{L['ph_addr']}" required></div>
 <div class="fields-2"><div class="field"><label for="postal">{L['lbl_postal']}</label><input id="postal" name="postal"{L.get('postal_type_attr', '')} inputmode="{L.get('postal_inputmode', 'numeric')}" autocomplete="postal-code" placeholder="{L['ph_postal']}"{L['postal_pattern']} required></div><div class="field"><label for="city">{L['lbl_city']}</label><input id="city" name="address-level2" autocomplete="address-level2" placeholder="{L['ph_city']}" required></div></div>
 <div class="field"><label for="province">{L['lbl_prov']}</label><input id="province" name="province" autocomplete="address-level1" placeholder="{L['ph_prov']}" required></div>
 <button class="btn" name="submit" type="submit">{L['submit']}</button>
 <button class="back" id="backStep" type="button">{L['back']}</button>
 <p class="microcopy">{L['micro2']}</p>
 </div>
{extra} <input name="uid" type="hidden" value="{UID}">
 <input name="offer" type="hidden" value="{L['offer_id']}">
 <input name="lp" type="hidden" value="{L['lp']}">
 <input name="thankyoupage" type="hidden" value="{thankyou}">
 <input name="webhook" type="hidden" value="{L['webhook']}">
 <input name="_key" type="hidden" value="{L['key']}">
 <input type="hidden" name="product" value="{L.get("product_value", "Vortek")}">
 </form>
 </aside>
 </div>
 </header>

 <div class="trust-strip" aria-label="{L['cod']}">
 <div class="wrap trust-grid">
 <div class="trust-item"><span class="trust-icon">50%</span><span><b>{L['t1b']}</b><small>{L['t1s']}</small></span></div>
 <div class="trust-item"><span class="trust-icon">{L.get('trust_pay_icon', '€')}</span><span><b>{L['t2b']}</b><small>{L['t2s']}</small></span></div>
 <div class="trust-item"><span class="trust-icon">↗</span><span><b>{L['t3b']}</b><small>{L['t3s']}</small></span></div>
 <div class="trust-item"><span class="trust-icon">↩</span><span><b>{L['t4b']}</b><small>{L['t4s']}</small></span></div>
 </div>
 </div>

 <main>
 <section>
 <div class="wrap problem-grid">
 <div>
 <p class="eyebrow">{L['prob_eye']}</p>
 <h2>{L['prob_h2']}</h2>
 <p class="section-copy">{L['prob_p']}</p>
 </div>
 <div class="problem-card">
 <div class="problem-item"><b>{L['m1b']}</b><span>{L['m1s']}</span></div>
 <div class="problem-item"><b>{L['m2b']}</b><span>{L['m2s']}</span></div>
 <div class="problem-item"><b>{L['m3b']}</b><span>{L['m3s']}</span></div>
 </div>
 </div>
 </section>

 <section class="features">
 <div class="wrap">
 <p class="eyebrow">{L['feat_eye']}</p>
 <h2>{L['feat_h2']}</h2>
 <p class="section-copy">{L['feat_p']}</p>

 <article class="feature-row"><div class="feature-media"><img src="/assets/img/products/vortek/feature-battery-swap.webp?v=6" alt="{L['f1alt']}" width="1200" height="1200"></div><div class="feature-body"><span class="feature-no">01</span><h3>{L['f1t']}</h3><p>{L['f1p']}</p><div class="chips"><span class="chip">{L['f1c1']}</span><span class="chip">{L['f1c2']}</span><span class="chip">{L['f1c3']}</span></div></div></article>
 <article class="feature-row"><div class="feature-media"><img src="/assets/img/products/vortek/feature-one-handed.webp?v=7" alt="{L['f2alt']}" width="1200" height="1200"></div><div class="feature-body"><span class="feature-no">02</span><h3>{L['f2t']}</h3><p>{L['f2p']}</p><div class="chips"><span class="chip">{L['f2c1']}</span><span class="chip">{L['f2c2']}</span><span class="chip">{L['f2c3']}</span></div></div></article>
 <article class="feature-row"><div class="feature-media"><img src="/assets/img/products/vortek/feature-spare-chain.webp?v=4" alt="{L['f3alt']}" width="1200" height="1200"></div><div class="feature-body"><span class="feature-no">03</span><h3>{L['f3t']}</h3><p>{L['f3p']}</p><div class="chips"><span class="chip">{L['f3c1']}</span><span class="chip">{L['f3c2']}</span><span class="chip">{L['f3c3']}</span></div></div></article>
 </div>
 </section>

 <section>
 <div class="wrap">
 <p class="eyebrow">{L['cmp_eye']}</p>
 <h2>{L['cmp_h2']}</h2>
 <p class="section-copy">{L['cmp_p']}</p>
 <div class="comparison" role="table" aria-label="{L['cmp_h2']}">
 <div class="compare-row compare-head"><div>{L['cmp_h']}</div><div>{L['cmp_a']}</div><div>{L['cmp_b']}</div></div>
 <div class="compare-row"><div>{L['c1']}</div><div class="yes">{L['c1a']}</div><div class="maybe">{L['c1b']}</div></div>
 <div class="compare-row"><div>{L['c2']}</div><div class="yes">{L['c2a']}</div><div>{L['c2b']}</div></div>
 <div class="compare-row"><div>{L['c3']}</div><div class="yes">{L['c3a']}</div><div>{L['c3b']}</div></div>
 <div class="compare-row"><div>{L['c4']}</div><div class="yes">{L['c4a']}</div><div>{L['c4b']}</div></div>
 <div class="compare-row"><div>{L['c5']}</div><div class="yes">{L['c5a']}</div><div>{L['c5b']}</div></div>
 </div>
 </div>
 </section>

 <section class="pack">
 <div class="wrap pack-grid">
 <div class="pack-image"><img src="/assets/img/products/vortek/hero.webp?v=6" alt="{L['pack_alt']}" width="1200" height="1200"></div>
 <div><p class="eyebrow">{L['pack_eye']}</p><h2>{L['pack_h2']}</h2><ul class="pack-list"><li>{L['li1']}</li><li>{L['li2']}</li><li>{L['li3']}</li><li>{L['li4']}</li><li>{L['li5']}</li><li>{L['li6']}</li></ul><div class="safety">{L['safety']}</div></div>
 </div>
 </section>

 <section class="reviews">
 <div class="wrap">
 <div class="review-head"><div><p class="eyebrow">{L['rev_eye']}</p><h2>{L['rev_h2']}</h2></div><div class="review-note">{L['rev_note']}</div></div>
 <div class="review-grid">
 <article class="review">
 <img class="review-photo" src="/assets/img/products/vortek/review-unbox-kit.webp?v=1" alt="{L['ph1']}" width="1024" height="768" loading="lazy">
 <div class="review-body">
 <div class="stars">★★★★★</div>
 <blockquote>{L['q1']}</blockquote>
 <div class="review-user"><img src="/assets/img/products/vortek/review-avatar-l.webp" alt="" width="92" height="92"><span><b>{L['r1n']}</b><small>{L['r1c']}</small></span></div>
 </div>
 </article>
 <article class="review">
 <img class="review-photo" src="/assets/img/products/vortek/review-unbox-box.webp?v=3" alt="{L['ph2']}" width="1024" height="768" loading="lazy">
 <div class="review-body">
 <div class="stars">★★★★★</div>
 <blockquote>{L['q2']}</blockquote>
 <div class="review-user"><img src="/assets/img/products/vortek/review-avatar-a.webp" alt="" width="92" height="92"><span><b>{L['r2n']}</b><small>{L['r2c']}</small></span></div>
 </div>
 </article>
 <article class="review">
 <img class="review-photo" src="/assets/img/products/vortek/review-unbox-hands.webp?v=2" alt="{L['ph3']}" width="1024" height="768" loading="lazy">
 <div class="review-body">
 <div class="stars">★★★★☆</div>
 <blockquote>{L['q3']}</blockquote>
 <div class="review-user"><img src="/assets/img/products/vortek/review-avatar-m.webp" alt="" width="92" height="92"><span><b>{L['r3n']}</b><small>{L['r3c']}</small></span></div>
 </div>
 </article>
 </div>
 </div>
 </section>

 <section>
 <div class="wrap faq-grid">
 <div><p class="eyebrow">{L['faq_eye']}</p><h2>{L['faq_h2']}</h2><p class="section-copy">{L['faq_p']}</p></div>
 <div class="faq-list">
{faq_html(L['faq'])}
 </div>
 </div>
 </section>

 <section class="final-cta">
 <div class="wrap cta-box"><div><h2>{L['cta_h2']}</h2><p>{L['cta_p']}</p></div><a class="btn" href="#pedido">{L['cta_btn']}</a></div>
 </section>
 </main>

 <footer>
 <div class="wrap">
 <div class="footer-grid">
 <div><a class="logo footer-brand" href="/" aria-label="trendtopia-store.com"><img src="/assets/img/site/logo-transparent.png" alt="" width="72" height="72"><span class="footer-brand__name">trendtopia-store<span>.com</span></span></a><p>{L['foot_p']}</p><p>{COMPANY}<br>{ADDR}<br><a href="mailto:info@trendtopia-store.com">info@trendtopia-store.com</a></p></div>
 <div><h3>{L['help']}</h3><a href="#pedido">{L['a_order']}</a><a href="{L['href_ship']}">{L['a_ship']}</a><a href="{L['href_contact']}">{L['a_contact']}</a></div>
 <div><h3>{L['legal']}</h3><a href="{L['href_priv']}">{L['a_priv']}</a><a href="{L['href_cook']}">{L['a_cook']}</a><a href="{L['href_terms']}">{L['a_terms']}</a><a href="{L['href_about']}">{L['a_about']}</a><button type="button" class="tt-cookie-change-link">{L['cookie_btn']}</button></div>
 </div>
 <p style="margin:25px 0 0">© <span id="year"></span> {COMPANY} — {L['rights']}</p>
 </div>
 </footer>

 <div class="sticky"><a class="btn" href="#pedido">{L['sticky']}</a></div>

<script>
(function () {{
 document.getElementById('year').textContent = new Date().getFullYear();
 var form = document.getElementById('orderForm');
 var step1 = document.getElementById('step1');
 var step2 = document.getElementById('step2');
 var progressBar = document.getElementById('progressBar');
 var stepLabel = document.getElementById('stepLabel');
 var error = document.getElementById('formError');
 var MSGS = {{
 name: {L['msg_name']!r},
 address: {L['msg_addr']!r},
 tel: {L['msg_tel']!r},
 postal: {L.get('msg_postal', '')!r},
 city: {L.get('msg_city', '')!r},
 province: {L.get('msg_province', '')!r},
 generic: {L['msg_generic']!r},
 submitting: {L['submitting']!r}
 }};
 var FIELD_SELECTOR = 'input[name="name"], input[name="tel"], input[name="street-address"], input[name="postal"], input[name="address-level2"], input[name="province"]';
{L['phone_js']}
 function errId(input) {{ return input.id + '-error'; }}
 function validateInput(input) {{
 var val = input.value.trim();
 if (input.name === 'postal') {{
 input.value = val;
 }}
 var msg = '';
 if (input.name === 'name') {{
 if (!val || val.length < 3 || val.length > 80 || /\\d/.test(val)) msg = MSGS.name;
 }} else if (input.name === 'street-address') {{
 if (!val || val.length < 5) msg = MSGS.address;
 }} else if (input.name === 'tel') {{
 if (!isValidLocalPhone(val)) msg = MSGS.tel;
 }} else if (input.name === 'postal' && MSGS.postal) {{
 if (!/^[0-9]{{2}}-[0-9]{{3}}$/.test(val)) msg = MSGS.postal;
 }} else if (input.name === 'address-level2' && MSGS.city) {{
 if (!val || val.length < 2) msg = MSGS.city;
 }} else if (input.name === 'province' && MSGS.province) {{
 if (!val || val.length < 2) msg = MSGS.province;
 }}
 var err = document.getElementById(errId(input));
 if (msg) {{
 input.setCustomValidity(msg);
 if (err) {{ err.textContent = msg; err.hidden = false; err.setAttribute('role', 'alert'); }}
 input.classList.add('is-invalid');
 input.setAttribute('aria-invalid', 'true');
 }} else {{
 input.setCustomValidity('');
 if (err) {{ err.textContent = ''; err.hidden = true; err.removeAttribute('role'); }}
 input.classList.remove('is-invalid');
 input.removeAttribute('aria-invalid');
 }}
 return !msg;
 }}
 form.querySelectorAll(FIELD_SELECTOR).forEach(function (input) {{
 var err = document.createElement('span');
 err.id = errId(input);
 err.className = 'vk-field-error';
 err.hidden = true;
 input.insertAdjacentElement('afterend', err);
 input.setAttribute('aria-describedby', err.id);
 input.addEventListener('input', function () {{ if (input.classList.contains('is-invalid')) validateInput(input); }});
 input.addEventListener('blur', function () {{ validateInput(input); }});
 }});
 document.getElementById('nextStep').addEventListener('click', function () {{
 var fields = [document.getElementById('name'), document.getElementById('tel')];
 var ok = fields.every(function (field) {{ return validateInput(field) && field.reportValidity(); }});
 if (!ok) {{ error.style.display = 'block'; return; }}
 error.style.display = 'none';
 step1.hidden = true;
 step2.hidden = false;
 progressBar.style.width = '100%';
 stepLabel.textContent = {L['step2']!r};
 document.getElementById('address').focus();
 }});
 document.getElementById('backStep').addEventListener('click', function () {{
 step2.hidden = true;
 step1.hidden = false;
 progressBar.style.width = '50%';
 stepLabel.textContent = {L['step1']!r};
 document.getElementById('tel').focus();
 }});
 form.addEventListener('submit', function (e) {{
 if (form.dataset.submitting === 'true') {{ e.preventDefault(); e.stopImmediatePropagation(); return; }}
 var valid = true, firstInvalid = null;
 form.querySelectorAll(FIELD_SELECTOR).forEach(function (input) {{
 if (!validateInput(input)) {{ valid = false; if (!firstInvalid) firstInvalid = input; }}
 }});
 if (!form.reportValidity() || !valid) {{
 e.preventDefault(); e.stopImmediatePropagation();
 error.style.display = 'block';
 error.textContent = MSGS.generic;
 if (firstInvalid) firstInvalid.focus();
 return;
 }}
 form.dataset.submitting = 'true';
 var btn = form.querySelector('button[type="submit"]');
 if (btn) {{ btn.disabled = true; btn.textContent = MSGS.submitting; }}
 }}, true);
 document.querySelectorAll('.tt-cookie-change-link').forEach(function (btn) {{
 btn.addEventListener('click', function () {{
 if (typeof window.ttOpenCookiePreferences === 'function') window.ttOpenCookiePreferences();
 }});
 }});{subid_js}
}})();
</script>
{tmfp_js}<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
</body>
</html>
"""

PHONE_HU = r"""
 function isValidLocalPhone(val) {
 if (!val || !/\d/.test(val)) return false;
 if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
 var compact = val.replace(/[\s\-().]/g, '');
 if (compact.indexOf('+36') === 0) compact = compact.slice(3);
 else if (compact.indexOf('0036') === 0) compact = compact.slice(4);
 if (compact.indexOf('06') === 0) compact = compact.slice(2);
 var digits = compact.replace(/\D/g, '');
 if (!/^[1-9]\d{7,8}$/.test(digits)) return false;
 if (/^(\d)\1+$/.test(digits)) return false;
 return true;
 }"""

PHONE_HR = r"""
 function isValidLocalPhone(val) {
 if (!val || !/\d/.test(val)) return false;
 if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
 var compact = val.replace(/[\s\-().]/g, '');
 if (compact.indexOf('+385') === 0) compact = compact.slice(4);
 else if (compact.indexOf('00385') === 0) compact = compact.slice(5);
 var digits = compact.replace(/\D/g, '');
 if (digits.charAt(0) === '0') digits = digits.slice(1);
 if (!/^[1-9]\d{7,8}$/.test(digits)) return false;
 if (/^(\d)\1+$/.test(digits)) return false;
 return true;
 }"""

PHONE_RO = r"""
 function isValidLocalPhone(val) {
 if (!val || !/\d/.test(val)) return false;
 if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
 var compact = val.replace(/[\s\-().]/g, '');
 if (compact.indexOf('+40') === 0) compact = compact.slice(3);
 else if (compact.indexOf('0040') === 0) compact = compact.slice(4);
 var digits = compact.replace(/\D/g, '');
 if (digits.charAt(0) === '0') digits = digits.slice(1);
 if (!/^7\d{8}$/.test(digits)) return false;
 if (/^(\d)\1+$/.test(digits)) return false;
 return true;
 }"""

PHONE_PT = r"""
 function isValidLocalPhone(val) {
 if (!val || !/\d/.test(val)) return false;
 if (!/^\+?[0-9\s().-]+$/.test(val)) return false;
 var compact = val.replace(/[\s\-().]/g, '');
 if (compact.indexOf('+351') === 0) compact = compact.slice(4);
 else if (compact.indexOf('00351') === 0) compact = compact.slice(5);
 var digits = compact.replace(/\D/g, '');
 if (!/^[29]\d{8}$/.test(digits)) return false;
 if (/^(\d)\1+$/.test(digits)) return false;
 return true;
 }"""

LOCALES = {
    "hu": {
        "lang": "hu",
        "locale": "hu-HU",
        "geo": "hu",
        "slug": "vortek-3232",
        "currency": "HUF",
        "price_num": 29999.00,
        "offer_id": "3232",
        "lp": "",
        "key": "",
        "offer_name": "Vortek HU 3232",
        "lp_id": "hu-vortek-3232",
        "logo_html": "VOR<span>TEK</span>",
        "product_value": "Vortek",
        "webhook": WEBHOOK_DEFAULT,
        "price": "29.999 Ft",
        "old": "59.998 Ft",
        "save": "29.999 Ft MEGTAKARÍTÁS",
        "trust_pay_icon": "Ft",
        "submitting": "Küldés…",
        "cookie_text": "Technikai és harmadik felek cookie-jait használjuk a felhasználói élmény javítására és elemzésre.",
        "cookie_accept": "Elfogadom",
        "cookie_learn": "Tudjon meg többet",
        "title": "Vortek™ — Teljes készlet 50% kedvezménnyel",
        "desc": "Vortek: akkumulátoros láncfűrész kefe nélküli motorral, két akkumulátorral és teljes készlettel. 50% kedvezmény és utánvétes fizetés.",
        "announce": "<strong>50% KEDVEZMÉNY</strong> · 59.998 Ft → 29.999 Ft · UTÁNVÉTES FIZETÉS",
        "ship": "Szállítás 24–48 óra*",
        "cod": "Utánvét",
        "rating": "Vásárlói értékelés*",
        "eyebrow": "Professzionális akkumulátoros láncfűrész",
        "h1": "FEJEZZE BE A MUNKÁT. <em>NE AZ AKKUMULÁTORT.</em>",
        "lead": "1500 W-os kefe nélküli motor, két akkumulátor és teljes készlet fatörzsek és ágak vágásához kábel és benzin nélkül.",
        "p1": "<strong>Akár 8 óra együttesen*</strong> a két mellékelt akkumulátorral.",
        "p2": "<strong>Akár 40 cm deklarált vágókapacitás*</strong> a fa típusától és a használattól függően.",
        "p3": "<strong>Mindössze 2,4 kg*</strong> vezetőlemezzel és akkumulátorral.",
        "p4": "<strong>Automatikus kenés és feszítés*</strong> a kevesebb megszakításért.",
        "p5": "<strong>Ajándék kesztyű</strong> a készletben.",
        "hero_alt": "Teljes Vortek láncfűrész-készlet akkumulátorokkal, láncokkal, töltővel, kofferrel és kesztyűvel",
        "badge_small": "AJÁNLAT",
        "pack_label": "TELJES KÉSZLET BENNE VAN",
        "pack_small": "2 akkumulátor · 2 lánc · koffer · ajándék kesztyű",
        "form_eye": "Bevezető ajánlat",
        "form_h2": "RENDELJE MEG A VORTEKET",
        "form_p": "Most nem fizet. Telefonon megerősítjük a rendelést, és átvételkor fizet.",
        "step1": "1 / 2. lépés",
        "step2": "2 / 2. lépés",
        "secure": "Biztonságos rendelés",
        "err": "Ellenőrizze a jelölt mezőket a folytatáshoz.",
        "lbl_name": "Teljes név",
        "ph_name": "Pl. Kovács Péter",
        "lbl_tel": "Telefonszám",
        "ph_tel": "Pl. 20 123 4567",
        "next": "TOVÁBB A RENDELÉSSEL →",
        "micro1": "Egyszer hívjuk fel az adatok és a cím megerősítéséhez.",
        "lbl_addr": "Szállítási cím",
        "ph_addr": "Utca, házszám, emelet, ajtó",
        "lbl_postal": "Irányítószám",
        "ph_postal": "1051",
        "postal_pattern": ' pattern="[0-9]{4}"',
        "lbl_city": "Város",
        "ph_city": "Budapest",
        "lbl_prov": "Vármegye",
        "ph_prov": "Pest",
        "submit": "RENDELÉS MEGERŐSÍTÉSE · 29.999 Ft",
        "back": "← Vissza",
        "micro2": "A megerősítéssel elfogadja a <a href=\"/hu/terms-conditions.html\">vásárlási feltételeket</a> és az <a href=\"/hu/privacy-policy.html\">adatvédelmi irányelveket</a>.",
        "t1b": "Ajánlat −50%",
        "t1s": "59.998 Ft → 29.999 Ft",
        "t2b": "Fizetés átvételkor",
        "t2s": "Nincs előre fizetés",
        "t3b": "Szállítás 24–48 óra*",
        "t3s": "Telefonos megerősítés után",
        "t4b": "30 nap*",
        "t4s": "Visszaküldési szabályzat",
        "prob_eye": "Dolgozzon a szokásos korlátok nélkül",
        "prob_h2": "EGYETLEN SZERSZÁM. EGÉSZ NAP.",
        "prob_p": "A Vortek kefe nélküli motort és két cserélhető akkumulátort ötvöz. Ha az egyik lemerül, behelyezi a másikat, és folytatja.",
        "m1b": "1 500 W*",
        "m1s": "A kefe nélküli motor deklarált teljesítménye.",
        "m2b": "2 AKKUMULÁTOR",
        "m2s": "Mellékelve, hogy munka közben válthasson.",
        "m3b": "40 CM*",
        "m3s": "Maximális deklarált kapacitás a fa típusától függően.",
        "feat_eye": "Arra tervezve, hogy haladjon",
        "feat_h2": "KEVESEBB MEGÁLLÁS. TÖBB ELVÉGZETT MUNKA.",
        "feat_p": "Három ok, amiért a Vortek készlet metszéshez és kerti vágáshoz készült.",
        "f1t": "1500 W-OS KEFE NÉLKÜLI MOTOR*",
        "f1p": "Egyenletes vágásra és kisebb túlmelegedésre tervezve hosszabb használatnál. A tényleges vágási teljesítmény a fától, a lánctól és a töltöttségtől függ.",
        "f1c1": "Kefe nélküli motor",
        "f1c2": "Hőelvezetés",
        "f1c3": "Kerti használat",
        "f1alt": "Fatörzs vágása Vortek láncfűrésszel",
        "f2t": "KÉT AKKUMULÁTOR, HOGY TOVÁBB VÁGHASSON",
        "f2p": "A két mellékelt akkumulátor együtt akár nyolc órát ad, a teljes töltés pedig körülbelül egy óra. A valós üzemidő a fa típusától és vastagságától függ.",
        "f2c1": "2 akkumulátor",
        "f2c2": "Gyors csere",
        "f2c3": "Töltő a készletben",
        "f2alt": "Fatörzs vágása Vortek láncfűrésszel közelről",
        "f3t": "AUTOMATIKUS KENÉS ÉS FESZÍTÉS*",
        "f3p": "Olajtartály és rendszer, amely a lánc feszességét állítja, hogy ritkábban kelljen megállni. Mindig tartsa be a gyártó karbantartási utasításait.",
        "f3c1": "2 lánc",
        "f3c2": "Olajtartály",
        "f3c3": "Automatikus beállítás*",
        "f3alt": "Vortek készlet akkumulátorokkal és töltővel a műhelyben",
        "cmp_eye": "Tárgyszerű összehasonlítás",
        "cmp_h2": "A VORTEK EGY ALAPMODELLEL SZEMBEN",
        "cmp_p": "A Vortek készlet összehasonlítása egy alap kerti láncfűrésszel.",
        "cmp_h": "Tulajdonság",
        "cmp_a": "Vortek",
        "cmp_b": "Alapmodell",
        "c1": "Mellékelt akkumulátorok",
        "c1a": "✓ 2 darab",
        "c1b": "Általában 1",
        "c2": "Töltő",
        "c2a": "✓ Mellékelve",
        "c2b": "Változó",
        "c3": "Mellékelt láncok",
        "c3a": "✓ 2 darab",
        "c3b": "Általában 1",
        "c4": "Koffer és védelem",
        "c4a": "✓ Mellékelve",
        "c4b": "Változó",
        "c5": "Utánvétes fizetés",
        "c5a": "✓ Elérhető",
        "c5b": "Változó",
        "pack_eye": "Minden benne van",
        "pack_h2": "NYISSA KI A KOFFERT, ÉS ÁLLJON MUNKÁBA.",
        "pack_alt": "A Vortek készlet teljes tartalma",
        "li1": "1 Vortek láncfűrész",
        "li2": "2 lítiumakkumulátor",
        "li3": "1 gyorstöltő",
        "li4": "2 lánc és szerelési tartozékok",
        "li5": "1 szállítókoffer",
        "li6": "Ajándék kesztyű, védőszemüveg és használati útmutató",
        "safety": "<strong>Biztonság:</strong> mindig használjon szemvédelmet, kesztyűt és megfelelő felszerelést. Olvassa el a teljes útmutatót, és ne használja a szerszámot, ha nincs felkészülve láncfűrész kezelésére.",
        "rev_eye": "Vélemények",
        "rev_h2": "AMIT AZOK MONDNAK, AKIK MÁR HASZNÁLJÁK.",
        "rev_note": "Vásárlói tapasztalatok a Vortekről. Az üzemidő és a vágás a fától és a munkakörülményektől függ.",
        "q1": "“Felaprítottam a tűzifát, és befejeztem a kerti munkát anélkül, hogy a következő töltésre kellett volna várnom.”",
        "q2": "“Meglepett, hogy vastagabb törzsekkel is elboldogult, miközben egyszerűen kezelhető maradt.”",
        "q3": "“A súlya miatt hosszabb munkánál kezelhetőbb, mint más szerszámok, amelyeket használtam.”",
        "r1n": "Péter K.",
        "r1c": "Debrecen",
        "r2n": "Eszter V.",
        "r2c": "Szeged",
        "r3n": "Gábor S.",
        "r3c": "Pécs",
        "ph1": "Vortek készlet az asztalon kicsomagolás után",
        "ph2": "Vortek láncfűrész egy fatörzs mellett a kertben",
        "ph3": "Vortek készlet kicsomagoláskor",
        "faq_eye": "Gyakori kérdések",
        "faq_h2": "RENDELÉS ELŐTT ÉRDEMES TUDNI…",
        "faq_p": "Válaszok az akkumulátorokról, a vágásról, a fizetésről, a szállításról, a visszaküldésről és a garanciáról.",
        "faq": [
            (
                "Mennyi ideig bírják az akkumulátorok?",
                "Együtt akár nyolc órát adnak. A gyorstöltő körülbelül egy óra alatt tölti fel őket. A valós üzemidő a fa vastagságától és típusától, a vágási nyomástól, a hőmérséklettől és az akkumulátorok állapotától függ.",
            ),
            (
                "Tud 40 cm-es törzseket vágni?",
                "A maximális deklarált kapacitás akár 40 cm. A fa keménysége, a technika és a karbantartás befolyásolja az eredményt.",
            ),
            (
                "Most kell fizetnem?",
                "Nem. A fizetés utánvéttel történik: a rendelést telefonon erősítjük meg, és átvételkor a futárnak fizet.",
            ),
            (
                "Pontosan mi van a készletben?",
                "Láncfűrész, két akkumulátor, töltő, két lánc, szerszámok, koffer, védőszemüveg, útmutató és ajándék kesztyű.",
            ),
            (
                "Visszaküldhetem?",
                "Igen, 30 napon belül a <a href=\"/hu/refund-policy.html\">visszatérítési szabályzat</a> szerint.",
            ),
            (
                "Milyen garancia jár hozzá?",
                "Az új termékekre a szállítás napjától 2 év jogszabályi szavatosság vonatkozik a magyar fogyasztóvédelmi szabályok szerint.",
            ),
        ],
        "cta_h2": "VORTEK 29.999 FT-ÉRT",
        "cta_p": "Teljes készlet, 50% kedvezmény és fizetés átvételkor. Az ajánlat készlet függvényében és megerősítés után érvényes.",
        "cta_btn": "RENDELÉS MOST →",
        "foot_p": "Akkumulátoros szerszám vágáshoz és kerti karbantartáshoz.",
        "help": "Segítség",
        "legal": "Jogi információk",
        "a_order": "Rendelés leadása",
        "a_ship": "Szállítás",
        "a_contact": "Kapcsolat",
        "a_priv": "Adatvédelem",
        "a_cook": "Cookie-k",
        "a_terms": "Vásárlási feltételek",
        "a_about": "Impresszum",
        "cookie_btn": "Cookie-beállítások módosítása",
        "rights": "Minden jog fenntartva. *Az üzemidő, a vágás és a határidők a fa típusától és a rendelés megerősítésétől függenek.",
        "sticky": "VORTEK RENDELÉSE · 29.999 Ft",
        "msg_name": "Adja meg a teljes nevét.",
        "msg_addr": "Adja meg a szállítási címet.",
        "msg_tel": "Adjon meg érvényes magyar telefonszámot.",
        "msg_generic": "A rendelést nem sikerült elküldeni. Próbálja meg újra.",
        "phone_js": PHONE_HU,
        "form_extra": "",
        "tmfp": False,
        "href_about": "/hu/about-us.html",
        "href_contact": "/hu/contact-us.html",
        "href_ship": "/hu/shipping-policy.html",
        "href_refund": "/hu/refund-policy.html",
        "href_priv": "/hu/privacy-policy.html",
        "href_cook": "/hu/cookie-policy.html",
        "href_terms": "/hu/terms-conditions.html",
    },
    "hr": {
        "lang": "hr",
        "locale": "hr-HR",
        "geo": "hr",
        "slug": "vortek-32300",
        "currency": "EUR",
        "price_num": 79.00,
        "offer_id": "32300",
        "lp": "",
        "key": "",
        "offer_name": "Vortek HR 32300",
        "lp_id": "hr-vortek-32300",
        "logo_html": "VOR<span>TEK</span>",
        "product_value": "Vortek",
        "webhook": WEBHOOK_DEFAULT,
        "price": "79,00 €",
        "old": "158,00 €",
        "save": "UŠTEDITE 79 €",
        "submitting": "Slanje…",
        "cookie_text": "Koristimo tehničke kolačiće i kolačiće trećih strana za poboljšanje iskustva i analitiku.",
        "cookie_accept": "Prihvati",
        "cookie_learn": "Saznajte više",
        "title": "Vortek™ — Kompletan set uz 50 % popusta",
        "desc": "Vortek: akumulatorska lančana pila s motorom bez četkica, dvije baterije i kompletnim setom. Popust 50 % i plaćanje pouzećem.",
        "announce": "<strong>50 % POPUSTA</strong> · 158,00 € → 79,00 € · PLAĆANJE POUZEĆEM",
        "ship": "Dostava 24–48 h*",
        "cod": "Pouzećem",
        "rating": "Ocjena kupaca*",
        "eyebrow": "Profesionalna akumulatorska lančana pila",
        "h1": "ZAVRŠITE POSAO. <em>NE BATERIJU.</em>",
        "lead": "Motor bez četkica od 1500 W, dvije baterije i kompletan set za rezanje debala i grana bez kabela i benzina.",
        "p1": "<strong>Do 8 sati zajedno*</strong> s dvije priložene baterije.",
        "p2": "<strong>Deklarirani kapacitet do 40 cm*</strong> ovisno o drvu i uvjetima korištenja.",
        "p3": "<strong>Samo 2,4 kg*</strong> uključujući vodilicu i bateriju.",
        "p4": "<strong>Automatsko podmazivanje i zatezanje*</strong> za manje prekida.",
        "p5": "<strong>Rukavice na poklon</strong> u setu.",
        "hero_alt": "Kompletan set lančane pile Vortek s baterijama, lancima, punjačem, koferom i rukavicama",
        "badge_small": "PONUDA",
        "pack_label": "KOMPLETAN SET UKLJUČEN",
        "pack_small": "2 baterije · 2 lanca · kofer · rukavice na poklon",
        "form_eye": "Uvodna ponuda",
        "form_h2": "NARUČITE SVOJ VORTEK",
        "form_p": "Sada ne plaćate. Narudžbu potvrđujemo telefonom, a plaćate pri preuzimanju.",
        "step1": "Korak 1 od 2",
        "step2": "Korak 2 od 2",
        "secure": "Sigurna narudžba",
        "err": "Provjerite označena polja kako biste nastavili.",
        "lbl_name": "Ime i prezime",
        "ph_name": "Npr. Ivan Horvat",
        "lbl_tel": "Telefon",
        "ph_tel": "Npr. 091 234 5678",
        "next": "NASTAVITE S NARUDŽBOM →",
        "micro1": "Nazvat ćemo vas jednom kako bismo potvrdili podatke i adresu.",
        "lbl_addr": "Adresa dostave",
        "ph_addr": "Ulica, kućni broj, kat",
        "lbl_postal": "Poštanski broj",
        "ph_postal": "10000",
        "postal_pattern": ' pattern="[0-9]{5}"',
        "lbl_city": "Grad",
        "ph_city": "Zagreb",
        "lbl_prov": "Županija",
        "ph_prov": "Grad Zagreb",
        "submit": "POTVRDITE NARUDŽBU · 79,00 €",
        "back": "← Natrag",
        "micro2": "Potvrdom prihvaćate <a href=\"/hr/terms-conditions.html\">uvjete kupnje</a> i <a href=\"/hr/privacy-policy.html\">pravila privatnosti</a>.",
        "t1b": "Ponuda −50%",
        "t1s": "158,00 € → 79,00 €",
        "t2b": "Plaćanje pri preuzimanju",
        "t2s": "Bez prethodnog plaćanja",
        "t3b": "Dostava 24–48 h*",
        "t3s": "Nakon telefonske potvrde",
        "t4b": "30 dana*",
        "t4s": "Politika povrata",
        "prob_eye": "Radite bez uobičajenih ograničenja",
        "prob_h2": "JEDAN ALAT. CIJELI DAN.",
        "prob_p": "Vortek spaja motor bez četkica s dvije izmjenjive baterije. Kad se jedna isprazni, stavite drugu i nastavite.",
        "m1b": "1 500 W*",
        "m1s": "Deklarirana snaga motora bez četkica.",
        "m2b": "2 BATERIJE",
        "m2s": "Uključene za izmjenu tijekom rada.",
        "m3b": "40 CM*",
        "m3s": "Maksimalni deklarirani kapacitet ovisno o vrsti drva.",
        "feat_eye": "Osmišljena da napredujete",
        "feat_h2": "MANJE STANKI. VIŠE OBAVLJENOG POSLA.",
        "feat_p": "Tri razloga zašto je Vortek set namijenjen rezidbi i rezanju u vrtu.",
        "f1t": "MOTOR BEZ ČETKICA 1 500 W*",
        "f1p": "Osmišljen za stalan rez i manje pregrijavanje pri duljoj uporabi. Stvarna snaga rezanja ovisi o drvu, lancu i stanju napunjenosti.",
        "f1c1": "Motor bez četkica",
        "f1c2": "Odvođenje topline",
        "f1c3": "Rad u vrtu",
        "f1alt": "Rezanje debla pilom Vortek",
        "f2t": "DVIJE BATERIJE DA REŽETE DALJE",
        "f2p": "Dvije priložene baterije zajedno daju do osam sati, a potpuno punjenje traje otprilike sat vremena. Stvarna autonomija ovisi o vrsti i debljini drva.",
        "f2c1": "2 baterije",
        "f2c2": "Brza zamjena",
        "f2c3": "Punjač u setu",
        "f2alt": "Rezanje debla pilom Vortek izbliza",
        "f3t": "AUTOMATSKO PODMAZIVANJE I ZATEZANJE*",
        "f3p": "Spremnik za ulje i sustav koji podešava napetost lanca kako biste rjeđe stajali. Uvijek slijedite upute proizvođača za održavanje.",
        "f3c1": "2 lanca",
        "f3c2": "Spremnik za ulje",
        "f3c3": "Automatsko podešavanje*",
        "f3alt": "Vortek set s baterijama i punjačem u radionici",
        "cmp_eye": "Objektivna usporedba",
        "cmp_h2": "VORTEK NASPRAM OSNOVNOG MODELA",
        "cmp_p": "Usporedba Vortek seta s osnovnom vrtnom lančanom pilom.",
        "cmp_h": "Značajka",
        "cmp_a": "Vortek",
        "cmp_b": "Osnovni model",
        "c1": "Baterije u setu",
        "c1a": "✓ 2 komada",
        "c1b": "Obično 1",
        "c2": "Punjač",
        "c2a": "✓ Uključen",
        "c2b": "Različito",
        "c3": "Lanci u setu",
        "c3a": "✓ 2 komada",
        "c3b": "Obično 1",
        "c4": "Kofer i zaštita",
        "c4a": "✓ Uključeno",
        "c4b": "Različito",
        "c5": "Plaćanje pouzećem",
        "c5a": "✓ Dostupno",
        "c5b": "Različito",
        "pack_eye": "Sve uključeno",
        "pack_h2": "OTVORITE KOFER I STANITE NA POSAO.",
        "pack_alt": "Cjelokupni sadržaj Vortek seta",
        "li1": "1 lančana pila Vortek",
        "li2": "2 litijske baterije",
        "li3": "1 brzi punjač",
        "li4": "2 lanca i pribor za montažu",
        "li5": "1 transportni kofer",
        "li6": "Rukavice na poklon, naočale i priručnik",
        "safety": "<strong>Sigurnost:</strong> uvijek koristite zaštitu za oči, rukavice i odgovarajuću opremu. Pročitajte cijeli priručnik i ne koristite alat ako niste osposobljeni za rad s lančanom pilom.",
        "rev_eye": "Recenzije",
        "rev_h2": "ŠTO KAŽU ONI KOJI JE VEĆ KORISTE.",
        "rev_note": "Iskustva kupaca s Vortekom. Autonomija i rez ovise o drvu i uvjetima rada.",
        "q1": "“Isjekao sam drva i završio vrtni posao bez čekanja na sljedeće punjenje.”",
        "q2": "“Iznenadilo me što se nosi s debljim deblima, a i dalje se jednostavno vodi.”",
        "q3": "“Zbog težine je tijekom duljeg rada upravljiviji od drugih alata koje sam koristio.”",
        "r1n": "Petar K.",
        "r1c": "Split",
        "r2n": "Elena V.",
        "r2c": "Rijeka",
        "r3n": "Marko S.",
        "r3c": "Osijek",
        "ph1": "Vortek set na stolu nakon otvaranja",
        "ph2": "Lančana pila Vortek uz deblo u vrtu",
        "ph3": "Vortek set pri otvaranju",
        "faq_eye": "Česta pitanja",
        "faq_h2": "PRIJE NARUDŽBE TREBATE ZNATI…",
        "faq_p": "Odgovori o baterijama, rezanju, plaćanju, dostavi, povratu i jamstvu.",
        "faq": [
            (
                "Koliko traju baterije?",
                "Zajedno daju do osam sati. Brzi punjač ih napuni otprilike za sat vremena. Stvarna autonomija ovisi o debljini i vrsti drva, pritisku rezanja, temperaturi i stanju baterija.",
            ),
            (
                "Može li rezati debla od 40 cm?",
                "Maksimalni deklarirani kapacitet je do 40 cm. Tvrdoća drva, tehnika i održavanje utječu na rezultat.",
            ),
            (
                "Moram li platiti sada?",
                "Ne. Plaćanje je pouzećem: narudžbu potvrđujemo telefonom, a dostavljaču plaćate pri preuzimanju.",
            ),
            (
                "Što točno set uključuje?",
                "Lančanu pilu, dvije baterije, punjač, dva lanca, alate, kofer, naočale, priručnik i rukavice na poklon.",
            ),
            (
                "Mogu li je vratiti?",
                "Da, unutar 30 dana prema <a href=\"/hr/refund-policy.html\">politici povrata</a>.",
            ),
            (
                "Kakvo je jamstvo?",
                "Na nove proizvode vrijedi 24-mjesečno zakonsko jamstvo sukladnosti od isporuke, u skladu s hrvatskim potrošačkim pravom.",
            ),
        ],
        "cta_h2": "VORTEK ZA 79,00 €",
        "cta_p": "Kompletan set, 50 % popusta i plaćanje pri preuzimanju. Ponuda vrijedi dok ima zaliha i nakon potvrde.",
        "cta_btn": "NARUČITE SADA →",
        "foot_p": "Akumulatorski alat za rezanje i vanjsko održavanje.",
        "help": "Pomoć",
        "legal": "Pravne informacije",
        "a_order": "Naručite",
        "a_ship": "Dostava",
        "a_contact": "Kontakt",
        "a_priv": "Privatnost",
        "a_cook": "Kolačići",
        "a_terms": "Uvjeti kupnje",
        "a_about": "Pravne napomene",
        "cookie_btn": "Promijeni postavke kolačića",
        "rights": "Sva prava pridržana. *Autonomija, rez i rokovi ovise o vrsti drva i potvrdi narudžbe.",
        "sticky": "NARUČITE VORTEK · 79,00 €",
        "msg_name": "Unesite ime i prezime.",
        "msg_addr": "Unesite adresu dostave.",
        "msg_tel": "Unesite važeći hrvatski broj telefona.",
        "msg_generic": "Narudžbu nije bilo moguće poslati. Pokušajte ponovno.",
        "phone_js": PHONE_HR,
        "form_extra": "",
        "tmfp": False,
        "href_about": "/hr/about-us.html",
        "href_contact": "/hr/contact-us.html",
        "href_ship": "/hr/shipping-policy.html",
        "href_refund": "/hr/refund-policy.html",
        "href_priv": "/hr/privacy-policy.html",
        "href_cook": "/hr/cookie-policy.html",
        "href_terms": "/hr/terms-conditions.html",
    },
    "ro": {
        "lang": "ro",
        "locale": "ro-RO",
        "geo": "ro",
        "slug": "vortek-32255",
        "currency": "RON",
        "price_num": 397.00,
        "offer_id": "32255",
        "lp": "",
        "key": "",
        "offer_name": "Vortek RO 32255",
        "lp_id": "ro-vortek-32255",
        "logo_html": "VOR<span>TEK</span>",
        "product_value": "Vortek",
        "webhook": WEBHOOK_DEFAULT,
        "price": "397,00 RON",
        "old": "794,00 RON",
        "save": "ECONOMISEȘTI 397 RON",
        "trust_pay_icon": "lei",
        "submitting": "Se trimite…",
        "cookie_text": "Folosim cookie-uri tehnice și de la terți pentru a-ți îmbunătăți experiența și pentru analiză.",
        "cookie_accept": "Accept",
        "cookie_learn": "Află mai multe",
        "title": "Vortek™ — Kit complet cu 50% reducere",
        "desc": "Vortek: drujbă cu acumulator, motor fără perii, două baterii și kit complet. Reducere de 50% și plata ramburs.",
        "announce": "<strong>50% REDUCERE</strong> · 794,00 RON → 397,00 RON · PLATA RAMBURS",
        "ship": "Livrare 24–48 h*",
        "cod": "Plata ramburs",
        "rating": "Evaluarea clienților*",
        "eyebrow": "Drujbă profesională cu acumulator",
        "h1": "TERMINĂ TREABA. <em>NU BATERIA.</em>",
        "lead": "Motor fără perii de 1.500 W, două baterii și kit complet pentru tăiat trunchiuri și crengi, fără cablu și fără benzină.",
        "p1": "<strong>Până la 8 ore împreună*</strong> cu cele două baterii incluse.",
        "p2": "<strong>Capacitate declarată de până la 40 cm*</strong> în funcție de lemn și de condițiile de utilizare.",
        "p3": "<strong>Doar 2,4 kg*</strong> inclusiv lama și bateria.",
        "p4": "<strong>Ungere și tensionare automate*</strong> pentru mai puține întreruperi.",
        "p5": "<strong>Mănuși cadou</strong> incluse în kit.",
        "hero_alt": "Kit complet de drujbă Vortek cu baterii, lanțuri, încărcător, valiză și mănuși",
        "badge_small": "OFERTĂ",
        "pack_label": "KIT COMPLET INCLUS",
        "pack_small": "2 baterii · 2 lanțuri · valiză · mănuși cadou",
        "form_eye": "Ofertă de lansare",
        "form_h2": "COMANDĂ VORTEK",
        "form_p": "Nu plătești acum. Confirmăm comanda la telefon și plătești la primire.",
        "step1": "Pasul 1 din 2",
        "step2": "Pasul 2 din 2",
        "secure": "Comandă sigură",
        "err": "Verifică câmpurile marcate ca să continui.",
        "lbl_name": "Nume și prenume",
        "ph_name": "Ex. Andrei Popescu",
        "lbl_tel": "Telefon",
        "ph_tel": "Ex. 0721 234 567",
        "next": "CONTINUĂ COMANDA →",
        "micro1": "Te sunăm o singură dată ca să confirmăm datele și adresa.",
        "lbl_addr": "Adresa de livrare",
        "ph_addr": "Stradă, număr, bloc, apartament",
        "lbl_postal": "Cod poștal",
        "ph_postal": "010011",
        "postal_pattern": ' pattern="[0-9]{6}"',
        "lbl_city": "Oraș",
        "ph_city": "București",
        "lbl_prov": "Județ",
        "ph_prov": "Ilfov",
        "submit": "CONFIRMĂ COMANDA · 397,00 RON",
        "back": "← Înapoi",
        "micro2": "Prin confirmare accepți <a href=\"/ro/terms-conditions.html\">condițiile de cumpărare</a> și <a href=\"/ro/privacy-policy.html\">politica de confidențialitate</a>.",
        "t1b": "Ofertă −50%",
        "t1s": "794,00 RON → 397,00 RON",
        "t2b": "Plată la primire",
        "t2s": "Fără plată în avans",
        "t3b": "Livrare 24–48 h*",
        "t3s": "După confirmarea telefonică",
        "t4b": "30 de zile*",
        "t4s": "Politica de returnare",
        "prob_eye": "Lucrează fără limitele de până acum",
        "prob_h2": "UN SINGUR INSTRUMENT. TOATĂ ZIUA.",
        "prob_p": "Vortek combină un motor fără perii cu două baterii interschimbabile. Când una se termină, o pui pe cealaltă și continui.",
        "m1b": "1.500 W*",
        "m1s": "Puterea declarată a motorului fără perii.",
        "m2b": "2 BATERII",
        "m2s": "Incluse ca să le schimbi în timpul lucrului.",
        "m3b": "40 CM*",
        "m3s": "Capacitatea maximă declarată în funcție de tipul de lemn.",
        "feat_eye": "Proiectată ca să avansezi",
        "feat_h2": "MAI PUȚINE OPRIRI. MAI MULT LUCRU FĂCUT.",
        "feat_p": "Trei motive pentru care kitul Vortek este gândit pentru tăieri și întreținere în grădină.",
        "f1t": "MOTOR FĂRĂ PERII DE 1.500 W*",
        "f1p": "Proiectat pentru tăiere constantă și încălzire mai redusă la utilizare prelungită. Puterea reală de tăiere depinde de lemn, lanț și nivelul de încărcare.",
        "f1c1": "Motor fără perii",
        "f1c2": "Disipare termică",
        "f1c3": "Utilizare în grădină",
        "f1alt": "Tăierea unui trunchi cu drujba Vortek",
        "f2t": "DOUĂ BATERII CA SĂ TĂI MAI DEPARTE",
        "f2p": "Cele două baterii incluse însumează până la opt ore, iar o încărcare completă durează aproximativ o oră. Autonomia reală depinde de tipul și grosimea lemnului.",
        "f2c1": "2 baterii",
        "f2c2": "Schimbare rapidă",
        "f2c3": "Încărcător inclus",
        "f2alt": "Tăierea unui trunchi cu drujba Vortek de aproape",
        "f3t": "UNGERE ȘI TENSIONARE AUTOMATE*",
        "f3p": "Rezervor de ulei și sistem care reglează tensiunea lanțului, ca să te oprești mai rar. Respectă întotdeauna instrucțiunile de întreținere ale producătorului.",
        "f3c1": "2 lanțuri",
        "f3c2": "Rezervor de ulei",
        "f3c3": "Reglare automată*",
        "f3alt": "Kit Vortek cu baterii și încărcător în atelier",
        "cmp_eye": "Comparație obiectivă",
        "cmp_h2": "VORTEK FAȚĂ DE UN MODEL DE BAZĂ",
        "cmp_p": "Comparația kitului Vortek cu o drujbă de grădină de bază.",
        "cmp_h": "Caracteristică",
        "cmp_a": "Vortek",
        "cmp_b": "Model de bază",
        "c1": "Baterii incluse",
        "c1a": "✓ 2 bucăți",
        "c1b": "De obicei 1",
        "c2": "Încărcător",
        "c2a": "✓ Inclus",
        "c2b": "Variabil",
        "c3": "Lanțuri incluse",
        "c3a": "✓ 2 bucăți",
        "c3b": "De obicei 1",
        "c4": "Valiză și protecție",
        "c4a": "✓ Incluse",
        "c4b": "Variabil",
        "c5": "Plata ramburs",
        "c5a": "✓ Disponibilă",
        "c5b": "Variabil",
        "pack_eye": "Totul inclus",
        "pack_h2": "DESCHIDE VALIZA ȘI PUNE-TE PE TREABĂ.",
        "pack_alt": "Conținutul complet al kitului Vortek",
        "li1": "1 drujbă Vortek",
        "li2": "2 baterii litiu",
        "li3": "1 încărcător rapid",
        "li4": "2 lanțuri și accesorii de montaj",
        "li5": "1 valiză de transport",
        "li6": "Mănuși cadou, ochelari și manual",
        "safety": "<strong>Siguranță:</strong> folosește întotdeauna protecție pentru ochi, mănuși și echipament adecvat. Citește manualul complet și nu folosi unealta dacă nu ești pregătit să mânuiești o drujbă.",
        "rev_eye": "Opinii",
        "rev_h2": "CE SPUN CEI CARE O FOLOSESC DEJA.",
        "rev_note": "Experiențe ale clienților cu Vortek. Autonomia și tăierea depind de lemn și de condițiile de lucru.",
        "q1": "“Am tăiat lemnele și am terminat treaba din grădină fără să aștept următoarea încărcare.”",
        "q2": "“M-a surprins că face față trunchiurilor mai groase, rămânând totuși ușor de manevrat.”",
        "q3": "“Datorită greutății, la lucrări lungi e mai ușor de folosit decât alte unelte pe care le-am avut.”",
        "r1n": "Andrei P.",
        "r1c": "Cluj-Napoca",
        "r2n": "Elena V.",
        "r2c": "Timișoara",
        "r3n": "Mihai S.",
        "r3c": "Iași",
        "ph1": "Kit Vortek pe masă după despachetare",
        "ph2": "Drujba Vortek lângă un trunchi în grădină",
        "ph3": "Kit Vortek la despachetare",
        "faq_eye": "Întrebări frecvente",
        "faq_h2": "ÎNAINTE SĂ COMANDI, TREBUIE SĂ ȘTII…",
        "faq_p": "Răspunsuri despre baterii, tăiere, plată, livrare, returnări și garanție.",
        "faq": [
            (
                "Cât țin bateriile?",
                "Împreună oferă până la opt ore. Încărcătorul rapid le încarcă în aproximativ o oră. Autonomia reală depinde de grosimea și tipul lemnului, de presiunea de tăiere, de temperatură și de starea bateriilor.",
            ),
            (
                "Poate tăia trunchiuri de 40 cm?",
                "Capacitatea maximă declarată este de până la 40 cm. Duritatea lemnului, tehnica și întreținerea influențează rezultatul.",
            ),
            (
                "Trebuie să plătesc acum?",
                "Nu. Plata este ramburs: confirmăm comanda la telefon și plătești curierului la primire.",
            ),
            (
                "Ce include exact?",
                "Drujbă, două baterii, încărcător, două lanțuri, unelte, valiză, ochelari, manual și mănuși cadou.",
            ),
            (
                "Pot să o returnez?",
                "Da, în 30 de zile conform <a href=\"/ro/refund-policy.html\">politicii de returnare</a>.",
            ),
            (
                "Ce garanție are?",
                "Produsele noi beneficiază de o garanție legală de conformitate de 2 ani de la livrare, conform legislației române privind protecția consumatorilor.",
            ),
        ],
        "cta_h2": "VORTEK LA 397,00 RON",
        "cta_p": "Kit complet, 50% reducere și plată la primire. Oferta depinde de stoc și de confirmare.",
        "cta_btn": "COMANDĂ ACUM →",
        "foot_p": "Unealtă cu acumulator pentru tăieri și întreținere în aer liber.",
        "help": "Ajutor",
        "legal": "Legal",
        "a_order": "Plasează comanda",
        "a_ship": "Livrări",
        "a_contact": "Contact",
        "a_priv": "Confidențialitate",
        "a_cook": "Cookie-uri",
        "a_terms": "Condiții de cumpărare",
        "a_about": "Mențiuni legale",
        "cookie_btn": "Schimbă preferințele de cookie-uri",
        "rights": "Toate drepturile rezervate. *Autonomia, tăierea și termenele depind de tipul de lemn și de confirmarea comenzii.",
        "sticky": "COMANDĂ VORTEK · 397,00 RON",
        "msg_name": "Introdu numele și prenumele.",
        "msg_addr": "Introdu adresa de livrare.",
        "msg_tel": "Introdu un număr de telefon românesc valid.",
        "msg_generic": "Comanda nu a putut fi trimisă. Încearcă din nou.",
        "phone_js": PHONE_RO,
        "form_extra": "",
        "tmfp": False,
        "href_about": "/ro/about-us.html",
        "href_contact": "/ro/contact-us.html",
        "href_ship": "/ro/shipping-policy.html",
        "href_refund": "/ro/refund-policy.html",
        "href_priv": "/ro/privacy-policy.html",
        "href_cook": "/ro/cookie-policy.html",
        "href_terms": "/ro/terms-conditions.html",
    },
    "pt": {
        "lang": "pt",
        "locale": "pt-PT",
        "geo": "pt",
        "slug": "vortek-14255",
        "currency": "EUR",
        "price_num": 59.00,
        "offer_id": "14255",
        "lp": "",
        "key": "",
        "offer_name": "Vortek PT 14255",
        "lp_id": "pt-vortek-14255",
        "logo_html": "VOR<span>TEK</span>",
        "product_value": "Vortek",
        "webhook": WEBHOOK_DEFAULT,
        "price": "59,00 €",
        "old": "118,00 €",
        "save": "POUPA 59 €",
        "submitting": "A enviar…",
        "cookie_text": "Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análise.",
        "cookie_accept": "Aceitar",
        "cookie_learn": "Mais informação",
        "title": "Vortek™ — Kit completo com 50 % de desconto",
        "desc": "Vortek: motosserra a bateria com motor sem escovas, duas baterias e kit completo. Desconto de 50 % e pagamento contra reembolso.",
        "announce": "<strong>50 % DE DESCONTO</strong> · 118,00 € → 59,00 € · PAGAMENTO À COBRANÇA",
        "ship": "Envio 24–48 h*",
        "cod": "Contra reembolso",
        "rating": "Avaliação de clientes*",
        "eyebrow": "Motosserra profissional a bateria",
        "h1": "TERMINE O TRABALHO. <em>NÃO A BATERIA.</em>",
        "lead": "Motor sem escovas de 1500 W, duas baterias e kit completo para cortar troncos e ramos sem cabos nem gasolina.",
        "p1": "<strong>Até 8 horas combinadas*</strong> com as duas baterias incluídas.",
        "p2": "<strong>Capacidade declarada até 40 cm*</strong> consoante a madeira e as condições de utilização.",
        "p3": "<strong>Apenas 2,4 kg*</strong> incluindo a espada e a bateria.",
        "p4": "<strong>Lubrificação e tensionamento automáticos*</strong> para reduzir interrupções.",
        "p5": "<strong>Luvas de oferta</strong> incluídas no kit.",
        "hero_alt": "Kit completo da motosserra Vortek com baterias, correntes, carregador, mala e luvas",
        "badge_small": "OFERTA",
        "pack_label": "KIT COMPLETO INCLUÍDO",
        "pack_small": "2 baterias · 2 correntes · mala · luvas de oferta",
        "form_eye": "Oferta de lançamento",
        "form_h2": "ENCOMENDE A SUA VORTEK",
        "form_p": "Não paga agora. Confirmamos a encomenda por telefone e paga quando a receber.",
        "step1": "Passo 1 de 2",
        "step2": "Passo 2 de 2",
        "secure": "Encomenda segura",
        "err": "Reveja os campos assinalados para continuar.",
        "lbl_name": "Nome e apelido",
        "ph_name": "Ex. João Silva",
        "lbl_tel": "Telefone",
        "ph_tel": "Ex. 912 345 678",
        "next": "CONTINUAR A ENCOMENDA →",
        "micro1": "Ligamos-lhe uma vez para confirmar os dados e a morada.",
        "lbl_addr": "Morada de entrega",
        "ph_addr": "Rua, número e andar",
        "lbl_postal": "Código postal",
        "ph_postal": "1000-001",
        "postal_pattern": ' pattern="[0-9]{4}-[0-9]{3}"',
        "lbl_city": "Cidade",
        "ph_city": "Lisboa",
        "lbl_prov": "Distrito",
        "ph_prov": "Lisboa",
        "submit": "CONFIRMAR ENCOMENDA · 59,00 €",
        "back": "← Voltar",
        "micro2": "Ao confirmar, aceita as <a href=\"/pt/terms-conditions.html\">condições de compra</a> e a <a href=\"/pt/privacy-policy.html\">política de privacidade</a>.",
        "t1b": "Oferta −50%",
        "t1s": "118,00 € → 59,00 €",
        "t2b": "Pagamento à cobrança",
        "t2s": "Sem pagamento prévio",
        "t3b": "Entrega 24–48 h*",
        "t3s": "Após confirmação por telefone",
        "t4b": "30 dias*",
        "t4s": "Política de devolução",
        "prob_eye": "Trabalhe sem as limitações de sempre",
        "prob_h2": "UMA SÓ FERRAMENTA. O DIA INTEIRO.",
        "prob_p": "A Vortek junta um motor sem escovas a duas baterias intercambiáveis. Quando uma acaba, coloca a outra e continua.",
        "m1b": "1 500 W*",
        "m1s": "Potência declarada do motor sem escovas.",
        "m2b": "2 BATERIAS",
        "m2s": "Incluídas para alternar durante o trabalho.",
        "m3b": "40 CM*",
        "m3s": "Capacidade máxima declarada consoante o tipo de madeira.",
        "feat_eye": "Feita para avançar",
        "feat_h2": "MENOS PARAGENS. MAIS TRABALHO FEITO.",
        "feat_p": "Três razões pelas quais o kit Vortek foi pensado para poda e corte em jardins e terrenos.",
        "f1t": "MOTOR SEM ESCOVAS DE 1 500 W*",
        "f1p": "Concebido para um corte constante e menos sobreaquecimento em utilizações prolongadas. A potência real de corte depende da madeira, da corrente e do estado de carga.",
        "f1c1": "Motor sem escovas",
        "f1c2": "Dissipação térmica",
        "f1c3": "Uso no jardim",
        "f1alt": "Pessoa a cortar um tronco com a motosserra Vortek",
        "f2t": "DUAS BATERIAS PARA CONTINUAR A CORTAR",
        "f2p": "As duas baterias incluídas somam até oito horas e uma carga completa demora cerca de uma hora. A autonomia real depende do tipo e da espessura da madeira.",
        "f2c1": "2 baterias",
        "f2c2": "Troca rápida",
        "f2c3": "Carregador incluído",
        "f2alt": "Corte de um tronco com a motosserra Vortek",
        "f3t": "LUBRIFICAÇÃO E TENSIONAMENTO AUTOMÁTICOS*",
        "f3p": "Depósito de óleo e sistema que ajusta a tensão da corrente para reduzir as paragens manuais. Siga sempre as instruções de manutenção do fabricante.",
        "f3c1": "2 correntes",
        "f3c2": "Depósito de óleo",
        "f3c3": "Ajuste automático*",
        "f3alt": "Kit Vortek com baterias e carregador na oficina",
        "cmp_eye": "Comparação objetiva",
        "cmp_h2": "A VORTEK FACE A UM MODELO BÁSICO",
        "cmp_p": "Comparação do kit Vortek com uma motosserra básica de jardim.",
        "cmp_h": "Característica",
        "cmp_a": "Vortek",
        "cmp_b": "Modelo básico",
        "c1": "Baterias incluídas",
        "c1a": "✓ 2 unidades",
        "c1b": "Habitualmente 1",
        "c2": "Carregador",
        "c2a": "✓ Incluído",
        "c2b": "Variável",
        "c3": "Correntes incluídas",
        "c3a": "✓ 2 unidades",
        "c3b": "Habitualmente 1",
        "c4": "Mala e proteção",
        "c4a": "✓ Incluídos",
        "c4b": "Variável",
        "c5": "Pagamento contra reembolso",
        "c5a": "✓ Disponível",
        "c5b": "Variável",
        "pack_eye": "Tudo incluído",
        "pack_h2": "ABRA A MALA E PONHA-SE A TRABALHAR.",
        "pack_alt": "Conteúdo completo do pack Vortek",
        "li1": "1 motosserra Vortek",
        "li2": "2 baterias de lítio",
        "li3": "1 carregador rápido",
        "li4": "2 correntes e acessórios de montagem",
        "li5": "1 mala de transporte",
        "li6": "Luvas de oferta, óculos e manual",
        "safety": "<strong>Segurança:</strong> utilize sempre proteção ocular, luvas e equipamento adequado. Leia o manual completo e não utilize a ferramenta se não estiver preparado para manusear uma motosserra.",
        "rev_eye": "Opiniões",
        "rev_h2": "O QUE DIZEM OS QUE JÁ A USAM.",
        "rev_note": "Opiniões de clientes sobre a Vortek. A autonomia e o corte dependem da madeira e das condições de trabalho.",
        "q1": "“Consegui cortar a lenha e acabar o trabalho do jardim sem parar à espera de outra carga.”",
        "q2": "“Surpreendeu-me conseguir trabalhar com troncos mais grossos e manter um manuseamento simples.”",
        "q3": "“O peso torna-a mais fácil de manejar em trabalhos longos do que outras ferramentas que já usei.”",
        "r1n": "Carlos M.",
        "r1c": "Porto",
        "r2n": "Elena V.",
        "r2c": "Coimbra",
        "r3n": "João S.",
        "r3c": "Braga",
        "ph1": "Kit Vortek em cima da mesa ao desembalar",
        "ph2": "Motosserra Vortek junto a um tronco no jardim",
        "ph3": "Kit Vortek ao desembalá-lo em casa",
        "faq_eye": "Perguntas frequentes",
        "faq_h2": "ANTES DE ENCOMENDAR, DEVE SABER…",
        "faq_p": "Respostas sobre baterias, corte, pagamento, envio, devoluções e garantia.",
        "faq": [
            (
                "Quanto duram as baterias?",
                "Juntas oferecem até oito horas combinadas. O carregador rápido carrega-as em cerca de uma hora. A autonomia real depende da espessura e do tipo de madeira, da pressão de corte, da temperatura e do estado das baterias.",
            ),
            (
                "Consegue cortar troncos de 40 cm?",
                "A capacidade máxima declarada é de até 40 cm. A dureza da madeira, a técnica e a manutenção influenciam o resultado.",
            ),
            (
                "Tenho de pagar agora?",
                "Não. O pagamento é contra reembolso: a encomenda confirma-se por telefone e paga ao transportador quando a receber.",
            ),
            (
                "O que inclui exatamente?",
                "Motosserra, duas baterias, carregador, duas correntes, ferramentas, mala, óculos, manual e luvas de oferta.",
            ),
            (
                "Posso devolvê-la?",
                "Sim, durante 30 dias segundo a <a href=\"/pt/refund-policy.html\">política de reembolso</a>.",
            ),
            (
                "Que garantia tem?",
                "Os produtos novos estão cobertos por uma garantia legal de conformidade de 3 anos a partir da entrega, nos termos da legislação portuguesa de defesa do consumidor.",
            ),
        ],
        "cta_h2": "VORTEK POR 59,00 €",
        "cta_p": "Kit completo, 50 % de desconto e pagamento à cobrança. Oferta sujeita a disponibilidade e confirmação.",
        "cta_btn": "ENCOMENDAR AGORA →",
        "foot_p": "Ferramenta a bateria para trabalhos de corte e manutenção no exterior.",
        "help": "Ajuda",
        "legal": "Legal",
        "a_order": "Fazer encomenda",
        "a_ship": "Envios",
        "a_contact": "Contacto",
        "a_priv": "Privacidade",
        "a_cook": "Cookies",
        "a_terms": "Condições de compra",
        "a_about": "Aviso legal",
        "cookie_btn": "Alterar preferências de cookies",
        "rights": "Todos os direitos reservados. *A autonomia, o corte e os prazos dependem do tipo de madeira e da confirmação da encomenda.",
        "sticky": "ENCOMENDAR VORTEK · 59,00 €",
        "msg_name": "Introduza o nome e o apelido.",
        "msg_addr": "Introduza a morada de entrega.",
        "msg_tel": "Introduza um número de telefone português válido.",
        "msg_generic": "Não foi possível enviar a encomenda. Tente novamente.",
        "phone_js": PHONE_PT,
        "form_extra": "",
        "tmfp": False,
        "href_about": "/pt/about-us.html",
        "href_contact": "/pt/contact-us.html",
        "href_ship": "/pt/shipping-policy.html",
        "href_refund": "/pt/refund-policy.html",
        "href_priv": "/pt/privacy-policy.html",
        "href_cook": "/pt/cookie-policy.html",
        "href_terms": "/pt/terms-conditions.html",
    },
}

TY = {
    "hu": {
        "title": "Rendelés rögzítve — Várja a visszaigazoló hívást | Vortek™",
        "desc": "Vortek™ rendelése rögzítve. Már csak egy utolsó lépés van hátra: vegye fel a visszaigazoló hívást.",
        "cookie": "Technikai és harmadik felek cookie-jait használjuk a felhasználói élmény javítására és elemzésre.",
        "accept": "Elfogadom",
        "learn": "Tudjon meg többet",
        "h1": "Rendelését sikeresen rögzítettük!",
        "sub": "Remek — <strong>Vortek™</strong> rendelése feldolgozás alatt van. Már csak <strong>egy utolsó lépés</strong> van hátra a véglegesítéshez és a szállításhoz.",
        "alt": "A trendtopia-store csapat munka közben: call center és utánvétes logisztika",
        "eye": "👇 Mit tegyen most",
        "call_t": "📞 Vegye fel a visszaigazoló hívást",
        "call_b": "Operátorunk <strong>a következő órákban</strong> felhívja Önt a rendelés megerősítéséhez.",
        "warn": "Ha nem veszi fel a telefont, a rendelés automatikusan törlődik.",
        "hours_h": "🕒 Kapcsolattartási idő",
        "hours": "<strong>Hétfő – Szombat</strong> · 9:00 – 18:00",
        "next_h": "📋 Mi történik ezután",
        "s1": "Vegye fel a hívást és <strong>erősítse meg adatait</strong>",
        "s2": "Rendelése <strong>24–48 órán belül</strong> elindul",
        "s3": "Házhoz szállítás és <strong>utánvét</strong>",
        "b1": "🔒 Utánvét",
        "b2": "🛡️ 2 év garancia",
        "b3": "🔐 SSL védelem",
        "info": "Információ",
        "about": "Rólunk",
        "contact": "Kapcsolat",
        "priv": "Adatvédelmi irányelvek",
        "terms": "Általános szerződési feltételek",
        "cook": "Cookie szabályzat",
        "ship": "Szállítási feltételek",
        "refund": "Visszatérítési szabályzat",
        "contact_h": "Elérhetőségek",
        "rights": "Minden jog fenntartva.",
        "cpa": 16.0,
        "currency": "HUF",
        "price": "29999.0",
    },
    "hr": {
        "title": "Narudžba zaprimljena — Pričekajte poziv za potvrdu | Vortek™",
        "desc": "Vaša Vortek™ narudžba je zabilježena. Ostaje još samo jedan korak: odgovorite na potvrdni poziv.",
        "cookie": "Koristimo tehničke kolačiće i kolačiće trećih strana za poboljšanje iskustva i analitiku.",
        "accept": "Prihvati",
        "learn": "Saznajte više",
        "h1": "Vaša narudžba je uspješno zabilježena!",
        "sub": "Odlično — vaša narudžba <strong>Vortek™</strong> se obrađuje. Ostaje još samo <strong>zadnji korak</strong> za dovršetak i slanje pošiljke.",
        "alt": "Tim trendtopia-store na poslu: call centar i logistika pouzećem",
        "eye": "👇 Što trebate učiniti sada",
        "call_t": "📞 Odgovorite na potvrdni poziv",
        "call_b": "Naš operater kontaktirat će vas <strong>u narednim satima</strong> kako bi potvrdio narudžbu.",
        "warn": "Ako ne odgovorite na poziv, narudžba će se automatski otkazati.",
        "hours_h": "🕒 Radno vrijeme kontakta",
        "hours": "<strong>Ponedjeljak – Subota</strong> · 9:00 – 18:00",
        "next_h": "📋 Što slijedi",
        "s1": "Odgovorite na poziv i <strong>potvrdite svoje podatke</strong>",
        "s2": "Vaša narudžba bit će poslana unutar <strong>24–48 sati</strong>",
        "s3": "Dostava na kućnu adresu i <strong>plaćanje pouzećem</strong>",
        "b1": "🔒 Plaćanje pouzećem",
        "b2": "🛡️ Jamstvo 24 mjeseca",
        "b3": "🔐 SSL zaštita",
        "info": "Informacije",
        "about": "O nama",
        "contact": "Kontakt",
        "priv": "Pravila privatnosti",
        "terms": "Uvjeti korištenja",
        "cook": "Pravila o kolačićima",
        "ship": "Pravila dostave",
        "refund": "Pravila povrata",
        "contact_h": "Kontakt",
        "rights": "Sva prava pridržana.",
        "cpa": 16.0,
        "currency": "EUR",
        "price": "79.0",
    },
    "ro": {
        "title": "Comandă înregistrată — Așteaptă apelul de confirmare | Vortek™",
        "desc": "Comanda ta Vortek™ a fost înregistrată. Mai rămâne un ultim pas: răspunde la apelul de confirmare.",
        "cookie": "Folosim cookie-uri tehnice și de la terți pentru a-ți îmbunătăți experiența și pentru analiză.",
        "accept": "Accept",
        "learn": "Află mai multe",
        "h1": "Comanda ta a fost înregistrată cu succes!",
        "sub": "Perfect — comanda ta <strong>Vortek™</strong> este în curs de procesare. Mai rămâne <strong>un singur pas</strong> pentru finalizare și expediere.",
        "alt": "Echipa trendtopia-store la lucru: call center și logistică pentru plata ramburs",
        "eye": "👇 Ce trebuie să faci acum",
        "call_t": "📞 Răspunde la apelul de confirmare",
        "call_b": "Un operator te va contacta <strong>în următoarele ore</strong> pentru confirmarea comenzii.",
        "warn": "Dacă nu răspunzi la apel, comanda va fi anulată automat.",
        "hours_h": "🕒 Program de contact",
        "hours": "<strong>Luni – Sâmbătă</strong> · 9:00 – 18:00",
        "next_h": "📋 Ce urmează",
        "s1": "Răspunde la apel și <strong>confirmă-ți datele</strong>",
        "s2": "Comanda ta va fi expediată în <strong>24–48 de ore</strong>",
        "s3": "Livrare la domiciliu și <strong>plata ramburs</strong>",
        "b1": "🔒 Plata ramburs",
        "b2": "🛡️ Garanție 2 ani",
        "b3": "🔐 Protecție SSL",
        "info": "Informații",
        "about": "Despre noi",
        "contact": "Contact",
        "priv": "Politica de confidențialitate",
        "terms": "Termeni și condiții",
        "cook": "Politica privind cookie-urile",
        "ship": "Politica de livrare",
        "refund": "Politica de returnare",
        "contact_h": "Contact",
        "rights": "Toate drepturile rezervate.",
        "cpa": 16.0,
        "currency": "RON",
        "price": "397.0",
    },
    "pt": {
        "title": "Encomenda recebida — Aguarde a chamada de confirmação | Vortek™",
        "desc": "A sua encomenda Vortek™ foi registada. Falta apenas um último passo: atenda a chamada de confirmação.",
        "cookie": "Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análise.",
        "accept": "Aceitar",
        "learn": "Mais informação",
        "h1": "A sua encomenda foi registada com sucesso!",
        "sub": "Perfeito — a sua encomenda <strong>Vortek™</strong> está a ser processada. Falta apenas <strong>um último passo</strong> para a concluir e iniciar o envio.",
        "alt": "A equipa trendtopia-store a trabalhar: centro de atendimento e logística contra reembolso",
        "eye": "👇 O que deve fazer agora",
        "call_t": "📞 Atenda a chamada de confirmação",
        "call_b": "Um operador irá contactá-lo <strong>nas próximas horas</strong> para confirmar a sua encomenda.",
        "warn": "Se não atender a chamada, a encomenda será automaticamente cancelada.",
        "hours_h": "🕒 Horário de contacto",
        "hours": "<strong>Segunda – Sábado</strong> · 9:00 – 18:00",
        "next_h": "📋 O que acontece a seguir",
        "s1": "Atenda a chamada e <strong>confirme os seus dados</strong>",
        "s2": "A sua encomenda será enviada no prazo de <strong>24–48 horas</strong>",
        "s3": "Entrega ao domicílio e <strong>pagamento contra reembolso</strong>",
        "b1": "🔒 Pagamento contra reembolso",
        "b2": "🛡️ Garantia 3 anos",
        "b3": "🔐 Proteção SSL",
        "info": "Informação",
        "about": "Quem somos",
        "contact": "Contacto",
        "priv": "Política de privacidade",
        "terms": "Termos e condições",
        "cook": "Política de cookies",
        "ship": "Política de envio",
        "refund": "Política de reembolso",
        "contact_h": "Contacto",
        "rights": "Todos os direitos reservados.",
        "cpa": 11.0,
        "currency": "EUR",
        "price": "59.0",
    },
}


def write_index(geo: str, slug: str, dest: Path) -> None:
    dest.write_text(
        f"""<!DOCTYPE html>
<html lang="{geo}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/{slug}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/{slug}/landing.html">
<link rel="canonical" href="https://trendtopia-store.com/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">Vortek™</a></p>
</body>
</html>
""",
        encoding="utf-8",
        newline="\n",
    )


def write_thankyou(geo: str, L: dict, T: dict) -> None:
    src = (ROOT / "es" / "vortek-1013" / "thank-you.html").read_text(encoding="utf-8")
    pairs = [
        ('<html lang="es">', f'<html lang="{geo}">'),
        (
            "Pedido recibido — Espera la llamada de confirmación | Vortek™",
            T["title"],
        ),
        (
            "Tu pedido Vortek™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
            T["desc"],
        ),
        (" GEO: 'es',", f" GEO: '{geo}',"),
        (" PRODUCT_SLUG: 'vortek-1013',", f" PRODUCT_SLUG: '{L['slug']}',"),
        (" CURRENCY: 'EUR',", f" CURRENCY: '{T['currency']}',"),
        (" PRICE: 69.0,", f" PRICE: {T['price']},"),
        (
            " COOKIE_TEXT: 'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.',",
            f" COOKIE_TEXT: {T['cookie']!r},",
        ),
        (" COOKIE_ACCEPT: 'Aceptar',", f" COOKIE_ACCEPT: {T['accept']!r},"),
        (" COOKIE_LEARN: 'Más información'", f" COOKIE_LEARN: {T['learn']!r}"),
        ("¡Tu pedido se ha registrado correctamente!", T["h1"]),
        (
            "Perfecto — tu pedido <strong>Vortek™</strong> está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.",
            T["sub"],
        ),
        (
            "El equipo de trendtopia-store trabajando: centro de atención telefónica y logística de pago contra reembolso",
            T["alt"],
        ),
        ("👇 Qué debes hacer ahora", T["eye"]),
        ("📞 Responde a la llamada de confirmación", T["call_t"]),
        (
            "Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido.",
            T["call_b"],
        ),
        (
            "Si no respondes a la llamada, el pedido se cancelará automáticamente.",
            T["warn"],
        ),
        ("🕒 Horario de contacto", T["hours_h"]),
        ("<strong>Lunes – Sábado</strong> · 9:00 – 18:00", T["hours"]),
        ("📋 Qué ocurre después", T["next_h"]),
        ("Responde a la llamada y <strong>confirma tus datos</strong>", T["s1"]),
        ("Tu pedido se enviará en un plazo de <strong>24–48 horas</strong>", T["s2"]),
        ("Entrega a domicilio y <strong>pago contra reembolso</strong>", T["s3"]),
        ("🔒 Pago contra reembolso", T["b1"]),
        ("🛡️ Garantía 3 años", T["b2"]),
        ("🔐 Protección SSL", T["b3"]),
        (">Información<", f">{T['info']}<"),
        ('href="/es/about-us.html">Quiénes somos</a>', f'href="/{geo}/about-us.html">{T["about"]}</a>'),
        ('href="/es/contact-us.html">Contacto</a>', f'href="/{geo}/contact-us.html">{T["contact"]}</a>'),
        (
            'href="/es/privacy-policy.html">Política de privacidad</a>',
            f'href="/{geo}/privacy-policy.html">{T["priv"]}</a>',
        ),
        (
            'href="/es/terms-conditions.html">Términos y condiciones</a>',
            f'href="/{geo}/terms-conditions.html">{T["terms"]}</a>',
        ),
        (
            'href="/es/cookie-policy.html">Política de cookies</a>',
            f'href="/{geo}/cookie-policy.html">{T["cook"]}</a>',
        ),
        (
            'href="/es/shipping-policy.html">Política de envío</a>',
            f'href="/{geo}/shipping-policy.html">{T["ship"]}</a>',
        ),
        (
            'href="/es/refund-policy.html">Política de reembolso</a>',
            f'href="/{geo}/refund-policy.html">{T["refund"]}</a>',
        ),
        (">Contacto</h4>", f">{T['contact_h']}</h4>"),
        ("Todos los derechos reservados.", T["rights"]),
        ("'value': 17.0,", f"'value': {T['cpa']},"),
    ]
    for old, new in pairs:
        if old not in src:
            raise SystemExit(f"{geo}: missing thank-you fragment: {old[:80]!r}")
        src = src.replace(old, new, 1)
    leftovers = [
        "Tu pedido",
        "llamada de confirmación",
        "Quiénes somos",
        "Más información",
        'href="/es/',
        "Lunes – Sábado",
        "¡Tu pedido",
    ]
    found = [w for w in leftovers if w in src]
    if found:
        raise SystemExit(f"{geo} thank-you leftover ES: {found}")
    dest = ROOT / geo / L["slug"] / "thank-you.html"
    dest.write_text(src, encoding="utf-8", newline="\n")


def main() -> None:
    for geo, L in LOCALES.items():
        folder = ROOT / geo / L["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        landing = folder / "landing.html"
        landing.write_text(render(L), encoding="utf-8", newline="\n")
        write_index(geo, L["slug"], folder / "index.html")
        write_thankyou(geo, L, TY[geo])
        print(f"wrote {folder.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
