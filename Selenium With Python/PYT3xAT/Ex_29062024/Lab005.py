class Password:

    def set_password(self, password):
        if len(password) >= 8:
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

object = Password()
password = input("Enter a password: ")
object.set_password(password)
print(object.get_password())