# Copyright (c) 2013, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	print"Hiiiii"
	columns, data = get_columns(), []
	return columns, data

def get_columns(filters=None):
	return [{
		"fieldname":"name",
		"label":("Delivery Note"),
		"fieldtype":"link",
		"option":"Delivery Note"
	}]
