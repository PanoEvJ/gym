# Using the __eq__, __ge__ and __le__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title  = title
        self.author = author
        self.price  = price
    
    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book object")
        return (self.title  == value.title  and 
                self.author == value.author and
                self.price  == value.price  )

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book object")
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book object")
        # return (self.price < value.price)
        return not Book.__ge__(self, value)
    
b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print(b1 == b3)
print(b1 == b2)
# print(b1 == "food")

# TODO: Check for greater and lesser value
print(b2 >= b3)
print(b2 < b3)


# TODO: Now we can sort them too
