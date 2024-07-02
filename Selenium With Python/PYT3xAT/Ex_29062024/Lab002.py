# Encapsulation: Wrapping or binding the data variables with the methods
# Data Members: Also called as Class Variables or Instance Varibales
# Function: Def function withing the function

class Car:
    name = None
    password = "123"

    def __init__(self):
        self.name = "Ram"
        print("I am a constructor", self.name, self.password)
    
    print("Password inside the class", password)
    
car_object = Car()
car_object.password = "345"
print("You are changing the password from outside", car_object.password)