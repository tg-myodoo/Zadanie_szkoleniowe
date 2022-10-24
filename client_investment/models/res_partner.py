from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    # Metody compute, onchange i constrain zawsze dajemy nad deklaracją pól.
    # Metody create, write, unlink (delete) zawsze są na samym dole.
    @api.depends('investment_ids')
    def _sum_investment_amount(self):
        """Compute method for obtaining summary of both taxed and untaxed amounts of client investments.

        :return: Investment amounts.
        """
        # Btw w zadaniu była mowa tylko o sumie netto, ale dobra, zróbmy też brutto xD
        # Iteruję po każdym rekordzie modelu res.partner.
        for partner in self:
            # Przypisuję zera do zmiennych. Robi się to po to,
            # żeby metoda compute nie wywalała błędu w przypadku kiedy nie będzie mogła nic wyliczyć.
            # Można dać w deklaracji pola default=0.
            partner.investment_untaxed_sum, partner.investment_total_sum = 0, 0

            # Pierw sprawdzam, czy klient w ogóle ma inwestycje.
            if partner.investment_ids:
                # Zwróć uwagę, że jedną metodą załatwiam oba pola. Można tak zrobić,
                # aczkolwiek trzeba uważać, by to dalej było czytelne.
                for investment in partner.investment_ids:
                    partner.investment_untaxed_sum += investment.amount_untaxed
                    partner.investment_total_sum += investment.amount_total

    # Pola relacyjne On2many powinno się kończyć "_ids".
    investment_ids = fields.One2many('sale.order', 'investor_id', string='Investments', readonly=True,
                                     domain=[('state', 'in', ['sale', 'done'])],
                                     help='List of investments for this partner.')
    # Pole compute domyślnie ma atrybut readonly=True, oraz store=False. Poczytaj w wolnej chiwli o atrybucie store.
    investment_untaxed_sum = fields.Float(string='Investment Untaxed Sum', compute='_sum_investment_amount',
                                          help='Sum of this partner investments untaxed amount.')
    investment_total_sum = fields.Float(string='Investment Total Sum', compute='_sum_investment_amount',
                                        help='Sum of this partner investments total amount.')
