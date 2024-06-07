# identifier = literal
# variable_name = variable_value
a = 8
b = 4

# Python is a dynamically typed language
b = 2

print(a + b)
print(a / b)
print(a * b)
print(a - b)
print(type(a))
print(type(a/b))

# Python loves snake_case
first_name = "John"
last_name = "Smith"
is_active = True

#Printing the strings using different approach
print(first_name + " " + last_name)
print(first_name, last_name)
print(first_name, last_name, sep="-")
print(first_name, last_name, sep=":")
print(first_name, last_name, end="\n")
print("Hello there,", first_name, "is active:", is_active)

#Printing the types of variables
print(type(first_name))
print(type(last_name))
print(type(a))
print(type(a/b))
print(type(True))

# complex expression
complex_exp = 2 + 3j
print(complex_exp)
print("Real Component: ", complex_exp.real)
print("Imaginary Component", complex_exp.imag)

# min or max
print(min(a, b), "is minimum value out of", a, "and", b)
print(max(a, b),  "is maximum value out of", a, "and", b)