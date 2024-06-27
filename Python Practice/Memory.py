list1 = [1, 2, 3]
list2 = list1

print(id(list1) == id(list2))  # Returns true. list2 points to the same memory location that list1 points
name = "Ram"
name2 = name
print(id(name) == print(name2))