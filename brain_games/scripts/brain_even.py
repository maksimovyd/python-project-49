#!/usr/bin/env python3

import brain_games.scripts.driver.engine
import brain_games.cli
from random import randint


def main():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    success = brain_games.scripts.driver.engine.games_engine(name, 'brain_even')
    if success:
        print("Congratulations, " + name + "!")


def play_brain_even(NAME):
    RAND_NUM = randint(1, 100)
    print('Question: ' + str(RAND_NUM))
    REAL_ANSWER = calculation_brain_even(RAND_NUM)
    if brain_games.scripts.driver.engine.final_output(REAL_ANSWER, NAME):
        return True
    else:
        return False


def calculation_brain_even(RAND_NUM):
    if RAND_NUM % 2 == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    main()
