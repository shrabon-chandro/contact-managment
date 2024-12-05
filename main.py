from add_contact import add_contact
from duplicate_preventer import duplicate_preventer
from view_contact import view_contact
from remove_contact import remove_contact
from search_contact import search_contact, load_contacts

while True:
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

    option = input("Enter you Choice : ")

    if option == "1":
        print("Add Contact Here ........")
        name=input("Enter your name : ")
        email=input("Enter your Email: ")
        phone_number=int(input("Enter your phone number : "))
        if duplicate_preventer(phone_number):
            continue
        address = input("Enter Address: ")
        add_contact(name, email, phone_number, address)
        print("Contact added successfully")

    elif option == "2":
        view_contact()
    elif option == "3":
        serial= int(input("Enter Serial Number : "))
        remove_contact(serial)
    elif option == "4":
        phone_number = input("Enter Phone Number: ")
        search_contact(phone_number)
    elif option == "5":
        print("Exiting Contact book Program")
        break
    else:
        print("Invalid choice")
    