import math
my_list = [625, 144, 100, 2500, 225]

# def find_sqrt(my_list):
#     temp_list = []
#     for i in my_list:
#         temp_list.append(int(math.sqrt(i)))
#     return temp_list

# sqrt_list = find_sqrt(my_list)
# print(sqrt_list)
        
# find_sqrt = lambda num: int(math.sqrt(num))

# sqrt_list = list(map(find_sqrt, my_list))
# print(sqrt_list)

print(list(map(lambda num: int(math.sqrt(num))(), my_list)))