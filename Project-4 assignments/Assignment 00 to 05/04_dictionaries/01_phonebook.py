print("01_phonebook\n")

def add_contact(phonebook):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    if name in phonebook:
        print(f"{name} already exists in the phonebook.")
    else:
        phonebook[name] = phone
        print(f"Contact {name} added with phone number.")

def search_contact(phonebook):
    name = input("Enter contact name to search: ")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} not found in the phonebook.")

def del_contact(phonebook):
    name = input("Enter contact name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"{name} not found in the phonebook.")


def display_contacts(phonebook):
    if phonebook:
        print("\n Phonebook contacts")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
        else:
            print("Phonebook is empty.")

if __name__ == "__main__":
    # Initialize the phonebook dictionary
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            del_contact(phonebook)
        elif choice == '4':
            display_contacts(phonebook)
        elif choice == '5':
            print("Exiting the phonebook program.")
            break
        else:
            print("Invalid choice. Please try again.")