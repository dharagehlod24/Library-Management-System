# Class Diagram

The project uses modules and dictionaries instead of Python classes.

## Book

- ID
- Title
- Author
- Availability

## Member

- ID
- Name

## Transaction

- Book ID
- Member ID
- Transaction Type

## Modules

Books:
- add_book()
- view_books()
- search_book()

Members:
- add_member()
- view_members()

Transactions:
- borrow_book()
- return_book()

Utils:
- show_menu()