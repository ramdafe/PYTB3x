# Take a string as an input and reverse it

the_string = input("What's the word or a sentence in your mind. Tell me, I would reverse it!!:\n")

char_list = []

# Solution 1

reversed_string = ""

for char in the_string:
    char_list.append(char)

char_list.reverse()

for char in char_list:
    reversed_string = reversed_string + char

print("Following is the reversed string using solution 1:\n" + reversed_string)

# Solution 2

reversed_string_2 = ""

temp_list = list(the_string)
temp_list.reverse()

for char in temp_list:
    reversed_string_2 = reversed_string_2 + char

print("Following is the reversed string using solution 2:\n" + reversed_string_2)

# Solution 3
str = ''.join(temp_list)
print("Following is the reversed string using solution 3:\n" + str)
