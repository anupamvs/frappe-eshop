// Copyright (c) 2020, anupamvs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
		if(frm.doc.docstatus == 0 && frm.doc.edit_date_time) {
			frm.set_df_property('date', 'read_only', 0);
			frm.set_df_property('time', 'read_only', 0);
		} else {
			frm.set_df_property('date', 'read_only', 1);
			frm.set_df_property('time', 'read_only', 1);
		}
	},
	edit_date_time: function(frm) {
		frm.refresh()
	},
	tax_template: function(frm) {
		frappe.call({
			method: "eshop.eshop_accounts.doctype.tax_template.tax_template.get_tax_list",
			args: {
				template: frm.doc.tax_template,
			},
			callback: function(r) {
				if(r.message) {
					frm.doc.tax_list=[];
					r.message.forEach(function(child){
						let childTable = frm.add_child("tax_list");
						childTable.title=child.title;
						childTable.rate=child.rate;
					});
					cur_frm.refresh_fields("tax_list");
				}
			}
		});
	},
	net_total: function(frm) {
		calculate_taxes(frm);
		calculate_grand_total(frm);
	}
});

frappe.ui.form.on('Invoice Item', {
	product: function(frm, cdt, cdn) {
		var product = frappe.model.get_doc(cdt,cdn);
		if(!(product.product)){
			frappe.model.set_value(cdt, cdn, "product", null);
			frappe.model.set_value(cdt, cdn, "rate", null);
			frappe.model.set_value(cdt, cdn, "total", null);
		}
		else{
			check_product_quantity_at_location(frm,cdt,cdn);
		}
	},
	quantity: function(frm, cdt, cdn) {
		set_item_total(cdt, cdn);
		set_total(frm);
		check_product_quantity_at_location(frm,cdt,cdn);
	},
	rate: function(frm, cdt, cdn){
		set_item_total(cdt, cdn);
		set_total(frm);
	}
});

var set_item_total = function(cdt, cdn){
	var quantity = frappe.model.get_value(cdt, cdn, "quantity");
	var rate = frappe.model.get_value(cdt, cdn, "rate");
	if(quantity && rate) {
		frappe.model.set_value(cdt, cdn, "total", rate*quantity);
	}
	else{
		frappe.model.set_value(cdt, cdn, "total", null);
	}
}

var set_total = function(frm){
	let quantity = 0;
	let total_amt = 0.00;
	frm.doc.product_list.forEach(function(elm){
		quantity += elm.quantity;
		total_amt += elm.total;
	});
	frappe.model.set_value(frm.doc.doctype, frm.doc.name, "net_quantity", quantity);
	frappe.model.set_value(frm.doc.doctype, frm.doc.name, "net_total", total_amt);
}

var check_product_quantity_at_location = function(frm,cdt,cdn){
	frappe.call({
		method: "eshop.inventory.doctype.basket.basket.get_basket_quantity",
		args: {
			company: frm.doc.company,
			product: frappe.model.get_value(cdt, cdn, "product"),
			location: frm.doc.source_inventory
		},
		callback: function(r) {
			if(r.message) {
				let quantity = frappe.model.get_value(cdt, cdn, "quantity");
				let product = frappe.model.get_value(cdt, cdn, "product");
				if(r.message.quantity < quantity){
					frappe.throw({
						message: frm.doc.source_inventory + " doesn't have " + quantity + " of " + product,
						title: "Insufficient Quantity"
					});
					alert(frm.doc.source_inventory + " doesn't have " + quantity + " of " + product);
					frappe.model.set_value(cdt, cdn, "product", null);
					frappe.model.set_value(cdt, cdn, "rate", null);
					frappe.model.set_value(cdt, cdn, "quantity", 1);
					frappe.model.set_value(cdt, cdn, "total", null);
				}
			}
		}
	});
}

var calculate_taxes = function(frm) {
	let total_tax = 0;
	frm.doc.tax_list.forEach(function (child){
		let tax = (frm.doc.net_total*frappe.model.get_value(child.doctype, child.name, "rate"))/100;
		frappe.model.set_value(child.doctype, child.name, "total", tax);
		total_tax += tax;
	});
	frappe.model.set_value(frm.doc.doctype, frm.doc.name, "total_taxes_and_charges", total_tax);
}

var calculate_grand_total = function(frm) {
	let grand_total = frappe.model.get_value(frm.doc.doctype, frm.doc.name, "total_taxes_and_charges") + frappe.model.get_value(frm.doc.doctype, frm.doc.name, "net_total");
	frappe.model.set_value(frm.doc.doctype, frm.doc.name, "grand_total", grand_total);
}