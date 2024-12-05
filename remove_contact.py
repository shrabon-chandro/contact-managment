from storage import load_contacts, save_contacts

def remove_contact(serial):
    contacts = load_contacts()
    if 0<serial<len(contacts):
        del contacts[serial-1]
        save_contacts(contacts)
        print("Contact Deleted Successfully")
    else:
        print("Not Found")