import tkinter as tk


class Bank_account:
    def __init__ (self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.history=[]

    def deposit(self,amount_to_deposit):
        self.balance += amount_to_deposit
        self.history.append(f"{amount_to_deposit}rs. were deposited to this account.")   
        output_label.config(text=f"{amount_to_deposit}rs. were deposited in your account.")

    def withdraw(self,amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            output_label.config(text="Insufficient balance for the withdrawl.")
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
        lines=[]       
        for position,transaction in enumerate(self.history,start=1):
            lines.append(f"{position}. {transaction}")
        full_lines='\n'.join(lines)
        output_label.config(text=full_lines)

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

accounts=[]

def on_account_create():
    found=False
    name=name_entry.get()
    for i in accounts:
        if i.owner == name:
            found=True
    if found == True:
        output_label.config(text="There is already an existing account with that name.")
    elif found == False:
        accounts.append(Bank_account(name))
        output_label.config(text=f"{name} your account has been created successfully.")

def on_money_deposit():
    account = get_account(accounts)
    if account is not None:
        amount_for_deposition = int(amount_entry.get())
        account.deposit(amount_for_deposition)

def on_money_withdraw():
    account = get_account(accounts)
    if account is not None:
        amount_for_withdrawl = int(amount_entry.get())
        account.withdraw(amount_for_withdrawl)

def on_balance_check():
    account = get_account(accounts)
    if account is not None:    
        account.check_balance()

def on_view_histroy():
    account = get_account(accounts)
    if account is not None:
        account.view_transaction_history()

root=tk.Tk()
root.title("Bank Account Manager")
root.geometry("400x300")

name_label=tk.Label(root , text = "Name:")
name_label.pack()
name_entry=tk.Entry(root)
name_entry.pack()

amount_label=tk.Label(root , text = "Amount:")
amount_label.pack()
amount_entry=tk.Entry(root)
amount_entry.pack()

output_label=tk.Label(root , text="" , wraplength=350 , justify="left")
output_label.pack()


button_to_create_account=tk.Button(root , text = "Create Account." , command = on_account_create)
button_to_create_account.grid()
button_to_deposit_money=tk.Button(root , text = "Deposit Money." , command = on_money_deposit)
button_to_deposit_money.grid()
button_to_withdraw_money=tk.Button(root , text = "Withdraw Money." , command = on_money_withdraw)
button_to_withdraw_money.grid()
button_to_check_balance=tk.Button(root , text = "Check Balance." , command = on_balance_check)
button_to_check_balance.grid()
button_to_see_histroy=tk.Button(root , text = "View Transaction Histroy." , command = on_view_histroy)
button_to_see_histroy.grid()

root.mainloop()