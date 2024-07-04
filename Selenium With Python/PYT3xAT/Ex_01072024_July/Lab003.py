class Square:
    
    # def __init__(self, side):
    #     print("The constructor of the parent class is executed.")
    #     self.side = side   
         
    def area(self, side):
        return side * side

class Cube(Square):
    def area(self, side):
        return super().area(side) * 6

cube_object = Cube()
print("Area of the cube is:", cube_object.area(3))