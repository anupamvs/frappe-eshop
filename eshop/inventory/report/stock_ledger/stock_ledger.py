# Copyright (c) 2013, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	data = frappe.db.get_list('SL Entry',
	fields=['date','time','company', 'product','inventory','quantity','balance','voucher_type', 'voucher_reference'],
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
			"label": "Company",
			"fieldname": "company",
			"fieldtype": "Link",
			"options": "Company",
			"width": 100
		},
		{
			"label": "Product",
			"fieldname": "product",
			"fieldtype": "Link",
			"options": "Product",
			"width": 200
		},
		{
			"label": "Inventory",
			"fieldname": "inventory",
			"fieldtype": "Link",
			"options": "Location",
			"width": 100
		},
		{
			"label": "Quantity",
			"fieldname": "quantity",
			"fieldtype": "Float",
			"width": 70
		},
		{
			"label": "Balance",
			"fieldname": "balance",
			"fieldtype": "Float",
			"width": 70
		},
		{
			"label": "Voucher Type",
			"fieldname": "voucher_type",
			"width": 120
		},
		{
			"label": "Voucher Ref",
			"fieldname": "voucher_reference",
			"fieldtype": "Dynamic Link",
			"options": "voucher_type",
			"width": 180
		}
	]
	return columns, data
