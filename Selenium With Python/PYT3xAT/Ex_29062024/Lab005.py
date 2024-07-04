class Password:
    def __init__(self, password):
        self.__password = password
        
    def set_password(self, password):
        if len(password) >= 8:
            print("Old password:", self.__password)
            self.__password = password
            self.__isAuth = True
        else:
            print("Please provide a strong password.")
            self.__isAuth = False
    
    def get_password(self):
        if self.__isAuth:
            return self.__password
        else:
            return "Get method would not work because password was not set correctly."

object = Password("abcdefghijk")
password = input("Enter a new password to set: ")
object.set_password(password)
print("New Password:", object.get_password())