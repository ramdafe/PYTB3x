my_list = [10, 15, 15, 20, 40, 30, "Radha"]
new_list = ["Ram", "Suvija", "Arpita", "Vanshaj"]
my_list.append(15)
my_list.append("Krishna")
my_list.remove(15) # Removes the first occurence
my_list.pop(6)
print(my_list)
print(my_list.__add__(new_list))
print(my_list)
print(new_list)