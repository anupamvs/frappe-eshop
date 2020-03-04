# -*- coding: utf-8 -*-
# Copyright (c) 2020, anupamvs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TaxTemplate(Document):
	pass

@frappe.whitelist()
def get_tax_list(template):
	if template:
		template = frappe.db.get_list('Tax List',
			filters = {
				'parent' : template
			},
			fields=['title','rate'])
		return template

