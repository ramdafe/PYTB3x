# Find the number of vowels and consonants in the given string

the_string = input("Enter a string:\n").lower()

count_of_vowels = 0
count_of_consonants = 0
list_of_vowels = []
list_of_consonants = []
my_dict = None

list_of_special_chars = [".", ",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "\'", "\"", "/", "\\"]

# Function to count the occurence of characters of individual characters of the given string
# Rturns the data in form of (key, value) dictionary
def find_char_occurence(list_of_chars):
    
    my_dict = dict()
    for char in list_of_chars:
        count_of_current_char = 0
        count_of__current_char = list_of_chars.count(char)
        new_dict = {char : count_of__current_char}
        my_dict.update(new_dict)
    
    return my_dict

# Iterate over the given string to find the number of consonants and the number of vowels
for char in the_string:
    if char == " " or list_of_special_chars.__contains__(char) == True:
        pass
    else:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            list_of_vowels.append(char)
            count_of_vowels = count_of_vowels + 1
        else:
            list_of_consonants.append(char)
            count_of_consonants = count_of_consonants + 1
            
# Calling the function to create a dictionary for tracking the occurence of individual vowels and consonants
vowels_dict = find_char_occurence(list_of_vowels)
consonant_dict = find_char_occurence(list_of_consonants)

#Printing the results
print("Count of vowels,", vowels_dict, "=", count_of_vowels)
print("Count of consonants,", consonant_dict, "=" ,count_of_consonants)