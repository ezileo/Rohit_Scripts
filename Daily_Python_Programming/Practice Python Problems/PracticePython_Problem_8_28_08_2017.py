# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 28, 2017
# Version 1.0
# Problem Exercise: 8

import datetime
import random

user_name = input("Please enter your name: ")
current_time = datetime.datetime.now()
print("Hi {}, you ran this script at {}".format(user_name, current_time))

play_objects = {"1": "Rock", "2": "Paper", "3": "Scissors"}
print(play_objects.keys())
print(play_objects.values())
key = input("Please select your option {} from {}".format(user_name, play_objects))
print(play_objects[key])
user_input = play_objects.get(key)
computer_input = str(random.choice(list(play_objects.values())))

print("The computer randomly choose {}".format(computer_input))
print(type(computer_input))
print("{} choose {}".format(user_name, user_input))
print(type(user_input))

while user_input == "None":
    print ("ERROR!!!!!!!!!!")
    break

while user_input == "Rock":
    if computer_input == "Paper":
        print ("Computer Wins")
    elif computer_input == "Rock":
        print("Its a Tie")
    else:
        print("User Wins")
    break

while user_input == "Paper":
    if computer_input == "Scissors":
        print ("Computer Wins")
    elif computer_input == "Paper":
            print("Its a Tie")
    else:
        print("User Wins")
    break


while user_input == "Scissors":
    if computer_input == "Rock":
        print ("Computer Wins")
    elif computer_input == "Scissors":
            print("Its a Tie")
    else:
        print("User Wins")
    break

