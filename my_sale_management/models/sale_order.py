from odoo import models, fields, api

from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    inwestor = fields.Many2one(comodel_name='res.partner')

    @api.constrains('partner_id', 'inwestor')
    def _check_investor(self):
        for record in self:
            if record.partner_id == record.inwestor:
                raise ValidationError("Fields Customer and Investor must be different")
