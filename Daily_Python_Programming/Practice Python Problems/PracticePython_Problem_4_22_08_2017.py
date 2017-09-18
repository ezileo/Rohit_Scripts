# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date: August 22, 2017
# Version 1.0
# Problem Exercise: 4

number = int(input("Please enter a number to find its divisor: "))
divisor_list = []
for a in range(1, number + 1):
    if number % a == 0:
        # print(a)
        divisor_list.append(a)
    else:
        break
print("The divisor list for {} is: ".format(number), divisor_list)
print("The total count of divisors for {} is: ".format(number), len(divisor_list))
