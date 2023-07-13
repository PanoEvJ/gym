# Using Abstract Base Classes to implement interfaces
from abc import ABC, abstractmethod

class JSONify(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass
    
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        # super().__init__()
        self.radius = radius
        
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{ \"Circle\" : {str(self.calcArea())} }}"

c = Circle(1.3)

print( 'Cirle area: ', c.calcArea())
print(c.toJSON())

