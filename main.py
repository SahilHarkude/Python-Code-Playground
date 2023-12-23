import random
import sys

print("Welcome to Number Guessing Game !!!")
RandomNum=random.randint(1,101)

while(True):
    guess=int(input("Guess a number between 1-100: "))
    if(guess==RandomNum):
        print(str(guess)+" is correct!!")
        sys.exit(True)
    elif(guess>RandomNum):
        print("Go Lower")
    elif(guess<RandomNum):
        print("Go Higher")