# Contact Book (Command Line)

A simple contact book you run in the terminal. Add, view, search and delete contacts, and they are saved to a file, so they are still there the next time you open the program.

## Features
- Add a contact with a name and phone number
- View all contacts as a numbered list
- Search by name (not case-sensitive)
- Delete a contact by its number
- Contacts are saved automatically in `contacts.json`
- Handles bad input (letters instead of numbers, numbers outside the list, empty list)

## How to run
1. Install Python 3.8 or newer from python.org
2. Download `contact_book.py`
3. Run: `python contact_book.py`

`contacts.json` is created automatically the first time you add a contact. No extra libraries are needed.

## Example
```
1. Add a contact
2. View all contacts
3. Search for a contact
4. Delete a contact
5. Quit

Enter the command number: 1
Enter the name of the contact: Ali
Enter the number of the contact: 0300-1234567
Contact Ali - 0300-1234567 has been added to the contact book.
```

## What I practiced
- Lists and dictionaries to store contacts
- Functions, one for each menu option
- Reading and writing JSON files
- `try`/`except` to handle bad input without crashing
- A flag variable to report whether a search found a match

## Possible improvements
- Let search match part of a name
- Add an edit option to change a number
- Store extra details like email or address