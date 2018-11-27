# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: October 26, 2017
# Version 2.4
# Problem Exercise: 13

import datetime
import random


def main():
    script_header()
    user_input = int(input("Enter 1 to choose FS or 2 to Randomly generate one: "))
    if user_input == 1:
        fs_length = int(input("Enter how long you want to calculate this: "))
        fs(fs_length)
    elif user_input == 2:
        fs_length = random.randint(1, 100)
        fs(fs_length)
        print(fs_length)
    else:
        print("Please select valid input")


def script_header():
    print("Welcome to the programme to calculate the fibonacci series")
    user_name = input("Please enter your name: ")
    print("The programme was run on: ", datetime.datetime.now())
    print("Your interaction with the script starts {} . . . . .".format(user_name))
    return


def fs(fs_length):
    if fs_length == 1:
        fs0 = [0]
        print(fs0)
    elif fs_length == 2:
        fs0 = [0, 1]
        print(fs0)
    elif fs_length > 2:
        fs0 = [0, 1]
        a = 1
        while a <= (fs_length-2):
            fs0.append(fs0[a] + fs0[a-1])
            a += 1
    print(fs0)
    print(len(fs0))


if __name__ == '__main__':
    main()
