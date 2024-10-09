# Contact Manager

# Dictionary to store contacts
contacts = {}

def display_menu():
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("\nEnter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter contact address: ")
    
    if name in contacts:
        print("This contact already exists. Try updating it instead.")
    else:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}")

def search_contact():
    search_term = input("\nEnter the name or phone number to search: ")
    found = False
    
    for name, info in contacts.items():
        if search_term == name or search_term == info['Phone']:
            print(f"\nContact found:\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}")
            found = True
            break

    if not found:
        print("No contact found with that name or phone number.")

def update_contact():
    name = input("\nEnter the name of the contact to update: ")
    
    if name in contacts:
        print("\nExisting contact details:")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
        
        print("\nEnter new details (press Enter to keep current value):")
        phone = input("New Phone (Leave blank to keep current): ") or contacts[name]['Phone']
        email = input("New Email (Leave blank to keep current): ") or contacts[name]['Email']
        address = input("New Address (Leave blank to keep current): ") or contacts[name]['Address']
        
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a valid number (1-6).")

if __name__ == "__main__":
    main()
