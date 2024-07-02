# Constructors - When an object of a class is created, the Constructor helps to initialize the data members i.e. assigning values to them.

class My_Class:

    def __init__(self):
        self.name = "Ram Dafe"
        self.age = 28
    
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
        
    def my_method(self):
        a = 10
        print("I am a method", a)
        print("Hi, my name is", self.name)
        print("My age is", self.age)

object1 = My_Class()
object1.my_method()

# object2 = My_Class("Suvija", 30)
# object2.my_method()