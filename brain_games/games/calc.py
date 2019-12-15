import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no". \n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(name))
    counter = 0
    while counter < 3:
        num1 = random.randint(10, 15)
        num2 = random.randint(1, 5)
        oper = random.choice('+-*')
        question = str(num1) + ' ' + oper + ' ' + str(num2)
        print('Question: ' + question)
        print('Your answer:', end=' ')
        answer = input()
        if answer == str(eval(question)):
            print('Correct!')
        else:
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, str(eval(question))))
            break
        counter += 1
    if counter == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
