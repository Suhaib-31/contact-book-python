import os

FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")

    print("Contact Added Successfully!")

def view_contacts():
    if not os.path.exists(FILE_NAME):
        print("No contacts found!")
        return

    print("\nContact List")
    print("-" * 30)

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            print(f"Name: {name} | Phone: {phone}")

def search_contact():
    keyword = input("Enter Name to Search: ")

    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")

                if keyword.lower() in name.lower():
                    print(f"Found: {name} | {phone}")
                    found = True

    if not found:
        print("Contact not found!")

def delete_contact():
    keyword = input("Enter Name to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("No contacts available!")
        return

    contacts = []

    with open(FILE_NAME, "r") as file:
        contacts = file.readlines()

    with open(FILE_NAME, "w") as file:
        deleted = False

        for contact in contacts:
            if not contact.lower().startswith(keyword.lower() + ","):
                file.write(contact)
            else:
                deleted = True

    if deleted:
        print("Contact Deleted Successfully!")
    else:
        print("Contact not found!")

while True:

    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")