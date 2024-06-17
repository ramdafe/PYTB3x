def say_hello_with_no_args():
    print("Hello!")
    
def say_hello_with_name(name):
    print(f"Hello, {name}!")

def say_hello_with_default_args(name = "Ram"):
    print(f"Hello, {name}!")
    
# Calling the functions
say_hello_with_no_args()
say_hello_with_default_args()
say_hello_with_name("John")