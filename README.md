Personal Finance Management Application

This is a command-line application to help users manage their personal finances. The app allows users to track their income and expenses, set budgets, generate financial reports, and securely back up and restore their data.

Features
User Registration and Authentication: Secure user login and registration system.
Income and Expense Tracking: Add, update, delete, and list income and expense transactions.
Financial Reports: Generate monthly and yearly financial reports.
Budgeting: Set and check budgets for different categories and receive notifications if the budget is exceeded.
Data Persistence: Store user data and transactions in a local SQLite database. Backup and restore data to ensure the safety of user information.
Requirements
Python 3.7+
SQLite3 (comes pre-installed with Python)
A terminal or command-line interface
Installation
Clone the repository to your local machine:


git clone https://github.com/Kuldeeppatil1659/personal-finance-management.git
cd personal-finance-management
Install the required dependencies:

pip install -r requirements.txt

Usage
1. Authentication
Register a new user:
Choose 1 to register and provide a unique username and password.
Login to your account:
Choose 2 to log in. Enter your username and password.

2. Transaction Management
Add a new transaction:
Choose 1 from the main menu to add a new transaction. Specify the type (income or expense), category, amount, and the date.
Update an existing transaction:
Choose 2 from the main menu to update a transaction. Select the transaction ID and the new details.
Delete a transaction:
Choose 3 to delete a transaction. The app will ask you to select a transaction ID and confirm deletion.
List all transactions:
Choose 4 to view all transactions. You can filter by type (income or expense) and view the transactions.


3. Budgeting
Set a budget:
Choose 5 to set a budget for a specific category (e.g., Food, Rent) and month/year.
Check budget:
Choose 6 to check if you are within your budget for a specific category and month/year. The app will notify you if the expenses exceed the budget.

4. Financial Reports
Generate a monthly report:
Choose 7 to generate a financial report for a specific month and year. The report will show total income, expenses, and savings.
Generate a yearly report:
Choose 8 to generate a financial report for a specific year. The report will show total income, expenses, and savings for the entire year.

5. Data Management
Backup data:
Choose 11 to create a backup of the current database. This will save a copy of your data to a backup file.
Restore data:
Choose 12 to restore data from the backup file. This will overwrite the current database with the backed-up data.

6. Logout and Exit
Logout: Choose 9 to log out of the current session and return to the authentication menu.
Exit: Choose 10 to exit the application.


Directory Structure
.

├── main.py                # Main application logic

├── auth.py                # User registration and login functionality

├── transactions.py        # Income and expense management functions

├── budgeting.py           # Budgeting functionality

├── financial_reports.py   # Financial report generation

├── data_persistence.py    # Backup and restore functions

├── models.py              # Database connection and schema management

├── requirements.txt       # Required Python libraries

└── README.md              # Documentation for the project



Database Schema
The application uses SQLite for data persistence. The following tables are used:

users: Stores user credentials (username, hashed password).
transactions: Stores transaction data (user_id, type, amount, category, date).
budgets: Stores user budget data (user_id, month, year, category, amount).
Backup and Restore
The app supports creating backups of the database and restoring from those backups. The backup is stored as finance_manager_backup.db, and the main database is finance_manager.db. The backup and restore functionality ensures that user data is safe and can be recovered if needed.

How to Backup Data:
Choose 11 from the main menu to create a backup.
How to Restore Data:
Choose 12 from the main menu to restore data from a backup file.
Running the Application
Run the application:


python main.py
Follow the on-screen prompts to interact with the application.

Example Usage
Register and Login:
Welcome to the Personal Finance Management Application!
--- Authentication Menu ---
1. Register
2. Login
3. Exit

Choose an option: 1

Enter username: john_doe

Enter password: ********


Registration successful!



--- Authentication Menu ---
1. Register
2. Login
3. Exit

Choose an option: 2

Enter username: john_doe

Enter password: ********

Login successful!




Add a Transaction:

--- Main Menu ---
1. Add Transaction
2. Update Transaction
3. Delete Transaction
4. List Transactions
5. Set Budget
6. Check Budget
7. Generate Monthly Report
8. Generate Yearly Report
9. Logout
10. Exit
11. Backup Data
12. Restore Data
Choose an option: 1
Enter type (income/expense): expense
Enter category (e.g., Rent, Food): Food
Enter amount: 100
Enter date (YYYY-MM-DD): 2024-11-01
Transaction added successfully!
