from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class L10nPyAuthorization(models.Model):
    """Timbrado de la SET: autoriza un rango de numeración para un tipo de
    documento, en un establecimiento y punto de expedición, durante un período.
    """
    _name = "l10n.py.authorization"
    _description = "Timbrado"
    _order = "date_to desc, name"

    name = fields.Char("Timbrado", size=8, required=True, help="Número de timbrado de la SET (8 dígitos).")
    document_type_id = fields.Many2one(
        "l10n_latam.document.type", "Tipo de documento", required=True,
        domain="[('country_id.code', '=', 'PY')]")
    establishment = fields.Char("Establecimiento", size=3, required=True, default="001")
    expedition_point = fields.Char("Punto de expedición", size=3, required=True, default="001")
    date_from = fields.Date("Vigente desde", required=True)
    date_to = fields.Date("Vigente hasta", required=True)
    number_from = fields.Integer("Desde número", required=True, default=1)
    number_to = fields.Integer("Hasta número", required=True, default=9999999)
    sequence_number_next = fields.Integer(
        "Próximo número", default=1,
        help="Siguiente número correlativo que se asignará dentro del rango.")
    company_id = fields.Many2one("res.company", "Compañía", required=True,
                                 default=lambda self: self.env.company)
    #state = fields.Selection(
    #    [("future", "Por iniciar"), ("valid", "Vigente"), ("expired", "Vencido")],
    #    compute="_compute_state", string="Estado")
    state = fields.Selection(
        [("future", "Por iniciar"), ("valid", "Vigente"), ("expired", "Vencido")],
        compute="_compute_state", string="Estado", store=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("unique_authorization",
         "unique(name, establishment, expedition_point, document_type_id, company_id)",
         "Ya existe un timbrado con ese número, establecimiento, punto y tipo de documento."),
    ]

    @api.depends("date_from", "date_to")
    def _compute_state(self):
        today = fields.Date.context_today(self)
        for auth in self:
            if auth.date_from and today < auth.date_from:
                auth.state = "future"
            elif auth.date_to and today > auth.date_to:
                auth.state = "expired"
            else:
                auth.state = "valid"

    @api.constrains("number_from", "number_to", "date_from", "date_to")
    def _check_ranges(self):
        for auth in self:
            if auth.number_from > auth.number_to:
                raise ValidationError(_("El número inicial no puede ser mayor que el final."))
            if auth.date_from > auth.date_to:
                raise ValidationError(_("La fecha de inicio no puede ser posterior a la de fin."))

    @api.onchange("number_from")
    def _onchange_number_from(self):
        if self.number_from and self.sequence_number_next < self.number_from:
            self.sequence_number_next = self.number_from

    def _take_next_number(self):
        """Reserva y devuelve el próximo número correlativo, serializando el
        acceso con un bloqueo de fila para evitar duplicados concurrentes."""
        self.ensure_one()
        self.env.cr.execute(
            "SELECT sequence_number_next FROM l10n_py_authorization WHERE id = %s FOR UPDATE",
            [self.id])
        current = self.env.cr.fetchone()[0] or self.number_from
        if current > self.number_to:
            raise UserError(_(
                "El timbrado %s agotó su rango de numeración (%s-%s).",
                self.name, self.number_from, self.number_to))
        self.env.cr.execute(
            "UPDATE l10n_py_authorization SET sequence_number_next = %s WHERE id = %s",
            [current + 1, self.id])
        self.invalidate_recordset(["sequence_number_next"])
        return current
