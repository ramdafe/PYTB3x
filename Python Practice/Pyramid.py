rows = int(input("How many rows do you want?: "))
for i in range(0,rows):
    for j in range(rows-1, i, -1):
        print(" ", end="")
    for j in range(0,i+1):
        print("* ", end="")
    print()