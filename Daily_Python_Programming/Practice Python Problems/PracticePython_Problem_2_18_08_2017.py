# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 18, 2017
# Version 1.0
# Problem Exercise: 2

user_name = input("Please input your name: ")
user_input = input("{} please enter a number to evaluate:".format(user_name))


if (int(user_input) % 4) == 0:
    print("This number is divisible by 4")
elif (int(user_input) % 2) == 0:
    print("This is an even number")
else:
    print("The number is odd")

num = input("{} enter a number to check if it would be divisible by another number: ".format(user_name))
check = input("{} enter another number to check if it would be divisible by {}: ".format(user_name, num))

if int(num) % int(check) == 0:
    print("{} {} is completely divisible by {}: ".format(user_name, num, check))
else:
    remainder = int(num) % int(check)
    print("{} {} is not completely divisible by {} and remainder is {}: ".format(user_name, num, check, remainder))
