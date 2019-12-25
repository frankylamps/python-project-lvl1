import random

RULES = 'What is the result of the expression?'


def calc_game():
    num_1 = random.randint(10, 15)
    num_2 = random.randint(1, 5)
    oper = random.choice('+-*')
    question = str(num_1) + ' ' + oper + ' ' + str(num_2)
    correct_answer = str(eval(question))
    return question, correct_answer
