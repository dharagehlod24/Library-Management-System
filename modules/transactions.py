from modules.data import books, members


def borrow_book():
    book_id = input("Enter book ID: ")
    member_id = input("Enter member ID: ")

    if book_id not in books:
        print("Book not found.")
        return

    if member_id not in members:
        print("Member not found.")
        return

    if not books[book_id]["available"]:
        print("Book is already borrowed.")
        return

    books[book_id]["available"] = False

    print("Book borrowed successfully.")


def return_book():
    book_id = input("Enter book ID: ")

    if book_id not in books:
        print("Book not found.")
        return

    books[book_id]["available"] = True

    print("Book returned successfully.")