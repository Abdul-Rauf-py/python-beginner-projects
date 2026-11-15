# Bank Account Manager (GUI)

The bank account program from my terminal project, rebuilt with a graphical window using Python's tkinter.

## Features
- Enter a name and an amount in text boxes
- Buttons to create an account, deposit, withdraw, check balance and view history
- Results appear in the window
- Multiple accounts, each with its own balance and history

## How to run
1. Install Python 3.8 or newer from python.org
2. Download `bank_account_gui.py`
3. Run: `python bank_account_gui.py`

tkinter comes with the standard Windows installer, so nothing else is needed.

## Note
Accounts are kept in memory only, so they are lost when the window closes.

## What I practiced
- Building a window with labels, entry boxes and buttons
- Connecting buttons to functions (callbacks)
- Updating a label to show results instead of printing
- Reusing a class from an earlier project

## Possible improvements
- Show a message instead of failing when the amount isn't a number
- Reject negative amounts
- Keep the class free of GUI code by having its methods return messages
- Save accounts to a file