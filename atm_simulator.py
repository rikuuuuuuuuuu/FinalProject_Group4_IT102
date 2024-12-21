# ATM Simulator - Final Project
# Group 4 (BUSTAMANTE, GARCIA, MAHINAY, RAMOS, SANTIAGO)

# imports the datetime module to access the current date and time for transaction logging.
from datetime import datetime

# variables
balance = 100000  # initial account balance
budgetcategories = []  # list for budget categories
budgetlimits = []  # list for corresponding budget limits
expenses = []  # list to track expenses

# transaction history storage
transactions = []  # stores transaction history
users = []  # stores registered users

# USER MANAGEMENT Module (RAMOS)
def register():
    username = input("Enter username: ")
    for user in users:
        if user['username'] == username:  # check if username already exists
            print("Username already exists!")
            return

    while True:
        pin = input("Enter a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():  # validate PIN
            users.append({'username': username, 'pin': pin})  # add user
            print("Account created!")
            return
        else:
            print("PIN must be a 4-digit number.")

def login():
    username = input("Enter username: ")
    pin = input("Enter your 4-digit PIN: ")
    for user in users:
        if user['username'] == username and user['pin'] == pin:  # check username and PIN
            print(f"Welcome, {username}!")
            return True
    print("Invalid username or PIN!")
    return False

# TRANSACTION HISTORY Module (MAHINAY)
def add_transaction(transaction_type, amount, category=None):
    # create a transaction record with details and add to the transaction history
    transaction = {
        'type': transaction_type,
        'amount': amount,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'category': category
    }
    transactions.append(transaction)

def view_transaction_history():
    if not transactions:  # check if no transactions exist
        print("No transactions found.")
        return
    
    print("\n---- Transaction History ----")
    for transaction in transactions:
        # print each transaction with details
        print(f"{transaction['date']} - {transaction['type']} - \u20b1{transaction['amount']:.2f} - Category: {transaction['category'] if transaction['category'] else 'N/A'}")
    print("-----------------------------")

def print_receipt(transaction_type, amount, balance, category=None):
    # print transaction receipt
    print("\n------ Receipt ------")
    print(f"Transaction Type: {transaction_type}")
    print(f"Amount: \u20b1{amount:.2f}")
    print(f"Current Balance: \u20b1{balance:.2f}")
    if category:
        print(f"Category: {category}")
    print("--------------------")

# BUDGET TRACKER Module (SANTIAGO)
def set_budget():
    category = input("Enter budget category: ")
    
    while True:
        try:
            limit = float(input(f"Enter budget limit for {category}: "))  # input and validate budget limit
            budgetcategories.append(category)  # add category
            budgetlimits.append(limit)  # add limit
            break
        except ValueError:
            print("Please enter a valid number for the budget limit.")

def add_expense():
    if not budgetcategories:  # check if no budgets are set
        print("Please set a budget first!")
        return
    
    print("\nAvailable Budget Categories:")
    for i, category in enumerate(budgetcategories):
        print(f"{i + 1}. {category}")  # display available budget categories
    
    category_index = int(input("Select category number: ")) - 1  # get selected category
    category = budgetcategories[category_index]
    
    expense_amount = float(input(f"Enter expense amount for {category}: "))  # input expense
    
    expenses.append({
        'category': category,
        'amount': expense_amount
    })
    
    add_transaction('Expense', expense_amount, category)  # log expense as a transaction

# ATM OPERATIONS Module (BUSTAMANTE)
def atm_operations():
    global balance
    
    while True:
        print("\nHello! Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Print a Receipt")
        print("5. Return to Main Menu")
        
        choice = int(input("Please select a number: "))
        
        if choice == 1:
            print(f"\nYour current balance is: \u20b1{balance:.2f}")  # display balance
            add_transaction('Balance Check', 0)  # log balance check transaction
        
        elif choice == 2:
            deposit = float(input("Enter the amount to deposit: "))
            if deposit > 0:
                balance += deposit  # update balance after deposit
                print(f"\u20b1{deposit:.2f} has been deposited successfully.")
                add_transaction('Deposit', deposit)  # log deposit transaction
            else:
                print("Invalid amount. Please enter a positive number.")
        
        elif choice == 3:
            withdraw = float(input("Enter the amount to withdraw: "))
            if withdraw > balance:  # check for sufficient balance
                print("Insufficient balance. Please try a smaller amount.")
            elif withdraw <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                balance -= withdraw  # update balance after withdrawal
                print(f"\u20b1{withdraw:.2f} has been withdrawn successfully.")
                add_transaction('Withdrawal', withdraw)  # log withdrawal transaction
        
        elif choice == 4:
            print("\n------ ATM Receipt ------")
            print(f"Your account Balance is: \u20b1{balance:.2f}")  # print receipt with balance
            print("-------------------------")
            print("Thank you for using our ATM!")
        
        elif choice == 5:
            break  # exit ATM operations
        
        else:
            print("\nInvalid choice. Kindly choose the (action) number you desire to use from 1 to 5.")

# MAIN MENU (GARCIA)
def main_menu():
    while True:
        # display main menu options
        print("\n--- ATM Simulator Main Menu ---")
        print("1. Login")
        print("2. Register")
        print("3. ATM Operations")
        print("4. Budget Tracker")
        print("5. Transaction History")
        print("6. Exit")
        
        # get user input
        choice = input("Enter your choice: ")
        
        # process user input
        if choice == '1':
            if login():
                pass
        elif choice == '2':
            register()
        elif choice == '3':
            atm_operations()
        elif choice == '4':
            budget_tracker_menu()
        elif choice == '5':
            view_transaction_history()
        elif choice == '6':
            print("Thank you for using ATM Simulator!")  # exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # invalid input handling

# BUDGET TRACKER MENU
def budget_tracker_menu():
    while True:
        print("\n1. Set Budget")
        print("2. Add Expense")
        print("3. Exit")
        
        choice = input("Enter number of your choice: ")
        
        if choice == '1':
            set_budget()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            break  # exit budget tracker menu
        else:
            print("Invalid number. Please try again.")  # invalid input handling

# MAIN PROGRAM ENTRY POINT
if __name__ == "__main__":
    main_menu()  # start the main menu
