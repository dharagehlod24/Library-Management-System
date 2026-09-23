from modules.books import add_book, view_books, search_book
from modules.members import add_member, view_members
from modules.transactions import borrow_book, return_book


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. View Members")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        add_member()

    elif choice == "5":
        view_members()

    elif choice == "6":
        borrow_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice.")