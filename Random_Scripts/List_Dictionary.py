# Author: Rohit Gupta
# Date: October 31, 2018
# Version 1.0

import datetime
from pprint import pprint


def main():
    header()
    read_files()


def header():
    print("Welcome to the programme to read and write to a log file")
    user_name = input("Please enter your name: ")
    print("The programme was run on", datetime.datetime.now())
    print("Your interaction with the script starts {}".format(user_name))
    current_time_format = "%I:%m %p on %B %w, &Y"
    #right_now.strftime(current_time_format)
    print(current_time_format)


def read_files():
    favorite_colors = [
        {"student": "Mary", "color": "red"},
        {"student": "John", "color": "blue"}
    ]
    print(favorite_colors)
    print(len(favorite_colors))
    pprint(favorite_colors)
    pprint(len(favorite_colors))
    # print(favorite_colors(1))
    # print(favorite_colors[student])
    # print(favorite_colors[color])


if __name__ == "__main__":
    main()
