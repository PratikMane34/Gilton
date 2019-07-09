# -*- coding: utf-8 -*-
# Copyright (c) 2019, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import base64
from frappe.utils import strip, get_files_path,get_datetime


class Base64Image(Document):
	def validate(self):
		self.upload_image('ABC',self.base64)
		#frappe.msgprint('Calling before save function')
		frappe.msgprint("printed base64")

	def upload_image(self,name,image):
		file_url = get_files_path ()
		time = str(get_datetime())
		file_url += "/"
		img_name = "_asmita"+name+time+".jpeg"
		file_url += img_name
		image_64_decode = base64.decodestring(self.base64)
		print "-----image_64_decode---",image_64_decode
		print file_url
		image_result = open(file_url, 'wb')
		image_result.write(image_64_decode)
		print "----------image "
		if image_result:
			file_doc = frappe.new_doc("File")
			file_doc.file_name =img_name
			file_doc.folder = "Home/Attachments"
			file_url_attach = get_files_path ()
			file_doc.file_url = file_url
			file_doc.file_url = "files/"+ img_name
			file_doc.validate()
			file_doc.insert(ignore_permissions=True)
			frappe.db.commit()
