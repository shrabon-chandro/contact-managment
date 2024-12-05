import json

def save_contacts(contacts):
    with open('contacts.json', mode="w") as info:
        json.dump(contacts, info, indent=4)

def load_contacts():
    with open('contacts.json', mode="r") as info:
        return json.load(info)