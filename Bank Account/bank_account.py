# Bank Account Manager: a command-line program to manage several bank accounts.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit
        self.history.append(f"{amount_to_deposit}rs. were deposited to this account.")
        print(f"After adding {amount_to_deposit} to your balance your total balance has increased to {self.balance} rs.")

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            print("Insufficient balance for the withdrawal.")
        else:
            self.balance -= amount_to_withdraw
            self.history.append(f"{amount_to_withdraw}rs. were withdrawn from this account.")
            print(f"After deducting {amount_to_withdraw} from your balance your total balance has decreased to {self.balance} rs.")

    def check_balance(self):
        print(f"Your current total balance is {self.balance} rs.")

    def view_transaction_history(self):
        if not self.history:
            print("There are no transactions.")
            return
        for position, transaction in enumerate(self.history, start=1):
            print(f"{position}. {transaction}")


def find_account(accounts, name):
    found_account = None
    for account in accounts:
        if account.owner == name:
            found_account = account
    return found_account


def get_account(accounts):
    name = input("Enter your name: ")
    account = find_account(accounts, name)
    if account is None:
        print("First create an account.")
    return account


def get_amount(prompt):
    try:
        amount = int(input(prompt))
    except ValueError:
        print("Please enter a whole number.")
        return None
    if amount <= 0:
        print("The amount must be greater than 0.")
        return None
    return amount


accounts = []

while True:
    print('''
1. Create an account
2. Deposit
3. Withdraw
4. Check balance
5. View transaction history
6. Quit
''')
    command = input("Enter your command: ")
    if command == "1":
        name = input("Enter your name: ")
        if find_account(accounts, name) is not None:
            print("There is already an existing account with that name.")
        else:
            accounts.append(BankAccount(name))
            print(f"{name} your account has been created successfully.")

    elif command == "2":
        account = get_account(accounts)
        if account is not None:
            amount = get_amount("Enter the amount you want to deposit: ")
            if amount is not None:
                account.deposit(amount)

    elif command == "3":
        account = get_account(accounts)
        if account is not None:
            amount = get_amount("Enter the amount you want to withdraw: ")
            if amount is not None:
                account.withdraw(amount)

    elif command == "4":
        account = get_account(accounts)
        if account is not None:
            account.check_balance()

    elif command == "5":
        account = get_account(accounts)
        if account is not None:
            account.view_transaction_history()

    elif command == "6":
        print("BYE!")
        break

    else:
        print("Enter a command number associated with the respective action you want to do.")