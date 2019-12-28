import random

RULES = 'Answer "yes" if number even otherwise answer "no"'


def start_round():
    guess = random.randint(1, 100)
    answer = 'yes' if guess % 2 == 0 else 'no'
    return guess, answer
