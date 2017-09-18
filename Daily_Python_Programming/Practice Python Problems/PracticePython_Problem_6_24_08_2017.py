# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 24, 2017
# Version 1.0
# Problem Exercise: 6

import datetime
user_name = (input("Please enter your name: "))
current_time = datetime.datetime.now()
print("It is nice meeting you {}, you ran this script at {}".format(user_name, current_time))
word = (input("{} Please enter a word to see if it is a Palindrome or not: ".format(user_name))).upper()
word_list = []
for w in word:
    # print (w)
    word_list.append(w)
print(word_list)
reverse_word_list = word_list[::-1]
print(reverse_word_list)

if word_list == reverse_word_list:
    print("The word {} you have entered {} is a Palindrome". format(word, user_name))
else:
    print("The word {} you have entered {} is not a Palindrome".format(word, user_name))

