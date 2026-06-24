"""
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

from . import ruc


class ResPartner(models.Model):
    _inherit = "res.partner"

    l10n_py_ruc_dv = fields.Char(
        string="Dígito verificador",
        compute="_compute_l10n_py_ruc_dv",
        help="Dígito verificador calculado para el número de RUC.",
    )

    def _is_py_ruc(self):
"""
"""True si el contribuyente está identificado con RUC paraguayo.
"""
"""
        self.ensure_one()
        ruc_type = self.env.ref("l10n_py_dnit_base.it_ruc", raise_if_not_found=False)
        return ruc_type and self.l10n_latam_identification_type_id == ruc_type

    @api.depends("vat", "l10n_latam_identification_type_id")
    def _compute_l10n_py_ruc_dv(self):
        for partner in self:
            if partner.vat and partner._is_py_ruc():
                number, _dv = ruc.split(partner.vat)
                partner.l10n_py_ruc_dv = str(ruc.check_digit(number)) if number else False
            else:
                partner.l10n_py_ruc_dv = False

    @api.constrains("vat", "l10n_latam_identification_type_id")
    def _check_l10n_py_ruc(self):
        for partner in self:
            if partner.vat and partner._is_py_ruc() and not ruc.is_valid(partner.vat):
                number, _dv = ruc.split(partner.vat)
                raise ValidationError(_(
                    "El RUC «%(ruc)s» no es válido. El dígito verificador "
                    "debería ser %(dv)s.",
                    ruc=partner.vat,
                    dv=ruc.check_digit(number) if number else "?",
                ))
        
"""
# Correcciones para que no guarde el - como parate del ruc#
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from . import ruc


class ResPartner(models.Model):
    _inherit = "res.partner"

    l10n_py_ruc_dv = fields.Char(
        string="Dígito verificador",
        compute="_compute_l10n_py_ruc_dv",
        store=True,  # Persistencia física en PostgreSQL para evitar recálculos en la vista
        help="Dígito verificador calculado para el número de RUC.",
    )

    def _is_py_ruc(self):
        """True si el contribuyente está identificado con RUC paraguayo."""
        self.ensure_one()
        ruc_type = self.env.ref("l10n_py_dnit_base.it_ruc", raise_if_not_found=False)
        return ruc_type and self.l10n_latam_identification_type_id == ruc_type

    @api.depends("vat", "l10n_latam_identification_type_id")
    def _compute_l10n_py_ruc_dv(self):
        """Calcula el DV oficial basándose puramente en la raíz numérica limpia."""
        for partner in self:
            if partner.vat and partner._is_py_ruc():
                # Aislamos el número base eliminando guiones o residuos visuales
                base_number = partner.vat.split("-")[0].strip()
                base_clean = "".join(filter(str.isdigit, base_number))
                if base_clean:
                    partner.l10n_py_ruc_dv = str(ruc.check_digit(base_clean))
                else:
                    partner.l10n_py_ruc_dv = False
            else:
                partner.l10n_py_ruc_dv = False

    @api.constrains("vat", "l10n_latam_identification_type_id")
    def _check_vat(self, *args, **kwargs):
        """Bypass del validador internacional de Odoo corporativo para el RUC local.
        Soporta argumentos variables (*args, **kwargs) para evitar errores de tipo RPC.
        """
        # Filtramos los registros que correspondan a RUC de Paraguay para darles inmunidad
        py_ruc_partners = self.filtered(lambda p: p.vat and p._is_py_ruc())
        other_partners = self - py_ruc_partners
        
        # El validador nativo de Odoo corporativo solo procesará las identificaciones no paraguayas
        if other_partners:
            super(ResPartner, other_partners)._check_vat(*args, **kwargs)

        # Validamos estrictamente que la matemática de la DNIT sea coherente
        for partner in py_ruc_partners:
            base_number = partner.vat.split("-")[0].strip()
            base_clean = "".join(filter(str.isdigit, base_number))
            if not base_clean:
                continue
            expected_dv = str(ruc.check_digit(base_clean))
            if partner.l10n_py_ruc_dv != expected_dv:
                raise ValidationError(_("Error DNIT: El número de RUC no coincide con el dígito verificador matemático."))