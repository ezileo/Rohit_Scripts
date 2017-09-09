# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 23, 2017
# Version 1.0
# Problem Exercise: 5


import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
new_list = []
for a_common in a:
    for b_common in b:
        if a_common == b_common:
            # print(a_common)
            new_list.append(a_common)
print("The new list containing common integers in two lists is: ", new_list)


random_list_1_length = random.randint(20, 200)
random_list_2_length = random.randint(20, 200)
random_list_1 = []
random_list_2 = []
new_list_random = []
print(random_list_1_length)
print(random_list_2_length)

for _ in range(0, random_list_1_length):
    random_integer = random.randint(1, 10000)
    random_list_1.append(random_integer)
print(random_list_1)

for _ in range(0, random_list_2_length):
    random_integer = random.randint(1, 10000)
    random_list_2.append(random_integer)
print(random_list_2)

for a_common in random_list_1:
    for b_common in random_list_2:
        if a_common == b_common:
            # print(a_common)
            new_list_random.append(a_common)
print("The new list containing common integers in two lists is: ", new_list_random)
