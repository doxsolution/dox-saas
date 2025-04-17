
import os
import frappe

def create_site_for_customer(customer_name):
    doc = frappe.get_doc("SaaS Customer", customer_name)
    site_name = doc.site_name.lower().replace(" ", "-")

    command = f"bench new-site {site_name} --mariadb-root-password 123 --admin-password admin"
    os.system(command)
    os.system(f"bench --site {site_name} install-app erpnext")
    os.system(f"bench --site {site_name} install-app dox_saas")
