# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: October 26, 2017
# Version 1.0
# Problem Exercise: 13

import datetime
import random

def script_header():
    print("Welcome to the programme to calculate the fibonacci series")
    user_name = input("Please enter your name: ")
    print("The programme was run on: ", datetime.datetime.now())

"""
fibonacci_series = []
#user_choice = input("Press 1 to enter a number or 2 to generate a random number")
#print("You chose {}".format(user_choice))

user_number = input("Please enter a number to calculate the Fibonacci series")
print(fibonacci_series)
if user_number == 1:
    print("We are here")
    print(fibonacci_series)
    fibonacci_series.append(user_number)
    print(fibonacci_series)

if user_number == 2:
    fibonacci_series.append(1, 1)
    print(fibonacci_series)

user_input = int(input("Enter a number to Calculate the series"))
"""
def main():
    script_header()

if __name__ == '__main__':
    main()

