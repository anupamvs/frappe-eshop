# -*- coding: utf-8 -*-
# Copyright (c) 2020, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.utils.nestedset import NestedSet

class ProductCategory(NestedSet):
	nsm_parent_field = "parent_product_category"
