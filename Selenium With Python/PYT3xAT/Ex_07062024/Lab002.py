first_name = "Ram"
last_name = "Dafe"
details = """
    Hello,
    My name is Ram Dafe.
    Nice to meet you.
    How had you been?
"""
print(f"Name: {first_name} {last_name}")
print(details)

name = first_name.lower() + " " + last_name.lower()
print(name)
name = name.upper()
print(name)
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.count("R"))
print("Length of the name is", len(name))
print(name.replace("R", "J"))

# The value from last line was not stored in name variable. Just a normal function call
print(name)