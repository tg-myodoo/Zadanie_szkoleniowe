# Miałeś robić osobne grupy dostępu? Nie, więc po co? A zrobiłeś je źle, bo powinieneś wtedy utworzyć nowe rekordy
# rup dostępu poprzez pliki xml.
# Kiedyś się nauczyć to robić, ale na razie nie interesuj się tym, bo trochę pojebane to jest, a niby proste.

{
	'name': 'Client Investment',
	'summary': 'Module for handling investors and investments.',
	'author': 'myOdoo.pl',
	'website': 'https://myodoo.pl',
	'category': 'Sales',
	'version': '[V15] 0.4',
	'depends': [
		'base',
		'contacts',
		'sale',
		'sale_management'
	],
	'data': [
		'report/investment_report_template.xml',
		'report/investment_report_caller.xml',

		'security/ir.model.access.csv',

		'views/investment_report_view.xml',
		'views/res_partner_view.xml',
		'views/sale_order_view.xml'
	],
	'application': True,
	'installable': True,
	'auto_install': False
}
