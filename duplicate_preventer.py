from storage import save_contacts, load_contacts

def duplicate_preventer(phone_number):
    contacts = load_contacts()
    for contact in contacts:
        if phone_number == contact['phone_number']:
            print("Contact Already Exits")
            return True
    return False