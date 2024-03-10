class Library:
    def __init__(self,title, author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def add_book(self):
        title=input("title: ")
        author=input("authr: ")
        isbn=input("isbn: ")
        return title,author,isbn

    def remove_book(self, isbn):
          if book not in self.isbn:
            return print("Book not found")

    def check_out_book(self, isbn):
            if book not in self.isbn:
                return print("Book already checked out") 



book=Library("River","Jane B","Rt01we")
# book2=Library("Rain","James k","Rt02we")
# book3=Library("Cloud","peter m","Rt03we")
# book4=Library("River","dan d","Rt04we")
# book5=Library("River","mary j","Rt05we")

   
print(book.title)
print(book.author)
print(book.isbn)
   
  
