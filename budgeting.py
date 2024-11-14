import sqlite3
from models import create_connection

def set_budget(user_id):
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    amount = float(input("Enter budget amount: "))

    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO budgets (user_id, month, year, category, amount)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(user_id, month, year, category) 
            DO UPDATE SET amount=excluded.amount
        ''', (user_id, month.zfill(2), year, category, amount))
        conn.commit()
        print(f"Budget for {category} in {month}/{year} set to {amount}.")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def check_budget(user_id, month, year, category):
    conn = create_connection()
    cursor = conn.cursor()

    # Get the budgeted amount
    cursor.execute('''
        SELECT amount FROM budgets
        WHERE user_id = ? AND month = ? AND year = ? AND category = ?
    ''', (user_id, month.zfill(2), year, category))

    budget_result = cursor.fetchone()
    if budget_result:
        budget_amount = budget_result[0]
    else:
        print(f"No budget set for {category} in {month}/{year}.")
        return

    # Calculate total expenses in this category for the given month and year
    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND type = 'expense' AND category = ?
        AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
    ''', (user_id, category, month.zfill(2), year))

    expense_result = cursor.fetchone()
    total_expenses = expense_result[0] if expense_result[0] else 0

    # Check if expenses exceed the budget
    if total_expenses > budget_amount:
        print(f"Alert! You have exceeded your budget for {category} by {total_expenses - budget_amount}.")
    else:
        print(f"Total expenses for {category}: {total_expenses}. Budget remaining: {budget_amount - total_expenses}.")

    conn.close()

