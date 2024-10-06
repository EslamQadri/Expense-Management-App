# Copyright (c) 2024, eslam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class Expense(Document):
    def before_insert(self):

        if not self.user:
            self.user = frappe.session.user

    def after_insert(self):

        self.update_total_expenses(self.user)

    def validate(self):
		

        if self.amount <= 0:
            frappe.throw(_("Amount must be a positive number"))

    def update_total_expenses(self, user):

        total_expenses = (
            frappe.db.sql(
                """
            SELECT SUM(amount) 
            FROM `tabExpense` 
            WHERE owner = %s
        """,
                user,
            )[0][0]
            or 0
        )

        total_expense_name = frappe.db.exists("User Expense", {"user": user})

        if total_expense_name:

            total_expense_doc = frappe.get_doc("User Expense", total_expense_name)

            total_expense_doc.total_expense = total_expenses

            total_expense_doc.save()
