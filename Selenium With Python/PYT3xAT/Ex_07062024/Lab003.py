val = None
print(val)
print("ID of val when it is None:", id(val))

print(type(val))
val = "Hello"

#Strings are immutable i.e. the characters inside it can't be changed
#val[0] = "T" -- NOT ALLOWED, TypeError: 'str' object does not support item assignment

print(val)
print(type(val))
print("ID of val when it has a value:", id(val))