from odoo import models, fields, api

from odoo.exceptions import ValidationError

class InvestorReport(models.Model):
    _name = 'investor.report'
    _description = 'Investor Report'

    name = fields.Char(string='Name', help='Name of this report.')

    partner = fields.Many2one(
        comodel_name = 'res.partner', 
        string = 'Partner', 
        required = True
    )

    start_date = fields.Date(string='Start Date', required=True)

    end_date = fields.Date(string='End Date', required=True)

    investments = fields.One2many(
        comodel_name = 'sale.order',
        compute = '_compute_investments'
    )

    currency_id = fields.Many2one(
        comodel_name = 'res.currency',
        related = 'investments.currency_id'
    )

    net_sum = fields.Float(
        string = 'Total untaxed',
        compute = '_calculate_net_sum'
    )

    tax_sum = fields.Float(
        string = 'Total tax',
        compute = '_calculate_tax_sum'
    )

    gross_sum = fields.Float(
        string = 'Total taxed',
        compute = '_calculate_gross_sum'
    )

    @api.onchange('partner','start_date','end_date')
    def _compute_investments(self):
        """
            Compute method for selected partner within selected dates.
        """

        if self.start_date > self.end_date:
            raise ValidationError("End Date cannot be set before Start Date.")

        self.investments = self.env['sale.order'].search([
            ('inwestor.id', '=', self.partner.id),
            ('state', 'in', ['sale','done']),
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date)])


    def _calculate_net_sum(self):
        """
            Calculate total untaxed (net)
        """

        temp_net_sum = 0

        for investment in self.investments:
            temp_net_sum += investment.amount_untaxed

        self.net_sum = temp_net_sum


    def _calculate_tax_sum(self):
        """
            Calculate total tax
        """

        temp_tax_sum = 0

        for investment in self.investments:
            temp_tax_sum += investment.amount_tax

        self.tax_sum = temp_tax_sum


    def _calculate_gross_sum(self):
        """
            Calculate total taxed (gross)
        """

        temp_gross_sum = 0
        
        for investment in self.investments:
            temp_gross_sum += investment.amount_total

        self.gross_sum = temp_gross_sum
