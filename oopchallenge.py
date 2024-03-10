"""Create a simple Object-Oriented Program (OOP) that simulates a basic library management system. 
This system will manage books and allow users to check out and return books
"""


class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        

    def check_out(self):
            return True or FALSE

    def return_book(self):
            return True or FALSE

mylibrary=Book("River","Jane B","Rt00we")

print(mylibrary.title)
print(mylibrary.author)
print(mylibrary.isbn)
print(mylibrary.check_out())
print(mylibrary.return_book())
