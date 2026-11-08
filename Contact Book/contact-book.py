# Contact Book: a command-line app to add, view, search and delete contacts, saved in a JSON file.

import json

def load_data():
    try:
        with open("contacts.json",'r') as c:
            return json.load(c)
    except FileNotFoundError:
        return []

def save_data(contacts):
    with open("contacts.json",'w') as c:
        json.dump(contacts,c,indent=2)

def add(contacts):
    name=input("Enter the name of the contact: ")
    number=input("Enter the number of the contact: ")
    contacts.append({"name":name,"number":number})
    save_data(contacts)
    print(f"Contact {name} - {number} has been added to the contact book.")

def view(contacts):
    if not contacts:
        print("No contacts saved yet.")
        return
    for position,contact in enumerate(contacts,start=1):
        print(f"{position}. {contact['name']} - {contact['number']}")

def search(contacts):
    if not contacts:
        print("Nothing to search.")
        return
    contact_to_find=input("Enter the contact name you are looking for: ")
    found = False
    for contact in contacts:
        cont = contact["name"]
        if cont.lower() in contact_to_find.lower():
            print(contact["name"] ,"-", contact["number"] )
            found = True
    if not found:
        print("No the contact is not in your contact book.")

def delete(contacts):
    if not contacts:
            print("Nothing to delete.")
            return
    try:
        view(contacts)
        contact_to_delete=int(input("Enter the number designated to the contact you want to delete: "))
        if contact_to_delete < 1 or contact_to_delete > len(contacts):
            print("That number isn't on the list.")
            return
        else:
            contacts.pop(contact_to_delete-1)
            save_data(contacts)
    except (IndexError,ValueError):
        print("Only write the number behinde the contact you want to delete or make a list then try deleting.")

contacts=load_data()
while True:
    print('''
1. Add a contact
2. View all contacts
3. Search for a contact
4. Delete a contact
5. Quit
''')
    command=input("Enter the command number: ")
    if command=='1':
        add(contacts)
    elif command=='2':
        view(contacts)
    elif command=='3':
        search(contacts)
    elif command=='4':
        delete(contacts)
    elif command=='5':
        print("Bye!")
        break
    else:
        print("Please choose a number from 1 to 5.")