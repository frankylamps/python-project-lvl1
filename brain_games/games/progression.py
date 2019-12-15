import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression? \n')
    NAME = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(NAME))
    counter = 0

    while counter < 3:
        start = random.randint(1, 100)
        step = random.randint(1, 20)
        ind = 1
        secret = 0
        rand_ind = random.randint(2, 9)
        print('Question: ', end='')
        while ind <= 10:
            if ind == rand_ind:
                secret = start
                print('..', end=' ')
            else:
                print(start, end=' ')
            start += step
            ind += 1
        print('')
        print('Answer: ', end='')
        answer = input()
        if answer == str(secret):
            print('Correct!')
        else:
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, secret))
            break
        counter += 1
    if counter == 3:
        print('Congratulations, {}!'.format(NAME))


if __name__ == '__main__':
    main()
