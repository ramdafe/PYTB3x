# Task 2
# Type of Triangle
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

side1 = float(input("Enter the length of one side of the triangle in cms: "))
side2 = float(input("Enter the length of the second side of the triangle in cms: "))
side3 = float(input("Enter the length of the third side of the triangle in cms: "))

#Solution 01
if side1 == side2 or side2 == side3:
    if side1 != side3:
        print("The triangle is an isosceles triangle.")
    else:
        print("The triangle is an equilateral triangle.")
elif side1 != side3:
    print("The triangle is a scalene triangle.")
    
# Solution 02 
# if side1 == side2 and side1 == side3:
#     print("The triangle is an equilateral triangel.")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is an isosceles triangle.")
# else:
#     print("The triangle is a scalene triangle.")

