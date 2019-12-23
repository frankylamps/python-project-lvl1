import random

RULES = 'What number is missing in the progression?'


def progression_game():
    START = random.randint(1, 100)
    current_number = START
    step = random.randint(1, 20)
    counter = 1
    secret = 0
    hide_counter = random.randint(2, 9)
    print('Question: ', end='')
    while counter <= 10:
        if counter == hide_counter:
            secret = current_number
            print('..', end=' ')
        else:
            print(current_number, end=' ')
        current_number += step
        counter += 1
    print('')
    print('Answer: ', end='')
    answer = input()
    if answer == str(secret):
        print('Correct!')
    else:
        print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, secret))
        return 'fail'


if __name__ == '__main__':
    progression_game()
