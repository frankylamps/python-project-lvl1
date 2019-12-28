import random

RULES = 'Find the greatest common divisor of given numbers.'


def get_div(a, b):
    div = a if a < b else b
    while a % div != 0 or b % div != 0:
        div -= 1
    return div


def start_round():
    num1 = random.randint(1, 200)
    num2 = random.randint(1, 200)
    question = ('{} {}'.format(str(num1),str(num2)))
    answer = get_div(num1, num2)
    return question, answer
