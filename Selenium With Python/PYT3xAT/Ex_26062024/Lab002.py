class hotel_booking:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def login_to_app(self):
        
        print("You age is:", self.age)
        
        print(f"Login successful. Welcome {self.name}" if self.age > 18 else "You can't login.")
        
        # if self.age > 18:
        #     print("Login successful. Welcome", self.name)
        # else: 
        #     print("You can't login.")
    
user_1 = hotel_booking()
user_1.login_to_app()