# -*- coding: utf-8 -*-
# Copyright (c) 2020, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Basket(Document):
	pass

def basket_exist(product, location):
	basket = frappe.db.get_value("Basket", {"product": product, "location": location})
	if basket:
		return True
	return False

def get_basket(product, location, create=False):
	if basket_exist(product, location):
		basket = frappe.db.get_value("Basket", {"product": product, "location": location})
		basket_doc = frappe.get_doc("Basket", basket)
		return basket_doc
	else:
		basket = frappe.new_doc("Basket")
		basket.product = product
		basket.location = location
		basket.quantity = 0.00
		basket.insert()
		return basket

def check_basket_quantity(basket):
	pass