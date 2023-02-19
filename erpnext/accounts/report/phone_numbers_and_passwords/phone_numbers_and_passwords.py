
# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	#condition = get_condition(filters)
	name = filters.get("name")
	print("\n\n\n\n\n\n\n\n")
	print(name)
	conditions = ""
	if(filters.get("phone")):
		conditions += f"WHERE phone_number = '{filters.get('phone')}'"
	

	data = frappe.db.sql(
		f"""
		SELECT your_name, phone_number, password
		FROM `tabDocType1`
		{conditions}
		"""
	)
	columns = get_columns(filters)
	return columns, data


def get_columns(filters):
	column=[
		{	"fieldname":"name",
			'label':"Name",
			"fieldtype":"Data",
			"width":200
		},
		{
			"fieldname":"phone_numbers",
			"label":"Phone numbers",
			"fieldtype":"Data",
			"width":200
		},
		{
			"fieldname":"password",
			"label":"Password",
			"fieldtype":"Password",
			"width":200
		}
	]
	return column
