import sys

def setup_phonebook():
    count = int(input("How many contacts do you want to add initially? "))
    phonebook = []
    
    for i in range(count):
        print(f"\nEnter details for contact {i+1}:")
        contact = []
        name = input("Name*: ")
        if name.strip() == "":
            sys.exit("Name is mandatory. Exiting...")
        contact.append(name)
        
        number = int(input("Phone Number*: "))
        contact.append(number)
        
        email = input("Email: ").strip() or None
        contact.append(email)
        
        dob = input("Date of Birth (dd/mm/yyyy): ").strip() or None
        contact.append(dob)
        
        category = input("Category (Family/Friends/Work/Others): ").strip() or None
        contact.append(category)
        
        phonebook.append(contact)
        
    return phonebook

def show_menu():
    print("\n--- SMARTPHONE DIRECTORY ---")
    print("1. Add new contact")
    print("2. Remove contact")
    print("3. Delete all contacts")
    print("4. Search contact")
    print("5. Show all contacts")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    return choice

def add_new_contact(pb):
    contact = []
    contact.append(input("Name: "))
    contact.append(int(input("Phone Number: ")))
    contact.append(input("Email: ").strip() or None)
    contact.append(input("Date of Birth: ").strip() or None)
    contact.append(input("Category (Family/Friends/Work/Others): ").strip() or None)
    pb.append(contact)
    return pb

def remove_contact(pb):
    query = input("Enter the name of the contact to remove: ")
    for i, c in enumerate(pb):
        if c[0] == query:
            print(pb.pop(i))
            print("Contact removed successfully.")
            return pb
    print("Contact not found.")
    return pb

def delete_all_contacts(pb):
    pb.clear()
    print("All contacts deleted.")
    return pb

def search_contact(pb):
    print("Search by: 1. Name 2. Number 3. Email 4. DOB 5. Category")
    choice = int(input("Enter choice: "))
    query = None
    results = []
    
    if choice == 1:
        query = input("Enter name: ")
        results = [c for c in pb if c[0] == query]
    elif choice == 2:
        query = int(input("Enter number: "))
        results = [c for c in pb if c[1] == query]
    elif choice == 3:
        query = input("Enter email: ")
        results = [c for c in pb if c[2] == query]
    elif choice == 4:
        query = input("Enter DOB: ")
        results = [c for c in pb if c[3] == query]
    elif choice == 5:
        query = input("Enter category: ")
        results = [c for c in pb if c[4] == query]
    else:
        print("Invalid choice")
        return
    
    if results:
        print("Search results:")
        for r in results:
            print(r)
    else:
        print("No contacts found.")

def show_all(pb):
    if not pb:
        print("Phonebook is empty.")
    else:
        for c in pb:
            print(c)

def exit_program():
    print("Thank you for using the phonebook. Goodbye!")
    sys.exit()

# Main Program
print("Welcome to your Smartphone Directory")
phonebook = setup_phonebook()

while True:
    choice = show_menu()
    if choice == 1:
        phonebook = add_new_contact(phonebook)
    elif choice == 2:
        phonebook = remove_contact(phonebook)
    elif choice == 3:
        phonebook = delete_all_contacts(phonebook)
    elif choice == 4:
        search_contact(phonebook)
    elif choice == 5:
        show_all(phonebook)
    else:
        exit_program()