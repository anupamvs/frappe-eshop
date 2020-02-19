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

	def on_submit(self):
		if self.from_location and self.to_location:
			self.transfer_product()
		elif self.from_location:
			self.remove_product_from_location()
		elif self.to_location:
			self.add_product_to_location()
		else:
			frappe.throw("Empty")
		
		# for item in self.items:
		# 	basket_doc = get_basket(item.product, self.to_location)
		# 	basket_doc.quantity = item.quantity
		# 	basket_doc.save(ignore_permissions=True)


		# basket = frappe.db.get_value("Basket", {
		# 	"product": self.product,
		# 	"location": self.location
		# })

		# if not basket:
		# 	basket_doc = frappe.get_doc({
		# 		"doctype": "Basket",
		# 		"product": self.product,
		# 		"location": self.location
		# 	})
		# 	basket_doc.insert(ignore_permissions=True)
		# else:
		# 	basket_doc = frappe.get_doc("Basket", basket)

		# bin_doc.update({
		# 	"product": self.product,
		# 	"location": self.location,
		# 	"quantity": self.quantity
		# })

		# basket_doc.save(ignore_permissions=True)
	
	def add_product_to_location(self):
		for item in self.items:
			basket_doc = get_basket(item.product, self.to_location)
			basket_doc.quantity += item.quantity
			basket_doc.save(ignore_permissions=True)
			# frappe.msgprint({
			# 					'title': 'Product Added',
			# 					'indicator': 'green',
			# 					'message': "{0} {1} Added to {2}".format(item.quantity, basket_doc.product, basket_doc.location)
			# 				})
			frappe.msgprint("{0} {1} Added to {2}".format(item.quantity, basket_doc.product, basket_doc.location))
		

	def remove_product_from_location(self):
		for item in self.items:
			basket_doc = get_basket(item.product, self.from_location)
			if basket_doc.quantity >= item.quantity:
				basket_doc.quantity -= item.quantity
				basket_doc.save(ignore_permissions=True)
				frappe.msgprint("{0} {1} Removed from {2}".format(item.quantity, basket_doc.product, basket_doc.location))
			else:
				frappe.msgprint("{0} didn't have {1} {2}".format(basket_doc.location, item.quantity, basket_doc.product))


	def transfer_product(self):
		for item in self.items:
			source_basket_doc = get_basket(item.product, self.from_location)
			dest_basket_doc = get_basket(item.product, self.to_location)
			if source_basket_doc.quantity >= item.quantity:
				source_basket_doc.quantity -= item.quantity
				dest_basket_doc.quantity += item.quantity
				source_basket_doc.save(ignore_permissions=True)
				dest_basket_doc.save(ignore_permissions=True)
				frappe.msgprint("{0} {1} is transfered from {2} to {3}".format(item.quantity, item.product,source_basket_doc.location, dest_basket_doc.location))
			else:
				frappe.throw("{0} didn't have {1} {2}".format(source_basket_doc.location, item.quantity, source_basket_doc.product))
