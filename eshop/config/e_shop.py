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
					"name": "Add Product",
					"description": _("Webhooks calling API requests into web apps"),
				},
				{
					"type": "doctype",
					"name": "Location",
					"description": _("Slack Webhooks for internal integration"),
				},
				{
					"type": "report",
					"name": "Product Balance",
					"description": _("Slack Webhooks for internal integration"),
				}
			]
		},
		{
			"label": _("Accounts"),
			"items": [
				{
					"type": "doctype",
					"name": "Google Settings",
					"description": _("Google API Settings."),
				},
				{
					"type": "doctype",
					"name": "Google Contacts",
					"description": _("Google Contacts Integration."),
				},
				{
					"type": "doctype",
					"name": "Google Calendar",
					"description": _("Google Calendar Integration."),
				},
				{
					"type": "doctype",
					"name": "Google Drive",
					"description": _("Google Drive Integration."),
				}
			]
		},
		{
			"label": _("Company"),
			"items": [
				{
					"type": "doctype",
					"name": "Google Settings",
					"description": _("Google API Settings."),
				},
				{
					"type": "doctype",
					"name": "Google Contacts",
					"description": _("Google Contacts Integration."),
				},
				{
					"type": "doctype",
					"name": "Google Calendar",
					"description": _("Google Calendar Integration."),
				},
				{
					"type": "doctype",
					"name": "Google Drive",
					"description": _("Google Drive Integration."),
				}
			]
		}
	]
