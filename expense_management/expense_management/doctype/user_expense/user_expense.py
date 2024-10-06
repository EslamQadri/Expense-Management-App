# Copyright (c) 2024, eslam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class UserExpense(Document):
    def validate(self):

        current_user = frappe.session.user

        if self.owner != current_user:

            raise frappe.PermissionError(
                "You do not have permission to access this document."
            )
