
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a random number number between 1 and {x}: '))
    print(f'Yay, you have guess the number {random_number} correctly')


guess(10)
