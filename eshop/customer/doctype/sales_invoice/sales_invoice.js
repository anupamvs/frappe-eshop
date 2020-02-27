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
	company: function(frm) {
		//alert(frm.doc.company)
	}
});

frappe.ui.form.on('Sales Invoice Items', {
	refresh: function(frm) {
		console.log(frm.doc)
	},
	product: function(frm, cdt, cdn) {
		var product = frappe.model.get_doc(cdt,cdn);
		if(!(product.product)){
			alert("cool");
			frappe.model.set_value(cdt, cdn, "product", null);
			frappe.model.set_value(cdt, cdn, "rate", null);
			frappe.model.set_value(cdt, cdn, "total", null);
		}
	},
	quantity: function(frm, cdt, cdn) {
		set_item_total(cdt, cdn);
		set_total(frm);
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