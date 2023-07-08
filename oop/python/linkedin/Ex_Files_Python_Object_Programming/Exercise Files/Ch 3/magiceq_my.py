# Using the __eq__, __ge__ and __le__ magic methods

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    # TODO: the __eq__ method checks for equality between two objects

    # TODO: the __ge__ establishes >= relationship with another obj

    # TODO: the __lt__ establishes < relationship with another obj
    
b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality


# TODO: Check for greater and lesser value


# TODO: Now we can sort them too
