shopping_list = ["Milk", "Bread", "Curd"]
print(shopping_list)
print(shopping_list[2])
print(shopping_list[-2])
print(shopping_list[0:2])
print(len(shopping_list))

shopping_list.append("Chocolate")
shopping_list.extend(["Chips", "Sugar", "Oats"])
shopping_list.insert(0, "Butter")

# x not in list
# shopping_list.remove("CURD")

shopping_list.remove("Chips")

print(shopping_list)

shopping_list.pop(1)
print(shopping_list)
print(len(shopping_list))

# Sort the List
shopping_list.sort()
print(shopping_list)

#Reverse the List
shopping_list.reverse()
print(shopping_list)