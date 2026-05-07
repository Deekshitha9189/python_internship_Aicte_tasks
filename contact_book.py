contacts = {}

while True:

    print("\n📒 CONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add contact
    if choice == "1":

        name = input("Enter name: ")
        number = input("Enter phone number: ")

        contacts[name] = number

        print("✅ Contact added!")

    # View contacts
    elif choice == "2":

        if len(contacts) == 0:
            print("No contacts available.")

        else:
            print("\n📋 Contact List:")

            for name, number in contacts.items():
                print(f"{name} : {number}")

    # Search contact
    elif choice == "3":

        search = input("Enter contact name: ")

        if search in contacts:
            print(f"{search}'s Number:", contacts[search])

        else:
            print("❌ Contact not found")

    # Delete contact
    elif choice == "4":

        delete = input("Enter contact name to delete: ")

        if delete in contacts:

            contacts.pop(delete)

            print("❌ Contact deleted")

        else:
            print("Contact not found")

    # Exit
    elif choice == "5":

        print("👋 Exiting Contact Book")
        break

    else:
        print("Invalid choice")