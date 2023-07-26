#!/usr/bin/env python3

import brain_games.scripts.driver.engine
import brain_games.cli
from random import randint


def main():
    name = brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    success = brain_games.scripts.driver.engine.games_engine(name, 'brain_gcd')
    if success:
        print("Congratulations, " + name + "!")


def play_brain_gcd(NAME):
    RANDOM_NUM_ONE, RANDOM_NUM_TWO = randint(1, 100), randint(1, 100)
    print('Question: ' + str(RANDOM_NUM_ONE) + ' ' + str(RANDOM_NUM_TWO))
    REAL_ANSWER = calculation_nod(RANDOM_NUM_ONE, RANDOM_NUM_TWO)
    if brain_games.scripts.driver.engine.final_output(REAL_ANSWER, NAME):
        return True
    else:
        return False


def calculation_nod(RANDOM_NUM_ONE, RANDOM_NUM_TWO):
    NOD = 0
    while True:
        NOD = RANDOM_NUM_ONE % RANDOM_NUM_TWO
        RANDOM_NUM_ONE = RANDOM_NUM_TWO
        if NOD == 0:
            return RANDOM_NUM_TWO
        RANDOM_NUM_TWO = NOD


if __name__ == '__main__':
    main()
