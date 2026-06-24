from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    l10n_py_establishment = fields.Char(
        "Establecimiento", size=3,
        help="Código de establecimiento (3 dígitos) para los documentos timbrados.")
    l10n_py_expedition_point = fields.Char(
        "Punto de expedición", size=3,
        help="Punto de expedición (3 dígitos) para los documentos timbrados.")
