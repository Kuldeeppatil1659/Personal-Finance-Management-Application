from models import create_connection

# Function to generate a monthly financial report
def generate_monthly_report(user_id):
    month = input("Enter the month (MM): ")
    year = input("Enter the year (YYYY): ")

    conn = create_connection()
    cursor = conn.cursor()

    # Calculate total income for the month
    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND type = 'income' AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
    ''', (user_id, month, year))
    total_income = cursor.fetchone()[0] or 0

    # Calculate total expenses for the month
    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND type = 'expense' AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
    ''', (user_id, month, year))
    total_expenses = cursor.fetchone()[0] or 0

    # Calculate savings for the month
    savings = total_income - total_expenses

    print(f"\n--- Monthly Report for {month}/{year} ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Savings: {savings}")

    # Breakdown by category
    cursor.execute('''
        SELECT category, SUM(amount) FROM transactions
        WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY category, type
    ''', (user_id, month, year))
    
    print("\nCategory Breakdown:")
    for category, amount in cursor.fetchall():
        print(f"Category: {category} | Amount: {amount}")

    conn.close()

# Function to generate a yearly financial report
def generate_yearly_report(user_id):
    year = input("Enter the year (YYYY): ")

    conn = create_connection()
    cursor = conn.cursor()

    # Calculate total income for the year
    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND type = 'income' AND strftime('%Y', date) = ?
    ''', (user_id, year))
    total_income = cursor.fetchone()[0] or 0

    # Calculate total expenses for the year
    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND type = 'expense' AND strftime('%Y', date) = ?
    ''', (user_id, year))
    total_expenses = cursor.fetchone()[0] or 0

    # Calculate savings for the year
    savings = total_income - total_expenses

    print(f"\n--- Yearly Report for {year} ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Savings: {savings}")

    # Breakdown by category
    cursor.execute('''
        SELECT category, SUM(amount) FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY category, type
    ''', (user_id, year))
    
    print("\nCategory Breakdown:")
    for category, amount in cursor.fetchall():
        print(f"Category: {category} | Amount: {amount}")

    conn.close()
