# CODSOFT/Python programming internship/Task 5/Contact Book

import json

class ContactBook:
    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contacts()
            print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print('-' * 30)

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for name, info in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in info['phone']:
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print('-' * 30)
                found = True
        if not found:
            print("No contact found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            print("Leave field empty to keep current value.")
            phone = input(f"Enter new phone number ({self.contacts[name]['phone']}): ") or self.contacts[name]['phone']
            email = input(f"Enter new email address ({self.contacts[name]['email']}): ") or self.contacts[name]['email']
            address = input(f"Enter new address ({self.contacts[name]['address']}): ") or self.contacts[name]['address']
            
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def show_menu(self):
        while True:
            print("\n-------Contact Book-------")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.show_menu()
