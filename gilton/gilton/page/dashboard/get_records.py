from __future__ import unicode_literals
import frappe
import json

def record_fields(doctype):
    fields = {
        "Customer":['customer_name','user_name','email_address','mobile','creation','credit_limit','language'],
        "User":['name','username','email','full_name','date(creation)','birth_date'],
#        "User":["select username,email,full_name,creation,birth_date from tabUser"],
        "Role":['name','date(creation)'],
        "Master":[],
        "Employee":[],
        "Item":[],
        "Sales Invoice":[],
        "Delivery Note":[],
        "Quotation":[],
        "Material Request":[]
        }

    return fields[doctype]

def records(doctype,filters):
    fields= record_fields(doctype)
    record=[]
    if filters:
        filters=filter_cleaner(doctype,filters)
    data=frappe.get_all(doctype,filters=filters, fields=fields)
    field_list=[]
    for row in data:
        # record.append([
		# 	row.get('name'),row.get('username'),row.get('birth_date'),row.get('creation'),
		# 	row.get('email'),row.get('full_name')
		# 	])
        record.append([row.get(field)for field in fields])
    return record
    #data=frappe.db.sql()

def filter_cleaner(doc,filters):
    print("---------------------------")
    print(filters)
    if(doc=='Customer'):
        if not(filters.get('customer_name')):
            del filters['customer_name']
        if not(filters.get('mobile')):
            del filters['mobile']
        if not(filters.get('creation')):
            del filters['creation']
        if not(filters.get('email_address')):
            del filters['email_address']
    print('-----------------------------')
    print(filters)
    return filters

def record_label(doctype):
    columns = {
        "Customer":['Customer Name','Username','Email Address','Mobile','Created Date','Credit Limit','Language'],
        "User":['User Id','Username','Email','Fullname','Created date','Birth Date'],
#        "User":["select username,email,full_name,creation,birth_date from tabUser"],
        "Role":["Role","Creation Date"],
        "Master":[],
        "Employee":[],
        "Item":[],
        "Sales Invoice":[],
        "Delivery Note":[],
        "Quotation":[],
        "Material Request":[]
        }
    column = columns[doctype]
    return column

def counts(doctype):

    print("*****************In records functions**********************")
    queries = {
        "Customer":[],
        "User":['1','0'],
        "Role":[],
        "Employee":[],
        "Item":[],
        "Sales Invoice":[],
        "Delivery Note":[],
        "Quotation":[],
        "Material Request":[]
        }
    status=queries[doctype]
    status = get_count(doctype,status)
    return status

def get_count(doctype,status):
    count=[]
    for i in range(len(status)):
        #count.append("")
        sql ="select count(name) from `tab{0}` where enabled = '{1}' ".format(doctype,status[i])
        count.append(frappe.db.sql(sql,as_dict=1)[0].get('count(name)'))
    return count
