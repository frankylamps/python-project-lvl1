import random

RULES = 'Answer "yes" if number even otherwise answer "no"'


def get_answer(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_round():
    guess = random.randint(1, 100)
    answer = get_answer(guess)
    return guess, answer
