
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


import frappe

@frappe.whitelist()
def set_si_autoname(doc, method):
	doc.name = doc.po_no # or in your case doc.my_order_no

	
def set_indicator(self):
		"""Set indicator for portal"""
		if self.outstanding_amount > 0:
			self.indicator_color = "orange"
			self.indicator_title = _("Unpaid")
		else:
			self.indicator_color = "green"
			self.indicator_title = _("Paid")

# def material_request_data(self,Document):
# 	query = frappe.db.sql("""select name, material_transfer_type
# 			from `tabMaterial Transfer` 
# 			WHERE material_request='{0}' """.format(self.material_request),as_dict=1)
	
# 	doc_details=""
# 	for i in query :
# 		doc_details += i.name+" - "+i.material_transfer_type+" \n"
		
# 	self.doc_details=doc_details

# def update_material_request_data(self,doc):
# 	query = frappe.db.sql("""select name, material_transfer_type
# 			from `tabMaterial Transfer` 
# 			WHERE material_request='{0}' """.format(self.material_request),as_dict=1)
	
# 	doc_details=""
# 	for i in query :
# 		doc_details += i.name+" - "+i.material_transfer_type+" \n"
	
# 	frappe.db.set_value("Material Request", self.material_request, 'doc_details', doc_details)
# 	# self.doc_details=doc_details
# 	# add_to_on_material_transfer(self,doc)

# def add_to_on_material_transfer(self,doc):
#         todo = frappe.new_doc("ToDo")
#         todo.owner = self.receiver
#         todo.assigned_by = self.owner
#         todo.description = "Material To Be Transfered"
#         todo.date = frappe.utils.nowdate()
#         todo.reference_type = "Material Transfer"
#         todo.reference_name = self.name
#         todo.insert(ignore_permissions=True)
#         frappe.db.commit()
