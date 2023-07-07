# Using Abstract Base Classes to implement interfaces
from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass
