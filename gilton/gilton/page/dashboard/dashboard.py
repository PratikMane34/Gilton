from __future__ import unicode_literals
import frappe
import json


@frappe.whitelist()
def get_doc_list(filters=None):
	doc_list = ['Customer','User','Role','Employee','Item','Sales Invoice','Delivery Note','Quotation','Material Request']
	return doc_list

@frappe.whitelist()
def get_data(doctype,filters=None):
	data={}
	if filters:
		filters = json.loads(filters)
		#print(type(filters))
	data['filter']=get_doc_filter(doctype)
	data['columns']=get_columns(doctype)
	data['record']=get_records(doctype,filters)
	data['status']=get_status(doctype)
	return data

@frappe.whitelist()
def get_status(doctype):
	import get_records
	counts=get_records.counts(doctype)
	return counts

@frappe.whitelist()
def get_records(doctype,filters=None):
	print("?????????????-- Filters----???????????????")
	print(filters)
	import get_records
	record=get_records.records(doctype,filters)
	return record

@frappe.whitelist()
def get_columns(doctype):
	import get_records
	record=get_records.record_label(doctype)
	return record

@frappe.whitelist()
def get_doc_filter(doctype):
	import get_filters
	filters=get_filters.filters(doctype)
	return filters
