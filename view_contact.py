from storage import load_contacts
def view_contact():
    contacts = load_contacts()
    print("View Contact list")
    for sl, contact in enumerate (contacts, start=1): 
        print(f" {sl}. Name: {contact['name']} | E-mail : {contact['email']} | Phone Number : {contact['phone_number']} | Address :{contact['address']}\n ")
