import prompt


def test():
    print('hello')


def engine(func, rule):
    print('Welcome to the Brain Games!')
    print(rule + '\n')
    NAME = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(NAME))
    counter = 1
    while counter <= 3:
        if func() == 'fail':
            break
        if counter == 3:
            print('Congratulations, {}!'.format(NAME))
        counter += 1
