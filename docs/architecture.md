# System Architecture

## Overview

The Library Management System is divided into three main functional modules:

1. Book Management
2. Member Management
3. Borrow and Return

## Architecture

```text
            Library Management System
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
   Book Management  Member Management  Borrow & Return
          |              |              |
          v              v              v
       books.py       members.py    transactions.py
          |              |              |
          +--------------+--------------+
                         |
                         v
                      data.py
                         |
                         v
                  Shared Library Data