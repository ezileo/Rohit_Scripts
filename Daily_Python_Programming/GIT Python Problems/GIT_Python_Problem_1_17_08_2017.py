# URL: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# Author: Rohit Gupta
# Date: August 17, 2017
# Version 1.0
# Problem Exercise: 1

l=[]
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i)
        l.append(i)
print("Total numbers between 2000 and 3200 divisible by 7 and not a multiplier of 5 are {}".format(len(l)))
print(l)
