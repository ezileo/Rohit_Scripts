# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 29, 2017
# Version 1.0
# Problem Exercise: 9

import datetime
import random

user_input = input("Please enter your name to start the game: ")
current_time = datetime.datetime.today()
print("{} you started this game at {}".format(user_input, current_time))
game_count = 0
user_win = 0
computer_win = 0

while game_count < 10:
    user_number = int(input("Please enter a number between 1 and 20"))
    computer_number = int(random.randrange(0, 20))
    print("Let the game begin. The attempts left are" + str(10 - game_count))
    print(computer_number)
    if computer_number == user_number:
        print("Its a Tie")
        game_count = game_count + 1
    elif computer_number > user_number:
        print("Computer Wins!!!")
        game_count = game_count + 1
        computer_win = computer_win + 1
    elif computer_number < user_number:
        print("User Wins")
        game_count = game_count + 1
        user_win = user_win + 1
print("The number of times game has been played is {}".format(game_count))
print("The number of time computer has won the game is {}".format(computer_win))
print("The number of time {} has won the game is {}".format(user_input, user_win))
