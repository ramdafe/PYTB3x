#Abstraction in Python

from abc import ABC, abstractmethod

class Shapes(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass

class Rectangle(Shapes):
    print("This is a rectangle.")
    
    def area(self, length, breadth):
        return length * breadth
    
    def volume(self):
        return super().volume()
    
rectangle = Rectangle()
area = rectangle.area(20, 50)
print("Area:", area)