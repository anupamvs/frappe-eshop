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
			"label": _("Accounts"),
			"items": [
				{
					"type": "doctype",
					"name": "Social Login Key",
					"description": _("Enter keys to enable login via Facebook, Google, GitHub."),
				},
				{
					"type": "doctype",
					"name": "LDAP Settings",
					"description": _("Ldap settings"),
				},
				{
					"type": "doctype",
					"name": "OAuth Client",
					"description": _("Register OAuth Client App"),
				},
				{
					"type": "doctype",
					"name": "OAuth Provider Settings",
					"description": _("Settings for OAuth Provider"),
				},
			]
		},
		{
			"label": _("Stock"),
			"items": [
				{
					"type": "doctype",
					"name": "Webhook",
					"description": _("Webhooks calling API requests into web apps"),
				},
				{
					"type": "doctype",
					"name": "Slack Webhook URL",
					"description": _("Slack Webhooks for internal integration"),
				},
			]
		},
		{
			"label": _("Customer"),
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
