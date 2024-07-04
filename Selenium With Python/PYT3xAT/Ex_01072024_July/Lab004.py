# Method Overloading in Python is not allowed. However, you can use the default arguments to call a function.

def my_function(a, b=0, c=0):
    return a + b - c

print(my_function(1)) #1
print(my_function(1, 2)) #3
print(my_function(1, 2, 3)) #0
print(my_function(1, b=3)) #4
print(my_function(a=10)) #10
print(my_function(5, c=10)) #-5
print(my_function(a=10, b=20, c=5)) #25