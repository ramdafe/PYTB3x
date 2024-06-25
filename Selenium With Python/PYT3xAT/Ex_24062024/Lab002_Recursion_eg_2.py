# Find sum of all digits of a number

number = int(input("Enter a number: "))

def find_sum_of_digits(n):
    # Base case
    if n < 10:
        return n
    else:
        return n % 10 + find_sum_of_digits(n // 10) 

print(find_sum_of_digits(number))