# System Architecture

The Library Management System follows a simple modular architecture. The system is divided into separate Python modules, with each module responsible for a specific part of the application. This makes the program easier to understand, maintain, and modify.

## Main Components

### 1. main.py

The `main.py` file is the main entry point of the application. It displays the library menu, accepts the user's choice, and calls the appropriate function from the required module.

### 2. books.py

The `books.py` module handles all book-related operations.

It provides functions to:

- Add a new book
- View all books
- Search for a book
- Check the availability of a book

### 3. members.py

The `members.py` module manages library member information.

It provides functions to:

- Add a new member
- View registered members

### 4. transactions.py

The `transactions.py` module manages book transactions.

It handles:

- Borrowing books
- Returning books
- Updating the availability status of books
- Recording transactions

### 5. data.py

The `data.py` module acts as the basic data storage for the application. It contains lists that store:

- Book records
- Member records
- Transaction records

### 6. utils.py

The `utils.py` module contains utility functions used by the system. Currently, it is responsible for displaying the main menu to the user.

## Module Interaction

The modules work together to complete library operations.

The basic flow of the system is:

```text
                 User
                   |
                   v
                main.py
                   |
        +----------+----------+
        |          |          |
        v          v          v
     books.py  members.py  transactions.py
        |          |          |
        +----------+----------+
                   |
                   v
                data.py
                   
                utils.py
                   |
                   v
             Display Menu