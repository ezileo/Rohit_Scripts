# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: October 23, 2017
# Version 1.0
# Problem Exercise: 12

import datetime
import random

user_name = input("Please enter your name: ")
print("This programme was run on:   " + str(datetime.datetime.today()))
user_input = int(input("Enter the length of the list"))
a = []
b = []
for _ in range(0, user_input):
    a.append(random.randint(0, 100))
print(a)
print("The length of the list is: ", len(a))

#def ListIteration():

first = a[0]
last = a[user_input-1]
print("The first number on the list is: ", first)
print("The last number on the list is: ", last)
b.append(first), b.append(last)
print("The new list is: ", b)