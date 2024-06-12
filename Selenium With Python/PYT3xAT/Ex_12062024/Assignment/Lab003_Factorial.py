# Task 2
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

num = int(input("Enter the number: "))
factorial_val = 1
for i in range(num, 0, -1):
    factorial_val *= i
print('The factorial value of ',str(num), ' is ', str(factorial_val))