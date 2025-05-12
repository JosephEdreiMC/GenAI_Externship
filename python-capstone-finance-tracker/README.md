This project consists of an expense tracker in the form of a dictionary.
In the dictionary, the keys are 'categories' given to each transaction. Notice that a category can have multiple transactions but each transaction has a unique category.
Inside each category, there is a list of expenses with the format (description, amount), each expense is defined as a tuple to impede being edited.
The program allows using a predefined dictionary; otherwise, an empty dictionary is used. There are 4 actions that one can perform on the expense dictionary:
- Add Expense (option 1): Provide a description, a category, and an amount to add as a record in the dictionary.
- View All Expenses (option 2): It displays each transaction in the dictionary, ordered by category.
- View Summary (option 3): It displays the total amount spent on each category.
- Exit (option 4): It closes the program.

In the end, the program will return a dictionary that can be saved as a .plk file by uncommenting the final lines on the .py file. 

This program uses concepts such as dictionaries, lists, tuples, loops, if-elif-else statements, and try-except-else handling of exceptions. Furthermore, it implements modular programming, one of the most powerful characteristics of Python.
