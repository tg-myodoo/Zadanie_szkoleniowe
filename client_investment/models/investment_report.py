from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InvestmentReport(models.Model):
    # Wiem, że Odoo robi '.' jako spację, ale dla mnie to pojebane jest, bo Pythonowo powinno się oddzielać '_'.
    # Rób jak chcesz, natomaist ja preferuję _ i z tego co kojarzę to u Nas wszyscy dają _ zamiast .
    _name = 'investment_report'
    _description = 'Investment Report'

    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        """Constrain method for not letting users to choose end date before start date.

        :return: ValidationError.
        """
        # Bardzo szanuję, że pomyślałeś o tym aby nie pierdolnąć zlego przedziału dat.
        # Masz plusa, bo ja o tym zapomniałem w periodic_invoice_report xD
        # Aczkolwiek lepiej by to było zrobić w constrain.
        for report in self:
            if report.start_date > report.end_date:
                raise ValidationError('End date cannot be set before start date.')

    @api.depends('partner_id', 'start_date', 'end_date')
    def _get_investment_list(self):
        """Compute method for obtaining all investments of selected client from given date period.

        :return: Investments.
        """
        for report in self:
            # inwestor.id było źle i nie mam pojęcia jakim cudem Ci to przeszło.
            # Nie możesz dawać relacji w tej pierwszej części, jedynie w trzeciej.

            # Nie przypisuję domyślnej wartości dla report.investment_ids,
            # ponieważ ta lista może być pusta i nie będzie to błędem.
            report.investment_ids = self.env['sale.order'].search([
                ('investor_id', '=', report.partner_id.id),
                ('state', 'in', ['sale', 'done']),
                ('date_order', '>=', report.start_date),
                ('date_order', '<=', report.end_date)
            ])

    @api.depends('investment_ids')
    def _compute_amount(self):
        """Compute method for calculating both untaxed and taxed amount of

        :return: Investment amounts.
        """
        for report in self:
            for investment in report.investment_ids:
                report.amount_untaxed += investment.amount_untaxed
                report.amount_total += investment.amount_total

    # Wyjebałem currency ID, ponieważ to będzie działać tylko w przypadku kiedy każde SO miałoby tę samą walutę.
    # Co jeżeli będą różne? W raporcie możesz walutę wyświetlić w inny sposób.

    # Chciałeś do pola przechowującego jedną daną wprowadzić wiele danych. Nunu.

    # Podatku nie musiałeś dawać≥ Nigdy nie rób więcej niż Ci każą robić, bo potem każdy będzie oczekiwał,
    # że zawsze zrobisz więcej niż trzeba. Poza tym czas to pieniądz, klient może się wkurwić,
    # że ma płacić za coś o co nie prosił.
    name = fields.Char(string='Name', help='Name of this report.')
    partner_id = fields.Many2one('res.partner', string='Investor', required=True,
                                 help='Investor chosen for this report.')
    start_date = fields.Date(string='Start Date', required=True, help='Start date of this report.')
    end_date = fields.Date(string='End Date', required=True, help='End date of this report.')
    investment_ids = fields.One2many('sale.order', 'investor_id', string='Investments', compute='_get_investment_list',
                                     help='List of investments of selected client from given date period.')

    # Oba pola mogę ogarnąć jednym compute i to wciąż nadal będzie czytelne, więc tak robię.
    amount_untaxed = fields.Float(string='Amount Untaxed', default=0.0, compute='_compute_amount',
                                  help='Untaxed amount of every investment in this report.')
    amount_total = fields.Float(string='Amount Total', default=0.0, compute='_compute_amount',
                                help='Total amount of every investment in this report.')
