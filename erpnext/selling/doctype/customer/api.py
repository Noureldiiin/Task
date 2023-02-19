import frappe

@frappe.whitelist()
def get_customer_details():
    return frappe.db.sql("""
                            SELECT *
                            FROM `tabCustomer`
                            where `tabCustomer`.customer_group = 'Individual'
    """,as_dict=1)