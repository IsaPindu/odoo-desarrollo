from odoo import models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _localization_use_documents(self):
        self.ensure_one()
        return self.country_id.code == "PY" or super()._localization_use_documents()
