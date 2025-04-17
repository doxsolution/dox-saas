
import frappe
from frappe.model.document import Document

class SaaSCustomer(Document):
    def after_insert(self):
        frappe.enqueue("dox_saas.api.create_site_for_customer", queue='short', customer=self.name)
