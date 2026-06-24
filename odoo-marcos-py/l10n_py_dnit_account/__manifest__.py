{
    "name": "Paraguay - Documentos y Timbrado",
    "summary": "Tipos de documento de la SET, timbrado y numeración fiscal de facturas",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "author": "Marcos Vallejos <vallejosmarcos.py@gmail.com>",
    "website": "https://github.com/VallejosMarcos/l10n-paraguay",
    "license": "LGPL-3",
    "countries": ["py"],
    "depends": [
        "l10n_py_dnit",
        "l10n_py_dnit_base",
        "l10n_latam_invoice_document",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/l10n_latam_document_type_data.xml",
        "views/l10n_py_authorization_views.xml",
        "views/account_journal_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
