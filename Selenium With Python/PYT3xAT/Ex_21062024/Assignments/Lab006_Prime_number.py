# To find if a number is a prime number or a composite number
number = int(input("Enter a number\n"))

# Function
def is_prime(num):
    
    flag = True
    if num == 0:
        flag = None
    
    for index in range (2, num):
        if num % index == 0:
            flag = False
            break
    
    return flag

is_a_prime_number = is_prime(number)
print(is_a_prime_number)

# Filter Program to find prime numbers from 1 to n (i.e any number given as input) 
list_of_numbers = []

for num in range(number + 1):
    list_of_numbers.append(num)

list_of_prime_numbers = list(filter(is_prime, list_of_numbers))

print("All the prime numbers till " + str(number) + ":\n" + str(list_of_prime_numbers))

# Map Program to find square of all the prime numbers from the above list
get_squares = lambda num: num * num
square_of_numbers = list(map(get_squares, list_of_numbers))

print("Square of the original list of numbers:\n" + str(square_of_numbers))