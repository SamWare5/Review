#Question1- Guess number
#1/
import random
#from random import *#
number = random.randint(1, 101)
number = input("Please enter a number from 1 to 100 :")

print("Choose a number between 1 and 100")
guessesTaken = 0
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Wrong guess, you guessed too low.')
    if guess > number:
        print('Wrong guess, you guessed too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Correct you win, in ' + str(guessesTaken) + ' guesses!')
if guess != number:
    number = str(number)
print('The number I was thinking of was ' + number)
