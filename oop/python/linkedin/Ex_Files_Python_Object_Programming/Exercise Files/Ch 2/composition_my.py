# Using composition to build complex objects

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author
        
        self.chapters = []
        
    def addchapter(self, chapter):
        self.chapters.append(chapter)
    
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result
    
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount
        
auth = Author("Tom", "Robbins")

b1 = Book("The Jitterbug Perfume", 29.9, auth)

chapter1 = Chapter("Chapter 1", 24)
chapter2 = Chapter("Chapter 2", 43)

b1.addchapter(chapter1)
b1.addchapter(chapter2)

print(b1.title)      
print(b1.author)      
print(b1.getbookpagecount())      