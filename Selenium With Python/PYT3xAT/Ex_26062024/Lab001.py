# Constructors 
# When an object of a class is created, the Constructor helps to initialize the data members/class variables i.e. assigning values to them.

#Types of constructors : 

# default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.

# parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

class Dog:
    
    #Attributes
    breed_name = None
    dog_name = None
    height = None
    age = None
    city = None
    
    # Parameterized constructor
    def __init__(self, breed_name, dog_name, height, age, city):
        self.breed_name = breed_name
        self.dog_name = dog_name
        self.height = height
        self. age = age
        self.city = city
    
    #Behavior
    def sleep(self):
        print("Who is sleeping?", self.dog_name, "of", self.breed_name, "breed from", self.city)
    
    def eat(self):
        print("Who is eating?", self.dog_name, "of", self.breed_name, "breed from", self.city)
        
    def walk(self):
        print("Who is walking?", self.dog_name, "of", self.breed_name, "breed from", self.city)

dog_1 = Dog("Akita", "Hachi", 3, 7, "Shanghai")
dog_1.sleep()

dog_2 = Dog("Himalayan Mastiff", "Bucky", 5, 4, "Ladakh")
dog_2.eat()
dog_2.walk()