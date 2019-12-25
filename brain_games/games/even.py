import random

RULES = 'Answer "yes" if number even otherwise answer "no"'


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    guess = random.randint(1, 100)
    correct_answer = is_even(guess)
    return guess, correct_answer
