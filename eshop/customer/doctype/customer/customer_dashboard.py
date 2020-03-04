from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'customer',
		'transactions': [
			{
                'label': "Invoice",
				'items': ['Sales Invoice']
			}
		]
	}