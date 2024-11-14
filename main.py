from auth import register_user, login_user
from transactions import add_transaction, update_transaction, delete_transaction, list_transactions
from budgeting import set_budget, check_budget
from financial_reports import generate_monthly_report, generate_yearly_report
from data_persistence import backup_data, restore_data

def main():
    user_id = None
    print("Welcome to the Personal Finance Management Application!")

    while True:
        if user_id:
            print("\n--- Main Menu ---")
            print("1. Add Transaction")
            print("2. Update Transaction")
            print("3. Delete Transaction")
            print("4. List Transactions")
            print("5. Set Budget")
            print("6. Check Budget")
            print("7. Generate Monthly Report")
            print("8. Generate Yearly Report")
            print("9. Logout")
            print("10. Exit")
            print("11. Backup Data")
            print("12. Restore Data")
        else:
            print("\n--- Authentication Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

        choice = input("Choose an option: ")

        # Authentication options
        if not user_id:
            if choice == '1':
                register_user()
            elif choice == '2':
                user_id = login_user()
                if user_id:
                    print("Login successful!")
                else:
                    print("Login failed. Please try again.")
            elif choice == '3':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice, please try again.")

        # Main menu options after login
        else:
            if choice == '1':
                add_transaction(user_id)
            elif choice == '2':
                update_transaction(user_id)
            elif choice == '3':
                delete_transaction(user_id)
            elif choice == '4':
                list_transactions(user_id)
            elif choice == '5':
                set_budget(user_id)
            elif choice == '6':
                month = input("Enter month (MM): ")
                year = input("Enter year (YYYY): ")
                category = input("Enter category: ")
                check_budget(user_id, month, year, category)
            elif choice == '7':
                generate_monthly_report(user_id)
            elif choice == '8':
                generate_yearly_report(user_id)
            elif choice == '9':
                user_id = None
                print("Logged out successfully.")
            elif choice == '10':
                print("Exiting the application.")
                break
            elif choice == '11':
                backup_data()
            elif choice == '12':
                restore_data()
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
