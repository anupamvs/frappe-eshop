# Copyright (c) 2013, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
def execute(filters=None):
	data = frappe.db.get_list('GL Entry',
	fields=['date', 'account', 'debit_amt', 'credit_amt', 'voucher_type', 'voucher_referance', 'against', 'party_type', 'party'],
    order_by='date desc',
    as_list=True
	)
	columns = [
		{
			"label": _("Date"),
			"fieldname": "date",
			"fieldtype": "Date",
			"width": 90
		},
		{
			"label": _("Account"),
			"fieldname": "account",
			"fieldtype": "Link",
			"options": "Account",
			"width": 180
		},
		{
			"label": _("Debit"),
			"fieldname": "debit_amt",
			"fieldtype": "Float",
			"width": 100
		},
		{
			"label": _("Credit"),
			"fieldname": "credit_amt",
			"fieldtype": "Float",
			"width": 100
		},
		{
			"label": _("Voucher Type"),
			"fieldname": "voucher_type",
			"width": 120
		},
		{
			"label": _("Voucher Ref"),
			"fieldname": "voucher_referance",
			"fieldtype": "Dynamic Link",
			"options": "voucher_type",
			"width": 180
		},
		{
			"label": _("Against Account"),
			"fieldname": "against",
			"width": 120
		},
		{
			"label": _("Party Type"),
			"fieldname": "party_type",
			"width": 100
		},
		{
			"label": _("Party"),
			"fieldname": "party",
			"fieldtype": "Dynamic Link",
			"options": "party_type",
			"width": 100
		}
	]
	return columns, data
