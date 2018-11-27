# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: November 13, 2018
# Version 1.0
# Problem Exercise: 16
import datetime
import random


def main():
    low_alpha = list("abcdefghijklmnopqrstuvwxyz")
    high_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("0123456789")
    spc_chr = list("!@#$%^&*()")
    print(low_alpha)
    print(high_alpha)
    print(num)
    print(spc_chr)
    user_input1 = int(input("Please enter the lower case characters in your password: "))
    user_input2 = int(input("Please enter the Higher case characters in your password: "))
    user_input3 = int(input("Please enter the numbers in your password: "))
    user_input4 = int(input("Please enter the special characters in your password: "))
    rslc = random.sample(low_alpha, user_input1)
    rsuc = random.sample(high_alpha, user_input2)
    rsnum = random.sample(num, user_input3)
    spc_chr = random.sample(spc_chr, user_input4)
    print(rslc, rsuc, rsnum, spc_chr)
    password_list = rslc + rsuc + rsnum + spc_chr
    print(password_list)
    random.shuffle(password_list)
    # print(pass_string)
    pass_string = "".join(password_list)
    print(pass_string)
    # random.shuffle(pass_string)
    # print(pass_string)
    print("Hi {}, the random generated password for you is {}".format(user_name, pass_string))


if __name__ == '__main__':
    print("Welcome to the programme to generate random password")
    user_name = input("Please enter your name: ")
    print("The programme was run on: ", datetime.datetime.now())
    print("Your interaction with the script starts {} . . . . .".format(user_name))
    main()
