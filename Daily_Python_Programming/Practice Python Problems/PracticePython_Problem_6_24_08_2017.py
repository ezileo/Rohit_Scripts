import random
import string
NumberOfNumbersToGuess = 4
PlayerNumber = []
RandomNumber = [random.choice(string.digits) for _ in range(NumberOfNumbersToGuess)]
print(RandomNumber)
Cows = 0
Bulls = 0

if __name__ == "__main__":
    while Cows < NumberOfNumbersToGuess:
        PlayerNumber = [n for n in input("Please enter a "+str(NumberOfNumbersToGuess)+"-digit number\nEnter 'exit' to quit the game.\n")]
        if PlayerNumber == ["e","x","i","t"]:
            break
        Cows = 0
        Bulls = 0
        for i in PlayerNumber:
            if i in RandomNumber:
                Bulls += 1
        j=0
        while j <NumberOfNumbersToGuess:
            if RandomNumber[j] == PlayerNumber [j]:
                Cows += 1
            j += 1
        print("\nCows:",Cows,"\nBulls:",Bulls-Cows)