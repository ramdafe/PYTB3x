# To verify if two words are anagrams to each other

str1 = input("Enter a word: ").lower()
str2 = input("Enter another word: ").lower()
first_word_list = []
second_word_list = []

for char in str1:
    first_word_list.append(char)

for char in str2:
    second_word_list.append(char)

first_word_list.sort()
second_word_list.sort()

if first_word_list == second_word_list:
    print("The words are anangram.")
else:
    print("The words are not anagram.")