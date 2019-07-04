# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gilton"
app_title = "Gilton"
app_publisher = "Indictrans"
app_description = "Products retail"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "indictrans@indictrans.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gilton/css/gilton.css"
# app_include_js = "/assets/gilton/js/gilton.js"

# include js, css files in header of web template
# web_include_css = "/assets/gilton/css/gilton.css"
# web_include_js = "/assets/gilton/js/gilton.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gilton.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gilton.install.before_install"
# after_install = "gilton.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gilton.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gilton.tasks.all"
# 	],
# 	"daily": [
# 		"gilton.tasks.daily"
# 	],
# 	"hourly": [
# 		"gilton.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gilton.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gilton.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gilton.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gilton.event.get_events"
# }



fixtures=['Custom Field','Property Setter','Role','Print Format']


doc_events = {
"Customer": {
 "validate":"gilton.gilton.Customization.Customer.user.create_user"
},
"Delivery Note":{
"validate":"gilton.gilton.Customization.Delivery_Note.delivery_note.submit",
"on_submit":"gilton.gilton.Customization.Delivery_Note.delivery_note.on_submit"
},
"Quotation": {
 "on_submit":"gilton.gilton.Customization.Customer.quotation.on_submit"

}
}


doctype_js = {
		"Customer" :["custom/customer.js"],
		"Quotation":["custom/quotation.js"],
        "Delivery Note":["custom/deliverynote.js"]
	}
