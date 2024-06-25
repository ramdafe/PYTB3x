import time
name = "Ram Dafe"

def my_decorator_1(say_hello):
    def wrapper():
        print("Decorator 1")
        say_hello(name)
    return wrapper()

def my_decorator_2(say_hello):
    def wrapper():
      print("Decorator 2")
      say_hello(name)
    return wrapper()

# @ my_decorator_1 
@ my_decorator_2
def say_hello(name):
    print("Hello", name)