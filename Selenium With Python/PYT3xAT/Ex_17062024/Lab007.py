def make_pizza(*toppings, base):
    print(toppings)
    print(type(toppings))
    print(base)
    print(type(base))
    print("Making a pizza with the following toppings:")
    print(toppings, base, sep=" With the base: ")

toppings = []
premium_toppings = ["olive"]
print(type(toppings))
toppings.append("pepperoni")
toppings.append("mushroom")
toppings.append("extra cheese")
toppings.append("sausage")
toppings.append("corn")

make_pizza(toppings, premium_toppings, base="thin crust")