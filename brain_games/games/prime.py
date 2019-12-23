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
    num = random.randint(2, 100)
    print('Question: ' + str(num))
    print('Answer: ', end='')
    answer = input()
    if answer == is_prime(num):
        print('Correct!')
    else:
        print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, is_prime(num)))
        return 'fail'


if __name__ == '__main__':
    prime_game()
