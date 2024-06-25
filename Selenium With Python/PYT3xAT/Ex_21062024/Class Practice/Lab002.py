# Show the table of a given number including an example of decorator

import time

num = int(input("Enter a number,\n"))

# Decorator function
def my_decorator(print_table):
    def random_wrapper_function():
        print(f"Doing the mathematics, to create a table of {num} for you...")
        time.sleep(1)
        print("\n*****")
        print_table(num)
        print("\n*****")
        print("Love Mathematics. Keep studying...\n")
    return random_wrapper_function()

# Give the annonation as @<decorator_function_name>
@ my_decorator
def print_table(num):
    print("Hello World!!!")
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

@ my_decorator
def print_table(num):
    print("Hello Third World!!! Doubled the number and showing the table...")
    for i in range(1, 11):
        print(f"{num*2} * {i} = {num * 2 * i}")
  
# time.sleep(1)      
# print("Normal function call, witout the decorator:")

# # Function calling - Throws a TypeError, "NoneType object not callable"
# print_table()