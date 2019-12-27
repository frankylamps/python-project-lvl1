import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer(num):
    div = 2
    while div <= round(num / 2):
        if num % div == 0:
            return 'no'
        div += 1
    return 'yes'


def start_round():
    question = random.randint(2, 100)
    answer = get_answer(question)
    return question, answer
