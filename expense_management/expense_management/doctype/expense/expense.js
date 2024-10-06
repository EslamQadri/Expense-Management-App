// Copyright (c) 2024, Eslam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expense', {
    validate: function(frm) {
        // Get the current date
        const today = new Date();
        today.setHours(0, 0, 0, 0); // Set to the start of the day

        // Get the expense date from the form
        const expenseDate = frm.doc.expense_date; // Change 'expense_date' to your actual field name

        // Check if the expense date is in the future
        if (expenseDate && new Date(expenseDate) > today) {
            frappe.msgprint(__('Expense Date cannot be in the future.'));
            frappe.validated = false; // Prevent the form from being submitted
        }
    },

    after_save: function(frm) {
        // Fetch the total expenses logged by the user
        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'Expense',
                fieldname: 'sum(amount)',
                filters: {
                    owner: frappe.session.user
                }
            },
            callback: function(response) {
                const total_expenses = response.message['sum(amount)'] || 0;

                // Show the pop-up message with the total amount
                frappe.msgprint({
                    title: __('Total Expenses'),
                    message: __('You have a total of {0}', [total_expenses]),
                    indicator: 'green'
                });
            }
        });
    }
});
