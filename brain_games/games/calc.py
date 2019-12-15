import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no". \n')
    NAME = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(NAME))
    counter = 0
    while counter < 3:
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
            break
        counter += 1
    if counter == 3:
        print('Congratulations, {}!'.format(NAME))


if __name__ == '__main__':
    main()
