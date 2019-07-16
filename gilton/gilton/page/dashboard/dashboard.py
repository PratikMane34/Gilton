from __future__ import unicode_literals
import frappe
import json

@frappe.whitelist()
def get_lead_details(filters=None):
	subscription_data = {}
	lead_lst = []

	conditions = "where 1=1"
	date_conditions = ""
	if filters:
		filters = json.loads(filters)
		if filters.get('from_date') and filters.get('to_date'):
			conditions += " and `tabLead`.creation between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
			date_conditions += " and `tabLead`.creation between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
		if filters.get('lead_status'):
			conditions += " and `tabLead`.status = '{0}'".format(filters.get('lead_status'))
	else:
		conditions = ""

	active_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Active' {}".format(date_conditions),as_dict=1,debug=1)[0].get('count(name)')
	inactive_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Inactive' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	lead_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Lead' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	open_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Open' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	replied_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Replied' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	opportunity_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Opportunity' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	quotation_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Quotation' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	lost_quotation_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Lost Quotation' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	interested_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Interested' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	converted_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Converted' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	do_not_contact_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Do Not Contact' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	dispatched_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Dispatched' {}".format(date_conditions),as_dict=1)[0].get('count(name)')

	subscription_data['status'] = [
		["Status", "Count"],
		["Active", active_count],
		["Inactive", inactive_count],
		["Lead", lead_count],
		["Open", open_count],
		["Replied", replied_count],
		["Opportunity", opportunity_count],
		["Quotation", quotation_count],
		["Lost Quotation", lost_quotation_count],
		["Interested", interested_count],
		["Converted", converted_count],
		["Do Not Contact", do_not_contact_count],
		["Dispatched", dispatched_count],
	]


	lead_data = frappe.db.sql("""
		SELECT
		    `tabLead`.name,
		    `tabLead`.lead_name,
			`tabLead`.company_name,
			`tabLead`.status,
			concat_ws(', ',
				trim(',' from `tabAddress`.address_line1),
				trim(',' from `tabAddress`.address_line2)
			)as address,
			`tabAddress`.state,
			`tabAddress`.pincode,
			`tabAddress`.country,
			`tabLead`.phone,
			`tabLead`.mobile_no,
			`tabLead`.email_id,
			`tabLead`.lead_owner,
			`tabLead`.source,
			`tabLead`.territory,
		    `tabLead`.owner
		FROM
			`tabLead`
			left join `tabDynamic Link` on (
				`tabDynamic Link`.link_name=`tabLead`.name
			)
			left join `tabAddress` on (
				`tabAddress`.name=`tabDynamic Link`.parent
			)
	{0}
			and `tabLead`.docstatus<2
	ORDER BY
			`tabLead`.name asc

			""".format(conditions),as_dict=1)

	for row in lead_data:
		lead_lst.append([
			row.get('name'),row.get('lead_name'),row.get('company_name'),
			row.get('status'),row.get('address'),row.get('state'),row.get('pincode'),
			row.get('country'),row.get('phone'),row.get('mobile_no'),row.get('email_id'),
			row.get('lead_owner'),row.get('source'),row.get('territory'),row.get('owner')])

	subscription_data['subscription_table'] = lead_lst

	return subscription_data


@frappe.whitelist()
def get_opportunity_details(filters=None):
	opportunity_data = {}
	opportunity_lst = []

	conditions = ""
	date_conditions = ""
	if filters:
		filters = json.loads(filters)
		if filters.get('from_date') and filters.get('to_date'):
			conditions += " and `tabOpportunity`.creation between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
			date_conditions += " and `tabOpportunity`.creation between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
		if filters.get('opportunity_status'):
			conditions += " and `tabOpportunity`.status = '{0}'".format(filters.get('opportunity_status'))
	else:
		conditions = ""


	open_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Open' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	quote_gen_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Quote Generated' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	tobe_quoted_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'To Be Quoted' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	not_tobe_quoted_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Not To Be Quoted' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	lost_order_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Order Lost' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	close_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Close Without Sale' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	converted_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Converted' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	closed_count = frappe.db.sql("select count(name) from `tabOpportunity` where status = 'Closed' {}".format(date_conditions),as_dict=1)[0].get('count(name)')

	opportunity_data['status'] = [
		["Status", "Count"],
		["Open", open_count],
		["Quote Generated", quote_gen_count],
		["To Be Quoted", tobe_quoted_count],
		["Not To Be Quoted", not_tobe_quoted_count],
		["Order Lost", lost_order_count],
		["Close Without Sale", close_count],
		["Converted", converted_count],
		["Closed", closed_count],

	]

	opportunity_details = frappe.db.sql("""
		select
			enquiry_from,opportunity_type,lead,status,customer_name,
			mins_to_first_response,customer_type,contact_by,to_discuss,
			contact_date,reminder_date,customer_address,contact_person,
			territory,contact_display,customer_group,contact_email,contact_mobile,
			source,company,city,transaction_date,enquiry_id,name_of_competitor,
			enquiry_category,expected_purchase_date,enquiry_closure_date,sales_stage,
			sic_code_type,channel,sic_code,reason_for_enquiry_lost,sales_partner,
			sales__won_reason,item_code,qty,item_name
		from
			`tabOpportunity`,`tabOpportunity Item`
		where
			`tabOpportunity`.name = `tabOpportunity Item`.parent
			and `tabOpportunity`.docstatus < 2 {}
			order by `tabOpportunity`.name asc """.format(conditions),as_dict=1,debug=1)

	for row in opportunity_details:
		opportunity_lst.append([
			row.get('enquiry_from'),row.get('opportunity_type'),row.get('lead'),
			row.get('status'),row.get('customer_name'),row.get('mins_to_first_response'),row.get('customer_type'),
			row.get('contact_by'),row.get('to_discuss'),str(row.get('contact_date')),str(row.get('reminder_date')),
			row.get('customer_address'),row.get('contact_person'),row.get('territory'),row.get('contact_display'),
			row.get('customer_group'),row.get('contact_email'),row.get('contact_mobile'),row.get('source'),
			row.get('company'),row.get('city'),str(row.get('transaction_date')),row.get('enquiry_id'),
			row.get('name_of_competitor'),row.get('enquiry_category'),str(row.get('expected_purchase_date')),str(row.get('enquiry_closure_date')),
			row.get('sales_stage'),row.get('sic_code_type'),row.get('channel'),row.get('sic_code'),
			row.get('reason_for_enquiry_lost'),row.get('sales_partner'),row.get('sales__won_reason'),row.get('item_code'),
			row.get('qty'),row.get('item_name')
			])

	opportunity_data['opportunity_table'] = opportunity_lst

	return opportunity_data
