str = input("Enter a word\n").lower()
flag = False

list_of_chars = list(str)

for index in range(int(len(list_of_chars)/2)):
    if list_of_chars[index] == list_of_chars[len(list_of_chars) - index - 1]:
        flag = True
    else:
        flag = False
        break

if flag == True:
    print("String is palindrome")
else:
    print("String is not a palindrome")