# To find whether a word is a Palindrome or not

english_word = input("Enter a word:\n").lower()

char_list = []
new_list = []

for char in english_word:
    char_list.append(char)
    
new_list = char_list.copy()

char_list.reverse()
if new_list == char_list:
    print("It is a palindrome word.")
else:
    print("Not a palindrome word.")