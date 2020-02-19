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
					"description": _("Braintree"),
				},
				{
					"type": "doctype",
					"name": "Product Category",
					"description": _("PayPal payment gateway settings"),
				}
			]
		},
		{
			"label": _("Customer"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Enter keys to enable login via Facebook, Google, GitHub."),
				},
				{
					"type": "doctype",
					"name": "Customer Type",
					"description": _("Ldap settings"),
				},
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("Register OAuth Client App"),
				},
				{
					"type": "doctype",
					"name": "Purchase Invoice",
					"description": _("Settings for OAuth Provider"),
				},
			]
		},
		{
			"label": _("Inventory"),
			"items": [
				{
					"type": "doctype",
					"name": "Product Movement",
					"description": _("Webhooks calling API requests into web apps"),
				},
				{
					"type": "doctype",
					"name": "Location",
					"description": _("Slack Webhooks for internal integration"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype":"Basket",
					"onboard": 1,
					"name": "Product Balance",
					"description": _("Slack Webhooks for internal integration"),
				}
			]
		},
		{
			"label": _("Accounts"),
			"items": [
				
			]
		},
		{
			"label": _("Company"),
			"items": [
				
			]
		}
	]
