from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def sendmail1(method=None):
    return {'Response':'this is first semd mail api \n carryon'}
