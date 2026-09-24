from modules.books import add_book, view_books, search_book
from modules.members import add_member, view_members
from modules.transactions import borrow_book, return_book
from modules.utils import show_menu


while True:

    show_menu()

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
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")