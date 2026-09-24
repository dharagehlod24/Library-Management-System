from modules.data import books, members, transactions


def borrow_book():
    book_id = input("Enter book ID: ")
    member_id = input("Enter member ID: ")

    book = None
    member = None

    for b in books:
        if b["id"] == book_id:
            book = b

    for m in members:
        if m["id"] == member_id:
            member = m

    if book is None:
        print("Book not found.")
        return

    if member is None:
        print("Member not found.")
        return

    if book["available"] == False:
        print("Book is already borrowed.")
        return

    book["available"] = False

    transaction = {
        "book_id": book_id,
        "member_id": member_id,
        "type": "Borrow"
    }

    transactions.append(transaction)

    print("Book borrowed successfully.")


def return_book():
    book_id = input("Enter book ID: ")

    book = None

    for b in books:
        if b["id"] == book_id:
            book = b

    if book is None:
        print("Book not found.")
        return

    if book["available"] == True:
        print("Book is already available.")
        return

    book["available"] = True

    transaction = {
        "book_id": book_id,
        "type": "Return"
    }

    transactions.append(transaction)

    print("Book returned successfully.")