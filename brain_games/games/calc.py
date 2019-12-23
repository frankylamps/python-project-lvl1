import random

RULES = 'What is the result of the expression?'


def calc_game():
    num_1 = random.randint(10, 15)
    num_2 = random.randint(1, 5)
    oper = random.choice('+-*')
    question = str(num_1) + ' ' + oper + ' ' + str(num_2)
    print('Question: ' + question)
    print('Your answer:', end=' ')
    answer = input()
    if answer == str(eval(question)):
        print('Correct!')
    else:
        print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, str(eval(question))))
        return 'fail'


if __name__ == '__main__':
    calc_game()
