import os
import random

os.system('cls')

number = random.randint(1, 100)

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')

diff = input('Choose a difficuty. Type \'easy\' or \'hard\': ').lower()

attempts = 10 if diff == 'easy' else 5

while attempts:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))

    if guess < number:
        print('Too low.')
    elif guess > number:
        print('Too high.')
    else:
        print('You got it!')
        break

    attempts -= 1
    if attempts == 0:
        break
    
    print('Guess again.')
