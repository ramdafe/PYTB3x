import math
# Task 2
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

num = int(input("Enter the number: "))
factorial_val = 1

# Using a for loop
for i in range(1, num + 1): #range(num, 0 , -1) would also work here.
    factorial_val *= i
print('The factorial value of ', num, ' is ', factorial_val, "using a For Loop.")

# Using a while loop
factorial_val_while_loop = 1
num2 = num
while num2 > 0:
    factorial_val_while_loop *= num2
    num2 = num2 - 1

print('The factorial value of ', num, ' is ', factorial_val_while_loop, "using a While Loop")

# Assertion
print(f"The factorial value is correct as per the factorial function, {math.factorial(num)}." if factorial_val == math.factorial(num) else "The values are not matching.")
