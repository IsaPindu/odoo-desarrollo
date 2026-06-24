from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    """Plan de cuentas paraguayo basado en el Modelo de Estados Financieros
    de la DNIT.

    El árbol de cuentas, grupos e impuestos vive en los CSV de
    ``data/template/`` (el framework los carga solo). Acá quedan los
    datos que el CSV no puede expresar: metadatos del plan y las cuentas
    por defecto de la compañía (cliente, IVA, diferencia de cambio).
    """

    _inherit = "account.chart.template"

    @template("py_dnit")
    def _get_py_dnit_template_data(self):
        return {
            "name": _("Paraguay - Plan de Cuentas DNIT"),
            "code_digits": "10",
            "currency_id": "base.PYG",
            "country_id": "base.py",
            "bank_account_code_prefix": "1-01-01-03",
            "cash_account_code_prefix": "1-01-01-01",
            "transfer_account_code_prefix": "1-01-01-02",
        }

    @template("py_dnit", "res.company")
    def _get_py_dnit_res_company(self):
        return {
            self.env.company.id: {
                "account_fiscal_country_id": "base.py",
                "bank_account_code_prefix": "1-01-01-03",
                "cash_account_code_prefix": "1-01-01-01",
                "transfer_account_code_prefix": "1-01-01-02",
                "account_default_pos_receivable_account_id": "dnit_1010301",
                "account_sale_tax_id": "dnit_tax_iva_10_venta",
                "account_purchase_tax_id": "dnit_tax_iva_10_compra",
                "income_currency_exchange_account_id": "dnit_31003",
                "expense_currency_exchange_account_id": "dnit_414",
            },
        }
