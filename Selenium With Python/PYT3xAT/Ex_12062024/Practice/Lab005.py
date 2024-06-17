#Range(start, stop, step)
print(range(1, 10, 2))

x = range(1, 10, 2)
even_numbers = list(range(0, 10, 2))
even_numbers.pop(0)
odd_numbers = list(range(1, 10, 2))

print("x:", x, "Type of x", type(x))
print("even_numbers:", even_numbers)
print("odd_numbers:", odd_numbers)
 
# Using "range" as a variable name
range = 190
print(range)
print(type(range))