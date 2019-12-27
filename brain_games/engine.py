import prompt


def engine(game_module):
    print('Welcome to the Brain Games!')
    print(game_module.RULES + '\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    counter = 1
    while counter <= 3:
        (question, correct_answer) = game_module.start_round()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print("'{}' is a wrong answer ;(. Correct answer was '{}'".format(answer, correct_answer))
            break
        print('Correct!')
        counter += 1
    else:
        print('Congratulations, {}!'.format(name))
