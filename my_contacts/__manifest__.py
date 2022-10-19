{
	'name': 'My Contacts',
	'summary': 'My modified module Contacts',
	'author': 'myOdoo.pl',
	'website': 'https://myodoo.pl',
	'category': 'Sales/CRM',
	'version': '[V15] 0.1',
	'depends': [
		'base',
		'mail',
		'contacts',
		'my_sale_management'
	],
	'data': [
		'report/investor_report_template.xml',
		'report/investor_report_caller.xml',
		'security/ir.model.access.csv',
		'views/res_partner_view.xml',
		'views/investor_report_view.xml'
	],
	'application': True,
	'installable': True,
	'auto_install': False
}
