from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    inwestycje = fields.One2many(
        comodel_name = 'sale.order',
        inverse_name = 'inwestor',
        domain = [('state', 'in', ['sale','done'])],
        readonly = True
    )

    suma_inwestycji_netto = fields.Float(
        string = 'Suma inwestycji netto',
        compute = '_sumuj_inwestycje_netto'
    )

    suma_inwestycji_brutto = fields.Float(
        string = 'Suma inwestycji brutto',
        compute = '_sumuj_inwestycje_brutto'
    )

    def _sumuj_inwestycje_netto(self):
        """
        Metoda ta zebiera wszystkie inwestycje danego partnera, zsumuje ich wartość netto i wstawia otrzymaną wartość do pola

        return: suma inwestycji
        """

        # tax_totals_json

        temp_suma_inwestycji_netto = 0

        for inwestycja in self.inwestycje:
            temp_suma_inwestycji_netto += inwestycja.amount_untaxed

        self.suma_inwestycji_netto = temp_suma_inwestycji_netto


    def _sumuj_inwestycje_brutto(self):
        """
        Metoda ta zebiera wszystkie inwestycje danego partnera, zsumuje ich wartość brutto i wstawia otrzymaną wartość do pola

        return: suma inwestycji brutto
        """

        # tax_totals_json

        temp_suma_inwestycji_brutto = 0

        for inwestycja in self.inwestycje:
            temp_suma_inwestycji_brutto += inwestycja.amount_total

        self.suma_inwestycji_brutto = temp_suma_inwestycji_brutto