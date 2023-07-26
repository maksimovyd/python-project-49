#!/usr/bin/env python3

import brain_games.scripts.driver.engine
import brain_games.cli
from random import randint


def main():
    name = brain_games.cli.welcome_user()
    print('What number is missing in the progression?')
    success = brain_games.scripts.driver.engine.\
        games_engine(name, 'brain_progression')
    if success:
        print("Congratulations, " + name + "!")



def play_brain_progression(NAME):
    QUANTITY_NUMS = randint(5, 15)
    NUMBER_NUM = randint(1, QUANTITY_NUMS)
    STEP = randint(2, 7)
    REAL_ANSWER = output_sequence(QUANTITY_NUMS, NUMBER_NUM, STEP)
    if brain_games.scripts.driver.engine.final_output(REAL_ANSWER, NAME):
        return True
    else:
        return False


def output_sequence(QUANTITY_NUMS, NUMBER_NUM, STEP):
    FIRST_NUM = randint(1, 100)
    SEQUENCE = ''
    i = 1
    REAL_ANSWER = FIRST_NUM + STEP
    while i <= QUANTITY_NUMS:
        if i == NUMBER_NUM:
            SEQUENCE += '..'
            REAL_ANSWER = FIRST_NUM + STEP
        else:
            SEQUENCE += str(FIRST_NUM + STEP)
        if i < QUANTITY_NUMS:
            SEQUENCE += ' '
        FIRST_NUM = FIRST_NUM + STEP
        i += 1
    SEQUENCE = 'Question: ' + SEQUENCE
    print(SEQUENCE)
    return REAL_ANSWER



if __name__ == '__main__':
    main()
