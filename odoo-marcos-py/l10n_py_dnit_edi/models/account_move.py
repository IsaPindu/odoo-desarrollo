from odoo import fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    l10n_py_edi_state = fields.Selection(
        [("to_send", "Por enviar"),
         ("sent", "Enviado"),
         ("accepted", "Aprobado"),
         ("rejected", "Rechazado")],
        string="Estado SIFEN", copy=False, readonly=True, tracking=True,
        help="Estado del documento electrónico ante la DNIT (SIFEN).")
    l10n_py_edi_cdc = fields.Char(
        "CDC", copy=False, readonly=True, size=44,
        help="Código de Control (44 dígitos) del documento electrónico.")

    def action_l10n_py_edi_send(self):
        """Punto de extensión para el envío a SIFEN.

        La generación del XML, la firma digital y el envío a la DNIT no están
        implementados en este módulo: dependen del certificado del
        contribuyente y de la librería de firma. Un módulo connector debe
        sobrescribir este método.
        """
        raise UserError(_(
            "El envío a SIFEN todavía no está implementado. Este módulo provee "
            "la estructura (estado, CDC) sobre la cual construir el conector de "
            "firma y envío a la DNIT."))
