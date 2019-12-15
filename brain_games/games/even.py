import random
import prompt


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no". \n')
    NAME = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(NAME))
    counter = 0
    while counter < 3:
        guess = random.randint(1, 100)
        print('Question: ' + str(guess))
        print('Your answer:', end=" ")
        answer = input()
        if answer == is_even(guess):
            print('Correct!')
            counter += 1
        else:
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, is_even(guess)))
            break
    if counter == 3:
        print('Congratulations, {}!'.format(NAME))


if __name__ == '__main__':
    main()
