import random
import operator

RULES = 'What is the result of the expression?'


def start_round():
    num_1 = random.randint(10, 15)
    num_2 = random.randint(1, 5)
    opt_add = ('add', '+')
    opt_mul = ('mul', '*')
    opt_sub = ('sub', '-')
    opt_rand = random.choice([opt_add, opt_mul, opt_sub])
    question = ('{} {} {}'.format(num_1, opt_rand[1], num_2))
    answer = getattr(operator, opt_rand[0])(num_1, num_2)
    return question, answer
