
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a random number number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again, to low.')
        elif guess > random_number:
            print('Sorry, guess again, too high')
    print(f'Yay, you have guess the number {random_number} correctly')


guess(10)
