from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Product"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Product",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Product Category",
					"label": "Product Category",
					"link": "Tree/Product Category",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Purchase Invoice"
				},
			]
		},
		{
			"label": _("Customer"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Customer Type",
				},
				{
					"type": "doctype",
					"name": "Sales Invoice",
				},
			]
		},
		{
			"label": _("Inventory"),
			"items": [
				{
					"type": "doctype",
					"name": "Product Movement",
				},
				{
					"type": "doctype",
					"name": "Location",
					"onboard": 1,
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype":"Basket",
					"onboard": 1,
					"name": "Product Balance",
				}
			]
		},
		{
			"label": _("Accounts"),
			"items": [
				{
					"type": "doctype",
					"name": "Account"
				}
			]
		},
		{
			"label": _("Company"),
			"items": [
				
			]
		}
	]
