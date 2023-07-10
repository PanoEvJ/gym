# Using data classes to represent data objects

from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : int
    
    def bookinfo(self):
        return f"{self.title} by {self.author}"
    
    # def __str__(self):
    #     return f"{self.title} by {self.author} costs {self.title}"
    
    # def __call__(self, title):
    #     self.title = title
    #     return "Set favorite book"
    
    # def getfavoritebook(self):
    #     return f"My favorite book is {self.title}"
    
# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print(b2)
print(b1.title)
# print(b1.bookinfo())
# print(b1("The Jitterbug Perfume"))
# print(b1.getfavoritebook())

# comparing two dataclasses
print(b2 == b3)

# change some fields
b1.title = 'The Master and Margarita'
print(b1.bookinfo())