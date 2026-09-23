# Workflow Diagram

## Library Management System Workflow

```text
Start
  |
  v
Display Main Menu
  |
  v
User Selects an Option
  |
  +---- Add Book ------> Save Book ------+
  |                                      |
  +---- View Books ----------------------+
  |                                      |
  +---- Search Book ---------------------+
  |                                      |
  +---- Add Member ----> Save Member ---+
  |                                      |
  +---- View Members --------------------+
  |                                      |
  +---- Borrow Book ---> Check Book -----+
  |                                      |
  +---- Return Book ---> Update Book ----+
                                         |
                                         v
                                  Display Result
                                         |
                                         v
                                  Return to Menu
                                         |
                                         v
                                       Exit