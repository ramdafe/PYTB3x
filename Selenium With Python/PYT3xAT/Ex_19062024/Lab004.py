def outer_function():
    print("Executing the outer function")
    def inner_function1():
        print("Executing the inner function 1")
    def inner_function2():
        print("Executing the inner function 2")
    inner_function1()
    inner_function2()

outer_function()