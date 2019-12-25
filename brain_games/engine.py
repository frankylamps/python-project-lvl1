import prompt


def engine(func, rule):
    print('Welcome to the Brain Games!')
    print(rule + '\n')
    NAME = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(NAME))
    counter = 1
    while counter <= 3:
        (question, correct_answer) = func()
        print('Question: ' + str(question))
        print('Your answer:', end=' ')
        answer = input()
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, correct_answer))
            break
        if counter == 3:
            print('Congratulations, {}!'.format(NAME))
        counter += 1
