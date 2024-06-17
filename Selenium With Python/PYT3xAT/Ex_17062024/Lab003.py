def f1(a = 1, b = 2, c = 3):
    sum = a + b + c
    return sum

sum1 = f1(10, 20, 30) # prints 60
sum2 = f1(10, 20) # prints 33
sum3 = f1(10) # prints 15
sum4 = f1(b = 10) # prints 14
sum5 = f1() # prints 6
sum6 = f1(c = 10, b = 10) # prints 21

print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)
print(sum6)