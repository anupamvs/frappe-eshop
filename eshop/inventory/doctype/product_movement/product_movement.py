# -*- coding: utf-8 -*-
# Copyright (c) 2020, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from eshop.inventory.doctype.basket.basket import get_basket

class ProductMovement(Document):
	def validate(self):
		if not self.from_location and not self.to_location:
			frappe.throw("Select atleast one location(From, TO)")
		print(self.__dict__)

	def on_submit(self):
		if self.from_location and self.to_location:
			self.transfer_product()
		elif self.from_location:
			self.remove_product_from_location()
		elif self.to_location:
			self.add_product_to_location()
	
	def add_product_to_location(self):
		sl_entries = []
		for item in self.items:
			basket_doc = get_basket(self.company,item.product, self.to_location)
			basket_doc.quantity += item.quantity
			basket_doc.save(ignore_permissions=True)
			sl_entries.append(self.sl_meta({
				"inventory": self.to_location,
				"quantity": item.quantity,
				"product" : item.product,
				"balance": basket_doc.quantity
			}))
		self.make_sl_entries(sl_entries)

	def remove_product_from_location(self):
		sl_entries = []
		for item in self.items:
			basket_doc = get_basket(self.company,item.product, self.from_location)
			if basket_doc.quantity >= item.quantity:
				basket_doc.quantity -= item.quantity
				basket_doc.save(ignore_permissions=True)
				sl_entries.append(self.sl_meta({
					"inventory": self.from_location,
					"quantity": -item.quantity,
					"product" : item.product,
					"balance": basket_doc.quantity
				}))

			else:
				frappe.msgprint("{0} didn't have {1} {2}".format(basket_doc.location, item.quantity, basket_doc.product))
		self.make_sl_entries(sl_entries)

	def transfer_product(self):
		sl_entries = []
		for item in self.items:
			source_basket_doc = get_basket(self.company,item.product, self.from_location)
			dest_basket_doc = get_basket(self.company,item.product, self.to_location)
			if source_basket_doc.quantity >= item.quantity:
				source_basket_doc.quantity -= item.quantity
				dest_basket_doc.quantity += item.quantity
				source_basket_doc.save(ignore_permissions=True)
				dest_basket_doc.save(ignore_permissions=True)
				sl_entries.append(self.sl_meta({
					"inventory": self.from_location,
					"quantity": -item.quantity,
					"product" : item.product,
					"balance": source_basket_doc.quantity
				}))
				sl_entries.append(self.sl_meta({
					"inventory": self.to_location,
					"quantity": item.quantity,
					"product" : item.product,
					"balance": dest_basket_doc.quantity
				}))

			else:
				frappe.throw("{0} didn't have {1} {2}".format(source_basket_doc.location, item.quantity, source_basket_doc.product))
		self.make_sl_entries(sl_entries)

	def make_sl_entries(self, sl_entries):
		for sl_entry in sl_entries:
			sl_entry.update({"doctype": "SL Entry"})
			sl = frappe.get_doc(sl_entry)
			sl.insert()
	
	def sl_meta(self, gl_entry):
		sl_entry_dic = frappe._dict({
			'company' : self.company,
			'voucher_type' : self.voucher_type,
			'voucher_reference' : self.voucher_referece,
			'date' : self.date,
		})
		return sl_entry_dic.update(gl_entry)