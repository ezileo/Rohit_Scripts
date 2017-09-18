# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 17, 2017
# Version 1.0
# Problem Exercise: 1

import datetime

name = input("Please enter your name: ")
age = input("Please enter your current age: ")
date = datetime.datetime.now()
year = date.year
#print(year)
year = int(year) + 100
#print(year)
print("{} the year in which you would turn 100 years is {}".format(name, year))