# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: November 29, 2017
# Version 1.0
# Problem Exercise: 14
import datetime
import random


def main():
    header()
    define_lists()


def header():
    print("Welcome to the Programme to de duplicate lists")
    user_name = input("PLease enter your name")
    print("The programme was run on", datetime.datetime.now())
    print("Your interaction with the script starts {}". format(user_name))


def define_lists():
    user_input = int(input("Please enter 1 to enter a list or "
                           "2 to generate random lists: "))
    if user_input == 1:
        list1 = []
        list2 = []
        a = 1
        while a <= 10:
            digit1 = int(input("Enter {} digit to be part of First list".format(a)))
            list1.append(digit1)
            digit2 = int(input("Enter {} digit to be part of Second list".format(a)))
            list2.append(digit2)
            a += 1
        print("The generated lists are: ", list1, list2)
        print("The length of list 1 is: ", len(list1), "and of second list is:", len(list2))
        de_dupe(list1, list2)
    elif user_input == 2:
        a1 = random.randint(10, 20)
        a2 = random.randint(10, 20)
        rlist1 = []
        rlist2 = []
        for _ in range(0, a1):
            rlist1.append(random.randint(0, 1000))
        for _ in range(0, a2):
            rlist2.append(random.randint(100, 1000))
        print("Random List 1:", rlist1, "Length of list is: ", len(rlist1))
        print("Random List 1:", rlist2, "Length of list is: ", len(rlist2))


def de_dupe():
    print(list1, list2)


if __name__ == "__main__":
    main()
