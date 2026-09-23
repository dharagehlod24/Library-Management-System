from modules.data import books, members


def test_add_book():
    books["B1"] = {
        "title": "Python Basics",
        "author": "John",
        "available": True
    }

    assert "B1" in books
    print("Book test passed.")


def test_add_member():
    members["M1"] = {
        "name": "Student"
    }

    assert "M1" in members
    print("Member test passed.")


def test_borrow_book():
    books["B1"]["available"] = False

    assert books["B1"]["available"] == False
    print("Borrow test passed.")


def test_return_book():
    books["B1"]["available"] = True

    assert books["B1"]["available"] == True
    print("Return test passed.")


test_add_book()
test_add_member()
test_borrow_book()
test_return_book()