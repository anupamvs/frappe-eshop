# Copyright (c) 2013, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
def execute(filters=None):
	data = frappe.db.get_list('GL Entry',
	fields=['date', 'time', 'account', 'debit_amt', 'credit_amt', 'voucher_type', 'voucher_referance', 'against', 'party_type', 'party'],
    order_by='date,time desc',
    as_list=True
	)
	columns = [
		{
			"label": "Date",
			"fieldname": "date",
			"fieldtype": "Date",
			"width": 90
		},
		{
			"label": "Time",
			"fieldname": "time",
			"fieldtype": "Time",
			"width": 90
		},
		{
			"label": "Account",
			"fieldname": "account",
			"fieldtype": "Link",
			"options": "Account",
			"width": 180
		},
		{
			"label": "Debit",
			"fieldname": "debit_amt",
			"fieldtype": "Float",
			"width": 100
		},
		{
			"label": "Credit",
			"fieldname": "credit_amt",
			"fieldtype": "Float",
			"width": 100
		},
		{
			"label": "Voucher Type",
			"fieldname": "voucher_type",
			"width": 120
		},
		{
			"label": "Voucher Ref",
			"fieldname": "voucher_referance",
			"fieldtype": "Dynamic Link",
			"options": "voucher_type",
			"width": 180
		},
		{
			"label": "Against Account",
			"fieldname": "against",
			"width": 120
		},
		{
			"label": "Party Type",
			"fieldname": "party_type",
			"width": 100
		},
		{
			"label": "Party",
			"fieldname": "party",
			"fieldtype": "Dynamic Link",
			"options": "party_type",
			"width": 100
		}
	]
	return columns, data
