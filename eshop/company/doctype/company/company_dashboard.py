from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'company',
		'transactions': [
			{
				'label': 'Product',
				'items': ['Product', 'Product Movement']
			},
			{
				'label': 'Orders',
				'items': ['Sales Invoice', 'Purchase Invoice']
			},
			{
				'label': '',
				'items': []
			}
		]
	}