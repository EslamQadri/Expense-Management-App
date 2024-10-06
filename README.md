# Expense Management App

## Overview

This application allows users to manage their expenses efficiently. Users can log expenses with relevant details and track their total expenses. It includes validation rules and custom scripts for a better user experience.

## Features

### Expense DocType
- **Expense Title**: (Data, Mandatory)
- **Expense Date**: (Date, Mandatory)
- **Amount**: (Currency, Mandatory)
- **Expense Category**: (Select, Mandatory, options include: 'Travel', 'Food', 'Office Supplies', etc.)
- **Description**: (Text, Optional)

### User Expense DocType
- **user**: (link,unique) a one-to-one relationship with the User, ensuring each user has a unique expense record
- **Total Expense** : (Currency, Optional)

## Why User Expense ? 
###  Because i have an Error with custom field  in the User DocType in "ERPNEXT 15 Hot fix" unlike ERPNEXT 14
###  
## Functionality

### Validation Rules in Python
- Ensures that the amount entered for the expense is a positive number.
- Prevents users from accessing expense data of other users through API calls.

### Server-Side Script
- A Python script that calculates the total expenses submitted by the current user and stores this in a custom field in the User DocType.

### Custom Form Script
- A JavaScript form script that displays a pop-up message when an expense is saved, showing the total amount logged by the user so far.

### Client-Side Validation
- Validates that the Expense Date is not in the future using JavaScript.

### Basic Report
- Generates a report that shows all expenses logged by  all users.

## Setup Instructions

To set up the app locally and test its functionality, follow these steps:


  
1.  **Clone the Repository**
   ```bash
  bench get-app  https://github.com/EslamQadri/Expense-Management-App.git
   ```
2. **install app in you site** 
  ```
 bench install-app expense_management
```

  
