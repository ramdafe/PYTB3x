class Square:
    
    def __init__(self, side):
        print("The constructor of the parent class is executed.")
        self.side = side   
         
    def area(self):
        return self.side * self.side

class Cube(Square):
    def area(self):
        return super().area() * 6

cube_object = Cube(2)
print("Area of the cube is:", cube_object.area())