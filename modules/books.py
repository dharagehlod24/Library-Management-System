from modules.data import books


def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully.")


def view_books():
    if len(books) == 0:
        print("No books available.")
        return

    print("\n--- BOOKS ---")

    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Borrowed")

        print("----------------")


def search_book():
    keyword = input("Enter book title or author: ")

    found = False

    for book in books:
        if (keyword.lower() in book["title"].lower()
                or keyword.lower() in book["author"].lower()):

            print("\nID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            found = True

    if not found:
        print("Book not found.")