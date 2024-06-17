# Match Case
# In Java it is is called Switch Case

# Match Case for browser
browser = input("Enter browser name: ").lower()
match browser:
    case "chrome":
        print("You are in the Chrome browser.")
    case "firefox":
        print("You are in the Firefox browser.")
    case "edge":
        print("You are in the Edge browser.")
    case _:
        print("We do not know this browser.")

# Match Case for age
age = int(input("Enter your age: "))
match age:
    case _ if age < 18:
        print("Your age is less than 18. Hence, you are not allowed for the admission")
    case _ :
        if age >= 18:
            print("You are allowed for the admission")
            print("Your age is", age, "or greater.", "Hence, you are allowed for the admission.")