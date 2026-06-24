{
    "name": "Paraguay - EDI (SIFEN) [scaffold]",
    "summary": "Estructura base para la facturación electrónica SIFEN / e-Kuatiá",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "author": "Marcos Vallejos <vallejosmarcos.py@gmail.com>",
    "website": "https://github.com/VallejosMarcos/l10n-paraguay",
    "license": "LGPL-3",
    "countries": ["py"],
    "depends": ["l10n_py_dnit_account"],
    "data": [
        "views/account_move_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    # Aviso: este módulo es el punto de extensión para SIFEN. NO incluye la
    # firma digital, los esquemas XSD ni el envío a la DNIT (requieren
    # certificado y la librería de firma). Ver README.
}
