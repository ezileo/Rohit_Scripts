# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 30, 2017
# Version 1.0
# Problem Exercise: 10

import datetime
import random

print("This program was run on " + str(datetime.datetime.now()))
list_1 = []
list_2 = []
overlapping_list = []
random_list = random.randrange(10, 30)

for _ in range(0, random_list):
    list_1.append(random.randint(0, 100))
print(list_1)
print(len(list_1))
for _ in range(0, random_list):
    list_2.append(random.randint(0, 100))
print(list_2)
print(len(list_2))

for a in list_1:
    for b in list_2:
        if a == b:
            overlapping_list.append(a)
print(overlapping_list)
print(len(overlapping_list))
