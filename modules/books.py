from modules.data import books


def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

    print("Book added successfully.")


def view_books():
    if not books:
        print("No books available.")
        return

    for book_id, book in books.items():
        print(book_id, "-", book["title"], "-", book["author"])


def search_book():
    title = input("Enter book title: ")

    for book in books.values():
        if book["title"].lower() == title.lower():
            print("Book found:", book["title"], "-", book["author"])
            return

    print("Book not found.")