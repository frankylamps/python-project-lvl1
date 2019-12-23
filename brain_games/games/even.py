import random

RULES = 'Answer "yes" if number even otherwise answer "no"'


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    guess = random.randint(1, 100)
    print('Question: ' + str(guess))
    print('Your answer:', end=" ")
    answer = input()
    if answer == is_even(guess):
        print('Correct!')
    else:
        print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, is_even(guess)))
        return 'fail'


if __name__ == '__main__':
    even_game()
