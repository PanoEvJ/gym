# Using the __getattribute__ and __setattribute methods

class Book:
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price   
        self._discount = 0.1  

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1.price)