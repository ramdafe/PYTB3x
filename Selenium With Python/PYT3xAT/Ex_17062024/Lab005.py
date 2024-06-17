def summing_the_prices(product_prices):
    print(product_prices)
    total = 0
    product_prices[0] = 100
    product_prices[2] = 50
    for i in product_prices:
        total = total + i
    return total

total_cost = 0

product_prices = [120.50, 30, 40.25, 500]
total_cost = summing_the_prices(product_prices)

print("The sum of all the prices is", total_cost)