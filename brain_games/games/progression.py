import random

RULES = 'What number is missing in the progression?'


def start_round():
    start = random.randint(1, 100)
    step = random.randint(1, 20)
    current_number = start
    counter = 1
    answer = 0
    hide_this_counter = random.randint(2, 9)
    question = ''
    while counter <= 10:
        if counter == hide_this_counter:
            answer = current_number
            question += '.. '
        else:
            question += str(current_number) + ' '
        current_number += step
        counter += 1
    question = question[0:-1:]
    return question, answer
