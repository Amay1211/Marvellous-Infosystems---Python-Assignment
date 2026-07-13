# 1: Write a Python program to implement a class named BookStore with the following
# specifications:
# • The class should contain two instance variables:
# ◦ Name (Book Name)
# ◦ Author (Book Author)
# • The class should contain one class variable:
# ◦ NoOfBooks (initialize it to 0)
# • Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
# • Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is
# created.
# • Implement an instance method:
# ◦ Display() – should display book details in the format:
# <BookName> by <Author>. No of books: <NoOfBooks>

# Example usage:
# Obj1 = BookStore("Linux System Programming", "Robert Love")
# Obj1.Display() # Linux System Programming by Robert Love. No of
# books: 1
# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2

class BookStore:
  noOfBooks = 0

  def __init__(self, bookName, author):
    self.bookName = bookName
    self.author = author 
    BookStore.noOfBooks = BookStore.noOfBooks + 1

  def display(self):
    print(f"{self.bookName} by {self.author}. No of books: {self.noOfBooks}")

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.display() # Linux System Programming by Robert Love. No of

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.display() # C Programming by Dennis Ritchie. No of books: 2

obj3 = BookStore("Linux System Programming", "Robert Love")
obj1.display() # Linux System Programming by Robert Love. No of 3

obj4 = BookStore("C Programming", "Dennis Ritchie")
obj2.display() # C Programming by Dennis Ritchie. No of books: 4
