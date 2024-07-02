class Dogs:
    
    #Attributes
    breed_name = None
    dog_name = None
    height = None
    age = None
    city = None
    
    # Default constructor
    def __init__(self):
        self.breed_name = "Inidan Pariah"
        self.dog_name = "Appy"
        self.height = 3
        self. age = 6
        self.city = "Indore"
    #Behavior
    def sleep(self):
        print("Who is sleeping?", self.dog_name, "of", self.breed_name, "breed from", self.city)
    
    def eat(self):
        print("Who is eating?", self.dog_name, "of", self.breed_name, "breed from", self.city)
        
    def walk(self):
        print("Who is walking?", self.dog_name, "of", self.breed_name, "breed from", self.city)

dog_1 = Dogs()
dog_1.sleep()
dog_1.eat()
dog_1.walk()