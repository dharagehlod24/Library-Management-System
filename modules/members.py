from modules.data import members


def add_member():
    member_id = input("Enter member ID: ")

    if member_id in members:
        print("Member ID already exists.")
        return

    name = input("Enter member name: ")

    if name == "":
        print("Member name cannot be empty.")
        return

    members[member_id] = {
        "name": name
    }

    print("Member added successfully.")