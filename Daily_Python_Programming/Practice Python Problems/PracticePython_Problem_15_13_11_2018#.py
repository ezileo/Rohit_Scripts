# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: November 13, 2018
# Version 1.0
# Problem Exercise: 15


import datetime


def main():
    user_list = input("Please type in a long sentence for me {}:".format(user_name))
    sort_list = user_list.split()
    print(sort_list)
    print(len(sort_list))
    print(type(sort_list))
    sort_list.reverse()
    print(sort_list)
    reverse_sentence = ' '.join(sort_list)
    print(reverse_sentence)


if __name__ == '__main__':
    print("Welcome to the programme to Reverse the order of sentences")
    user_name = input("Please enter your name: ")
    print("The programme was run on: ", datetime.datetime.now())
    print("Your interaction with the script starts {} . . . . .".format(user_name))
    main()
