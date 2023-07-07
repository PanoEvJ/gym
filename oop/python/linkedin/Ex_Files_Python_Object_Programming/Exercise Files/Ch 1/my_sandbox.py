# Create a Book class
# Assign instance variables and instace methods
# Assign class variables and class methods
# Assign static variables and static methods
# Create another class and typecheck

class Book:
    
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

print(Book)

b1 = Book("The Jitterbug Perfume", 23, 304)
print(b1)
print(type(b1))
print(isinstance(b1, Book))

print("Book: \n title {}, \n price{}, \n pages{}".format(b1.title, b1.price, b1.pages))
print(f"Book: \n title {b1.title}, \n price{b1.price}, \n pages{b1.pages}")