# Author: Rohit Gupta
# Date: October 18, 2018
# Version 1.0

import datetime


def main():
    header()
    read_log()
    write_log()


def header():
    print("Welcome to the programme to read and write to a log file")
    user_name = input("Please enter your name: ")
    print("The programme was run on", datetime.datetime.now())
    print("Your interaction with the script starts {}".format(user_name))


def read_log():
    log_file = "example.log"
    with open(log_file, 'r') as a:
        print(a.read())


def write_log():
    log_file = "example.log"
    log_time = datetime.datetime.now()
    with open(log_file, 'a') as a:
        a.write("The file was accessed at: {}".format(str(log_time)))
        a.write("\n")
        a.writelines("Entry logged in at: {} by \n ".format(log_time))


if __name__ == "__main__":
    main()
