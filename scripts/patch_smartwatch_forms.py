#!/usr/bin/env python3
"""Patch Smartwatch landings with Adrice form HTML credentials."""
from __future__ import annotations

import re
from pathlib import Path

from smartwatch_network_forms import (
    ACTION,
    FORM_COPY,
    FORMS,
    SCRIPT,
    SUBID_SCRIPT,
    TMFP_SCRIPT,
    UID,
    WEBHOOK,
)

ROOT = Path(__file__).resolve().parents[1]
SLUG = "smartwatch"
ACTIVE_OFFERS = ("3137", "3141", "1842")


def render_form(offer: str, suffix: str = "", secondary: bool = False) -> str:
    copy = FORM_COPY[offer]
    net = FORMS[offer]
    geo = copy["geo"]
    ty = f"https://trendtopia-store.com/{geo}/{SLUG}/thank-you.html"
    submit = copy["submit2" if secondary else "submit"]
    subid_id = "subid" if not suffix else f"subid{suffix}"
    tmfp_id = "tmfp" if not suffix else f"tmfp{suffix}"
    lines = [f'<form class="cf-form tm-order-form" action="{ACTION}" method="post">']
    for field_name, label, placeholder in copy["fields"]:
        field_id = f"{field_name}{suffix}"
        autocomplete = "name" if field_name == "name" else field_name
        input_type = "tel" if field_name == "tel" else "text"
        lines.extend(
            [
                f'<label class="cf-lbl" for="{field_id}">{label}</label>',
                f'<input id="{field_id}" type="{input_type}" name="{field_name}" autocomplete="{autocomplete}" placeholder="{placeholder}" required><br>',
            ]
        )
    lines.extend(
        [
            f'<input name="uid" type="hidden" value="{UID}" />',
            f'<input name="offer" type="hidden" value="{offer}" />',
            f'<input name="lp" type="hidden" value="{net["lp"]}" />',
            f'<input name="subid" id="{subid_id}" type="hidden" value="" />',
            f'<input name="tmfp" id="{tmfp_id}" type="hidden" value="" />',
            f'<input name="thankyoupage" type="hidden" value="{ty}"/>',
            f'<input name="webhook" type="hidden" value="{WEBHOOK}"/>',
            f'<input name="_key" type="hidden" value="{net["key"]}" />',
            '<div style="margin-top: 10px; text-align: center">',
            f'<button name="submit" type="submit">{submit}</button>',
            "</div>",
            SUBID_SCRIPT,
            f'<script src="{TMFP_SCRIPT}" crossorigin="anonymous" defer></script>',
            f'<script src="{SCRIPT}" async></script>',
            "</form>",
        ]
    )
    return "\n".join(lines)


def patch_landing(path: Path, offer: str) -> None:
    html = path.read_text(encoding="utf-8")
    forms = list(re.finditer(r'<form class="cf-form tm-order-form"[\s\S]*?</form>', html))
    if len(forms) != 2:
        raise RuntimeError(f"Expected 2 forms in {path}, found {len(forms)}")
    form1 = render_form(offer, "", secondary=False)
    form2 = render_form(offer, "2", secondary=True)
    html = html[: forms[0].start()] + form1 + html[forms[0].end() : forms[1].start()] + form2 + html[forms[1].end() :]
    path.write_text(html, encoding="utf-8")
    print(f"Patched {path.relative_to(ROOT)}")


def main() -> None:
    for offer in ACTIVE_OFFERS:
        copy = FORM_COPY[offer]
        landing = ROOT / copy["geo"] / SLUG / "landing.html"
        if not landing.exists():
            print(f"Skip missing {landing.relative_to(ROOT)}")
            continue
        patch_landing(landing, offer)


if __name__ == "__main__":
    main()
