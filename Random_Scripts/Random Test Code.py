import random


def fs():
    if FS_Length == 1:
        FS0 = [0]
        print(FS0)
    elif FS_Length == 2:
        FS0 = [0, 1]
        print(FS0)
    elif FS_Length > 2:
        FS0 = [0, 1]
        a = 1
        while a <= (FS_Length-2):
            FS0.append(FS0[a] + FS0[a-1])
            a += 1
    print(FS0)
    print(len(FS0))

    return


user_input = int(input("Enter 1 to choose FS or 2 to Randomly generate one: "))
print(type(user_input))
if user_input == 1:
    FS_Length = int(input("Enter how long you want to calculate this: "))
    fs()

elif user_input == 2:
    FS_Length = random.randint(1, 100)
    fs()

else:
    print("Please select valid input")


