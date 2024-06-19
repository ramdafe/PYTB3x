global_var  = 20

def function1():
    local_var = 10
    print("Local Variable", local_var)

function1()
print("Global Variable", global_var)
# print("Local Variable", local_var) # NameError: name 'local_var' is not defined.
