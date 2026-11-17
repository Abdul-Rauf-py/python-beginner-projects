# Bank Account Manager (GUI): create accounts, deposit, withdraw, check balance
# and view history in a tkinter window.
import tkinter as tk


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit
        self.history.append(f"{amount_to_deposit}rs. were deposited to this account.")
        output_label.config(text=f"{amount_to_deposit}rs. were deposited in your account.")

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            output_label.config(text="Insufficient balance for the withdrawal.")
        else:
            self.balance -= amount_to_withdraw
            self.history.append(f"{amount_to_withdraw}rs. were withdrawn from this account.")
            output_label.config(text=f"{amount_to_withdraw}rs. were withdrawn from your account.")

    def check_balance(self):
        output_label.config(text=f"Your current total balance is {self.balance} rs.")

    def view_transaction_history(self):
        if not self.history:
            output_label.config(text="There are no transactions.")
            return
        lines = []
        for position, transaction in enumerate(self.history, start=1):
            lines.append(f"{position}. {transaction}")
        output_label.config(text="\n".join(lines))


def find_account(accounts, name):
    found_account = None
    for account in accounts:
        if account.owner == name:
            found_account = account
    return found_account


def get_account(accounts):
    name = name_entry.get()
    account = find_account(accounts, name)
    if account is None:
        output_label.config(text="First create an account.")
    return account


def get_amount():
    try:
        amount = int(amount_entry.get())
    except ValueError:
        output_label.config(text="Please enter a whole number in the Amount box.")
        return None
    if amount <= 0:
        output_label.config(text="The amount must be greater than 0.")
        return None
    return amount


accounts = []


def on_account_create():
    name = name_entry.get()
    if find_account(accounts, name) is not None:
        output_label.config(text="There is already an existing account with that name.")
    else:
        accounts.append(BankAccount(name))
        output_label.config(text=f"{name} your account has been created successfully.")


def on_money_deposit():
    account = get_account(accounts)
    if account is not None:
        amount = get_amount()
        if amount is not None:
            account.deposit(amount)


def on_money_withdraw():
    account = get_account(accounts)
    if account is not None:
        amount = get_amount()
        if amount is not None:
            account.withdraw(amount)


def on_balance_check():
    account = get_account(accounts)
    if account is not None:
        account.check_balance()


def on_view_history():
    account = get_account(accounts)
    if account is not None:
        account.view_transaction_history()


root = tk.Tk()
root.title("Bank Account Manager")
root.geometry("400x380")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

output_label = tk.Label(root, text="", wraplength=350, justify="left")
output_label.pack()

button_to_create_account = tk.Button(root, text="Create Account", command=on_account_create)
button_to_create_account.pack()
button_to_deposit_money = tk.Button(root, text="Deposit Money", command=on_money_deposit)
button_to_deposit_money.pack()
button_to_withdraw_money = tk.Button(root, text="Withdraw Money", command=on_money_withdraw)
button_to_withdraw_money.pack()
button_to_check_balance = tk.Button(root, text="Check Balance", command=on_balance_check)
button_to_check_balance.pack()
button_to_see_history = tk.Button(root, text="View Transaction History", command=on_view_history)
button_to_see_history.pack()

root.mainloop()
