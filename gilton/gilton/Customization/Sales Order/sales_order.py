
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document



def check_availability(doc,method):
	print(doc.name)
	email=frappe.utils.get_email_address(frappe.session.user)
	quantity=doc.items[0].qty
	print(quantity)
	available_qty=check_stock()
	print(available_qty)
	if(quantity <= available_qty):
		frappe.msgprint("Ok ,Make Sales Order")
	else:
		frappe.msgprint("Insufficient stock ,please contact sales manager")
		doc.docstatus=0
		frappe.sendmail(recipients=email,subject="Regarding insufficient items in stock",message="Please update the stock")

		
		
			
def check_stock():
	doc=frappe.get_doc("Bin","MAT-BIN-2019-00001")
	actual_qty=doc.actual_qty
	print(actual_qty)
	return actual_qty
