# To find the factorial of a given number using ta recursion function
# A recursion function is a function that calls itself in order to perform calculations

number = int(input("Enter a number: "))

# Function
def find_factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recusrsive case
    else:
        return n * find_factorial(n - 1)

factorial_value = find_factorial(number)
print(factorial_value)