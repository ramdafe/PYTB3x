# Task 2

# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

num = int(input("Enter a number:\n"))
# Finding square of a number
square = num ** 2
print("Square of the number:", square)

#Finding cube of a number
cube = num ** 3
print("Cube of the number:", cube)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))

if(num1 == num2):
    print(f'{num1} and {num2} are equal.')
elif(num1 > num2):
    print(f'{num1} is greater than {num2}.')
else:
    print(f'{num1} is less than {num2}.')