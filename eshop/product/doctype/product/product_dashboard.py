from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'product',
		'transactions': [
			{
                'label': "Invoice",
				'items': ['Purchase Invoice', 'Sales Invoice']
			},
            {
                'label': "Inventory",
				'items': ['Product Movement', 'Basket']
			},
		]
	}