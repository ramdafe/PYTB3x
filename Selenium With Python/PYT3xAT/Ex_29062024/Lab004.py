class BankAccount:
    
    def __init__(self):
        self.__balance = 0
    
    def __authorize_the_user():
        __pin = input("Enter the 4-digit PIN: ")
        if __pin == "1234":
            return True
        else:
            return False
    
    def deposit_money(self, amount):
        self.__balance += amount
        # print("Updated balance after deposit:", self.__balance)
    
    def withdraw_money(self, amount):
        if BankAccount.__authorize_the_user() == True:
            self.__balance -= amount
            # print("Updated balance after withdrawal:", self.__balance)
        else:
            print("You are not authorized to withdraw money.")
            
    def check_balance(self):
        if BankAccount.__authorize_the_user() == True:
            print("Your balance is", self.__balance)

jp_chase_object = BankAccount()
jp_chase_object.deposit_money(200)
jp_chase_object.withdraw_money(100)
jp_chase_object.check_balance()