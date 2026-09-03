# -*- coding: utf-8 -*-
"""Adrice Network form credentials — CoreSync (ES, PL, GR)."""
UID = "019e5f4e-b178-7d63-91e1-6fda72088957"
WEBHOOK = "https://hook.eu2.make.com/otlkouarqencnd3tdlobo9xhdex1wcei"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"
TMFP_SCRIPT = "https://offers.adricenetwork.com/forms/tmfp/"

FORMS: dict[str, dict[str, str]] = {
    "3137": {"lp": "3171", "key": "e4902d24a201fe03eb3c43937bbcef784ded5f43"},
    "3141": {"lp": "3175", "key": "b8326e3eb2c8bd4345a5a7b1ec4397f181131c7e"},
    "1842": {"lp": "1862", "key": "f9c80134e3e627afb228790d616668b0b70aa1c4"},
}

CPA: dict[str, float] = {
    "3137": 15.0,
    "3141": 13.0,
    "1842": 15.0,
}

FORM_COPY: dict[str, dict] = {
    "3137": {
        "geo": "es",
        "fields": [
            ("name", "Nombre y apellidos*", "Nombre y apellidos"),
            ("tel", "Teléfono*", "Teléfono"),
            ("street-address", "Dirección de entrega*", "Dirección de entrega"),
        ],
        "submit": "Sí, quiero mi CoreSync a 49,00 €",
        "submit2": "Haz tu pedido",
    },
    "3141": {
        "geo": "pl",
        "fields": [
            ("name", "Imię i nazwisko*", "Imię i nazwisko"),
            ("tel", "Telefon*", "Telefon"),
            ("street-address", "Adres dostawy*", "Adres dostawy"),
        ],
        "submit": "Tak, chcę CoreSync za 199,00 zł",
        "submit2": "Złóż zamówienie",
    },
    "1842": {
        "geo": "gr",
        "fields": [
            ("name", "Ονοματεπώνυμο*", "Ονοματεπώνυμο"),
            ("tel", "Τηλέφωνο*", "Τηλέφωνο"),
            ("street-address", "Διεύθυνση παράδοσης*", "Διεύθυνση παράδοσης"),
        ],
        "submit": "Ναι, θέλω το CoreSync μου στα 69,00 €",
        "submit2": "Υποβολή παραγγελίας",
    },
}

SUBID_SCRIPT = """<script>
document.addEventListener("DOMContentLoaded", function () {
var params = new URLSearchParams(window.location.search);
var campaign = params.get("utm_campaign") || "";
document.querySelectorAll('input[name="subid"]').forEach(function (subidInput) {
subidInput.value = campaign;
});
});
</script>"""
