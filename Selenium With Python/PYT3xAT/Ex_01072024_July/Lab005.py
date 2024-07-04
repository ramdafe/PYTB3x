"""This line is not executed...
Checking the behavior of super() method if there are siblings. 
"""

class Parents:
    child_name = None
    def __init__(self, name):
        self.child_name = name
        print("The child name", self.child_name)
        
    def home(self):
        print("This is our home.", self.child_name)
    
class Brother(Parents):
    def __init__(self, name):
        super().__init__(name)
        super().home()
        
    def home(self):
        print("This is my home and I have one room near the hall.", self.child_name)
        
class Sister(Parents):
    def __init__(self, name):
        super().__init__(name)
        super().home()
        
    def home(self):
        print("This is my home and I have one room near the kitchen.", self.child_name)

bro = Brother("David")
bro.home()

sis = Sister("Liza")
sis.home()