#!/usr/bin/env python3

import brain_games.cli
import brain_games.scripts.driver.engine
from random import choice
from random import randint


def main():
    name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    success = brain_games.scripts.driver.engine.games_engine(name, 'brain_calc')
    if success:
        print("Congratulations, " + name + "!")


def play_brain_calc(NAME):
    RANDOM_NUM_ONE, RANDOM_NUM_TWO = randint(1, 100), randint(1, 100)
    OPER = choice(['+', '-', '*'])
    real_answer = calc_rotvet(RANDOM_NUM_ONE, RANDOM_NUM_TWO, OPER)
    print('Question: ' + str(RANDOM_NUM_ONE) + ' ' + str(OPER) + ' ' + str(RANDOM_NUM_TWO))
    if brain_games.scripts.driver.engine.final_output(real_answer, NAME):
        return True
    else:
        return False


def calc_rotvet(RANDOM_NUM_ONE, RANDOM_NUM_TWO, OPER):
    if OPER == '+':
        return RANDOM_NUM_ONE + RANDOM_NUM_TWO
    elif OPER == '-':
        return RANDOM_NUM_ONE - RANDOM_NUM_TWO
    else:
        return RANDOM_NUM_ONE * RANDOM_NUM_TWO


if __name__ == '__main__':
    main()