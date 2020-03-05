# -*- coding: utf-8 -*-
# Copyright (c) 2020, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Product(Document):
	pass

@frappe.whitelist()
def get_product_cp(product):
	price = frappe.db.get_value('Product',product,'cost_price')
	return price