#*args --> any number of arguments accepted
# *args --> tuple
# tuple is immutable
# list is mutable

def print_argument(*args):  # ("pramod","amit","lucky"]
    print(args)  # ("pramod", "amit", "lucky")
    for i in args:
        print(i, end="\n")

print_argument("pramod", "amit", "lucky")

# a = ["pramod", "amit", "lucky"]
# for i in a:
#     print(i)


# for i in range(1, 10):
#     print(i)
