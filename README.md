# Library Management System

## Introduction

The Library Management System is a basic Python-based application developed to manage the daily operations of a library.

The system provides a simple menu-driven interface through which users can manage books, library members, and book transactions. It demonstrates the use of Python functions, modules, dictionaries, lists, conditional statements, and user input.

## Objectives

The main objectives of this project are:

- To maintain basic information about library books.
- To manage library member information.
- To allow users to search for books.
- To keep track of book availability.
- To manage borrowing and returning of books.
- To demonstrate modular programming using Python.

## Features

### 1. Add Book

Allows the user to add a new book by entering its book ID, title, and author name. The book is stored with an available status.

### 2. View Books

Displays all books currently stored in the system along with their ID, title, author, and availability status.

### 3. Search Book

Allows the user to search for a book using its title or author name.

### 4. Add Member

Allows the user to register a new library member using a member ID and name.

### 5. View Members

Displays the list of registered library members along with their member IDs and names.

### 6. Borrow Book

Allows a registered member to borrow an available book. The system checks whether the book and member exist and whether the book is available.

### 7. Return Book

Allows a borrowed book to be returned. The availability status of the book is updated after the return.

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

## Project Modules

### main.py

The main program controls the entire application. It displays the menu and calls the appropriate function based on the user's choice.

### books.py

This module manages all book-related operations.

Functions include:

- `add_book()`
- `view_books()`
- `search_book()`

### members.py

This module manages library member information.

Functions include:

- `add_member()`
- `view_members()`

### transactions.py

This module manages book borrowing and returning operations.

Functions include:

- `borrow_book()`
- `return_book()`

### data.py

This module stores the main data collections used by the application, including books, members, and transactions.

### utils.py

This module contains the function used to display the main menu of the application.

## Data Management

The system uses Python lists and dictionaries to store information.

Book information includes:

- Book ID
- Book Title
- Author
- Availability Status

Member information includes:

- Member ID
- Member Name

Transaction information includes:

- Book ID
- Member ID
- Transaction Type

## How to Run

Make sure Python is installed on the system.

Open the project folder in the terminal and run:

```text
python main.py