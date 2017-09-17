# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 31, 2017
# Version 1.0
# Problem Exercise: 11

import datetime
import random

user_name = input("Please enter your name: ")
print("This programme was run on:   " + str(datetime.datetime.today()))
user_input = int(input("Press 1 to input a number and find if it's a Prime"
                       "or Press 2 to generate a random number and find if it's a Prime: "))
list_1 = []
list_2 = []

if user_input == 1:
    user_number = int(input("Please enter a number of your choice: "))

    for a in range(2, user_number):
        for b in range (2, user_number):
            if user_number % a == 0:
                list_1.append(a)
    print("Number of divisors for {} is".format(user_number), list_1)
    print("Number is Prime")

if user_input == 2:
    random_number = random.randint(1, 99)
    print("The Random Number selected by Computer is", random_number)

    for b in range(2, random_number):
        if random_number % b == 0:
            list_2.append(b)
            print("The number is not Prime")
        else:
            print("The number is Prime")
    print("Number of divisors is", list_2)
