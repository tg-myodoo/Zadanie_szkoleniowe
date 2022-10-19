{
	'name': 'My Sale',
	'summary': 'My modified module Sale',
	'author': 'myOdoo.pl',
	'website': 'https://myodoo.pl',
	'category': 'Accounting',
	'version': '[V15] 0.1',
	'depends': [
		'base',
		'sale',
		'sale_management'
	],
	'data': [
		'views/sale_order_view.xml'
	],
	'application': True,
	'installable': True,
	'auto_install': False
}
