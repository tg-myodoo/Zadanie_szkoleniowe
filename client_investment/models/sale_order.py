from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.constrains('partner_id', 'investor_id')
    def _check_investor(self):
        """Constrain method for not letting users to choose the same partner and investor in same SO.

        :return: ValidationError.
        """
        for sale in self:
            if sale.partner_id == sale.investor_id:
                raise ValidationError("Fields Customer and Investor must be different")

    # Pierwszy szczegół, pola relacyjne Many2one powinno się kończyć "_id".
    # Nie jest to błąd, po prostu taka szkoła pisania w Odoo.

    # Zawsze dodajemy atrybut "help". Jest on nie tylko dla użytkownika (wyświelta się po najechaniu kursorem na pole),
    # ale też dla Nas, żebyśmy spojrzeli na zadeklarowane pole i mieli mniej więcej info o chuj z nim chodzi.
    investor_id = fields.Many2one('res.partner', string='Investor', help='Investor for this sale order.')
