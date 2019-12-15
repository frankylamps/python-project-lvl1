import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers \n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(name))
    counter = 0

    def get_div(a, b):
        div = a if a < b else b
        while a % div != 0 or b % div != 0:
            div -= 1
        return div

    while counter < 3:
        num1 = random.randint(1, 200)
        num2 = random.randint(1, 200)
        question = str(num1) + ' ' + str(num2)
        print('Question: ' + question)
        print('Your answer:', end=' ')
        answer = input()
        if answer == str(get_div(num1, num2)):
            print('Correct!')
        else:
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, str(get_div(num1, num2))))
            break
        counter += 1
    if counter == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
