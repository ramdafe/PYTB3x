# Lambda expression in python
# Map in python

my_list = [1, 2, 3, 4, 5]
print("Doubled List:", list(map(lambda list_item: list_item * 2, my_list)))

# Find the maximum of two numbers using the lambda expression
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
find_max = lambda num1, num2: num1 if num1 > num2 else num2
print(find_max(num1, num2))