# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 21, 2017
# Version 1.0
# Problem Exercise: 3

a = [5, 8, 13, 21, 34, 55, 89, 100, 120, 144,
     189, 200, 200, 249, 367, 490, 599, 611, 749, 801,
     934, 1002, 2010, 3982, 4068, 5923]
b = []
user_value = int(input("Please enter a number to evaluate: "))
for value in a:
    if value <= user_value:
        b.append(value)
        # print(value)
    else:
        break
print("Total numbers in the list less than {} is ".format(user_value), len(b))
print(b)

    # else:
    # print("No values are less than 5 in the list")