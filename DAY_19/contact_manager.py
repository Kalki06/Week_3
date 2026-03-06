contacts = [
    {"id": 1, "name": "Amit", "phone": "9876543210"},
    {"id": 2, "name": "Manjeet", "phone": "9873348821"}
]

def add_contact(contacts):
    contact_id = int(input("Enter the id of contact : "))
    name = input("Enter the name of contact : ")
    phone = input("Enter the number of contact : ")

    for contact in contacts:
        if contact["id"] == contact_id:
            print("ID already exists.")
            return

    new_contact = {
        "id": contact_id,
        "name": name,
        "phone": phone
    }

    contacts.append(new_contact)

def delete_contact(contacts):
    found = False

    contact_id = int(input("Enter the id of contact : "))
    for i in range(len(contacts)):
        if contacts[i]["id"] == contact_id:
            contacts.pop(i)
            found = True
            break

    if not found:
        print("Contact not found")

def search_contact(contacts):
    found = False

    contact_id = int(input("Enter the id of contact : "))
    for contact in contacts:
        if contact["id"] == contact_id:
            print(contact)
            found = True
            break

    if not found:
        print("Contact not found")

def show_contacts(contacts):
    if(len(contacts) == 0):
        print("Contact list is empty.")
    else:
        for contact in contacts:
            print(f"ID : {contact ['id']}")
            print(f"Name : {contact ['name']}")
            print(f"Phone : {contact ['phone']}\n")

def main():
    while True:
        print("1 Add")
        print("2 Delete")
        print("3 Search")
        print("4 Show")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            delete_contact(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            show_contacts(contacts)

        elif choice == "5":
            break

if __name__ == "__main__":
    main()