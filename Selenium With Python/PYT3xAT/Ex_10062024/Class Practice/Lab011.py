# Program - Calculate the area of circle.
# input -> radius
# output -> area

import math
# In Python, a module is a file containing Python definitions and statements.
# math is not a class, it is a built-in module in Python.
# The math module is written in C and provides a wide range of mathematical functions that can be used in Python programs.

# data types
# input -> int or float -> float
# output -> float

# Core Logic -> area of circle = pi*r*r (where, r is the radius of circle.)

radius = float(input("Enter the radius\n"))
print(math.pi)
area = math.pi*(radius**2) # Exponentiation Operator
area2 = math.pi*(math.pow(radius,2)) # Power function from math module
print(area)
print(area2)