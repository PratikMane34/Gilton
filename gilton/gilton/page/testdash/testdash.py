from __future__ import unicode_literals
import frappe
import json

@frappe.whitelist()
def get_lead_details(filters=None):
	lead_details = {}
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
		if filters.get('lead_id'):
			conditions += " and `tabLead`.name = '{0}'".format(filters.get('lead_id'))
		if filters.get('company_name'):
			conditions += " and `tabLead`.company_name = '{0}'".format(filters.get('company_name'))

	else:
		conditions = ""

	active_count = frappe.db.sql("select count(name) from `tabLead` where status = 'Active' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
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

	lead_details['status'] = [
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
			`tabLead`.contact_date,
			`tabLead`.contact_by,
			`tabLead`.market_segment,
			`tabLead`.industry

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
			row.get('lead_owner'),row.get('source'),row.get('territory'),
			row.get('contact_date'),row.get('contact_by'),
			row.get('market_segment'),row.get('industry')
			])

	lead_details['subscription_table'] = lead_lst
	lead_list = frappe.db.sql("""select distinct(name) from `tabLead`""")
	company_list = frappe.db.sql("""select distinct(company_name) from `tabLead`""")
	lead_details['lead_id'] = lead_list
	lead_details['company_name'] = company_list
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	print(lead_details)

	return lead_details


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
		if filters.get('opportunity_name'):
			conditions += " and `tabOpportunity`.name = '{0}'".format(filters.get('opportunity_name'))
		if filters.get('customer_name'):
			conditions += " and `tabOpportunity`.customer_name = '{0}'".format(filters.get('customer_name'))
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
			`tabOpportunity`.name,`tabOpportunity`.status,`tabOpportunity`.customer_name,
			`tabOpportunity`.contact_by,`tabOpportunity`.contact_date,`tabOpportunity`.reminder_date,
			`tabOpportunity`.customer_address,`tabOpportunity`.contact_person,
			`tabOpportunity`.territory,`tabOpportunity`.contact_display,`tabOpportunity`.contact_email,
			`tabOpportunity`.contact_mobile,`tabOpportunity`.source,`tabOpportunity`.enquiry_id,`tabOpportunity`.name_of_competitor,
			`tabOpportunity`.enquiry_category,`tabOpportunity`.expected_purchase_date,`tabOpportunity`.enquiry_closure_date,
			`tabOpportunity`.sales_stage,,`tabOpportunity`.channel,
			`tabOpportunity`.reason_for_enquiry_lost,`tabOpportunity`.sales_partner,`tabOpportunity`.sales__won_reason,
			`tabOpportunity Item`.item_code,`tabOpportunity Item`.qty,
			`tabOpportunity Item`.item_name
		from
			`tabOpportunity`,`tabOpportunity Item`
		where
			`tabOpportunity`.name = `tabOpportunity Item`.parent
			and `tabOpportunity`.docstatus < 2 {}
			order by `tabOpportunity`.name asc """.format(conditions),as_dict=1)

	for row in opportunity_details:
		opportunity_lst.append([
			row.get('name'),row.get('status'),row.get('customer_name'),
			row.get('contact_by'),str(row.get('contact_date')),str(row.get('reminder_date')),
			row.get('customer_address'),row.get('contact_person'),row.get('territory'),row.get('contact_display'),
			row.get('contact_email'),row.get('contact_mobile'),row.get('source'),
			row.get('enquiry_id'),
			row.get('name_of_competitor'),row.get('enquiry_category'),str(row.get('expected_purchase_date')),str(row.get('enquiry_closure_date')),
			row.get('sales_stage'),row.get('channel'),
			row.get('reason_for_enquiry_lost'),row.get('sales_partner'),row.get('sales__won_reason'),row.get('item_code'),
			row.get('qty'),row.get('item_name')
			])
	opportunity_data['opportunity_table'] = opportunity_lst
	opportunity_list = frappe.db.sql("""select distinct(name) from `tabOpportunity`""")
	customer_list = frappe.db.sql("""select distinct(customer_name) from `tabOpportunity`""")
	opportunity_data['opportunity_name'] = opportunity_list
	opportunity_data['customer_name'] = customer_list

	return opportunity_data

@frappe.whitelist()
def get_quotation_details(filters=None):
	quotation_data = {}
	quotation_lst = []
	customer_list = []
	item_list = []
	conditions = ""
	date_conditions = ""
	if filters:
		filters = json.loads(filters)
		if filters.get('from_date') and filters.get('to_date'):
			conditions += " and `tabQuotation`.creation between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
			date_conditions += " and `tabQuotation`.creation between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
		if filters.get('quotation_status'):
			conditions += " and `tabQuotation`.status = '{0}'".format(filters.get('quotation_status'))
		if filters.get('item_name'):
			conditions += " and `tabQuotation Item`.item_name = '{0}'".format(filters.get('item_name'))
		if filters.get('quotation_name'):
			conditions += " and `tabQuotation`.name = '{0}'".format(filters.get('quotation_name'))
	else:
		conditions = ""
	draft_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Draft' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	submitted_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Submitted' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	ordered_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Ordered' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	lost_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Lost' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	cancelled_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Cancelled' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	open_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Open' {}".format(date_conditions),as_dict=1)[0].get('count(name)')
	replied_count = frappe.db.sql("select count(name) from `tabQuotation` where status = 'Replied' {}".format(date_conditions),as_dict=1)[0].get('count(name)')

	quotation_data['status'] = [
		["Status", "Count"],
		["Draft", draft_count],
		["Submitted", submitted_count],
		["Ordered", ordered_count],
		["Lost", lost_count],
		["Cancelled", cancelled_count],
		["Open", open_count],
		["Replied", replied_count]
	]

	quotation_details = frappe.db.sql("""
		select `tabQuotation`.name,
		`tabQuotation`.transaction_date,`tabQuotation`.status,
		`tabQuotation`.source,
		`tabQuotation Item`.item_code,
		`tabQuotation Item`.item_name,
		`tabQuotation Item`.qty,rate, `tabQuotation Item`.amount from
		 `tabQuotation` inner join `tabQuotation Item` on
		 `tabQuotation`.name=`tabQuotation Item`.parent
		where
			`tabQuotation`.docstatus < 2 {}
			order by `tabQuotation`.name asc """.format(conditions),as_dict=1)

	for row in quotation_details:
		quotation_lst.append([
			row.get('name'),str(row.get('transaction_date')),
			row.get('status'),
			row.get('source'),row.get('item_code'),row.get('item_name'),
			row.get('qty'),row.get('rate'), row.get('amount')
			])

	item_list =frappe.db.sql("""select distinct(item_name) from `tabQuotation Item`""")

	quotation_list = frappe.db.sql("""select distinct(name) from `tabQuotation`""")
	quotation_data['quotation_table'] = quotation_lst

	quotation_data['item_name'] = item_list
	quotation_data['quotation_name'] = quotation_list

	return quotation_data
