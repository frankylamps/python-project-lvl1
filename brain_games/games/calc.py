import random
from operator import add, mul, sub

RULES = 'What is the result of the expression?'


def start_round():
    num1 = random.randint(10, 15)
    num2 = random.randint(1, 5)
    function, symbol = random.choice([
        (add, '+'),
        (mul, '*'),
        (sub, '-'),
    ])
    question = ('{} {} {}'.format(num1, symbol, num2))
    answer = function(num1, num2)
    return question, answer
