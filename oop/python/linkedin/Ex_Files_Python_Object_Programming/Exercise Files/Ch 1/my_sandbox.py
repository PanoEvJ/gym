# Create a Book class
# Assign instance variables and instace methods
# Assign class variables and class methods
# Assign static variables and static methods
# Create another class and typecheck

class Book:
    BOOKTYPE = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages
        
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price * (1 - self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount
        
    @classmethod
    def getbooktypes(cls):
        return Book.BOOKTYPE

print(Book)

b1 = Book("The Jitterbug Perfume", 23, 304)

print(b1)
print(type(b1))
print(isinstance(b1, Book))

print("Book: \n title {}, \n price{}, \n pages{}".format(b1.title, b1.price, b1.pages))
print(f"Book: \n title {b1.title}, \n price{b1.price}, \n pages{b1.pages}")

print(b1.getprice())

prc1 = b1.getprice
print(type(prc1))

print(isinstance(prc1, object))

print(b1.getprice())
b1.setdiscount(0.3)
print(b1.getprice())

print(Book.BOOKTYPE)
print("Book types: ", Book.getbooktypes())

