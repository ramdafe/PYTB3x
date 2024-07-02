class VW_Login:
    
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        
    def __reset_password(self):
        __new_password = input("Enter a new password: ")
        self.__password = __new_password
        print("Your password has been reset to", self.__password)
       
    def __check_auth(self):
        security_token = input("Enter the security token:\n")   
        if self.__email == "ram.dafe@ccmllc.com" and self.__password == "Ccm@123" and security_token == "CCM12345":
            print("Authorized.")
            want_to_reset_pwd = input("Do you want to reset the password?\n").lower()
            if want_to_reset_pwd == "yes" or want_to_reset_pwd == "true":
                VW_Login.__reset_password(self)
            else:
                print("Alright.")
        else:
            print("Not authorized.")
    
    def login_confirm(self):
        VW_Login.__check_auth(self)

email = input("Enter the email: ")
password = input("Enter the password: ")

login_object = VW_Login(email, password)

# print(login_object.__email) # Not allowed, since __email is private

login_object.login_confirm()