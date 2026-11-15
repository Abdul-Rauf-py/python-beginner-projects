# Bank Account Manager (Command Line)

A terminal program that manages several bank accounts, each with its own balance and transaction history. Built to practice classes and objects.

## Features
- Create accounts (each name can only be used once)
- Deposit and withdraw money
- Withdrawals are refused if the balance is too low
- Check balance
- View each account's transaction history

## How to run
1. Install Python 3.8 or newer from python.org
2. Download `bank_account.py`
3. Run: `python bank_account.py`

No extra libraries are needed.

## Note
Accounts are kept in memory only, so they are lost when the program closes.

## What I practiced
- A `BankAccount` class with its own data (owner, balance, history) and methods
- A list of objects, and a function that finds one by name
- Pulling repeated code into a helper function
- Menu loop with input checks
- Validating input with try/except, and rejecting negative amounts

## Possible improvements
- Save accounts to a JSON file
- Reject negative or zero amounts
- Handle letters typed instead of numbers