# -*- coding: utf-8 -*-
# Copyright (c) 2020, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SalesInvoice(Document):
	
	def on_submit(self):
		self.make_gl_entries()
		self.make_product_movement()

	def make_gl_entries(self):
		gl_entries = []
		self.make_customer_gl_entry(gl_entries)
		self.make_taxes_gl_entry(gl_entries)
		self.make_sales_gl_entry(gl_entries)
		if self.is_paid :
			self.make_bank_gl_entry(gl_entries)
	
		for gl_entry in gl_entries:
			gl_entry.update({"doctype": "GL Entry"})
			gl = frappe.get_doc(gl_entry)
			gl.insert()
	
	def make_customer_gl_entry(self, gl_entries):
		company = frappe.get_doc('Company', self.company)
		credit_amt = self.grand_total if self.is_paid else 0
		gl_entries.append(self.gl_meta({
			'account': company.default_debtor,
			'against': company.default_sales,
			'debit_amt' : self.grand_total,
			'credit_amt' :credit_amt,
			'party_type' : 'Customer',
			'party' : self.customer
		}))
	
	def make_taxes_gl_entry(self, gl_entries):
		company = frappe.get_doc('Company', self.company)
		gl_entries.append(self.gl_meta({
			'account': company.default_taxes,
			'credit_amt': self.total_taxes_and_charges,
			'against' : self.customer,
		}))

	def make_sales_gl_entry(self, gl_entries):
		company = frappe.get_doc('Company', self.company)
		gl_entries.append(self.gl_meta({
			'account': company.default_sales,
			'credit_amt' : self.net_total,
			'against' : self.customer,
		}))

	def make_bank_gl_entry(self, gl_entries):
		company = frappe.get_doc('Company', self.company)
		gl_entries.append(self.gl_meta({
			'account': company.default_bank,
			'debit_amt' : self.grand_total,
			'against' : self.customer,
		}))

	def gl_meta(self, gl_entry):
		gl_entry_dic = frappe._dict({
			'company' : self.company,
			'account' : None,
			'debit_amt' : 0,
			'credit_amt' : 0,
			'voucher_type' : self.doctype,
			'voucher_referance' : self.name,
			'against' : None,
			'party_type' : None,
			'party' : None,
			'date' : self.date,
			'time' :self.time
		})
		return gl_entry_dic.update(gl_entry)

	def make_product_movement(self):
		items = []
		for item in self.product_list:
			items.append({
				"product": item.product,
				"quantity": item.quantity
			})
		movement = frappe._dict({
			'doctype' : 'Product Movement',
			'company' : self.company,
			'date' : self.date,
			'time' : self.time,
			'from_location': self.source_inventory,
			'voucher_type' : self.doctype,
			'voucher_referece' : self.name,
			'docstatus' : 1,
			'items': items
		})
		movement = frappe.get_doc(movement)
		movement.insert()