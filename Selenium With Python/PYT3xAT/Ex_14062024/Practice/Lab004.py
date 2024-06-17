# Example of "pass" in a for loop
        
# Break ->  based on condition if will kick you
# out of the loop.

# Pass -> ? pass do nothing  - Skip the code


for i in range(0, 11, 2):
    if i == 0:
        pass
    else:
        print(i)

for i in range(10):  # 0-9
    if i == 5 or i == 6:
        pass
    else:
        print(i)