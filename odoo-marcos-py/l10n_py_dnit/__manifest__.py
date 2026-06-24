{
    "name": "Paraguay - Plan de Cuentas DNIT",
    "summary": "Plan de cuentas paraguayo según el Modelo de Estados Financieros de la DNIT",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations/Account Charts",
    "author": "Marcos Vallejos <vallejosmarcos.py@gmail.com>",
    "website": "https://github.com/VallejosMarcos/l10n_py_dnit",
    "license": "LGPL-3",
    "countries": ["py"],
    "depends": ["account"],
    # El plan, impuestos y posiciones fiscales se cargan vía los decoradores
    # @template('py_dnit') desde los CSV de data/template/. No hace falta data:.
    "data": [],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
