import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no". \n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(name))
    counter = 0

    def is_prime(num):
        div = 2
        while div <= round(num / 2):
            if num % div == 0:
                return 'no'
            div += 1
        return 'yes'

    while counter < 3:
        num = random.randint(2, 100)
        print('Question: ' + str(num))
        print('Answer: ', end='')
        answer = input()
        if answer == is_prime(num):
            print('Correct!')
        else:
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, is_prime(num)))
            break
        counter += 1
    if counter == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
