# transactions.py

import sqlite3
from models import create_connection

# Function to add a new transaction
def add_transaction(user_id):
    trans_type = input("Enter transaction type (income/expense): ").lower()
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (user_id, type, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, trans_type, category, amount, date))

    conn.commit()
    print("Transaction added successfully.")
    conn.close()

# Function to list recent transactions
def list_transactions(user_id):
    conn = create_connection()
    cursor = conn.cursor()

    # Retrieve and display the last 10 transactions for the user
    cursor.execute('''
        SELECT id, category, amount, date
        FROM transactions
        WHERE user_id = ?
        ORDER BY date DESC
        LIMIT 10
    ''', (user_id,))

    transactions = cursor.fetchall()

    print("\n--- Your Recent Transactions ---")
    for trans in transactions:
        trans_id, category, amount, date = trans
        print(f"ID: {trans_id} | Category: {category} | Amount: {amount} | Date: {date}")

    conn.close()
    return transactions

# Function to update a transaction
def update_transaction(user_id):
    transactions = list_transactions(user_id)
    
    # Ask the user to choose the transaction by ID
    trans_id = input("Enter the ID of the transaction you want to update (or type 'cancel' to cancel): ")
    
    if trans_id.lower() == 'cancel':
        print("Update operation canceled.")
        return
    
    # Validate if the chosen ID is valid
    if not any(str(t[0]) == trans_id for t in transactions):
        print("Invalid transaction ID. Please try again.")
        return
    
    new_category = input("Enter new category (or type 'cancel' to cancel): ")
    if new_category.lower() == 'cancel':
        print("Update operation canceled.")
        return
    
    try:
        new_amount = float(input("Enter new amount (or type 'cancel' to cancel): "))
    except ValueError:
        print("Update operation canceled.")
        return
    
    new_date = input("Enter new date (YYYY-MM-DD) (or type 'cancel' to cancel): ")
    if new_date.lower() == 'cancel':
        print("Update operation canceled.")
        return

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE transactions
        SET category = ?, amount = ?, date = ?
        WHERE id = ? AND user_id = ?
    ''', (new_category, new_amount, new_date, trans_id, user_id))

    conn.commit()
    print("Transaction updated successfully.")
    conn.close()

# Function to delete a transaction
def delete_transaction(user_id):
    transactions = list_transactions(user_id)
    
    # Ask the user to choose the transaction by ID
    trans_id = input("Enter the ID of the transaction you want to delete (or type 'cancel' to cancel): ")

    if trans_id.lower() == 'cancel':
        print("Deletion operation canceled.")
        return

    # Validate if the chosen ID is valid
    if not any(str(t[0]) == trans_id for t in transactions):
        print("Invalid transaction ID. Please try again.")
        return

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM transactions
        WHERE id = ? AND user_id = ?
    ''', (trans_id, user_id))

    conn.commit()
    print("Transaction deleted successfully.")
    conn.close()
