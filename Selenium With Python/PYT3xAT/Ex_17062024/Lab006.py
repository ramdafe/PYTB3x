def make_pizza(*toppings):
    print("Print the list of toppings that have been requested.")
    
    # toppings[0] = 'Cheese' TypeError: 'tuple' object does not support item assignment
    # tuples are immutable
    
    print('Number of toppings:', len(toppings))
    print(toppings)
    
    
pizza_for_vaishnavi = make_pizza('olive', 'cheese', 'black pepper', 'paneer')

pizza_for_ram = make_pizza('corn', 'onion', 'capsicum', 'paneer', 'cheese')