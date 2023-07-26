#!/usr/bin/env python3

import brain_games.cli
import brain_games.scripts.driver.engine
from random import randint


def main():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    success = brain_games.scripts.driver.engine.\
        games_engine(name, 'brain_prime')
    if success:
        print("Congratulations, " + name + "!")


def play_brain_prime(NAME):
    RANDOM_NUM = randint(1, 100)
    print('Question: ' + str(RANDOM_NUM))
    REAL_ANSWER = calculation_brain_prime(RANDOM_NUM)
    if brain_games.scripts.driver.engine.final_output(REAL_ANSWER, NAME):
        return True
    else:
        return False


def calculation_brain_prime(RANDOM_NUM):
    if RANDOM_NUM < 2:
        return 'no'
    for i in range(2, RANDOM_NUM // 2 + 1):
        if RANDOM_NUM % i == 0:
            return 'no'
    return 'yes'


if __name__ == '__main__':
    main()
