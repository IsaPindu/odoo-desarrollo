from odoo import api, fields, models, _
from odoo.exceptions import UserError

PY_DOCUMENT_TYPES = ("out_invoice", "out_refund")


class AccountMove(models.Model):
    _inherit = "account.move"

    l10n_py_authorization_id = fields.Many2one(
        "l10n.py.authorization", "Timbrado", copy=False,
        domain="[('document_type_id', '=', l10n_latam_document_type_id),"
               " ('company_id', '=', company_id), ('state', '=', 'valid')]",
        help="Timbrado de la SET que numera este documento.")
    l10n_py_number = fields.Char(
        "Número fiscal", copy=False, readonly=True,
        help="Número correlativo asignado dentro del timbrado.")
    l10n_py_full_number = fields.Char(
        "Documento", compute="_compute_l10n_py_full_number", store=True,
        help="Número completo en formato establecimiento-punto-número.")

    def _l10n_py_needs_number(self):
        self.ensure_one()
        return (
            self.country_code == "PY"
            and self.l10n_latam_use_documents
            and self.move_type in PY_DOCUMENT_TYPES
        )

    @api.depends("l10n_py_number", "l10n_py_authorization_id")
    def _compute_l10n_py_full_number(self):
        for move in self:
            auth = move.l10n_py_authorization_id
            if move.l10n_py_number and auth:
                move.l10n_py_full_number = "%s-%s-%s" % (
                    auth.establishment, auth.expedition_point, move.l10n_py_number)
            else:
                move.l10n_py_full_number = False

    def _post(self, soft=True):
        for move in self.filtered(lambda m: m._l10n_py_needs_number() and not m.l10n_py_number):
            if not move.l10n_py_authorization_id:
                raise UserError(_(
                    "Indique el timbrado antes de validar el documento «%s».", move.name))
            number = move.l10n_py_authorization_id._take_next_number()
            move.l10n_py_number = str(number).zfill(7)
        return super()._post(soft=soft)

    def write(self, vals):
        # El número fiscal es inmutable una vez asignado.
        if "l10n_py_number" in vals and not self.env.context.get("l10n_py_assign_number"):
            locked = self.filtered(lambda m: m.l10n_py_number and m.l10n_py_number != vals["l10n_py_number"])
            if locked:
                raise UserError(_("El número fiscal ya asignado no puede modificarse."))
        return super().write(vals)
