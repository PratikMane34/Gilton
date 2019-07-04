# Copyright (c) 2013, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	# print("execute function")
	columns, data = get_columns(), get_data(filters)
	print("------------------------------------------")
	print(data)
	print("------------------------------------------")
	return columns, data

def get_data(filters):
	query_data = frappe.db.sql("""
		select c.name,q.name,sa.name, si.name,dn.name  
		
		from `tabCustomer` as c
		join  `tabQuotation` as q on q.customer_name = c.name
        join  `tabSales Order` as sa on sa.customer_name = c.name
        join  `tabSales Invoice` as si on si.customer_name = c.name
        join  `tabDelivery Note` as dn on dn.customer_name = c.name
		where {0}
		group by sa.name	
			""".format(validate_filters(filters)),debug=1)

	return query_data	

def validate_filters(filters):
	conditions = '1 = 1' 
	if filters.get("from_date"): 
		conditions += " and q.creation >= '{}'".format(filters.get("from_date"))
	if filters.get("to_date"): 
		conditions += " and q.creation <= '{}'".format(filters.get("to_date"))

	if filters.get('customer_name'):
		conditions += " and c.customer_name = '{0}'".format(filters.get('customer_name'))
	print("///////////////",conditions)
	return conditions	

def get_columns():
	
	return [
		{
			"fieldname": "c.name",
			"label": _("Customer Name"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 110
		},
		{
			"fieldname": "title",
			"label": _("Qutation No"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "name",
			"label": _("Sales Order No"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "name",
			"label": _("Sales Invoice No"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "dn.name",
			"label": _("Delivery Note"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
	]
