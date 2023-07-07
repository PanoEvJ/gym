# Using composition to build complex objects

class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price
        self.authorfname = authorfname
        self.authorlname = authorlname
        
        self.chapters = []
        
    def addchapter(self, name, pages):
        self.chapters.append((name,pages))
    
    # def pagecount(self):
    #     result = 0
    #     for ch in self.chapters:
            
        

b1 = Book("The Jitterbug Perfume", 29.9, "Tom", "Robbins")
b1.addchapter("Chapter 1", 24)
b1.addchapter("Chapter 2", 43)

print(b1.title)      