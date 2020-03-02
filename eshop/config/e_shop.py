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
				{
					"type": "doctype",
					"name": "Supplier"
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
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype":"Product Movement",
					"onboard": 1,
					"name": "Stock Ledger",
				}
			]
		},
		{
			"label": _("Accounts"),
			"items": [
				{
					"type": "doctype",
					"name": "Account"
				},
				{
					"type": "doctype",
					"name": "Account",
					"icon": "fa fa-sitemap",
					"label": _("Account Tree"),
					"link": "Tree/Account",
					"onboard": 1,
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype":"GL Entry",
					"onboard": 1,
					"name": "General Ledger",
				}
			]
		},
		{
			"label": _("Company"),
			"items": [
				{
					"type": "doctype",
					"name": "Company"
				}
			]
		}
	]
