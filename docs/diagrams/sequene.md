# Sequence Diagram

## Borrow Book Process

```text
User
 |
 | Select Borrow Book
 v
main.py
 |
 | Call borrow_book()
 v
transactions.py
 |
 | Check Book
 v
data.py
 |
 | Book Available
 v
transactions.py
 |
 | Update Book Status
 v
data.py
 |
 | Success
 v
transactions.py
 |
 | Display Result
 v
User