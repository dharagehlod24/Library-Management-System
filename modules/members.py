from modules.data import members


def add_member():
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")

    member = {
        "id": member_id,
        "name": name
    }

    members.append(member)

    print("Member added successfully.")


def view_members():
    if len(members) == 0:
        print("No members available.")
        return

    print("\n--- MEMBERS ---")

    for member in members:
        print("ID:", member["id"])
        print("Name:", member["name"])
        print("----------------")