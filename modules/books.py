from modules.data import books


def add_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        print("Book ID already exists.")
        return

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

    print("Book added successfully.")