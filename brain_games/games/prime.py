import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    div = 2
    while div <= round(num / 2):
        if num % div == 0:
            return False
        div += 1
    return True


def start_round():
    question = random.randint(2, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
