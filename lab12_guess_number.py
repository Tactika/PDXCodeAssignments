'''
PDX Code Guild
Python Bootcamp
Damien Richcreek
Lab 12 - Guess the Number
'''
# Imports
import random
import math

def average(n1, n2):
    number = int((n1 + n2) / 2)
    return number
print(average(1,10))
def improve(guess, answer):
    guess_range = [*range(1, 10)]
    lowest = min(guess_range)
    highest = len(guess_range)
    new_guess = 0

    while True:
        if answer in range(lowest, guess):
            guess = average(lowest, guess)
            return new_guess
        elif answer in range(guess, highest):
            guess = average(guess, highest)
            return new_guess

def closer(guess, last_guess, answer):
    while True:
        if abs(guess - answer) > abs(last_guess - answer):
            print('You\'re getting closer!')
            break
        else:
            print('You\'re getting further away!')
            break

# REPL (Read, Evaluate, Print, Loop)
def main():
    guess = average(1, 10)
    answer = int(input('Please pick a number between 1 and 10:  '))
    guess_count = 1
    last_guess = 0
    new_guess = 0
    
    while True:
        if guess_count == 10:
            print(f'Too many guesses, the correct number was {answer}.')
            break
        elif guess == answer:
            print(f'Correct, {answer} was the number!')
            print(f'It only took you {guess_count} guesses!')
            break
        elif guess < answer:
            print(f'Try again, your guess of {guess} was too low!')
            closer(guess, last_guess, answer)
            improve(guess,answer)
            last_guess = guess
            guess = new_guess
            guess_count += 1
           # guess = int(input('Please pick a number between 1 and 10:  '))
        elif guess > answer:
            print(f'Try again, your guess of {guess} was too high!')
            closer(guess, last_guess, answer)
            improve(guess, answer)
            last_guess = guess
            guess = new_guess
            guess_count += 1
           # guess = int(input('Please pick a number between 1 and 10:  '))
        else:
            print('Please enter a valid integer, 1 - 10!')
            closer(guess, last_guess, answer)
            improve(guess, answer)
            last_guess = guess
            guess = new_guess
            guess_count += 1
           # guess = int(input('Please pick a number between 1 and 10:  '))
main()
