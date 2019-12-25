import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    div = 2
    while div <= round(num / 2):
        if num % div == 0:
            return 'no'
        div += 1
    return 'yes'


def prime_game():
    question = random.randint(2, 100)
    answer = is_prime(question)
    return question, answer
