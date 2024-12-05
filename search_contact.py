from storage import load_contacts

def search_contact(phone_number):
    contacts = load_contacts()
    details = []
    for contact in contacts:
        if phone_number == contact['phone_number']:
            details.append(contact)
            print(f" Name : {contact['name']} | Email : {contact['email']} | Phone Number : {contact['phone_number']} | Address{contact['address']}\n")
        