# -*- coding: utf-8 -*-
"""Adrice Network form credentials per Casa Fuego offer id."""
UID = "019e5f4e-b178-7d63-91e1-6fda72088957"
WEBHOOK = "https://hook.eu2.make.com/otlkouarqencnd3tdlobo9xhdex1wcei"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

FORMS = {
    "1476": {"lp": "1496", "key": "a28c49be2b5def739690fd3217a391ff6df0db05"},
    "2409": {"lp": "2434", "key": "6b2e2c5e1b0a4c414b4ac68145700f6e01d3d81d"},
    "3176": {"lp": "3210", "key": "11d65f1d13d333374d5526fe541c73e0c5752a5f"},
    "3177": {"lp": "3211", "key": "929fc039d3784ba1edb5a176c1a162aad1905c01"},
    "3178": {"lp": "3212", "key": "649303b60cc4cebb22e018da131b30b4e706b2b8"},
    "3179": {"lp": "3213", "key": "355c00bd91b5cb59cd2fa680ac74a9e6f3ec11ec"},
    "3251": {"lp": "3285", "key": "0af7749e1e5ae84ab4405c78558227e061a30b80"},
    "3702": {"lp": "3742", "key": "c9fb0b2bbaca32e82d72fae2741f14e4a388647a"},
}

CPA = {
    "1476": 16,
    "2409": 18,
    "3176": 17,
    "3177": 22,
    "3178": 17,
    "3179": 19,
    "3251": 15,
    "3702": 16,
}

# Per-offer form field copy (from Adrice HTML snippets).
FORM_COPY = {
    "1476": {
        "geo": "pt",
        "fields": [
            ("name", "Nome e sobrenome*", "Nome e sobrenome"),
            ("tel", "Telefone*", "Telefone"),
            ("street-address", "Endereço*", "Endereço"),
        ],
        "submit": "Enviar o pedido",
    },
    "2409": {
        "geo": "hu",
        "fields": [
            ("name", "Keresztnév Vezetéknév*", "Keresztnév Vezetéknév"),
            ("street-address", "Cím*", "Cím"),
            ("tel", "Telefon*", "Telefon"),
        ],
        "submit": "Rendeljen most",
    },
    "3176": {
        "geo": "es",
        "fields": [
            ("name", "Nombre Apellido*", "Nombre Apellido"),
            ("street-address", "Dirección*", "Dirección"),
            ("tel", "Teléfono*", "Teléfono"),
        ],
        "submit": "Haz tu pedido",
    },
    "3177": {
        "geo": "de",
        "fields": [
            ("name", "Vorname Nachname*", "Vorname Nachname"),
            ("street-address", "Anschrift*", "Anschrift"),
            ("tel", "Telefon*", "Telefon"),
        ],
        "submit": "Jetzt bestellen",
    },
    "3178": {
        "geo": "lt",
        "fields": [
            ("name", "Vardas Pavardė*", "Vardas Pavardė"),
            ("street-address", "Adresas*", "Adresas"),
            ("tel", "Telefonas*", "Telefonas"),
        ],
        "submit": "Užsisakykite dabar",
    },
    "3179": {
        "geo": "pl",
        "fields": [
            ("name", "Imię Nazwisko*", "Imię Nazwisko"),
            ("street-address", "Adres*", "Adres"),
            ("tel", "Telefon*", "Telefon"),
        ],
        "submit": "Zamów teraz",
    },
    "3251": {
        "geo": "cz",
        "fields": [
            ("name", "Jméno Příjmení*", "Jméno Příjmení"),
            ("street-address", "Adresa*", "Adresa"),
            ("tel", "Telefon*", "Telefon"),
        ],
        "submit": "Objednat nyní",
    },
    "3702": {
        "geo": "sk",
        "fields": [
            ("name", "Meno Priezvisko*", "Meno Priezvisko"),
            ("street-address", "Adresa*", "Adresa"),
            ("tel", "Telefón*", "Telefón"),
        ],
        "submit": "Objednajte si teraz",
    },
}
