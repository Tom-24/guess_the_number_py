# Guess the number program
# Tom_24
# February, 2016
# Initial version
import random

num = random.randint(1, 10)
guess = 11
nTries = 1
maxTries = 3

while True:
    try:
        print('Guess a number between 1 and 10.', 'You get to guess', maxTries, 'times')
        guess = int(input(''))
        break
    except ValueError:
        print('Whoops! That' "'s not a number between 1 and 10! Try again")

while guess != num and nTries < maxTries:

    while True:
        try:
            print('That' "'s not the correct number... ")
            if maxTries - nTries > 1:
                print('Try again!', 'You have:', maxTries - nTries, 'guesses left...')
                guess = int(input(''))
                nTries = nTries + 1
            else:
                print('Try again!', 'You have:', maxTries - nTries, 'guess left...')
                guess = int(input(''))
                nTries = nTries + 1
            break
        except ValueError:
            print('Whoops! That' "'s not a number between 1 and 10! Try again")
            nTries = ntries + 1

if nTries <= maxTries and guess == num:
    print('You win!')
else:
    print('You did not guess the number.', 'The number was:', num, 'Better luck next time!')
