from __future__ import unicode_literals
import frappe
import json

def filters(doctype):
    print("In filters functions")
    filter = {
        "Customer":[{
            "field_name":"customer_name",
            "label":"Customer Name",
            "fieldtype":"Link",
            "option":"User"
            },
            {
                "field_name":"email_address",
                "label":"Email",
                "fieldtype":"Data"
            },
            {
                "field_name":"mobile",
                "label":"Mobile",
                "fieldtype":"Data"
            },
            {
                "field_name":"creation",
                "label":"Created Date",
                "fieldtype":"date"
            }
        ],
        "User":[{
            "field_name":"name",
            "label":"User",
            "fieldtype":"Data"
            },
            {
            "field_name":"creation",
            "label":"Date",
            "fieldtype":"Date"
            },
            {
            "field_name":"mobile_no",
            "label":"Contact Number",
            "fieldtype":"Data"
            }
            ],

        "Role":[{
            "field_name":"name",
            "label":"Role",
            "fieldtype":"Data"
            }],
        "Employee":[],
        "Item":[],
        "Sales Invoice":[],
        "Delivery Note":[],
        "Quotation":[],
        "Material Request":[]
        }
    return(filter[doctype])
