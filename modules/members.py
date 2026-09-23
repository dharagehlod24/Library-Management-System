from modules.data import members


def add_member():
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")

    members[member_id] = {
        "name": name
    }

    print("Member added successfully.")


def view_members():
    if not members:
        print("No members available.")
        return

    for member_id, member in members.items():
        print(member_id, "-", member["name"])