from storage import save_contacts, load_contacts

def add_contact(name, email, phone_number, address):
    contacts = load_contacts()
    contact = {
        'name' : name,
        'email' : email,
        'phone_number' : phone_number,
        'address' : address
    }
    contacts.append(contact)
    save_contacts(contacts)




                  
