# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 25, 2017
# Version 1.0
# Problem Exercise: 7

import datetime
import random
user_name = input("Please enter your name: ")
current_time = datetime.datetime.now()
print("Welcome {}, you ran this programme at {}". format(user_name, current_time))

initial_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
final_list = []

for i in initial_list:
    if i % 2 == 0:
        final_list.append(i)

print(final_list)

random_list = []
random_list_even = []
random_list_length = random.randint(10, 100)
for _ in range(5, random_list_length):
    random_list_data = random.randint(100, 200)
    random_list.append(random_list_data)
print(random_list)

for i in random_list:
    if i % 2 == 0:
        random_list_even.append(i)
print(random_list_even)
