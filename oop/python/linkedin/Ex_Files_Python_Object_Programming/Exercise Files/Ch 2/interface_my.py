# Using Abstract Base Classes to implement interfaces
from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass
    
class Circle(GraphicShape):
    def __init__(self, radius):
        # super().__init__()
        self.radius = radius
        
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

c = Circle(1.3)

print( 'Cirle area: ', c.calcArea())

