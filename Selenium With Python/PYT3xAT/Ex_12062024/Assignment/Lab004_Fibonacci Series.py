# Task 2
# Fibonacci Series
# Fibonacci series upto 10 terms is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
num = int(input("Enter a range for the fibonacci series: "))
sum = 0
fibonacci_series = []

for i in range(num):
    if sum == 0:
        sum = sum + i
        fibonacci_series.append(sum)
    else:
        fibonacci_series.append(sum)
        sum = sum + fibonacci_series[i-1] 
    
print(fibonacci_series)
    